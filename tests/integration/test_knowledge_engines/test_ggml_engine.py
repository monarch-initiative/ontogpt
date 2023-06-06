"""Tests for using local GGML models."""
import unittest

import yaml
from linkml_runtime.linkml_model import ClassDefinitionName
from oaklib import get_implementation_from_shorthand

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

@unittest.skip("GGML/GPT4ALL tests not run by default")
class TestCore(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.ke = GGMLEngine(template=TEMPLATE, local_model=MODEL_PATH)

    def test_setup(self):
        """Tests template and module is loaded."""
        ke = self.ke
        pyc = ke.template_pyclass
        print(pyc)
        obj = pyc(genes=["a"], gene_organisms=[{"gene": "a", "organism": "b"}])
        print(yaml.dump(obj.dict()))
        self.assertEqual(obj.genes, ["a"])
        self.assertEqual(obj.gene_organisms[0].gene, "a")
        self.assertEqual(obj.gene_organisms[0].organism, "b")
        slot = ke.schemaview.induced_slot("genes", "GeneOrganismRelationship")
        self.assertEqual(slot.name, "genes")
        self.assertEqual(slot.multivalued, True)
        self.assertEqual(slot.range, "Gene")

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
        ann = ke.extract_from_text(PAPER, object={"pathways": ["GO:0140896"]})
        print(f"RESULTS={ann}")
        print(yaml.dump(ann.dict()))
        results = ann.extracted_object
        if not isinstance(results, MendelianDisease):
            raise ValueError(f"Expected MendelianDisease, got {type(results)}")
