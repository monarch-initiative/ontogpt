"""Core tests."""

import pickle
import unittest

from ontogpt.io.html_exporter import HTMLExporter
from tests import OUTPUT_DIR
from tests.unit.test_exporters import TEST_PICKLED_RESULTS


@unittest.skip("Not yet fully compatible with linkml exporters and test fixtures")
class TestExportHTML(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.exporter = HTMLExporter()
        with open(TEST_PICKLED_RESULTS, "rb") as f:
            self.extraction_result = pickle.load(f)

    def test_export(self):
        """Test export."""
        with open(str(OUTPUT_DIR / "test-output.html"), "w", encoding="utf-8") as f:
            self.exporter.export(self.extraction_result, f)
