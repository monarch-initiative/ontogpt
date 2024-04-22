"""Core tests."""
import unittest
from pathlib import Path

import yaml
from oaklib import get_adapter

from ontogpt.evaluation.enrichment.eval_enrichment import EvalEnrichment
from ontogpt.io.yaml_wrapper import dump_minimal_yaml
from ontogpt.utils.gene_set_utils import GeneSet, fill_missing_gene_set_values, load_gene_sets
from tests import GENE_SETS_DIR, INPUT_DIR, OUTPUT_DIR

RESULTS_PATH = OUTPUT_DIR / "enrichment_results"

GENES2GO_PATH = INPUT_DIR / "genes2go.tsv.gz"

GENE_SETS = [
    ("peroxisome", ["PEX1", "PEX2", "PEX3", "PEX4", "PEX5", "PEX6", "PEX7", "PEX8"]),
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
    (
        "meiosis I",
        [
            "ANKLE1",
            "BCL2L11",
            "BRIP1",
            "CCNB1IP1",
            "CENPC",
            "CENPS",
            "CENPX",
            "CNTD1",
            "DMC1",
            "EME1",
            "EME2",
            "ERCC4",
            "FANCD2",
            "HFM1",
            "IHO1",
            "KASH5",
            "MAJIN",
            "MEI1",
            "MEI4",
            "MEIKIN",
            "MEIOB",
            "MEIOC",
            "MND1",
            "MSH4",
            "MSH5",
            "MUS81",
            "PSMC3IP",
            "PTTG1",
            "PTTG2",
            "PTTG3P",
            "RAD51",
            "RAD51C",
            "RAD51D",
            "RAD54B",
            "RAD54L",
            "RMI1",
            "RNF212",
            "RNF212B",
            "SHOC1",
            "SIX6OS1",
            "SLX4",
            "SPO11",
            "SPO16",
            "SYCE3",
            "SYCP1",
            "TERB1",
            "TERB2",
            "TEX11",
            "TEX12",
            "TEX15",
            "TOP2A",
            "TOP2B",
            "TOP6BL",
            "TRIP13",
        ],
    ),
    (
        "FA",
        [
            "FANCC",
            "FANCD2",
            "FANCA",
            "FANCB",
            "FANCE",
            "FANCF",
            "BRCA2",
            "FANCI",
            "BRIP1",
            "PALB2",
            "RAD51C",
            "SLX4",
            "FANCG",
            "FANCL",
            "ERCC4",
            "UBE2T",
            "MAD2L2",
            "RAD51",
            "XRCC2",
        ],
    ),
    (
        "mtorc1",
        [
            "ABCF2",
            "ACACA",
            "ACLY",
            "ACSL3",
            "ACTR2",
            "ACTR3",
            "ADD3",
            "ADIPOR2",
            "AK4",
            "ALDOA",
            "ARPC5L",
            "ASNS",
            "ATP2A2",
            "ATP5MC1",
            "ATP6V1D",
            "AURKA",
            "BCAT1",
            "BHLHE40",
            "BTG2",
            "BUB1",
            "CACYBP",
            "CALR",
            "CANX",
            "CCNF",
            "CCNG1",
            "CCT6A",
            "CD9",
            "CDC25A",
            "CDKN1A",
            "CFP",
            "COPS5",
            "CORO1A",
            "CTH",
            "CTSC",
            "CXCR4",
            "CYB5B",
            "CYP51A1",
            "DAPP1",
            "DDIT3",
            "DDIT4",
            "DDX39A",
            "DHCR24",
            "DHCR7",
            "DHFR",
            "EBP",
            "EDEM1",
            "EEF1E1",
            "EGLN3",
            "EIF2S2",
            "ELOVL5",
            "ELOVL6",
            "ENO1",
            "EPRS1",
            "ERO1A",
            "ETF1",
            "FADS1",
            "FADS2",
            "FDXR",
            "FGL2",
            "FKBP2",
            "G6PD",
            "GAPDH",
            "GBE1",
            "GCLC",
            "GGA2",
            "GLA",
            "GLRX",
            "GMPS",
            "GOT1",
            "GPI",
            "GSK3B",
            "GSR",
            "GTF2H1",
            "HK2",
            "HMBS",
            "HMGCR",
            "HMGCS1",
            "HPRT1",
            "HSP90B1",
            "HSPA4",
            "HSPA5",
            "HSPA9",
            "HSPD1",
            "HSPE1",
            "IDH1",
            "IDI1",
            "IFI30",
            "IFRD1",
            "IGFBP5",
            "IMMT",
            "INSIG1",
            "ITGB2",
            "LDHA",
            "LDLR",
            "LGMN",
            "LTA4H",
            "M6PR",
            "MAP2K3",
            "MCM2",
            "MCM4",
            "ME1",
            "MLLT11",
            "MTHFD2",
            "MTHFD2L",
            "NAMPT",
            "NFIL3",
            "NFKBIB",
            "NFYC",
            "NIBAN1",
            "NMT1",
            "NUFIP1",
            "NUP205",
            "NUPR1",
            "P4HA1",
            "PDAP1",
            "PDK1",
            "PFKL",
            "PGK1",
            "PGM1",
            "PHGDH",
            "PIK3R3",
            "PITPNB",
            "PLK1",
            "PLOD2",
            "PNO1",
            "PNP",
            "POLR3G",
            "PPA1",
            "PPIA",
            "PPP1R15A",
            "PRDX1",
            "PSAT1",
            "PSMA3",
            "PSMA4",
            "PSMB5",
            "PSMC2",
            "PSMC4",
            "PSMC6",
            "PSMD12",
            "PSMD13",
            "PSMD14",
            "PSME3",
            "PSMG1",
            "PSPH",
            "QDPR",
            "RAB1A",
            "RDH11",
            "RIT1",
            "RPA1",
            "RPN1",
            "RRM2",
            "RRP9",
            "SC5D",
            "SCD",
            "SDF2L1",
            "SEC11A",
            "SERP1",
            "SERPINH1",
            "SHMT2",
            "SKAP2",
            "SLA",
            "SLC1A4",
            "SLC1A5",
            "SLC2A1",
            "SLC2A3",
            "SLC37A4",
            "SLC6A6",
            "SLC7A11",
            "SLC7A5",
            "SLC9A3R1",
            "SORD",
            "SQLE",
            "SQSTM1",
            "SRD5A1",
            "SSR1",
            "STARD4",
            "STC1",
            "STIP1",
            "SYTL2",
            "TBK1",
            "TCEA1",
            "TES",
            "TFRC",
            "TM7SF2",
            "TMEM97",
            "TOMM40",
            "TPI1",
            "TRIB3",
            "TUBA4A",
            "TUBG1",
            "TXNRD1",
            "UBE2D3",
            "UCHL5",
            "UFM1",
            "UNG",
            "USO1",
            "VLDLR",
            "WARS1",
            "XBP1",
            "YKT6",
        ],
    ),
]


class TestEvalEnrichment(unittest.TestCase):
    """Test GO Enrichment."""

    def setUp(self) -> None:
        """Set up all engines in advance."""
        self.evaluator = EvalEnrichment()
        self.evaluator.load_annotations(GENES2GO_PATH)
        self.davinci_evaluator = EvalEnrichment(model="gpt-3.5-turbo-instruct")
        self.hgnc = get_adapter("sqlite:obo:hgnc")

    def test_load(self):
        for a in list(self.evaluator.ontology.associations())[0:10]:
            print(a)

    def test_write_gene_sets(self):
        tmpdir = Path(OUTPUT_DIR / "tmp")
        tmpdir.mkdir(exist_ok=True)
        for gs in GENE_SETS:
            name, gene_symbols = gs
            geneset = GeneSet(name=name, gene_symbols=gene_symbols)
            with open(tmpdir / f"{name}.yaml", "w") as f:
                yaml.dump(geneset.dict(), f)

    def test_closure(self):
        engine = self.evaluator
        self.evaluator.load_annotations(GENES2GO_PATH)
        for name, gene_symbols in GENE_SETS:
            gene_set = GeneSet(name=name, gene_symbols=gene_symbols)
            fill_missing_gene_set_values(gene_set, self.hgnc)
            payload = self.evaluator.gene_term_closure(gene_set)
            print(payload)

    def test_standard_enrichment(self):
        """Tests normal OAK enrichment."""
        engine = self.evaluator
        self.evaluator.load_annotations(GENES2GO_PATH)
        for name, gene_symbols in GENE_SETS:
            gene_set = GeneSet(name=name, gene_symbols=gene_symbols)
            fill_missing_gene_set_values(gene_set, self.hgnc)
            payload = self.evaluator.standard_enrichment(gene_set)
            print(payload)

    def test_standard_enrichment_no_ontology(self):
        """Tests normal OAK enrichment."""
        engine = self.evaluator
        self.evaluator.load_annotations(GENES2GO_PATH)
        for name, gene_symbols in GENE_SETS:
            gene_set = GeneSet(name=name, gene_symbols=gene_symbols)
            fill_missing_gene_set_values(gene_set, self.hgnc)
            payload = self.evaluator.standard_enrichment(gene_set, use_ontology=False)
            print(payload)
            self.assertTrue(len(payload.term_ids) > 0)

    def test_random_enrichment(self):
        """Tests random terms."""
        engine = self.evaluator
        self.evaluator.load_annotations(GENES2GO_PATH)
        payload = self.evaluator.random_enrichment()
        print(payload)
        payload2 = self.evaluator.random_enrichment()
        print(payload2)
        # this could conceivably spuriously fail but highly unlikely
        self.assertNotEqual(payload.term_ids, payload2.term_ids)

    def test_null_enrichment(self):
        """Tests null enrichment terms."""
        engine = self.evaluator
        self.evaluator.load_annotations(GENES2GO_PATH)
        genes = ["PEX1", "PEX2", "PEX3", "PEX4"]
        payload = self.evaluator.null_enrichment(genes)
        print(payload)

    def test_random_gene_id(self):
        """Tests random gene id."""
        gene_id = self.evaluator.random_gene_symbol()
        print(gene_id)
        gene_id2 = self.evaluator.random_gene_symbol()
        print(gene_id2)
        self.assertNotEqual(gene_id, gene_id2)

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
        for engine in [self.davinci_evaluator, self.evaluator]:
            RESULTS_PATH.mkdir(exist_ok=True, parents=True)
            outpath = f"{RESULTS_PATH / str(engine.model)}.yaml"
            print(f"OUTPATH: {outpath}")
            self.evaluator.load_annotations(GENES2GO_PATH)
            all = []
            gene_sets = load_gene_sets(GENE_SETS_DIR, get_adapter("sqlite:obo:hgnc"))
            for gene_set in gene_sets.gene_sets:
                print(gene_set)
                comps = engine.evaluate_methods_on_gene_set(gene_set)
                all.extend([comp.dict() for comp in comps])
            with open(outpath, "w") as file:
                file.write(dump_minimal_yaml(all))

    def test_full_v2(self):
        """Tests complete all by all comparisons."""
        for engine in [self.davinci_evaluator, self.evaluator]:
            RESULTS_PATH.mkdir(exist_ok=True, parents=True)
            outpath = f"{RESULTS_PATH / str(engine.model)}.yaml"
            print(f"OUTPATH: {outpath}")
            self.evaluator.load_annotations(GENES2GO_PATH)
            all = []
            gene_sets = load_gene_sets(GENE_SETS_DIR, get_adapter("sqlite:obo:hgnc"))
            for gene_set in gene_sets.gene_sets:
                print(gene_set)
                comps = engine.evaluate_methods_on_gene_set(gene_set)
                all.extend([comp.dict() for comp in comps])
            with open(outpath, "w") as file:
                file.write(dump_minimal_yaml(all))

    def test_full_mini(self):
        """Tests complete all by all comparisons."""
        engine = self.evaluator
        self.evaluator.load_annotations(GENES2GO_PATH)
        all = []
        gene_sets = load_gene_sets(GENE_SETS_DIR)
        print(type(gene_sets))
        for gene_set in gene_sets.gene_sets[0:1]:
            print(gene_set)
            comps = engine.evaluate_methods_on_gene_set(gene_set, max_size=10, n=1)
            print(comps)
            all.extend([comp.dict() for comp in comps])
        with open(RESULTS_PATH, "w") as file:
            print(dump_minimal_yaml(all))
