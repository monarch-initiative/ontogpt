"""Core tests."""

import pickle
import unittest

from ontogpt.io.markdown_exporter import MarkdownExporter
from tests import OUTPUT_DIR
from tests.unit.test_exporters import TEST_PICKLED_RESULTS


@unittest.skip("Not yet fully compatible with linkml exporters and test fixtures")
class TestExport(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.exporter = MarkdownExporter()
        with open(TEST_PICKLED_RESULTS, "rb") as f:
            self.extraction_result = pickle.load(f)
        # print(yaml.dump(self.extraction_result.dict()))

    def test_export(self):
        """Test export."""
        with open(str(OUTPUT_DIR / "test-output.md"), "w", encoding="utf-8") as f:
            self.exporter.export(self.extraction_result, f)
