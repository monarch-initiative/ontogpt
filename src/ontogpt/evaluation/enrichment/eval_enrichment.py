import datetime
import gzip
import logging
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple

from cachier import cachier
from oaklib import get_adapter, get_implementation_from_shorthand
from oaklib.datamodels.association import Association
from oaklib.datamodels.vocabulary import EQUIVALENT_CLASS, HAS_PART, IS_A, PART_OF
from oaklib.interfaces.class_enrichment_calculation_interface import (
    ClassEnrichmentCalculationInterface,
)
from oaklib.interfaces.obograph_interface import OboGraphInterface
from pydantic import BaseModel

from ontogpt.engines import create_engine
from ontogpt.engines.enrichment import ENTITY_ID, SYMBOL, EnrichmentEngine, EnrichmentPayload
from ontogpt.evaluation.evaluation_engine import EvaluationEngine, SimilarityScore

THIS_DIR = Path(__file__).parent
DATABASE_DIR = Path(__file__).parent / "database"

AUTO = "auto"
MANUAL = "manual"
STANDARD = "standard"
STANDARD_NO_ONTOLOGY = "standard_no_ontology"
RANDOM = "random"


class Overlap(BaseModel):
    """Overlap between two sets."""

    jaccard: Optional[float] = None
    common: Optional[List[str]] = None
    overlap_score: Optional[int] = None
    left_jaccard: float = None
    right_jaccard: float = None


class GeneSetComparison(BaseModel):
    name: str
    gene_symbols: List[str]
    payloads: Dict[str, EnrichmentPayload] = None
    overlaps: Dict[Tuple[str, str], Overlap] = None


@cachier(stale_after=datetime.timedelta(days=3))
def get_symbol_to_gene_id_map() -> Dict[SYMBOL, ENTITY_ID]:
    hgnc = get_adapter("sqlite:obo:hgnc")
    label2id = {s: id.upper() for id, s in hgnc.labels(hgnc.entities())}
    return label2id


@dataclass
class EvalEnrichment(EvaluationEngine):
    def __post_init__(self):
        ontology = get_implementation_from_shorthand("sqlite:obo:go")
        if not isinstance(ontology, OboGraphInterface):
            raise TypeError
        self.ontology: ClassEnrichmentCalculationInterface = ontology
        self.engine: EnrichmentEngine = create_engine(None, EnrichmentEngine)
        self.engine.add_resolver("sqlite:obo:hgnc")

    def compare_analysis_pairwise(
        self, gene_symbols: List[str], name: str = None
    ) -> GeneSetComparison:
        """Compare OntoGPT enrichment vs standard."""
        print("Doing manual enrichment...")
        enrichment_auto = self.engine.summarize(gene_symbols, auto_synopsis=True, normalize=True)
        print("Doing auto enrichment...")
        enrichment_manual = self.engine.summarize(gene_symbols, auto_synopsis=False, normalize=True)
        comp = GeneSetComparison(
            name=name,
            gene_symbols=gene_symbols,
            payloads={MANUAL: enrichment_manual, AUTO: enrichment_auto},
        )
        combos = [(MANUAL, AUTO)]
        print("Comparing...")
        for tup in combos:
            t1, t2 = tup
            p1 = comp.payloads[t1]
            p2 = comp.payloads[t2]
            ov = self.compare_payloads(p1, p2)
            if comp.overlaps is None:
                comp.overlaps = {}
            comp.overlaps[tup] = ov
        return comp

    def compare_analysis(self, gene_symbols: List[str], name: str = None) -> GeneSetComparison:
        """Compare OntoGPT enrichment vs standard."""
        print("Doing manual enrichment...")
        enrichment_auto = self.engine.summarize(gene_symbols, auto_synopsis=True, normalize=True)
        print("Doing auto enrichment...")
        enrichment_manual = self.engine.summarize(gene_symbols, auto_synopsis=False, normalize=True)
        print("Doing standard enrichment...")
        enrichment_standard = self.standard_enrichment(gene_symbols)
        print("Doing standard enrichment, no ontology...")
        enrichment_standard_no_ontology = self.standard_enrichment(gene_symbols, use_ontology=False)
        enrichment_random = self.random_enrichment(gene_symbols)
        comp = GeneSetComparison(
            name=name,
            gene_symbols=gene_symbols,
            payloads={
                MANUAL: enrichment_manual,
                AUTO: enrichment_auto,
                STANDARD: enrichment_standard,
                STANDARD_NO_ONTOLOGY: enrichment_standard_no_ontology,
                RANDOM: enrichment_random,
            },
        )
        combos = [
            (MANUAL, AUTO),
            (MANUAL, STANDARD),
            (AUTO, STANDARD),
            (STANDARD, STANDARD_NO_ONTOLOGY),
            (MANUAL, STANDARD_NO_ONTOLOGY),
            (AUTO, STANDARD_NO_ONTOLOGY),
            (RANDOM, STANDARD),
            (RANDOM, STANDARD_NO_ONTOLOGY),
            (RANDOM, MANUAL),
            (RANDOM, AUTO),
        ]
        print("Comparing...")
        for tup in combos:
            t1, t2 = tup
            p1 = comp.payloads[t1]
            p2 = comp.payloads[t2]
            ov = self.compare_payloads(p1, p2)
            if comp.overlaps is None:
                comp.overlaps = {}
            comp.overlaps[tup] = ov
        return comp

    def standard_enrichment(self, gene_symbols: List[str], use_ontology=True) -> EnrichmentPayload:
        """Standard enrichment."""
        gene_ids = []
        m = get_symbol_to_gene_id_map()
        for sym in gene_symbols:
            if sym in m:
                gene_ids.append(m[sym])
        if use_ontology:
            predicates = [IS_A, PART_OF]
        else:
            predicates = [EQUIVALENT_CLASS]  # TODO
        results = self.ontology.enriched_classes(
            gene_ids, autolabel=True, object_closure_predicates=predicates
        )
        payload = EnrichmentPayload()
        for result in results:
            payload.term_strings.append(result.class_label)
            payload.term_ids.append(result.class_id)
        return payload

    def random_enrichment(self, gene_symbols: List[str], n=20) -> EnrichmentPayload:
        anns = list(self.ontology.associations())
        random.shuffle(anns)
        payload = EnrichmentPayload()
        term_ids = list({ann.object for ann in anns[:n]})
        payload.term_ids = term_ids
        # payload.term_strings = [self.ontology.label(id) for id in term_ids]
        return payload



    def compare_payloads(self, a: EnrichmentPayload, b: EnrichmentPayload) -> Overlap:
        """Compare two payloads."""
        a_ids = set(a.term_ids)
        b_ids = set(b.term_ids)
        overlap = a_ids.intersection(b_ids)
        len_overlap = len(overlap)
        len_union = len(a_ids) + len(b_ids) - len_overlap
        return Overlap(
            common=list(overlap),
            overlap_score=len_overlap,
            left_jaccard=len_overlap / len(a_ids) if len(a_ids) else 0,
            right_jaccard=len_overlap / len(b_ids) if len(b_ids) else 0,
            jaccard=len_overlap / len_union if len_union else 0,
        )

    def get_annotation_tuples(self, path=None) -> Tuple[str, str]:
        """Load."""
        if path is None:
            DATABASE_DIR / "gene2go.tsv.gz"
        with gzip.open(str(path), "rt") as f:
            for line in f.readlines():
                line = line.strip("\n")
                yield tuple(line.split("\t"))

    def get_mapped_annotations(self, path=None) -> Iterator[Tuple[str, str]]:
        """Load."""
        tupls = list(self.get_annotation_tuples(path))
        symbols = set([sym for sym, _ in tupls])
        m = map_hgnc_symbols(tuple(symbols))
        for sym, term_id in tupls:
            if sym in m:
                yield sym, m[sym]
                continue

    def load_annotations(self, path=None) -> None:
        """Load."""
        m = get_symbol_to_gene_id_map()
        assocs = []
        for sym, term_id in self.get_annotation_tuples(path):
            if sym in m:
                gene_id = m[sym]
                assocs.append(Association(subject=gene_id, object=term_id))
        self.ontology.add_associations(assocs)
