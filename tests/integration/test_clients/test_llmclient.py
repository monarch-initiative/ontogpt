"""LLMClient tests."""
import re
import unittest

import yaml

from ontogpt.clients import LLMClient
from tests import PROMPTS_FILE

PROMPT = """
example:

name: ornithine biosynthesis
def: The biological process that results in the output of ornithine, ornithine,
     an amino acid only rarely found in proteins, but which is important in living
     organisms as an intermediate in the reactions of the urea cycle and in arginine biosynthesis.
parent: biosynthetic process
differentia:
  outputs: ornithine

===

name: selenocysteine biosynthesis
"""

CODE_PROMPT_GENERALIZATION = """
- name: ornithine biosynthesis
  description: The biological process that results in the output of ornithine,
  ornithine, an amino acid only rarely found in proteins, but which is important in
  living organisms as an intermediate in the reactions of the urea
  cycle and in arginine biosynthesis
  subclass_of:
    - amino acid biosynthetic process
  pattern:
    - biosynthetic process
  outputs:
    - ornithine
- name: selenocysteine biosynthesis
"""

CODE_PROMPT_EXTRACT = """
- abstract: >-
     Amelogenesis imperfecta type 1K (AI1K) is characterized by hypoplastic enamel of all teeth.
     In some individuals, the pulp chambers may be enlarged and some molars may exhibit taurodontism
     Amelogenesis imperfecta segregated as an autosomal dominant trait in the family described by
     Smith et al.
     amelogenesis imperfecta type IK (AI1K) is caused by heterozygous mutation in the
     SP6 gene (608613) on chromosome 17q21.

   name: amelogenesis imperfecta type 1K
   synonyms:
    - AI1K
   subclass_of:
     - amelogenesis imperfecta
   genes:
     - SP6
   inheritance: autosomal dominant
   phenotypes:
     - hypoplastic enamel
     - pulp chamber enlargement
     - taurodontism
- abstract: >-
    Familial hemiplegic migraine-2 (FHM-2) is a rare subtype of familial hemiplegic migraine (FHM)
    characterized by migraine with aura,
    nystagmus, and progressive cognitive decline. It is caused by mutations in ATP1A2.
  name: Familial hemiplegic migraine-2
  synonyms:
   - FHM2
   - Familial hemiplegic migraine type 2
  subclass_of:
   - familial hemiplegic migraine
  genes:
    - ATP1A2
  inheritance: autosomal dominant
  phenotypes:
    - migraine with aura
    - nystagmus
    - progressive cognitive impairment
- abstract: >-
     neurodevelopmental disorder with eye movement abnormalities and ataxia (NEDEMA)
     is caused by heterozygous mutation in the FRMD5 gene.
     Neurodevelopmental disorder with eye movement abnormalities and ataxia (NEDEMA)
     is characterized by global developmental delay apparent from infancy.
     Affected individuals show delayed walking with an unsteady gait,
     variably impaired intellectual development, learning disabilities,
     and speech difficulties. Abnormal eye movements, which are often noted in early childhood,
     include opsoclonus, nystagmus, and strabismus. Some patients have seizures,
     which may be refractor.
     Lu et al. (2022) reported 8 unrelated patients, ranging in age from 3 to 27 years,
     with a similar neurodevelopmental disorder and de novo heterozygous mutations
     in the FRMD5 gene. The patients presented in infancy with global developmental
     delay and showed delayed walking, variably impaired intellectual development,
     and poor or absent speech. Those that achieved walking had an unsteady gait,
     and most had hypotonia and ataxia; a few demonstrated spasticity.
     Some patients had dyslexia or learning disabilities. Six patients had seizures
     or evidence of seizures, including 2 patients who were diagnosed in infancy
     with refractory epilepsy and West syndrome. All patients had eye movement abnormalities,
     ranging from strabismus and intermittent esotropia to opsoclonus and nystagmus.
     Two were visually impaired and had myopia or hypermetropia. Brain imaging was normal
     in most patients, but one had pachygyria and another had delayed myelination.
     A few patients had additional features such as myoclonus, dystonia, dyskinesia,
     and behavioral problems.
     Inheritance:
     The heterozygous mutations in the FRMD5 gene that were identified in most
     patients with NEDEMA by Lu et al. (2022) occurred de novo.

  name: """

TUNED_TEST_PROMPT = """
From the text below, extract the following entities in the following YAML::

name: <name of disease>
synonyms: <list of synonyms>
subclass_of: <list of superclasses>
genes: <list of causative genes>
inheritance: <mode of inheritance>
phenotypes: <list of phenotypes>

Text:
neurodevelopmental disorder with eye movement abnormalities and ataxia (NEDEMA)
is caused by heterozygous mutation in the FRMD5 gene.
Neurodevelopmental disorder with eye movement abnormalities and ataxia (NEDEMA)
is characterized by global developmental delay apparent from infancy.
Affected individuals show delayed walking with an unsteady gait, variably impaired
intellectual development, learning disabilities, and speech difficulties.
Abnormal eye movements, which are often noted in early childhood, include opsoclonus,
nystagmus, and strabismus. Some patients have seizures, which may be refractor.
Lu et al. (2022) reported 8 unrelated patients, ranging in age from 3 to 27 years,
with a similar neurodevelopmental disorder and de novo heterozygous mutations in the FRMD5 gene.
The patients presented in infancy with global developmental delay and showed delayed walking,
variably impaired intellectual development, and poor or absent speech.
Those that achieved walking had an unsteady gait, and most had hypotonia and ataxia;
a few demonstrated spasticity. Some patients had dyslexia or learning disabilities.
Six patients had seizures or evidence of seizures, including 2 patients who were diagnosed
in infancy with refractory epilepsy and West syndrome. All patients had eye movement
abnormalities, ranging from strabismus and intermittent esotropia to opsoclonus and nystagmus.
Two were visually impaired and had myopia or hypermetropia. Brain imaging was
normal in most patients, but one had pachygyria and another had delayed myelination.
A few patients had additional features such as myoclonus, dystonia, dyskinesia, and
behavioral problems.
Inheritance:
###
"""


class TestCompletion(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        self.llm_client = LLMClient()

    def test_all_prompts(self):
        """Test all prompts."""
        prompt_doc = yaml.safe_load(open(PROMPTS_FILE))
        default_engine = prompt_doc.get("default_engine", "gpt-4o")
        for prompt in prompt_doc["prompts"]:
            prompt_text = prompt["prompt"]
            if not isinstance(prompt_text, str):
                prompt_text = yaml.dump(prompt_text)
            engine = prompt.get("engine", default_engine)
            client = LLMClient(model=engine)
            pre_prompt = prompt.get("pre_prompt", "")
            prompt_text = "".join([pre_prompt, prompt_text])
            print(f"## Testing prompt [{engine}: [{len(prompt_text)}] {prompt_text}")
            ann = client.complete(prompt_text)
            print(f"## Response: len={len(ann)}")
            print(ann)
            for expected in prompt.get("expected", []):
                self.assertTrue(re.search(expected, ann, re.IGNORECASE))

    def test_completion(self):
        """Tests end to end knowledge extraction."""
        client = self.llm_client
        ann = client.complete(PROMPT)
        print(ann)

    def test_drug_mech_db(self):
        """Test drug mechanism database."""
        client = self.llm_client
        ann = client.complete(
            """
        Explain the chain of events that relate a drug to a disease as a semi-colon separated list.

        Example:

        cortisone treats keratitis:

        cortisone increases glucocorticoid receptor; glucocorticoid receptor regulates COX;
        COX regulates prostaglandin; prostaglandin regulates inflammation;
        inflammation cause keratitis

        Text:

        imatinib treats chronic myeloid leukemia:
        """
        )
        print(ann)

    def test_code_completion_generalization(self):
        """Tests structured responses."""
        engine = "gpt-4o"
        client = LLMClient(model=engine)
        print(len(CODE_PROMPT_GENERALIZATION))
        ann = client.complete(CODE_PROMPT_GENERALIZATION)
        print(ann)

    def test_extract_via_code_completion(self):
        """Tests structured responses."""
        engine = "gpt-4o"
        client = LLMClient(model=engine)
        ann = client.complete(CODE_PROMPT_EXTRACT)
        print(ann)

    @unittest.skip("Doesn't work well with current OpenAI API")
    def test_fine_tuned(self):
        engine = (
            "davinci:ft-lawrence-berkeley-national-laboratory:mendelian-disease-2022-12-22-00-53-36"
        )
        client = LLMClient(model=engine)
        ann = client.complete(TUNED_TEST_PROMPT)
        print(ann)
