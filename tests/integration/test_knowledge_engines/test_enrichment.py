"""Core tests."""
import unittest

from ontogpt.engines import create_engine
from ontogpt.engines.enrichment import EnrichmentEngine
from ontogpt.utils.gene_set_utils import GeneSet, gene_info
from ontogpt.templates.gene_description_term import GeneDescriptionTerm

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
        desc = gene_info("HGNC:11584")
        print(desc)
        _symbol, _d1, _d2 = desc

    def test_enrichment(self):
        """Tests gene set enrichment."""
        ke: EnrichmentEngine = self.ke
        ids = [id for id, _ in PEX]
        desc = ke.summarize(GeneSet(name="pex", gene_ids=ids))
        print(desc)
        self.assertIn("peroxisome", desc.response_text.lower())
        self.assertTrue(any(s for s in desc.term_strings if "peroxisome" in s))
        print(desc.term_ids)

    def test_normalize(self):
        texts = [("nucleus", "GO:0005634"), ("1. protein folding (go:0006457)\n", "GO:0006457")]
        for text, expected in texts:
            print(text)
            grounding = self.ke.normalize_named_entity(text, GeneDescriptionTerm.__name__)
            print(grounding)
            self.assertEqual(grounding, expected)
