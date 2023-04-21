"""Enrichment engine."""
import datetime
import glob
import json
import logging
import re
from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import requests
import yaml
from cachier import cachier
from oaklib import BasicOntologyInterface, get_adapter
from oaklib.interfaces.class_enrichment_calculation_interface import (
    ClassEnrichmentCalculationInterface,
)
from pydantic import BaseModel

from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.templates.gene_description_term import GeneDescriptionTerm

logger = logging.getLogger(__name__)


SUMMARY_KEYWORD = "Summary"
MECHANISM_KEYWORD = "Mechanism"
ENRICHED_TERMS_KEYWORD = "Enriched Terms"

BASE_PROMPT = f"""
I will give you a list of genes together with descriptions of their functions.
Perform a term enrichment test on these genes.
i.e. tell me what the commonalities are in their function.
Make use of classification hierarchies when you do this.
Only report gene functions in common, not diseases.
e.g if gene1 is involved in "toe bone growth" and gene2 is involved in "finger morphogenesis"
then the term "digit development" would be enriched as represented by gene1 and gene2.
Only include terms that are statistically over-represented.
Also include a hypothesis of the underlying biological mechanism or pathway.

Provide results in the format

{SUMMARY_KEYWORD}: <high level summary>
{MECHANISM_KEYWORD}: <mechanism>
{ENRICHED_TERMS_KEYWORD}: <term1>; <term2>; <term3>

###

Here are the gene summaries:
"""

FOOTER = """
Summary and enriched terms:
"""

ANNOTATION_FREE_PROMPT = f"""
I will give you a list of genes symbols.
Perform a term enrichment test on these genes.
i.e. tell me what the commonalities are in their function.
Make use of classification hierarchies when you do this.
Only report gene functions in common, not diseases.
e.g if gene1 is involved in "toe bone growth" and gene2 is involved in "finger morphogenesis"
then the term "digit development" would be enriched as represented by gene1 and gene2.
Only include terms that are statistically over-represented.

Provide results in the format

{SUMMARY_KEYWORD}: <high level summary>
{ENRICHED_TERMS_KEYWORD}: <term1>; <term2>; <term3>

###

Here are the genes:
"""

ENTITY_ID = str
SYMBOL = str
DESCRIPTION = str
GENE_TUPLE = Tuple[ENTITY_ID, SYMBOL, DESCRIPTION]


class GeneSet(BaseModel):
    """A set of genes."""

    name: str
    gene_symbols: Optional[List[str]] = None
    gene_ids: Optional[List[str]] = None
    taxon: str = "human"
    description: Optional[str] = None
    target_term_ids: Optional[List[str]] = None


class GeneSetCollection(BaseModel):
    """A collection of gene sets."""

    gene_sets: List[GeneSet]


class EnrichmentPayload(BaseModel):
    """Payload for enrichment."""

    prompt: str = None
    response_text: str = None
    truncation_factor: float = None
    summary: str = None
    term_strings: List[str] = []
    term_ids: List[str] = []
    ontological_synopsis: bool = None
    combined_synopsis: bool = None
    annotations: bool = None
    response_token_length: int = None
    model: str = None
    method: str = None


def parse_gene_set(input_path: str, format: str = None) -> GeneSet:
    """
    Parse a gene set from a file.

    Accepts:

    - yaml (native gene set format; recommended)
    - json (msigdb format)
    - txt (one gene symbol per line)

    This does no normalization of gene symbols or ids.

    """
    if format is None:
        format = input_path.split(".")[-1]
    if format == "yaml":
        with open(input_path, "r") as f:
            gene_set = GeneSet(**yaml.safe_load(f))
    elif format == "json" or format == "msigdb":
        with open(input_path, "r") as f:
            name, msig = list(json.load(f).items())[0]
            gene_set = GeneSet(name=name, gene_symbols=msig["geneSymbols"])
    elif format == "txt":
        with open(input_path, "r") as f:
            gene_symbols = [line.strip() for line in f.readlines()]
            gene_set = GeneSet(name=input_path, gene_symbols=gene_symbols)
    else:
        raise ValueError(f"Unknown format {format}")
    return gene_set


def load_gene_sets(
    path: str, ontology_adapter: BasicOntologyInterface = None, strict=False
) -> GeneSetCollection:
    """Load gene sets from a folder.

    If ontology_adapter is provided, gene symbols will be converted to gene ids and vice versa.
    """
    gene_sets = []
    for input_path in glob.glob(f"{path}/*.yaml"):
        gene_set = parse_gene_set(input_path)
        gene_sets.append(gene_set)
        if not gene_set.gene_ids and not gene_set.gene_symbols:
            raise ValueError(f"Gene set {gene_set.name} has no gene symbols or ids")
        populate_ids_and_symbols(gene_set, ontology_adapter, strict)
    return GeneSetCollection(gene_sets=gene_sets)


def populate_ids_and_symbols(
    gene_set: GeneSet, ontology_adapter: BasicOntologyInterface = None, strict=False
):
    if ontology_adapter:
        if not gene_set.gene_ids:
            print(f"Fetching ids for {len(gene_set.gene_symbols)} genes")
            gene_set.gene_ids = []
            for sym in gene_set.gene_symbols:
                ids = ontology_adapter.curies_by_label(sym)
                if strict and len(ids) != 1:
                    raise ValueError(f"Could not find a single id for symbol {sym}")
                # hack! normalize casing
                gene_set.gene_ids.extend([id.upper() for id in ids])
        if not gene_set.gene_symbols:
            print(f"Fetching labels for {len(gene_set.gene_ids)} genes")
            gene_set.gene_symbols = []
            for id in gene_set.gene_ids:
                # HACK! lowercase the id to avoid issues with obo-dv-ingest
                lbl = ontology_adapter.label(id.lower())
                print(f"{id} -> {lbl}")
                if lbl:
                    gene_set.gene_symbols.append(lbl)
                else:
                    if strict:
                        raise ValueError(f"Could not find a label for id {id}")


@cachier(stale_after=datetime.timedelta(days=7))
def gene_info(id: ENTITY_ID) -> Tuple[SYMBOL, DESCRIPTION, DESCRIPTION]:
    url = f"https://www.alliancegenome.org/api/gene/{id}"
    logging.info(f"Fetching gene summary from {url}")
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Error fetching issues: {response.status_code} // {response.text}")
    obj = response.json()
    symbol = obj["symbol"]
    return symbol, obj["geneSynopsis"], obj["automatedGeneSynopsis"]


@dataclass
class EnrichmentEngine(KnowledgeEngine):
    """Engine for performing term enrichment.

    Algorithm: SPINDOCTER

    Structured Prompting Interpalating Narrative
    Descriptions Ontology Classification Term Enrichment

    """

    # engine: str = "text-davinci-003"
    # model: str = "xxxgpt-3.5-turbo"

    label_resolvers: Dict[str, BasicOntologyInterface] = field(default_factory=dict)

    completion_length = 250

    def __post_init__(self):
        if not self.template:
            self.template = "gene_description_term"
        super().__post_init__()

    def __key(self):
        return "enrichment_engine"

    def __eq__(self, other):
        if isinstance(other, EnrichmentEngine):
            return self.__key() == other.__key()
        return NotImplemented

    def __hash__(self):
        return hash(self.__key())

    def summarize(
        self,
        gene_set: GeneSet,
        normalize=False,
        strict=False,
        ontological_synopsis=True,
        combined_synopsis=False,
        annotations=True,
    ) -> EnrichmentPayload:
        """
        Summarize a list of gene IDs.

        :param ids: list of gene IDs
        :param normalize: whether to normalize labels to IDs
        :param strict: whether to raise an error if a gene symbol cannot be normalized
        :param ontological_synopsis: whether to use the auto-generated synopsis
        :param combined_synopsis: whether to combine the auto-generated and manual synopsis
        :param annotations: whether to use annotations
        :return: summary
        """
        if not gene_set.gene_ids and not gene_set.gene_symbols:
            raise ValueError(f"Gene set {gene_set.name} has no gene symbols or ids")
        if not gene_set.gene_ids or normalize:
            gene_set.gene_ids = list(self.map_labels(gene_set.gene_symbols, strict=strict))
            logger.info(f"gene ids: {gene_set.gene_ids}")
        gene_tuples = []
        for gene_id in gene_set.gene_ids:
            logging.info(f"Looking up gene summary for {gene_id}...")
            symbol, desc_manual, desc_auto = gene_info(gene_id)
            if combined_synopsis:
                if ontological_synopsis:
                    desc = desc_auto + "; " + desc_manual
                    logging.debug(f"Combined synopsis (priority: auto): {desc}")
                else:
                    desc = desc_manual + "; " + desc_auto
                    logging.debug(f"Combined synopsis (priority: manual): {desc}")
            elif ontological_synopsis:
                desc = desc_auto
                logging.debug(f"Auto synopsis: {desc}")
            else:
                desc = desc_manual
                logging.debug(f"Manual synopsis: {desc}")
            gene_tuples.append((gene_id, symbol, desc))
        logging.info(f"Found {len(gene_tuples)} gene summaries")
        if not annotations:
            return self.summarize_annotation_free(gene_tuples)
        prompt, tf = self._prompt(gene_tuples)
        response_text = self.client.complete(prompt, max_tokens=self.completion_length)
        response_token_length = len(self.encoding.encode(response_text))
        logging.info(f"Response token length: {response_token_length}")
        payload = EnrichmentPayload(
            prompt=prompt,
            response_text=response_text,
            truncation_factor=tf,
            used_auto_synopsis=ontological_synopsis,
            used_combined_synopsis=combined_synopsis,
            annotations=True,
            response_token_length=response_token_length,
            model=self.model,
        )
        self.process_payload(payload)
        return payload

    def summarize_annotation_free(self, genes: List[GENE_TUPLE]) -> EnrichmentPayload:
        """Summarize gene IDs without using any annotations."""
        prompt = ANNOTATION_FREE_PROMPT
        if not genes:
            raise ValueError("No genes provided")
        prompt += "; ".join([symbol for _id, symbol, _desc in genes])
        prompt += FOOTER
        response_text = self.client.complete(prompt)
        response_token_length = len(self.encoding.encode(response_text))
        logging.info(f"Response token length: {response_token_length}")
        payload = EnrichmentPayload(
            prompt=prompt,
            response_text=response_text,
            annotations=False,
            response_token_length=response_token_length,
            model=self.model,
        )
        self.process_payload(payload)
        return payload

    def standard_enrichment(
        self,
        gene_ids: List[ENTITY_ID],
        ontology: ClassEnrichmentCalculationInterface = None,
        predicates: List[ENTITY_ID] = None,
    ) -> EnrichmentPayload:
        """Enrichment using an ontology."""
        if ontology is None:
            ontology = get_adapter("sqlite:obo:go")
        results = ontology.enriched_classes(
            gene_ids, autolabel=True, object_closure_predicates=predicates
        )
        payload = EnrichmentPayload()
        for result in results:
            payload.term_strings.append(result.class_label)
            payload.term_ids.append(result.class_id)
        return payload

    def _prompt(self, genes: List[GENE_TUPLE], truncation_factor=1.0) -> Tuple[str, float]:
        prompt = BASE_PROMPT
        for _, symbol, desc in genes:
            if desc is None:
                desc = ""
            if truncation_factor < 1.0:
                desc = desc[: int(len(desc) * truncation_factor)] + "..."
            prompt += f"{symbol}: {desc}\n"
        # prompt += "\nEnriched terms:"
        prompt += FOOTER
        logging.info(f"Prompt [{truncation_factor}] Length: {len(prompt)}")
        # https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
        prompt_length = len(self.encoding.encode(prompt))
        logging.info(f"Prompt [{truncation_factor}] Tokens: {prompt_length} Strlen={len(prompt)}")
        max_len = 4097 - self.completion_length
        if prompt_length > max_len:  # TODO: check this
            logging.warning(f"Prompt is too long; toks: {prompt_length} len: {len(prompt)}")
            return self._prompt(genes, truncation_factor=truncation_factor * 0.8)
        return prompt, truncation_factor

    def map_labels(self, labels: List[str], strict=False) -> Iterator[ENTITY_ID]:
        """Map labels to IDs."""
        for label in labels:
            if ":" in label and " " not in label:
                yield label
            for adapter in self.label_resolvers.values():
                try:
                    curies = [x.upper() for x in adapter.curies_by_label(label)]
                    if len(curies) != 1:
                        logging.warning(f"Found {len(curies)} curies for label: {label}")
                        if strict:
                            raise ValueError(f"Found {len(curies)} curies for label: {label}")
                    if curies:
                        yield curies[0]
                except ValueError:
                    continue

    def add_resolver(self, resolver: str):
        self.label_resolvers[resolver] = get_adapter(resolver)

    def process_payload(self, payload: EnrichmentPayload) -> EnrichmentPayload:
        """Process the payload."""
        toks = re.split(f"{ENRICHED_TERMS_KEYWORD}:", payload.response_text, flags=re.IGNORECASE)
        if len(toks) > 2:
            logging.warning(
                f"Found more than one {ENRICHED_TERMS_KEYWORD} in response: {payload.response_text}"
            )
            toks[1] = " ".join(toks[1:])
        if len(toks) > 1:
            payload.summary = toks[0]
            rest = toks[1]
        else:
            payload.summary = "COULD NOT PARSE"
            rest = payload.response_text
        if "hypothesis:" in rest.lower():
            # this is a little ad-hoc; turbo is prone to inserting a "hypothesis" at the end
            # even though this is not in the prompt
            toks = re.split("hypothesis:", rest, flags=re.IGNORECASE)
            rest = toks[0]
            payload.summary += "\nHypothesis: " + toks[1]
        # we ask to split on ";" but sometimes the model disobeys and uses "," instead
        tok_chars = [";", ",", "-"]
        tokenizations = {}
        for tok_char in tok_chars:
            toks = rest.split(f"{tok_char} ")
            tokenizations[tok_char] = toks
        tokenizations = sorted(tokenizations.items(), key=lambda x: len(x[1]), reverse=True)
        best_tokens = tokenizations[0][1]
        payload.term_strings = [s.lower().strip(":-*;. -\n") for s in best_tokens]  # noqa
        payload.term_ids = []
        for term in payload.term_strings:
            payload.term_ids.append(self.normalize_named_entity(term, GeneDescriptionTerm.__name__))
        return payload
