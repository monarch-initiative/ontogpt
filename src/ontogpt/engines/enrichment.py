import logging
from collections.abc import Iterator
from dataclasses import dataclass, field
from typing import List, Dict

import requests
from oaklib import BasicOntologyInterface, get_adapter

from ontogpt.engines.knowledge_engine import KnowledgeEngine

BASE_PROMPT = """
I will give you a list of genes together with descriptions of their functions.
Perform a term enrichment test on these genes. 
i.e. tell me what the commonalities are in their function.
Make use of classification hierarchies when you do this. 
e.g if gene1 is involved in "toe bone browth" and gene2 is involved in "finger morphogenesis" 
then the term "digit development" would be enriched as represented by gene1 and gene2.

Here are the gene summaries:
"""

ENTITY_ID = str

@dataclass
class EnrichmentEngine(KnowledgeEngine):
    """Engine for performing term enrichment."""

    engine: str = "text-davinci-003"

    label_resolvers: Dict[str, BasicOntologyInterface] = field(default_factory=dict)

    def summarize(self, ids: List[ENTITY_ID], normalize=False, strict=False) -> str:
        """Summarize gene IDs."""
        genes = []
        if normalize:
            logging.info(f"Normalizing {len(ids)} gene IDs: {ids}")
            ids = list(self.map_labels(ids, strict=strict))
            logging.info(f"Normalized {len(ids)} gene IDs => {ids}")
        for id in ids:
            logging.info(f"Fetching gene summary for {id}...")
            symbol, desc = self.gene_summary(id)
            genes.append((id, symbol, desc))
        prompt = BASE_PROMPT
        for id, symbol, desc in genes:
            prompt += f"{symbol}: {desc}\n"
        payload = self.client.complete(prompt)
        return payload

    def gene_summary(self, id: ENTITY_ID) -> str:
        url = f"https://www.alliancegenome.org/api/gene/{id}"
        logging.info(f"Fetching gene summary from {url}")
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error fetching issues: {response.status_code} // {response.text}")
            raise ValueError()
        obj = response.json()
        symbol = obj["symbol"]
        description = obj["automatedGeneSynopsis"]
        return symbol, description

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

