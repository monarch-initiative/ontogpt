from dataclasses import dataclass
from typing import List

import requests

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

@dataclass
class EnrichmentEngine(KnowledgeEngine):
    """Engine for performing term enrichment."""

    engine: str = "text-davinci-003"

    def summarize(self, ids: List[str]) -> List[str]:
        """Summarize gene IDs."""
        genes = []
        for id in ids:
            symbol, desc = self.gene_summary(id)
            genes.append((id, symbol, desc))
        prompt = BASE_PROMPT
        for id, symbol, desc in genes:
            prompt += f"{symbol}: {desc}\n"
        payload = self.client.complete(prompt)
        return payload

    def gene_summary(self, id: str) -> str:
        url = f"https://www.alliancegenome.org/api/gene/{id}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error fetching issues: {response.status_code} // {response.text}")
            raise ValueError()
        obj = response.json()
        symbol = obj["symbol"]
        description = obj["automatedGeneSynopsis"]
        return symbol, description
