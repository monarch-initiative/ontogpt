"""Core tests."""
import pickle
import sys
import unittest

import yaml

from ontogpt.io.markdown_exporter import MarkdownExporter
from tests import INPUT_DIR, OUTPUT_DIR


class TestExport(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.exporter = MarkdownExporter()
        with open(str(INPUT_DIR / "eds-output.pickle"), "rb") as f:
            self.extraction_result = pickle.load(f)
        # print(yaml.dump(self.extraction_result.dict()))

    def test_export(self):
        """Test export."""
        with open(str(OUTPUT_DIR / "eds-output.md"), "w", encoding="utf-8") as f:
            self.exporter.export(self.extraction_result, f)
