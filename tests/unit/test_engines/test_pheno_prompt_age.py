"""Tests for the subject age in the phenopacket diagnosis prompt, without network access."""

import json
import unittest
from unittest.mock import MagicMock

from oaklib.interfaces import TextAnnotatorInterface

from ontogpt.engines.pheno_engine import PhenoEngine
from tests import INPUT_DIR

EXTL3_PHENOPACKET = INPUT_DIR / "Guo-2017-EXTL3-Patient_1.json"


def phenopacket(subject_time=None):
    """Return a minimal phenopacket whose subject has the given timeAtLastEncounter."""
    subject = {"id": "patient-1", "sex": "FEMALE"}
    if subject_time is not None:
        subject["timeAtLastEncounter"] = subject_time
    return {
        "id": "case-1",
        "subject": subject,
        "phenotypicFeatures": [
            {"type": {"id": "HP:0001263", "label": "Global developmental delay"}}
        ],
    }


class TestPhenoPromptAge(unittest.TestCase):
    def setUp(self):
        self.client = MagicMock()
        self.client.complete.return_value = "[]"
        self.engine = PhenoEngine(client=self.client, mappers=[])
        self.engine._mondo = MagicMock(spec=TextAnnotatorInterface)

    def prompt_for(self, packet):
        self.engine.predict_disease(packet)
        return self.client.complete.call_args.args[0]

    def test_phenopacket_v1_age_at_collection(self):
        packet = json.loads(EXTL3_PHENOPACKET.read_text())
        self.assertIn("The case is a FEMALE of age P2Y.", self.prompt_for(packet))

    def test_time_at_last_encounter_forms(self):
        cases = [
            ({"age": {"iso8601duration": "P6Y"}}, "P6Y"),
            ({"gestationalAge": {"weeks": 19, "days": 0}}, "19+0 weeks gestation"),
            ({"gestationalAge": {"weeks": 22, "days": 2}}, "22+2 weeks gestation"),
            (
                {"ontologyClass": {"id": "HP:0003593", "label": "Infantile onset"}},
                "Infantile onset",
            ),
            (None, "UNKNOWN"),
        ]
        for subject_time, age in cases:
            with self.subTest(subject_time=subject_time):
                prompt = self.prompt_for(phenopacket(subject_time))
                self.assertIn(f"The case is a FEMALE of age {age}.", prompt)
