"""Tests the command-line interface."""
import unittest

from click.testing import CliRunner

from talisman.cli import main
from tests import OUTPUT_DIR
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

    def test_enrichment(self):
        ids = [id for id, _ in PEX]
        cmd = ["enrichment"] + ids
        result = self.runner.invoke(main, cmd)
        self.assertEqual(0, result.exit_code)
        out = result.stdout
        print(out)
