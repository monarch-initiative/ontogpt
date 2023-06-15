"""Core tests."""
import unittest

import yaml
from linkml_runtime.linkml_model import ClassDefinitionName
from oaklib import get_implementation_from_shorthand

from ontogpt.clients.pubmed_client import PubmedClient
from ontogpt.engines import create_engine
from ontogpt.engines.knowledge_engine import chunk_text
from ontogpt.engines.spires2_engine import SPIRES2Engine
from ontogpt.engines.spires_engine import SPIRESEngine
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.templates.biological_process import BiologicalProcess
from ontogpt.templates.gocam import (
    ExtractionResult,
    Gene,
    GeneLocation,
    GeneOrganismRelationship,
    GoCamAnnotations,
)

TEMPLATE = "gocam.GoCamAnnotations"

PAPER = """
Title: β-Catenin Is Required for the cGAS/STING Signaling Pathway but
       Antagonized by the Herpes Simplex Virus 1 US3 Protein.
Text:
The cGAS/STING-mediated DNA-sensing signaling pathway is crucial
for interferon (IFN) production and host antiviral
responses. Herpes simplex virus I (HSV-1) is a DNA virus that has
evolved multiple strategies to evade host immune responses. Here,
we demonstrate that the highly conserved β-catenin protein in the
Wnt signaling pathway is an important factor to enhance the
transcription of type I interferon (IFN-I) in the cGAS/STING
signaling pathway, and the production of IFN-I mediated by
β-catenin was antagonized by HSV-1 US3 protein via its kinase
activity. Infection by US3-deficienct HSV-1 and its kinase-dead
variants failed to downregulate IFN-I and IFN-stimulated
gene (ISG) production induced by β-catenin. Consistent with this,
absence of β-catenin enhanced the replication of US3-deficienct
HSV-1, but not wild-type HSV-1. The underlying mechanism was the
interaction of US3 with β-catenin and its hyperphosphorylation of
β-catenin at Thr556 to block its nuclear translocation. For the
first time, HSV-1 US3 has been shown to inhibit IFN-I production
through hyperphosphorylation of β-catenin and to subvert host
antiviral innate immunity.IMPORTANCE Although increasing evidence
has demonstrated that HSV-1 subverts host immune responses and
establishes lifelong latent infection, the molecular mechanisms
by which HSV-1 interrupts antiviral innate immunity, especially
the cGAS/STING-mediated cellular DNA-sensing signaling pathway,
have not been fully explored. Here, we show that β-catenin
promotes cGAS/STING-mediated activation of the IFN pathway, which
is important for cellular innate immune responses and intrinsic
resistance to DNA virus infection. The protein kinase US3
antagonizes the production of IFN by targeting β-catenin via its
kinase activity. The findings in this study reveal a novel
mechanism for HSV-1 to evade host antiviral immunity and add new
knowledge to help in understanding the interaction between the
host and HSV-1 infection.

Keywords: HSV-1; US3; type I IFN; β-catenin.
"""

EXAMPLE_RESULTS = """
genes: β-Catenin; cGAS; STING; US3; IFN; ISG
organisms: Herpes Simplex Virus I (HSV-1);
gene_organisms: β-Catenin:host; cGAS:host; STING:host; US3:HSV-1; IFN:host; ISG:host
activities: production of type I IFN; transcription of type I IFN; replication of HSV-1;
nuclear translocation of β-catenin.
gene_functions: β-catenin:enhance the transcription of type I IFN; US3:antagonize
the production of IFN; β-catenin:block nuclear translocation.
cellular_processes: cGAS/STING-mediated DNA-sensing signaling; activation of IFN pathway
pathways: IFN pathway; Wnt signalling pathway
gene_gene_interactions: US3:β-catenin
gene_localizations: US3:host; β-catenin:host
"""

EXAMPLE_RESULTS_ALT = """
genes: β-Catenin; cGAS; STING; US3; IFN; ISG
organisms: Herpes Simplex Virus I (HSV-1);
gene_organisms: β-Catenin - Human; cGAS - Human; STING - Human;
US3 - Human; IFN - Human; ISG - Human.
activities: Transcription; Production; Downregulation; Replication; Nuclear Translocation
gene_functions: β-Catenin - Enhances Transcription; US3 - Antagonizes Production;
US3 - Downregulates IFN-I; US3 - Blocks Nuclear Translocation; β-Catenin - Enhances Production
cellular_processes: DNA-sensing; Interferon Production; Antiviral Innate Immunity;
Host Innate Immune Responses; Interaction with Host; Evade Host Antiviral Immunity
pathways: cGAS/STING-mediated DNA-sensing; Wnt Signaling; IFN pathway
gene_gene_interactions: US3 - β-Catenin; β-Catenin - US3
gene_localizations: β-Catenin - Nuclear; US3 - Hyperphosphorylation
"""

TEST_PROCESS = BiologicalProcess(
    label="autophagosome assembly",
    description="The formation of a double membrane-bounded structure, the autophagosome,\
        that occurs when a specialized membrane sac, called the isolation membrane,\
        starts to enclose a portion of the cytoplasm",
    subclass_of="GO:0022607",
    outputs=["GO:0005776"],
)

DIRECT_PARSE = {
    "genes": ["β-Catenin", "cGAS", "STING", "US3", "IFN", "ISG"],
    "gene_organisms": [
        ("β-Catenin", "host"),
        ("cGAS", "host"),
        ("STING", "host"),
        ("US3", "HSV-1"),
        ("IFN", "host"),
        ("ISG", "host"),
    ],
}


class TestCore(unittest.TestCase):
    """Test annotation."""

    def setUp(self) -> None:
        """Set up."""
        #self.ke = create_engine(TEMPLATE, SPIRESEngine)
        self.ke = SPIRES2Engine(template=TEMPLATE)

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
        slot = ke.schemaview.induced_slot("gene", "GeneOrganismRelationship")
        self.assertEqual(slot.name, "gene")
        self.assertEqual(slot.multivalued, True)
        self.assertEqual(slot.range, "Gene")


    def test_extract(self):
        """Tests end to end knowledge extraction."""
        ke = self.ke
        ann = ke.extract_from_text(PAPER)
        print(f"RESULTS={ann}")
        print(yaml.dump(ann.dict()))
        results = ann.extracted_object
        print(results)
        if not isinstance(results, GoCamAnnotations):
            raise ValueError(f"Expected GoCamAnnotations, got {type(results)}")
        self.assertIn("HGNC:2514", results.genes)

