"""Eval enrichment template."""
import datetime
import gzip
import logging
import random
from collections import defaultdict
from copy import copy
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple

import tiktoken
import yaml
from cachier import cachier
from oaklib import get_adapter, get_implementation_from_shorthand
from oaklib.datamodels.association import Association
from oaklib.datamodels.vocabulary import EQUIVALENT_CLASS, IS_A, PART_OF
from oaklib.interfaces.class_enrichment_calculation_interface import (
    ClassEnrichmentCalculationInterface,
)
from oaklib.interfaces.obograph_interface import OboGraphInterface
from pydantic import BaseModel
from tiktoken import Encoding

from ontogpt.engines import create_engine
from ontogpt.engines.enrichment import (
    ENTITY_ID,
    SYMBOL,
    EnrichmentEngine,
    EnrichmentPayload,
    GeneSet,
    gene_info,
    populate_ids_and_symbols,
)
from ontogpt.engines.knowledge_engine import MODEL_GPT_3_5_TURBO, MODEL_NAME, MODEL_TEXT_DAVINCI_003
from ontogpt.evaluation.evaluation_engine import EvaluationEngine

THIS_DIR = Path(__file__).parent
DATABASE_DIR = Path(__file__).parent / "database"

ONTOLOGICAL_SYNOPSIS = "ontological_synopsis"
NARRATIVE_SYNOPSIS = "narrative_synopsis"
NO_SYNOPSIS = "no_synopsis"
STANDARD = "standard"
STANDARD_NO_ONTOLOGY = "standard_no_ontology"
RANDOM = "random"
RANK_BASED = "rank_based"

ENRICHMENT_MODELS = [MODEL_GPT_3_5_TURBO, MODEL_TEXT_DAVINCI_003]


logger = logging.getLogger(__name__)


class Overlap(BaseModel):
    """Overlap between two sets."""

    jaccard: Optional[float] = None
    common: Optional[List[str]] = None
    overlap_score: Optional[int] = None
    left_jaccard: float = None
    right_jaccard: float = None
    summary_jaccard: float = None


class GeneSetComparison(BaseModel):
    name: str
    gene_symbols: List[str]
    model: str = None
    payloads: Dict[str, EnrichmentPayload] = None
    overlaps: Dict[Tuple[str, str], Overlap] = None
    number_of_genes_swapped_out: int = None


@cachier(stale_after=datetime.timedelta(days=3))
def get_symbol_to_gene_id_map() -> Dict[SYMBOL, ENTITY_ID]:
    hgnc = get_adapter("sqlite:obo:hgnc")
    label2id = {s: id.upper() for id, s in hgnc.labels(hgnc.entities())}
    return label2id


@dataclass
class EvalEnrichment(EvaluationEngine):
    tokenizer_encoding: Encoding = None

    loaded: bool = False

    model: str = None

    engines: Dict[MODEL_NAME, EnrichmentEngine] = field(default_factory=dict)

    def __post_init__(self):
        ontology = get_implementation_from_shorthand("sqlite:obo:go")
        if not isinstance(ontology, OboGraphInterface):
            raise TypeError
        self.ontology: ClassEnrichmentCalculationInterface = ontology
        self.engine: EnrichmentEngine = create_engine(None, EnrichmentEngine, model=self.model)
        for model in ENRICHMENT_MODELS:
            self.engines[model] = create_engine(None, EnrichmentEngine, model=model)
            self.engines[model].add_resolver("sqlite:obo:hgnc")
        self.engine.add_resolver("sqlite:obo:hgnc")
        self.tokenizer_encoding = tiktoken.encoding_for_model(self.engine.model)

    def evaluate_methods_on_gene_set(
        self, gene_set: GeneSet, max_size=999, n=4
    ) -> List[GeneSetComparison]:
        """
        Perform evaluation of different methods on a gene set.

        Different permutations of the gene set are created, dropping out some members, and
        inserting random genes.

        :param gene_set: Gene set to evaluate
        :param max_size: Maximum size of gene set, above this the gene set will be truncated
        :param n: Number of dropouts to perform
        """
        if n < 1:
            raise ValueError(f"n must be greater than 0: {n}")
        if n > 5:
            raise ValueError(f"n must be less than 5: {n}")
        name = gene_set.name
        hgnc = get_adapter("sqlite:obo:hgnc")
        populate_ids_and_symbols(gene_set, hgnc)
        gene_symbols = gene_set.gene_symbols
        comparisons = []
        if len(gene_symbols) <= 1:
            raise ValueError(f"Gene set must have at least two genes: {gene_set}")
        for i in range(0, n):
            logger.info(f"{gene_set.name} [{i}]")
            expt_name = f"{name}-{i}"
            expt_gene_symbols = copy(gene_symbols)
            random.shuffle(expt_gene_symbols)
            num_to_drop = int(len(expt_gene_symbols) * (i / 10))
            logger.info(f"Dropping {num_to_drop} genes (iteration: {i})")
            expt_gene_symbols = expt_gene_symbols[num_to_drop:max_size]
            for _ in range(0, num_to_drop):
                random_gene = self.random_gene_symbol()
                logger.info(f"Adding random gene: {random_gene}")
                expt_gene_symbols.append(random_gene)
            logger.info(f"New symbols: {expt_gene_symbols}")
            comp = self.compare_analysis(
                expt_gene_symbols, expt_name, number_of_genes_swapped_out=num_to_drop
            )
            logger.debug(comp)
            logger.info(yaml.dump(comp.dict(), sort_keys=False))
            comparisons.append(comp)
        return comparisons

    def compare_analysis(
        self, gene_symbols: List[str], name: str = None, **kwargs
    ) -> GeneSetComparison:
        """Compare OntoGPT enrichment vs standard."""
        payloads = {}
        gene_set = GeneSet(name=name, gene_symbols=gene_symbols)
        logger.info(f"Gene symbols: {gene_symbols}")
        for model in ENRICHMENT_MODELS:
            engine = self.engines[model]
            for method in [NO_SYNOPSIS, ONTOLOGICAL_SYNOPSIS, NARRATIVE_SYNOPSIS]:
                if method == ONTOLOGICAL_SYNOPSIS:
                    args = dict(ontological_synopsis=True)
                elif method == NARRATIVE_SYNOPSIS:
                    args = dict(ontological_synopsis=False)
                elif method == NO_SYNOPSIS:
                    args = dict(annotations=False)
                else:
                    raise AssertionError(f"Unknown method: {method}")
                payload = engine.summarize(gene_set, normalize=True, **args)
                payload.method = method
                model_method = f"{model}.{method}"
                payloads[model_method] = payload
        payloads[STANDARD] = self.standard_enrichment(gene_set)
        payloads[STANDARD_NO_ONTOLOGY] = self.standard_enrichment(gene_set, use_ontology=False)
        payloads[RANDOM] = self.random_enrichment(gene_set)
        payloads[RANK_BASED] = self.null_enrichment(gene_set)
        for k in [STANDARD, STANDARD_NO_ONTOLOGY, RANDOM, RANK_BASED]:
            payloads[k].method = k
        comp = GeneSetComparison(
            name=name,
            gene_symbols=gene_symbols,
            payloads=payloads,
            **kwargs,
        )
        return comp

    def random_gene_symbol(self) -> ENTITY_ID:
        """Get a random gene."""
        assocs = list(self.ontology.associations())
        logger.debug(f"Got {len(assocs)} associations")
        ann = random.SystemRandom().choice(assocs)
        info = gene_info(ann.subject)
        return info[0]

    def standard_enrichment(self, gene_set: GeneSet, use_ontology=True) -> EnrichmentPayload:
        """Enrichment."""
        gene_ids = gene_set.gene_ids
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

    def random_enrichment(self, gene_set: GeneSet = None, n: int = None) -> EnrichmentPayload:
        """Randomized enrichment results."""
        if n is None:
            # by default, return a number of terms proportional to the number of genes
            if gene_set:
                n = len(gene_set.gene_symbols)
            else:
                n = 20
        anns = list(self.ontology.associations())
        random.shuffle(anns)
        payload = EnrichmentPayload()
        term_ids = list({ann.object for ann in anns[:n]})
        payload.term_ids = term_ids
        payload.term_strings = [self.ontology.label(id) for id in term_ids]
        return payload

    def null_enrichment(self, gene_set: GeneSet, n: int = None) -> EnrichmentPayload:
        """Psuedo-enrichment, returning all top ranking direct terms, no ontology rollup."""
        gene_symbols = gene_set.gene_symbols
        if n is None:
            # by default, return a number of terms proportional to the number of genes
            n = len(gene_symbols)
        anns = list(self.ontology.associations())
        counts = defaultdict(int)
        for ann in anns:
            counts[ann.object] += 1
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        payload = EnrichmentPayload()
        term_ids = list({term for term, _ in sorted_counts[:n]})
        payload.term_ids = term_ids
        payload.term_strings = [self.ontology.label(id) for id in term_ids]
        return payload

    def create_gene_set_from_term(self, term: ENTITY_ID, name: str = None) -> GeneSet:
        """Create a gene set from a list of terms."""
        assocs = self.ontology.associations(
            objects=[term], object_closure_predicates=[IS_A, PART_OF]
        )
        gene_ids = list(set([str(assoc.subject) for assoc in assocs]))
        hgnc = get_adapter("sqlite:obo:hgnc")
        gene_symbols = [hgnc.label(id) for id in gene_ids]
        gene_symbols = [str(sym) for sym in gene_symbols if sym is not None]
        if name is None:
            name = f"term-{term}"
        return GeneSet(name=name, gene_symbols=gene_symbols, gene_ids=gene_ids)

    def compare_payloads(self, a: EnrichmentPayload, b: EnrichmentPayload) -> Overlap:
        """Compare two payloads."""
        a_ids = set(a.term_ids)
        b_ids = set(b.term_ids)
        overlap = a_ids.intersection(b_ids)
        len_overlap = len(overlap)
        len_union = len(a_ids) + len(b_ids) - len_overlap
        ov = Overlap(
            common=list(overlap),
            overlap_score=len_overlap,
            left_jaccard=len_overlap / len(a_ids) if len(a_ids) else 0,
            right_jaccard=len_overlap / len(b_ids) if len(b_ids) else 0,
            jaccard=len_overlap / len_union if len_union else 0,
        )
        if a.summary and b.summary:
            a_toks = set(self.tokenizer_encoding.encode(a.summary))
            b_toks = set(self.tokenizer_encoding.encode(b.summary))
            overlap_toks = a_toks.intersection(b_toks)
            len_overlap_toks = len(overlap_toks)
            union_toks = a_toks.union(b_toks)
            len_union_toks = len(union_toks)
            ov.summary_jaccard = len_overlap_toks / len_union_toks if len_union_toks else 0
        return ov

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
        for sym, _ in tupls:
            if sym in m:
                yield sym, m[sym]
                continue

    def load_annotations(self, path=None) -> None:
        """Load."""
        if self.loaded:
            return
        m = get_symbol_to_gene_id_map()
        assocs = []
        for sym, term_id in self.get_annotation_tuples(path):
            if sym in m:
                gene_id = m[sym]
                assocs.append(Association(subject=gene_id, object=term_id))
        self.ontology.add_associations(assocs)
        self.loaded = True
