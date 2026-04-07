"""Core tests."""

import io
import pickle
import unittest

from linkml_runtime import SchemaView

from ontogpt.io.rdf_exporter import RDFExporter
from ontogpt.templates import PATH_TO_TEMPLATES
from ontogpt.templates.core import ExtractionResult, Publication
from tests import OUTPUT_DIR
from tests.unit.test_exporters import TEST_PICKLED_RESULTS


@unittest.skip("Not yet fully compatible with linkml exporters and test fixtures")
class TestExportRDF(unittest.TestCase):
    """Test RDF export."""

    def setUp(self) -> None:
        """Set up."""
        self.exporter = RDFExporter()
        self.schemaview = SchemaView(str(PATH_TO_TEMPLATES / "recipe.yaml"))
        with open(TEST_PICKLED_RESULTS, "rb") as f:
            self.extraction_result = pickle.load(f)

    def test_export(self):
        """Test export."""
        with open(str(OUTPUT_DIR / "test-output.ttl"), "w", encoding="utf-8") as f:
            self.exporter.export(self.extraction_result, f, self.schemaview)


def test_rdf_exporter_smoke():
    """Ensure the exporter works with current Pydantic serialization."""
    exporter = RDFExporter()
    schemaview = SchemaView(str(PATH_TO_TEMPLATES / "core.yaml"))
    extraction_result = ExtractionResult(
        extracted_object=Publication(id="PMID:1", title="Example title", abstract="Example abstract")
    )
    output = io.StringIO()

    exporter.export(extraction_result, output, schemaview)

    rendered = output.getvalue()
    assert "core:Publication" in rendered
    assert 'core:title "Example title"' in rendered
