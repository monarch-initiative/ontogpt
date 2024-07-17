"""Tests the command-line interface."""
import unittest

import inflection
from click.testing import CliRunner

import tests.integration.test_knowledge_engines.test_cases as extract_cases
from ontogpt.cli import main
from tests import CASES_DIR, OUTPUT_DIR
from tests.integration.test_knowledge_engines.test_enrichment import PEX

CACHE_DB = str(OUTPUT_DIR / "cli_cache.db")
CLI_OUTPUT_DIR = OUTPUT_DIR / "cli"


class TestCommandLineInterface(unittest.TestCase):
    """Tests all command-line subcommands."""

    def setUp(self) -> None:
        runner = CliRunner(mix_stderr=False)
        self.runner = runner

    def test_main_help(self):
        result = self.runner.invoke(main, ["--help"])
        out = result.stdout
        self.assertIn("extract", out)
        self.assertIn("halo", out)
        self.assertEqual(0, result.exit_code)

    def test_extract(self):
        for case in extract_cases.CASES:
            template, input_name = case
            input_file = str(CASES_DIR / f"{input_name}.txt")
            fmts = ["yaml", "html", "md"]
            if template == "recipe":
                fmts.append("owl")
            for fmt in fmts:
                output_file = str(CLI_OUTPUT_DIR / f"{input_name}.{fmt}")
                cmd = [
                    "--cache-db",
                    CACHE_DB,
                    "extract",
                    "-t",
                    template,
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
        cases = [
            ("treatment.DiseaseTreatmentSummary", "COVID-19", ["review"]),
        ]
        for template, term, keywords in cases:
            for fmt in ["yaml", "html"]:
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
        ids = [id for id, _ in PEX]
        cmd = ["enrichment"] + ids
        result = self.runner.invoke(main, cmd)
        self.assertEqual(0, result.exit_code)
        out = result.stdout
        print(out)
