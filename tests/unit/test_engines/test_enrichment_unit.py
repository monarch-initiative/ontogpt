"""Core tests."""
import logging
import unittest

import yaml

from ontogpt.engines import halo_engine
from ontogpt.utils.gene_set_utils import load_gene_sets
from tests import GENE_SETS_DIR

logger = logging.getLogger(halo_engine.__name__)
logger.setLevel(level=logging.INFO)


class TestEnrichment(unittest.TestCase):
    """Test enrichment."""

    def setUp(self) -> None:
        """Set up."""
        pass

    def test_load_gene_sets(self):
        """Test loading from folder."""
        gene_sets = load_gene_sets(GENE_SETS_DIR)
        print(yaml.dump(gene_sets.dict(), sort_keys=False))
        self.assertGreater(len(gene_sets.gene_sets), 3)
