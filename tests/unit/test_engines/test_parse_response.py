"""Tests for parsing the pseudo-YAML completion without network access."""

from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.template_loader import get_template_details


def test_empty_field_does_not_swallow_next_field():
    """A field with no value must not cause the following filled field to be dropped."""
    ke = SPIRESEngine(
        template_details=get_template_details(template="gocam"),
        model="ollama/llama3",
    )
    completion = "\n".join(
        [
            "genes:",
            "organisms: human; mouse",
            "activities:",
            "pathways: Wnt signaling pathway; apoptosis",
        ]
    )
    ann = ke._parse_response_to_dict(completion)
    assert ann["organisms"] == ["human", "mouse"]
    assert ann["pathways"] == ["Wnt signaling pathway", "apoptosis"]
    assert "genes" not in ann
    assert "activities" not in ann
