"""Core tests."""
import logging
import unittest

from ontogpt.utils import gene_set_utils
from ontogpt.utils.gene_set_utils import load_gene_sets
from tests import GENE_SETS_DIR

logger = logging.getLogger(gene_set_utils.__name__)
logger.setLevel(level=logging.INFO)


class TestGeneSetUtils(unittest.TestCase):
    """Test ability to load and manipulate gene sets."""

    def test_load_gene_sets(self):
        """Test loading from folder."""
        gene_sets = load_gene_sets(GENE_SETS_DIR)
        # print(yaml.dump(gene_sets.dict(), sort_keys=False))
        self.assertGreater(len(gene_sets.gene_sets), 3)
