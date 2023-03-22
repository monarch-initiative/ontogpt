"""Core tests."""
import logging
import pickle
import unittest

from linkml_runtime import SchemaView

from ontogpt.engines import create_engine
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.owl_exporter import OWLExporter
from tests import INPUT_DIR, OUTPUT_DIR

class TestExportOWL(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.exporter = OWLExporter()
        self.ke = create_engine("recipe", SPIRESEngine)
        self.schemaview = self.ke.schemaview
        with open(str(INPUT_DIR / "recipe-spaghetti.pickle"), "rb") as f:
            self.extraction_result = pickle.load(f)

    def test_export(self):
        """Test export."""
        with open(str(OUTPUT_DIR / "recipe-spaghetti.owl"), "w", encoding="utf-8") as f:
            self.exporter.export(self.extraction_result, f, self.schemaview, id_value="AUTO:_ROOT")
