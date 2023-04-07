"""Core tests."""
import unittest

import yaml

from ontogpt.evaluation.enrichment.eval_enrichment import EvalEnrichment
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from tests import INPUT_DIR, OUTPUT_DIR

RESULTS_PATH = OUTPUT_DIR / "enrichment_results.yaml"

GENES2GO_PATH = INPUT_DIR / "genes2go.tsv.gz"

GENE_SETS = [
    ("peroxisome", ["PEX1", "PEX2", "PEX3", "PEX4", "PEX5", "PEX6"]),
    (
        "amigo-example",
        [
            "APOH",
            "APP",
            "CND2",
            "COL3A1",
            "COL5A2",
            "CXCL6",
            "FGFR1",
            "FSTL1",
            "ITGAV",
            "JAG1",
            "JAG2",
            "KCNJ8",
            "LPL",
            "LRPAP1",
            "LUM",
            "MSX1",
            "NRP1",
            "OLR1",
            "PDGFA",
            "PF4",
            "PGLYRP1",
            "POSTN",
            "PRG2",
            "PTK2",
            "S100A4",
            "SERPINA5",
            "SLCO2A1",
            "SPP1",
            "STC1",
            "THBD",
            "TIMP1",
            "TNFRSF21",
            "VAV2",
            "VCAN",
            "VEGFA",
            "VTN",
        ],
    ),
    ("meiosis I",
     ['ANKLE1', 'BCL2L11', 'BRIP1', 'CCNB1IP1', 'CENPC', 'CENPS', 'CENPX', 'CNTD1', 'DMC1', 'EME1', 'EME2', 'ERCC4', 'FANCD2', 'HFM1', 'IHO1', 'KASH5', 'MAJIN', 'MEI1', 'MEI4', 'MEIKIN', 'MEIOB', 'MEIOC', 'MND1', 'MSH4', 'MSH5', 'MUS81', 'PSMC3IP', 'PTTG1', 'PTTG2', 'PTTG3P', 'RAD51', 'RAD51C', 'RAD51D', 'RAD54B', 'RAD54L', 'RMI1', 'RNF212', 'RNF212B', 'SHOC1', 'SIX6OS1', 'SLX4', 'SPO11', 'SPO16', 'SYCE3', 'SYCP1', 'TERB1', 'TERB2', 'TEX11', 'TEX12', 'TEX15', 'TOP2A', 'TOP2B', 'TOP6BL', 'TRIP13']
     ),
]


class TestEvalEnrichment(unittest.TestCase):
    """Test GO Enrichment."""

    def setUp(self) -> None:
        """Set up all engines in advance."""
        self.evaluator = EvalEnrichment()

    def test_load(self):
        self.evaluator.load_annotations(GENES2GO_PATH)
        for a in list(self.evaluator.ontology.associations())[0:10]:
            print(a)

    def test_standard_enrichment(self):
        """Tests normal OAK enrichment."""
        engine = self.evaluator
        self.evaluator.load_annotations(GENES2GO_PATH)
        for gene_set in GENE_SETS:
            print(gene_set)
            name, gene_ids = gene_set
            payload = self.evaluator.standard_enrichment(gene_ids)
            print(payload)

    def test_standard_enrichment_no_ontology(self):
        """Tests normal OAK enrichment."""
        engine = self.evaluator
        self.evaluator.load_annotations(GENES2GO_PATH)
        for gene_set in GENE_SETS:
            print(gene_set)
            name, gene_ids = gene_set
            payload = self.evaluator.standard_enrichment(gene_ids, use_ontology=False)
            print(payload)
            self.assertTrue(len(payload.term_ids) > 0)

    def test_pairwise(self):
        """Tests template and module is loaded."""
        engine = self.evaluator
        for gene_set in GENE_SETS:
            print(gene_set)
            name, gene_ids = gene_set
            comp = engine.compare_analysis_pairwise(gene_ids, name)
            print(comp)
            print(yaml.dump(comp.dict(), sort_keys=False))

    def test_full(self):
        """Tests complete all by all comparisons."""
        engine = self.evaluator
        self.evaluator.load_annotations(GENES2GO_PATH)
        all = []
        for gene_set in GENE_SETS:
            print(gene_set)
            name, gene_ids = gene_set
            comp = engine.compare_analysis(gene_ids, name)
            print(comp)
            print(yaml.dump(comp.dict(), sort_keys=False))
            all.append(comp.dict())
        with open(RESULTS_PATH, "w") as file:
            file.write(dump_minimal_yaml(all))
            # yaml.dump(all, file, sort_keys=False)
