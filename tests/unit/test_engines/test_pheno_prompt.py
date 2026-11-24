"""Tests for the phenopacket diagnosis prompt, without network access."""

import unittest
from unittest.mock import MagicMock

from oaklib.interfaces import TextAnnotatorInterface

from ontogpt.engines.pheno_engine import PhenoEngine

PHENOPACKET = {
    "id": "case-1",
    "subject": {
        "id": "patient-1",
        "sex": "MALE",
        "timeAtLastEncounter": {"age": {"iso8601duration": "P32Y"}},
    },
    "phenotypicFeatures": [
        {"type": {"id": "HP:0007328", "label": "Impaired pain sensation"}},
        {"type": {"id": "HP:0002064", "label": "Spastic gait"}, "excluded": True},
        {"type": {"id": "HP:0003487", "label": "Babinski sign"}, "excluded": True},
        {"type": {"id": "HP:0009072", "label": "Decreased Achilles reflex"}, "excluded": False},
    ],
}


class TestPhenoPrompt(unittest.TestCase):
    def setUp(self):
        self.client = MagicMock()
        self.client.complete.return_value = "[]"
        self.engine = PhenoEngine(client=self.client, mappers=[])
        self.engine._mondo = MagicMock(spec=TextAnnotatorInterface)

    def test_excluded_features_not_listed_as_case_phenotypes(self):
        self.engine.predict_disease(PHENOPACKET)
        prompt = self.client.complete.call_args.args[0]
        self.assertIn("* Impaired pain sensation", prompt)
        self.assertIn("* Decreased Achilles reflex", prompt)
        self.assertNotIn("Spastic gait", prompt)
        self.assertNotIn("Babinski sign", prompt)
