"""Core tests."""
import unittest

import yaml
from oaklib import get_implementation_from_shorthand

from ontogpt.engines.spires_engine import SPIRESEngine
from tests import INSTANCES_DIR, OUTPUT_DIR

CASES = [
    (
        "drug.DrugMechanism",
        [{"disease": "MESH:D014552", "drug": "drugbank:DB00438"}],
        [
            ["disease", "drug"],
        ],
        [
            "sqlite:obo:mesh",
            "sqlite:obo:drugbank",
            "sqlite:obo:go",
            "sqlite:obo:uberon",
            "sqlite:obo:pr",
        ],
        "drug-mechanisms-001",
    ),
    (
        "reaction.Reaction",
        [
            {
                "label": "pseudouridine 5'-phosphatase activity",
                "description": "Catalysis of the reaction:\
                    pseudouridine 5'-phosphate + H2O = pseudouridine + phosphate.",
            },
            {
                "label": "L-altrarate dehydratase activity",
                "description": "Catalysis of the reaction:\
                    L-altrarate = 5-dehydro-4-deoxy-D-glucarate + H2O.",
            },
            # rhea:40031
            {"description": "ent-copalyl diphosphate + H2O = diphosphate + ent-manool"},
        ],
        [
            ["label"],
            ["description"],
            ["label", "description"],
        ],
        [],
        "reactions-001",
    ),
]


class TestGeneralize(unittest.TestCase):
    """Test generalization."""

    def setUp(self) -> None:
        """Set up all engines in advance."""
        ke_map = {}
        for c in CASES:
            template = c[0]
            ke_map[template] = SPIRESEngine(template)
        self.ke_map = ke_map

    def test_cases(self):
        """Tests generalization over all cases."""
        for template, objs, combos, labelers, input_file in CASES:
            ke = self.ke_map[template]
            ke.labelers = [get_implementation_from_shorthand(labeler) for labeler in labelers]
            print(f"Loading {input_file}")
            with open(INSTANCES_DIR / f"{input_file}.yaml") as f:
                examples = yaml.safe_load(f)
            print(examples)
            nu_objs = []
            for obj in objs:
                for combo in combos:
                    if any(c not in obj for c in combo):
                        continue
                    print(f"Testing {combo}")
                    test_obj = {k: obj[k] for k in combo}
                    nu_obj = ke.generalize(test_obj, examples)
                    print(nu_obj)
                    nu_obj = nu_obj.dict()
                    nu_obj["_combo"] = list(combo)
                    nu_obj["_input"] = test_obj
                    nu_objs.append(nu_obj)
            with open(
                str(OUTPUT_DIR / f"generalized-{input_file}.yaml"), "w", encoding="utf-8"
            ) as f:
                yaml.dump(nu_objs, f)
