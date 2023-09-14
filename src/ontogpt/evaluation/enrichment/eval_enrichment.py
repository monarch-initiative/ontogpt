"""Eval enrichment template."""
import datetime
import gzip
import logging
import random
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterator, List, Optional, Tuple

import tiktoken
import yaml
from cachier import cachier
from linkml_runtime.dumpers import json_dumper
from oaklib import get_adapter, get_implementation_from_shorthand
from oaklib.datamodels.association import Association
from oaklib.datamodels.vocabulary import EQUIVALENT_CLASS, IS_A, PART_OF
from oaklib.interfaces.class_enrichment_calculation_interface import (
    ClassEnrichmentCalculationInterface,
)
from oaklib.interfaces.obograph_interface import OboGraphInterface
from oaklib.parsers.association_parser_factory import get_association_parser
from pydantic import BaseModel
from tiktoken import Encoding

from ontogpt.engines import create_engine
from ontogpt.engines.enrichment import ENTITY_ID, EnrichmentEngine, EnrichmentPayload
from ontogpt.engines.knowledge_engine import MODEL_NAME
from ontogpt import MODELS
from ontogpt.evaluation.evaluation_engine import EvaluationEngine
from ontogpt.templates.class_enrichment import ClassEnrichmentResult
from ontogpt.utils.gene_set_utils import SYMBOL, GeneSet, drop_genes_from_gene_set, gene_info

THIS_DIR = Path(__file__).parent
DATABASE_DIR = Path(__file__).parent / "database"

ONTOLOGICAL_SYNOPSIS = "ontological_synopsis"
NARRATIVE_SYNOPSIS = "narrative_synopsis"
NO_SYNOPSIS = "no_synopsis"
STANDARD = "standard"
STANDARD_NO_ONTOLOGY = "standard_no_ontology"
RANDOM = "random"
RANK_BASED = "rank_based"
CLOSURE = "closure"

# Set up enrichment-appropriate models
ENRICHMENT_MODELS = [
    model["alternative_names"][0] for model in MODELS if model["provider"] == "OpenAI"
]


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
    gene_ids: List[str] = None
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
        for modelname in ENRICHMENT_MODELS:
            model = modelname["names"][0]
            self.engines[model] = create_engine(None, EnrichmentEngine, model=model)
            self.engines[model].add_resolver("sqlite:obo:hgnc")
        self.engine.add_resolver("sqlite:obo:hgnc")
        self.tokenizer_encoding = tiktoken.encoding_for_model(self.engine.model)

    def evaluate_methods_on_gene_set(
        self, gene_set: GeneSet, max_size=999, n=4, randomize_gene_descriptions=False, **kwargs
    ) -> List[GeneSetComparison]:
        """
        Perform evaluation of different methods on a gene set.

        Different permutations of the gene set are created, dropping out some members, and
        inserting random genes.

        :param gene_set: Gene set to evaluate
        :param max_size: Maximum size of gene set, above this the gene set will be truncated
        :param n: Number of dropouts to perform
        :param randomize_gene_descriptions: use random gene descriptions
        """
        if n < 1:
            raise ValueError(f"n must be greater than 0: {n}")
        if n > 5:
            raise ValueError(f"n must be less than 5: {n}")
        name = gene_set.name
        comparisons = []
        for i in range(0, n):
            perturbed_gene_set = drop_genes_from_gene_set(gene_set, i * 10)
            perturbed_gene_set.name = f"{name}-{i}"
            comp = self.compare_analysis(
                perturbed_gene_set,
            )
            logger.debug(comp)
            logger.info(yaml.dump(comp.dict(), sort_keys=False))
            comparisons.append(comp)
        return comparisons

    def compare_analysis(self, gene_set: GeneSet, **kwargs) -> GeneSetComparison:
        """Compare OntoGPT enrichment vs standard."""
        payloads = {}
        logger.info(f"Gene symbols: {gene_set.gene_symbols}")
        for modelname in ENRICHMENT_MODELS:
            engine = self.engines[modelname[0]]
            for method in [NO_SYNOPSIS, ONTOLOGICAL_SYNOPSIS, NARRATIVE_SYNOPSIS]:
                if method == ONTOLOGICAL_SYNOPSIS:
                    args = dict(ontological_synopsis=True)
                elif method == NARRATIVE_SYNOPSIS:
                    args = dict(ontological_synopsis=False)
                elif method == NO_SYNOPSIS:
                    args = dict(annotations=False)
                else:
                    raise AssertionError(f"Unknown method: {method}")
                for prompt_variant, end_marker in [("v1", "==="), ("v2", "###")]:
                    engine.end_marker = end_marker
                    payload = engine.summarize(gene_set, normalize=True, **args)
                    payload.method = method
                    payload.prompt_variant = prompt_variant
                    model_method = f"{model}.{method}.{prompt_variant}"
                    payloads[model_method] = payload
        payloads[STANDARD] = self.standard_enrichment(gene_set)
        payloads[STANDARD_NO_ONTOLOGY] = self.standard_enrichment(gene_set, use_ontology=False)
        payloads[RANDOM] = self.random_enrichment(gene_set)
        payloads[RANK_BASED] = self.null_enrichment(gene_set)
        payloads[CLOSURE] = self.gene_term_closure(gene_set)
        for k in [STANDARD, STANDARD_NO_ONTOLOGY, RANDOM, RANK_BASED]:
            payloads[k].method = k
        comp = GeneSetComparison(
            name=gene_set.name,
            gene_symbols=gene_set.gene_symbols,
            gene_ids=gene_set.gene_ids,
            number_of_genes_swapped_out=gene_set.number_of_genes_dropped,
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
        """Perform standard gene set enrichment.

        :param gene_set: GeneSet object, with gene_ids populated
        """
        gene_ids = gene_set.gene_ids
        if use_ontology:
            predicates = [IS_A, PART_OF]
        else:
            predicates = [EQUIVALENT_CLASS]  # TODO
        results = self.ontology.enriched_classes(
            gene_ids, autolabel=True, object_closure_predicates=predicates
        )
        # awkward: convert from oaklib dataclasses to pydantic
        results = [ClassEnrichmentResult(**json_dumper.to_dict(result)) for result in results]
        payload = EnrichmentPayload(enrichment_results=results)
        for result in results:
            if result.p_value_adjusted > 0.05:
                continue
            payload.term_strings.append(result.class_label)
            payload.term_ids.append(result.class_id)
        return payload

    def gene_term_closure(self, gene_set: GeneSet) -> EnrichmentPayload:
        gene_ids = gene_set.gene_ids
        term_ids = {a.object for a in self.ontology.associations(subjects=gene_ids)}
        ancs = list(self.ontology.ancestors(list(term_ids), [IS_A, PART_OF]))
        payload = EnrichmentPayload()
        for anc in ancs:
            payload.term_ids.append(anc)
            payload.term_strings.append(self.ontology.label(anc))
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

    def load_annotations(self, path=None, format=None) -> None:
        """
        Load annotations from a two-column TSV file or a GAF.

        :param path:
        :return:
        """
        if self.loaded:
            return
        assocs = []
        if not format:
            if path.endswith(".tsv.gz"):
                format = "tsv.gz"
            elif path.endswith(".gaf"):
                format = "gaf"
            else:
                raise ValueError(f"Unknown format: {format}")
        if format == "tsv.gz":
            # We have a slightly awkward special case for HGNC as the GO GAFs
            # use UniProtKB IDs
            m = get_symbol_to_gene_id_map()
            for sym, term_id in self.get_annotation_tuples(path):
                if sym in m:
                    gene_id = m[sym]
                    assocs.append(Association(subject=gene_id, object=term_id))
        elif format == "gaf":
            association_parser = get_association_parser("gaf")
            with open(path) as file:
                assocs = list(association_parser.parse(file))
        else:
            raise ValueError(f"Unknown format: {format}")
        self.ontology.add_associations(assocs)
        self.loaded = True
