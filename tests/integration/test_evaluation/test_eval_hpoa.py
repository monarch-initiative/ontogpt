"""Core tests for Human Phenotype Ontology Annotations (HPOA) evaluation."""
import unittest

import yaml

from ontogpt.evaluation.hpoa.eval_hpoa import EvalHPOA
from tests import OUTPUT_DIR

NORMALIZED_OUT = OUTPUT_DIR / "hpoa-normalized.yaml"
PREDICTIONS_OMIM_OUT = OUTPUT_DIR / "eval-hpoa-predictions-omim.yaml"
PREDICTIONS_PUBS_OUT = OUTPUT_DIR / "eval-hpoa-predictions-pubs.yaml"
PREDICTIONS_ALL_OUT = OUTPUT_DIR / "eval-hpoa-predictions-all.yaml"


class Testhpoa(unittest.TestCase):
    """Test HPOA evaluation."""

    def setUp(self) -> None:
        """Set up all engines in advance."""
        self.engine = EvalHPOA()

    def test_load_hpoa(self):
        diseases = self.engine.annotations_to_diseases()
        objs = [m.model_dump() for m in diseases]
        print(yaml.dump(objs[0:3]))
        self.assertGreater(len(diseases), 0)

    def test_diseases(self):
        diseases = self.engine.diseases()
        for test_case in diseases[0:2]:
            text = self.engine.disease_text(test_case.id)
            self.assertIsNotNone(text)
            self.assertGreater(len(text), 100)
        objs = [m.model_dump() for m in diseases]
        print(yaml.dump(objs[0:3]))
        self.assertGreater(len(diseases), 0)

    def test_diseases_by_publication(self):
        t2d = self.engine.diseases_by_publication()
        t2d_sample = {k: t2d[k] for k in list(t2d)[0:2]}
        for k, disease in t2d_sample.items():
            text = self.engine.disease_text(disease.id)
            self.assertIsNotNone(text)
            self.assertGreater(len(text), 100)
            print(f"## {k}: {disease.id} ")
            print(yaml.dump(disease.model_dump()))

    def test_eval_pubs(self):
        evaluator = self.engine
        eos = evaluator.eval("pubs")
        with open(PREDICTIONS_PUBS_OUT, "w") as f:
            yaml.dump(eos.model_dump(), f)

    @unittest.skip("Need to retrieve more OMIM texts - stochastic")
    def test_eval_all(self):
        evaluator = self.engine
        eos = evaluator.eval("all")
        with open(PREDICTIONS_ALL_OUT, "w") as f:
            yaml.dump(eos.model_dump(), f)

    @unittest.skip("Need to retrieve more OMIM texts - stochastic")
    def test_eval_omim(self):
        """Evaluates extraction purely from OMIM texts."""
        evaluator = self.engine
        eos = evaluator.eval("omim")
        with open(PREDICTIONS_OMIM_OUT, "w") as f:
            yaml.dump(eos.model_dump(), f)
