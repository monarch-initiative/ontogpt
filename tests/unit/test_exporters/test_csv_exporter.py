"""CSV exporter tests."""

import io

from ontogpt.io.csv_exporter import CSVExporter
from ontogpt.templates.core import ExtractionResult, Publication


def test_csv_exporter_smoke():
    """Ensure the exporter works with current Pydantic serialization."""
    exporter = CSVExporter()
    extraction_result = ExtractionResult(
        extracted_object=Publication(id="PMID:1", title="Example title", abstract="Example abstract")
    )
    output = io.StringIO()

    exporter.export(extraction_result, output, None)

    rendered = output.getvalue()
    assert ",values" in rendered
    assert "id,PMID:1" in rendered
    assert "title,Example title" in rendered
