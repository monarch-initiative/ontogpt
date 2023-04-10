"""Core tests."""
import logging
import unittest

import yaml
from oaklib import get_implementation_from_shorthand
from oaklib.datamodels.vocabulary import IS_A, PART_OF
from oaklib.interfaces.obograph_interface import OboGraphInterface

from ontogpt.converters.ontology_converter import OntologyConverter
from ontogpt.engines import halo_engine
from ontogpt.engines.enrichment import load_gene_sets
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from tests import INPUT_DIR, OUTPUT_DIR, GENE_SETS_DIR

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