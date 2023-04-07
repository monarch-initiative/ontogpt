import datetime
import logging
import re
from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

import requests
from cachier import cachier
from oaklib import BasicOntologyInterface, get_adapter
from pydantic import BaseModel

from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.templates.gene_description_term import GeneDescriptionTerm

SUMMARY_KEYWORD = "Summary"
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

Provide results in the format

{SUMMARY_KEYWORD}: <high level summary>
{ENRICHED_TERMS_KEYWORD}: <term1>; <term2>; <term3>

###

Here are the gene summaries:
"""

FOOTER = """
Summary and enriched terms:
"""

ENTITY_ID = str
SYMBOL = str
DESCRIPTION = str
GENE_TUPLE = Tuple[ENTITY_ID, SYMBOL, DESCRIPTION]


class EnrichmentPayload(BaseModel):
    """Payload for enrichment."""

    prompt: str = None
    response_text: str = None
    truncation_factor: float = None
    summary: str = None
    term_strings: List[str] = []
    term_ids: List[str] = []
    used_auto_synopsis: bool = None
    used_combined_synopsis: bool = None


@dataclass
class EnrichmentEngine(KnowledgeEngine):
    """Engine for performing term enrichment."""

    engine: str = "text-davinci-003"

    label_resolvers: Dict[str, BasicOntologyInterface] = field(default_factory=dict)

    def __post_init__(self):
        if not self.template:
            self.template = "gene_description_term"
        super().__post_init__()

    def summarize(
        self,
        ids: List[ENTITY_ID],
        normalize=False,
        strict=False,
        auto_synopsis=True,
        combined_synopsis=False,
    ) -> EnrichmentPayload:
        """Summarize gene IDs."""
        genes = []
        if normalize:
            logging.info(f"Normalizing {len(ids)} gene IDs: {ids}")
            ids = list(self.map_labels(ids, strict=strict))
            logging.info(f"Normalized {len(ids)} gene IDs => {ids}")
        for id in ids:
            logging.info(f"Fetching gene summary for {id}...")
            symbol, desc_manual, desc_auto = self.gene_info(id)
            if combined_synopsis:
                if auto_synopsis:
                    logging.info(f"Combined synopsis (priority: auto): {desc}")
                    desc = desc_auto + "; " + desc_manual
                else:
                    logging.info(f"Combined synopsis (priority: manual): {desc}")
                    desc = desc_manual + "; " + desc_auto
            elif auto_synopsis:
                desc = desc_auto
                logging.info(f"Auto synopsis: {desc}")
            else:
                desc = desc_manual
                logging.info(f"Manual synopsis: {desc}")
            genes.append((id, symbol, desc))
        prompt, tf = self._prompt(genes)
        response_text = self.client.complete(prompt)
        payload = EnrichmentPayload(
            prompt=prompt,
            response_text=response_text,
            truncation_factor=tf,
            used_auto_synopsis=auto_synopsis,
            used_combined_synopsis=combined_synopsis,
        )
        self.process_payload(payload)
        return payload

    def _prompt(self, genes: List[GENE_TUPLE], truncation_factor=1.0) -> Tuple[str, float]:
        prompt = BASE_PROMPT
        for id, symbol, desc in genes:
            if truncation_factor < 1.0:
                desc = desc[: int(len(desc) * truncation_factor)] + "..."
            prompt += f"{symbol}: {desc}\n"
        # prompt += "\nEnriched terms:"
        prompt += FOOTER
        logging.info(f"Prompt [{truncation_factor}] Length: {len(prompt)}")
        # https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
        if len(prompt) > 4200:  # TODO: use actual tokens;
            logging.warning(f"Prompt is too long: {len(prompt)}")
            return self._prompt(genes, truncation_factor=truncation_factor * 0.8)
        return prompt, truncation_factor

    @cachier(stale_after=datetime.timedelta(days=3))
    def gene_info(self, id: ENTITY_ID) -> Tuple[SYMBOL, DESCRIPTION, DESCRIPTION]:
        url = f"https://www.alliancegenome.org/api/gene/{id}"
        logging.info(f"Fetching gene summary from {url}")
        response = requests.get(url)
        if response.status_code != 200:
            raise ValueError(f"Error fetching issues: {response.status_code} // {response.text}")
        obj = response.json()
        symbol = obj["symbol"]
        return symbol, obj["geneSynopsis"], obj["automatedGeneSynopsis"]

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

        toks = re.split(ENRICHED_TERMS_KEYWORD, payload.response_text, flags=re.IGNORECASE)
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
        payload.term_strings = [s.lower().strip(":-*;. ") for s in rest.split("; ")]
        payload.term_ids = []
        for term in payload.term_strings:
            payload.term_ids.append(self.normalize_named_entity(term, GeneDescriptionTerm.__name__))
        return payload
