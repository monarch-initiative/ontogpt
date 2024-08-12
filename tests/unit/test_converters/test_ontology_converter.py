"""Core tests."""

import logging
import unittest

import yaml
from oaklib import get_implementation_from_shorthand
from oaklib.datamodels.vocabulary import IS_A, PART_OF
from oaklib.interfaces.obograph_interface import OboGraphInterface

from ontogpt.converters.ontology_converter import OntologyConverter
from ontogpt.engines import halo_engine
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from tests import INPUT_DIR, OUTPUT_DIR

TEST_ONTOLOGY_OAK = INPUT_DIR / "go-nucleus.db"
TEST_ONTOLOGY_HALO = INPUT_DIR / "go-nucleus.halo.yaml"
TEST_ONTOLOGY_OUTPUT = OUTPUT_DIR / "go-nucleus.halo.yaml"
HALLUCINATED_ONTOLOGY_OUTPUT = OUTPUT_DIR / "go-nucleus.hallucinated.halo.yaml"

logger = logging.getLogger(halo_engine.__name__)
logger.setLevel(level=logging.INFO)


class TestOntologyConverter(unittest.TestCase):
    """Test ability to convert from OAK to native HALO form."""

    def setUp(self) -> None:
        """Set up."""
        self.adapter = get_implementation_from_shorthand(str(TEST_ONTOLOGY_OAK))
        self.converter = OntologyConverter(self.adapter)

    def test_ontology_from_obograph(self):
        """Test ontology from obograph."""
        oi = self.adapter
        if not isinstance(oi, OboGraphInterface):
            raise ValueError("Not an OboGraphInterface")
        graph = oi.as_obograph()
        converter = self.converter
        ontology = converter.from_obograph(graph)
        # print(yaml.dump(ontology.dict()))
        [nucleus] = [x for x in ontology.elements if x.name == "Nucleus"]
        self.assertCountEqual(["NuclearEnvelope", "NuclearMembrane"], nucleus.parts)
        self.assertCountEqual(["IntracellularMembrane-boundedOrganelle"], nucleus.subclass_of)
        self.assertCountEqual(["cell nucleus", "horsetail nucleus"], nucleus.synonyms)
        self.assertIn("A membrane-bounded organelle", nucleus.description)

    def test_extract_seed_ontology(self):
        """Test extract seed ontology."""
        converter = self.converter
        preds = [IS_A, PART_OF]
        ontology = converter.extract_seed_ontology(
            ["GO:0031965", "GO:0005635", "GO:0006793"], preds
        )
        [nucleus] = [x for x in ontology.elements if x.name == "Nucleus"]
        self.assertCountEqual(["NuclearEnvelope", "NuclearMembrane"], nucleus.parts)
        self.assertCountEqual(["IntracellularMembrane-boundedOrganelle"], nucleus.subclass_of)
        self.assertCountEqual(["cell nucleus", "horsetail nucleus"], nucleus.synonyms)
        self.assertIn("A membrane-bounded organelle", nucleus.description)
        [nm] = [x for x in ontology.elements if x.name == "NuclearMembrane"]
        print(yaml.dump(nm.model_dump()))
        self.assertEqual("Membrane and part of some Nucleus", nm.equivalent_to)
        with open(TEST_ONTOLOGY_OUTPUT, "w") as f:
            f.write(dump_minimal_yaml(ontology))
