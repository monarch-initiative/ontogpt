"""Core tests."""
import logging
import unittest

from ontogpt.evaluation.ctd import eval_ctd
from ontogpt.evaluation.ctd.eval_ctd import EvalCTD
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from tests import OUTPUT_DIR

EXTRACTIONS_OUT = OUTPUT_DIR / "eval-ctd-extractions.yaml"

ALT_EXAMPLE = """Title: Cocaine induced myocardial ischemia.
Abstract: We report a case of myocardial ischemia induced by cocaine.
The ischemia probably induced by coronary artery spasm was reversed by
nitroglycerin and calcium blocking agents.
"""

EXAMPLE = """Title: Downbeat nystagmus associated with intravenous patient-controlled
administration of morphine.
Abstract: IMPLICATIONS: This case documents a patient who developed dizziness with
downbeating nystagmus while receiving a relatively large dose of IV patient-controlled
analgesia morphine.Although there have been case reports of epidural morphine with these
symptoms and signs,this has not been previously documented with IV or patient-controlled
analgesia morphine.
"""

logger = logging.getLogger(eval_ctd.__name__)
logger.setLevel(logging.INFO)


class TestCTD(unittest.TestCase):
    """Test CTD evaluation."""

    def setUp(self) -> None:
        """Set up all engines in advance."""
        self.engine = EvalCTD()

    def test_load_test_sets(self):
        docs = list(self.engine.load_test_cases())
        self.assertGreater(len(docs), 100)
        for d in docs:
            logger.debug(dump_minimal_yaml(d))

    def test_eval(self):
        evaluator = self.engine
        evaluator.num_tests = 1
        eos = evaluator.eval()
        with open(EXTRACTIONS_OUT, "w") as f:
            f.write(dump_minimal_yaml(eos, minimize=False))
            # yaml.dump(eos.dict(), f)

    def test_individual_case(self):
        evaluator = self.engine
        ke = evaluator.extractor
        r = ke.extract_from_text(EXAMPLE)
        print(dump_minimal_yaml(r))

    def test_is_valid_identifier(self):
        evaluator = self.engine
        ke = evaluator.extractor
        chemical = ke.schemaview.get_class("Chemical")
        disease = ke.schemaview.get_class("Disease")
        cases = [
            ("MESH:C1", chemical, False, "too short"),
            ("MESH:D009020", chemical, True, "valid chemical"),
            ("MESH:D000071256", chemical, False, "too long"),
            ("CHEBI:12345", chemical, False, "not an requested ID space"),
            ("MESH:D054556", chemical, False, "disease"),
            ("MESH:D054556", disease, True, "valid disease"),
        ]
        for case, cls, valid, reason in cases:
            self.assertEqual(valid, ke.is_valid_identifier(case, cls), reason)

    def test_normalize_identifier(self):
        evaluator = self.engine
        ke = evaluator.extractor
        chemical = ke.schemaview.get_class("Chemical")
        disease = ke.schemaview.get_class("Disease")
        cases = [
            ("CHEBI:17303", chemical, ["MESH:D009020"], "via node normalization"),
            ("MESH:D009020", chemical, ["MESH:D009020"], "reflexive (chemical)"),
            ("MESH:D054556", chemical, [], "disease"),
            ("MESH:D054556", disease, ["MESH:D054556"], "reflexive (disease)"),
            ("MESH:D009020", disease, [], "disease"),
        ]
        for case, cls, expected, reason in cases:
            normalized = list(ke.normalize_identifier(case, cls))
            print(normalized)
            self.assertCountEqual(expected, normalized, reason)
