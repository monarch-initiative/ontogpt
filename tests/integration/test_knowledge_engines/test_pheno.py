"""Core tests."""
import json
import logging
import unittest

from oaklib import get_adapter

from ontogpt.clients import openai_client
from ontogpt.engines import mapping_engine
from ontogpt.engines.pheno_engine import PhenoEngine
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from tests import INPUT_DIR

PHENOPACKET_FILE = INPUT_DIR / "Guo-2017-EXTL3-Patient_1.json"

logger = logging.getLogger(mapping_engine.__name__)
client_logger = logging.getLogger(openai_client.__name__)

# client_logger.setLevel(logging.DEBUG)


class TestPhenopackets(unittest.TestCase):
    def setUp(self) -> None:
        """Set up OAK adapter, extractor, and reasoner."""
        self.adapter = get_adapter("sqlite:obo:hp")

    def test_diagnose(self):
        phenopacket = json.load(open(PHENOPACKET_FILE))
        engine = PhenoEngine()
        result = engine.predict_disease(phenopacket)
        print(result)

    def test_eval(self):
        phenopacket = json.load(open(PHENOPACKET_FILE))
        engine = PhenoEngine()
        results = engine.evaluate([phenopacket])
        print(dump_minimal_yaml(results))
