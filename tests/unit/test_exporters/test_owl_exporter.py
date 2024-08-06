"""Core tests."""

import pickle
import unittest

from linkml_runtime import SchemaView

from ontogpt.io.owl_exporter import OWLExporter
from ontogpt.templates import PATH_TO_TEMPLATES
from tests import OUTPUT_DIR
from tests.unit.test_exporters import TEST_PICKLED_RESULTS


@unittest.skip("Not yet fully compatible with linkml exporters and test fixtures")
class TestExportOWL(unittest.TestCase):
    """Test exporting from pre-made results to OWL."""

    def setUp(self) -> None:
        """Set up."""
        self.exporter = OWLExporter()
        self.schemaview = SchemaView(str(PATH_TO_TEMPLATES / "recipe.yaml"))
        with open(TEST_PICKLED_RESULTS, "rb") as f:
            self.extraction_result = pickle.load(f)

    def test_export(self):
        """Test export."""
        print(f"URL={self.extraction_result.extracted_object.url}")
        print(f"Label={self.extraction_result.extracted_object.label}")
        with open(str(OUTPUT_DIR / "recipe-spaghetti.owl"), "w", encoding="utf-8") as f:
            self.exporter.export(self.extraction_result, f, self.schemaview, id_value="AUTO:_ROOT")

    def test_export2(self):
        """Test export."""
        with open(str(OUTPUT_DIR / "recipe-palak-paneer.owl"), "w", encoding="utf-8") as f:
            self.exporter.export(self.extraction_result, f, self.schemaview, id_value="AUTO:_ROOT")
