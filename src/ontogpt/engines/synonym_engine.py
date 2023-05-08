"""Synonym engine."""
from dataclasses import dataclass
from typing import List

from ontogpt.engines.knowledge_engine import KnowledgeEngine


@dataclass
class SynonymEngine(KnowledgeEngine):
    """Engine for generating synonyms."""

    engine: str = "text-davinci-003"

    def synonyms(self, named_entity: str, domain: str) -> List[str]:
        """Get synonyms for a given text."""
        prompt = f"List the example formal scientific\
            synonyms for the {domain} concept {named_entity} as a semi-colon separated list."
        prompt += " Only include terms with identical meaning, not more specific or general terms."
        payload = self.client.complete(prompt)
        return payload.split("; ")
