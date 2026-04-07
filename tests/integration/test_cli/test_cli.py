"""Tests the command-line interface."""
import importlib.util
import os
import unittest
from pathlib import Path

import inflection
from click.testing import CliRunner

from ontogpt.cli import main

TESTS_DIR = Path(__file__).resolve().parents[2]
CASES_DIR = TESTS_DIR / "input" / "cases"
OUTPUT_DIR = TESTS_DIR / "output"

_test_cases_path = TESTS_DIR / "integration" / "test_knowledge_engines" / "test_cases.py"
_test_cases_spec = importlib.util.spec_from_file_location("ontogpt_test_cases", _test_cases_path)
if _test_cases_spec is None or _test_cases_spec.loader is None:
    raise ImportError(f"Unable to load test cases from {_test_cases_path}")
extract_cases = importlib.util.module_from_spec(_test_cases_spec)
_test_cases_spec.loader.exec_module(extract_cases)

_test_enrichment_path = TESTS_DIR / "integration" / "test_knowledge_engines" / "test_enrichment.py"
if _test_enrichment_path.exists():
    _test_enrichment_spec = importlib.util.spec_from_file_location(
        "ontogpt_test_enrichment", _test_enrichment_path
    )
    if _test_enrichment_spec is None or _test_enrichment_spec.loader is None:
        raise ImportError(f"Unable to load enrichment fixtures from {_test_enrichment_path}")
    _test_enrichment = importlib.util.module_from_spec(_test_enrichment_spec)
    _test_enrichment_spec.loader.exec_module(_test_enrichment)
    PEX = _test_enrichment.PEX
else:
    PEX = None

CACHE_DB = str(OUTPUT_DIR / "cli_cache.db")
CLI_OUTPUT_DIR = OUTPUT_DIR / "cli"
RUN_FULL_LIVE_EXTRACTION = os.getenv("ONTOGPT_RUN_FULL_LIVE_EXTRACTION") == "1"


class TestCommandLineInterface(unittest.TestCase):
    """Tests all command-line subcommands."""

    def setUp(self) -> None:
        CLI_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        runner = CliRunner()
        self.runner = runner

    def test_main_help(self):
        result = self.runner.invoke(main, ["--help"])
        out = result.stdout
        self.assertIn("extract", out)
        self.assertIn("halo", out)
        self.assertEqual(0, result.exit_code)

    def test_extract(self):
        if not RUN_FULL_LIVE_EXTRACTION:
            self.skipTest(
                "Set ONTOGPT_RUN_FULL_LIVE_EXTRACTION=1 to run live CLI extraction coverage"
            )
        for case in extract_cases.CASES:
            template, input_name = case
            input_file = str(CASES_DIR / f"{input_name}.txt")
            fmts = ["yaml"]
            for fmt in fmts:
                output_file = str(CLI_OUTPUT_DIR / f"{input_name}.{fmt}")
                cmd = [
                    "--cache-db",
                    CACHE_DB,
                    "extract",
                    "-t",
                    template,
                    "-i",
                    input_file,
                    "-O",
                    fmt,
                    "-o",
                    output_file,
                ]
                print(cmd)
                result = self.runner.invoke(main, cmd)
                self.assertEqual(0, result.exit_code)
                out = result.stdout
                print(out)

    def test_search_and_extract(self):
        if not RUN_FULL_LIVE_EXTRACTION:
            self.skipTest(
                "Set ONTOGPT_RUN_FULL_LIVE_EXTRACTION=1 to run live CLI extraction coverage"
            )
        cases = [
            ("treatment.DiseaseTreatmentSummary", "COVID-19", ["review"]),
        ]
        for template, term, keywords in cases:
            for fmt in ["yaml"]:
                safe_term = inflection.underscore(term)
                output_file = str(CLI_OUTPUT_DIR / f"{template}-search-{safe_term}.{fmt}")
                cmd = [
                    "--cache-db",
                    CACHE_DB,
                    "search-and-extract",
                    "-t",
                    template,
                    term,
                    "-O",
                    fmt,
                    "-o",
                    output_file,
                ]
                for kw in keywords:
                    cmd.extend(["-k", kw])
                print(cmd)
                result = self.runner.invoke(main, cmd)
                self.assertEqual(0, result.exit_code)
                out = result.stdout
                print(out)

    def test_enrichment(self):
        if not PEX:
            self.skipTest("Enrichment integration fixtures are not available in this checkout")
        ids = [id for id, _ in PEX]
        cmd = ["enrichment"] + ids
        result = self.runner.invoke(main, cmd)
        self.assertEqual(0, result.exit_code)
        out = result.stdout
        print(out)
