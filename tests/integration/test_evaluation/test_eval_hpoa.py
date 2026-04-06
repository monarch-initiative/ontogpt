"""Core tests for Human Phenotype Ontology Annotations (HPOA) evaluation."""
import os
import unittest

import yaml

from ontogpt.evaluation.hpoa.eval_hpoa import EvalHPOA
from tests import OUTPUT_DIR

NORMALIZED_OUT = OUTPUT_DIR / "hpoa-normalized.yaml"
PREDICTIONS_OMIM_OUT = OUTPUT_DIR / "eval-hpoa-predictions-omim.yaml"
PREDICTIONS_PUBS_OUT = OUTPUT_DIR / "eval-hpoa-predictions-pubs.yaml"
PREDICTIONS_ALL_OUT = OUTPUT_DIR / "eval-hpoa-predictions-all.yaml"
RUN_FULL_LIVE_EXTRACTION = os.getenv("ONTOGPT_RUN_FULL_LIVE_EXTRACTION") == "1"


class Testhpoa(unittest.TestCase):
    """Test HPOA evaluation."""

    def setUp(self) -> None:
        """Set up all engines in advance."""
        self.engine = EvalHPOA()

    def _annotations_for_n_subjects(self, n: int):
        anns = list(self.engine.parse_hpoa())
        subjects = []
        subset = []
        for ann in anns:
            if ann.subject not in subjects:
                if len(subjects) >= n:
                    break
                subjects.append(ann.subject)
            if ann.subject in subjects:
                subset.append(ann)
        return subset

    def _annotations_for_n_publications(self, n: int):
        anns = list(self.engine.parse_hpoa())
        publications = []
        subset = []
        for ann in anns:
            key = (ann.subject, ann.publication)
            if not ann.publication or not ann.publication.startswith("PMID:"):
                continue
            if key not in publications:
                if len(publications) >= n:
                    break
                publications.append(key)
            if key in publications:
                subset.append(ann)
        return subset

    def test_load_hpoa(self):
        diseases = self.engine.annotations_to_diseases()
        objs = [m.model_dump() for m in diseases]
        print(yaml.dump(objs[0:3]))
        self.assertGreater(len(diseases), 0)

    def test_diseases(self):
        diseases = self.engine.diseases(self._annotations_for_n_subjects(2))
        for test_case in diseases[0:2]:
            text = self.engine.disease_text(test_case.id)
            self.assertIsNotNone(text)
            self.assertGreater(len(text), 100)
        objs = [m.model_dump() for m in diseases]
        print(yaml.dump(objs[0:3]))
        self.assertGreater(len(diseases), 0)

    def test_diseases_by_publication(self):
        t2d = self.engine.diseases_by_publication(self._annotations_for_n_publications(2))
        t2d_sample = {k: t2d[k] for k in list(t2d)[0:2]}
        for k, disease in t2d_sample.items():
            text = self.engine.disease_text(disease.id)
            self.assertIsNotNone(text)
            self.assertGreater(len(text), 100)
            print(f"## {k}: {disease.id} ")
            print(yaml.dump(disease.model_dump()))

    @unittest.skipUnless(
        RUN_FULL_LIVE_EXTRACTION,
        "Set ONTOGPT_RUN_FULL_LIVE_EXTRACTION=1 to run live HPOA publication evaluation",
    )
    def test_eval_pubs(self):
        evaluator = self.engine
        eos = evaluator.eval("pubs", num_tests=1)
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
