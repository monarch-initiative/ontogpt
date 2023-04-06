"""Core tests."""
import unittest

import yaml
from linkml_runtime.linkml_model import ClassDefinitionName
from oaklib import get_implementation_from_shorthand

from ontogpt.engines import create_engine
from ontogpt.engines.enrichment import EnrichmentEngine

PEX = [
    ("HGNC:8850", "PEX1"),
    ("HGNC:8851", "PEX10"),
    ("HGNC:8852", "PEX11A"),
    ("HGNC:8853", "PEX11B"),
]

class TestEnrichment(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.ke: EnrichmentEngine = create_engine(None, EnrichmentEngine)

    def test_gene_summaries(self):
        """Tests template and module is loaded."""
        ke: EnrichmentEngine = self.ke
        desc = ke.gene_summary("HGNC:11584")
        print(desc)

    def test_enrichment(self):
        """Tests gene set enrichment."""
        ke: EnrichmentEngine = self.ke
        ids = [id for id, _ in PEX]
        desc = ke.summarize(ids)
        print(desc)

