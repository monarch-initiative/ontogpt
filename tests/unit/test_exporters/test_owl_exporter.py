"""Core tests."""
import logging
import pickle
import unittest

from linkml_runtime import SchemaView

from ontogpt.engines import create_engine
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.owl_exporter import OWLExporter
from tests import INPUT_DIR, OUTPUT_DIR
from tests.unit.test_exporters import TEST_PICKLED_RESULTS


class TestExportOWL(unittest.TestCase):
    """Test exporting from pre-made results to OWL."""

    def setUp(self) -> None:
        """Set up."""
        self.exporter = OWLExporter()
        self.ke = create_engine("recipe", SPIRESEngine)
        self.schemaview = self.ke.schemaview
        with open(TEST_PICKLED_RESULTS, "rb") as f:
            self.extraction_result = pickle.load(f)

    def test_export(self):
        """Test export."""
        with open(str(OUTPUT_DIR / "recipe-spaghetti.owl"), "w", encoding="utf-8") as f:
            self.exporter.export(self.extraction_result, f, self.schemaview, id_value="AUTO:_ROOT")
