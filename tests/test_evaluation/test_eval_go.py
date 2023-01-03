"""Core tests."""
import unittest

import yaml

from ontogpt.evaluation.go.eval_go import EvalGO, EvaluationObjectSetGO
from ontogpt.templates.metabolic_process import MetabolicProcess
from tests import OUTPUT_DIR

EXAMPLES_OUT = OUTPUT_DIR / "eval-go-examples.yaml"
PREDICTIONS_OUT = OUTPUT_DIR / "eval-go-predictions.yaml"


class TestEvalGO(unittest.TestCase):
    """Test GO evaluation."""

    def setUp(self) -> None:
        """Set up all engines in advance."""
        self.engine = EvalGO()

    def test_dm(self):
        mp = MetabolicProcess(
            id="GO:0008152",
        )
        eos = EvaluationObjectSetGO(test=[mp], training=[])
        print(yaml.dump(eos.dict()))

    def test_create_test_and_training(self):
        engine = self.engine
        ke = engine.extractor
        eos = engine.create_test_and_training()
        with open(EXAMPLES_OUT, "w") as f:
            yaml.dump(eos.dict(), f)
        for t in eos.test:
            print(yaml.dump(t.dict()))
            ser = ke.serialize_object(t)
            print(f"Serialized: {ser}")

    def test_eval_predictions(self):
        engine = self.engine
        eos = engine.eval()
        with open(PREDICTIONS_OUT, "w") as f:
            yaml.dump(eos.dict(), f)
