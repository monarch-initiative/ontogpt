"""Core tests."""
import pickle
import unittest

from ontogpt.io.html_exporter import HTMLExporter
from tests import INPUT_DIR, OUTPUT_DIR


class TestExportHTML(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.exporter = HTMLExporter()
        with open(str(INPUT_DIR / "eds-output.pickle"), "rb") as f:
            self.extraction_result = pickle.load(f)

    def test_export(self):
        """Test export."""
        with open(str(OUTPUT_DIR / "eds-output.html"), "w", encoding="utf-8") as f:
            self.exporter.export(self.extraction_result, f)
