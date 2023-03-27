"""Core tests."""
import logging
import unittest

import yaml
from oaklib import get_implementation_from_shorthand
from oaklib.datamodels.vocabulary import IS_A, PART_OF

from ontogpt.converters.ontology_converter import OntologyConverter
from ontogpt.engines import halo_engine
from ontogpt.engines.halo_engine import HALOEngine
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from tests import INPUT_DIR, OUTPUT_DIR

TEST_ONTOLOGY_OAK = INPUT_DIR / "go-nucleus.db"
TEST_ONTOLOGY_HALO = INPUT_DIR / "go-nucleus.halo.yaml"
TEST_ONTOLOGY_OUTPUT = OUTPUT_DIR / "go-nucleus.halo.yaml"
HALLUCINATED_ONTOLOGY_OUTPUT = OUTPUT_DIR / "go-nucleus.hallucinated.halo.yaml"

logger = logging.getLogger(halo_engine.__name__)
logger.setLevel(level=logging.INFO)


class TestHALO(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.ke = HALOEngine(
            expand_horizon=False,
            fixed_slot_values={"context": "subcellular"},
        )
        self.ke.seed_from_file(TEST_ONTOLOGY_HALO)
        adapter = get_implementation_from_shorthand(str(TEST_ONTOLOGY_OAK))
        self.converter = OntologyConverter(adapter)

    @unittest.skip("Algorithm changed")
    def test_get_candidate_elements(self):
        ke = self.ke
        elts = ke.get_candidate_elements()
        print(len(elts))
        self.assertGreater(len(elts), 10)
        print(elts[0:5])

    def test_hallucinate_element(self):
        ke = self.ke
        candidates = set(ke.get_candidate_elements())
        name = "Axon"
        elt = ke.hallucinate_element(name)
        print("## ELEMENT:")
        print(yaml.dump(elt.dict()))
        [elt2] = [elt for elt in ke.ontology.elements if elt.name == name]
        self.assertEqual(elt, elt2)
        self.assertIn(name, ke.visited)
        next_candidates = set(ke.get_candidate_elements())
        new_candidates = next_candidates.difference(candidates)
        print(f"New candidates={new_candidates}")
        self.assertGreater(len(new_candidates), 0)
        # ensure that new ones are added to the end
        self.assertIn(ke.get_candidate_elements()[-1], new_candidates)

    def test_hallucinate(self):
        ke = self.ke
        elts = ke.hallucinate(["Axon", "Dendrite"], num_iterations=4)
        for e in elts:
            print(f"{e.name} {e.description}")
        print(f"ELTS: {len(elts)}")
        with open(HALLUCINATED_ONTOLOGY_OUTPUT, "w") as f:
            f.write(dump_minimal_yaml(ke.ontology))

    def test_hallucinate_metabolism(self):
        ke = HALOEngine(
            expand_horizon=False,
            fixed_slot_values={"context": "metabolism"},
        )
        preds = [IS_A, PART_OF]
        adapter = get_implementation_from_shorthand("sqlite:obo:go")
        converter = OntologyConverter(adapter)
        ke.ontology = converter.extract_seed_ontology(["GO:0034651", "GO:0034653"], preds)
        elts = ke.hallucinate(
            ["KetoaldopentoseBiosyntheticProcess", "IsomaltotrioseMetabolicProcess"],
            num_iterations=3,
        )
        for e in elts:
            print(f"{e.name} {e.description}")
        print(f"ELTS: {len(elts)}")
        with open(str(OUTPUT_DIR / "carbohydrate-metabolism.hallucinated.halo.yaml"), "w") as f:
            f.write(dump_minimal_yaml(ke.ontology))
