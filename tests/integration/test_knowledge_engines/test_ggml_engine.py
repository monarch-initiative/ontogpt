"""Tests for using local GGML models."""
import unittest

import yaml

from ontogpt.engines.ggml_engine import GGMLEngine
from ontogpt.templates.mendelian_disease import MendelianDisease
from ontogpt.utils.model_utils import get_model

TEMPLATE = "mendelian_disease.MendelianDisease"

# This is a full-size model - unfortunately smaller models
# don't provide the results sufficient for a meaningful test.
# That's why these tests are skipped by default - the model is > 3 Gb
TEST_MODEL_URL = "https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin"
MODEL_PATH = get_model(TEST_MODEL_URL)

PAPER = """
Sly syndrome, also called mucopolysaccharidosis type VII (MPS-VII),
is an autosomal recessive lysosomal storage disease caused by a deficiency
of the enzyme β-glucuronidase. This enzyme is responsible for breaking down
large sugar molecules called glycosaminoglycans (AKA GAGs, or mucopolysaccharides).
The inability to break down GAGs leads to a buildup in many tissues and organs of the body.
The severity of the disease can vary widely.
"""


# @unittest.skip("GGML/GPT4ALL tests not run by default")
class TestCore(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.ke = GGMLEngine(template=TEMPLATE, local_model=MODEL_PATH)

    def test_extract(self):
        """Tests end to end knowledge extraction."""
        ke = self.ke
        ann = ke.extract_from_text(PAPER)
        print(f"RESULTS={ann}")
        print(yaml.dump(ann.dict()))
        results = ann.extracted_object
        if not isinstance(results, MendelianDisease):
            raise ValueError(f"Expected MendelianDisease, got {type(results)}")

    def test_extract_with_stub(self):
        """Tests end to end knowledge extraction."""
        ke = self.ke
        ann = ke.extract_from_text(PAPER, object={"genes": ["HGNC:8850"]})  # PEX1
        print(f"RESULTS={ann}")
        print(yaml.dump(ann.dict()))
        results = ann.extracted_object
        if not isinstance(results, MendelianDisease):
            raise ValueError(f"Expected MendelianDisease, got {type(results)}")
