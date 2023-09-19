"""Tests for using local GGML models."""
import unittest

import yaml

from ontogpt.engines.gpt4all_engine import GPT4AllEngine

TEMPLATE = "mendelian_disease.MendelianDisease"

# This is a small test model. It doesn't really
# do extraction - it's a BERT model for sentence
# embeddings - but it tests functionality.
TEST_MODEL = "ggml-all-MiniLM-L6-v2-f16"

TEXT_INPUT = "Peanut butter and cheese"


class TestCore(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.ke = GPT4AllEngine(template=TEMPLATE, model=TEST_MODEL)

    def test_extract(self):
        """Tests end to end knowledge extraction."""
        ke = self.ke
        ann = ke.extract_from_text(TEXT_INPUT)
        print(f"RESULTS={ann}")
        print(yaml.dump(ann.dict()))
        results = ann.extracted_object
        if results is not None:
            raise ValueError(f"Unexpected output type, got {type(results)}")
