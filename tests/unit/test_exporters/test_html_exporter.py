"""Core tests."""

import io
import pickle
import unittest

from ontogpt.io.html_exporter import HTMLExporter
from ontogpt.templates.core import ExtractionResult, NamedEntity, Publication
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


def test_html_exporter_smoke():
    """Ensure the exporter works with current Pydantic model metadata."""
    exporter = HTMLExporter()
    extraction_result = ExtractionResult(
        input_id="PMID:1",
        input_title="Example",
        input_text="Input text",
        raw_completion_output="Raw output",
        prompt="Prompt text",
        extracted_object=Publication(id="PMID:1", title="Example title", abstract="Example abstract"),
        named_entities=[NamedEntity(id="PMID:1", label="Example title")],
    )
    output = io.StringIO()

    exporter.export(extraction_result, output)

    rendered = output.getvalue()
    assert "<h3>id</h3>" in rendered
    assert 'Example title <a href="https://bioregistry.io/PMID:1">PMID:1</a>' in rendered
    assert "Prompt text" in rendered
