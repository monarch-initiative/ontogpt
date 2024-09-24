"""
Synonym engine.

This module defines the SynonymEngine class,
which is responsible for generating synonyms
for given named entities within a specified domain.

Classes:
    SynonymEngine: Inherits from KnowledgeEngine and
    provides a method to retrieve synonyms.

Methods:
    synonyms(named_entity: str, domain: str) -> List[str]:
        Retrieves synonyms for the given named entity
        within the specified domain.
"""

from dataclasses import dataclass
from typing import List

from ontogpt.engines.knowledge_engine import KnowledgeEngine


@dataclass
class SynonymEngine(KnowledgeEngine):
    """Engine for generating synonyms."""

    def synonyms(self, named_entity: str, domain: str) -> List[str]:
        """Get synonyms for a given text."""
        prompt = f"List the example formal scientific\
            synonyms for the {domain} concept {named_entity} as a semi-colon separated list."
        prompt += " Only include terms with identical meaning, not more specific or general terms."
        payload = self.client.complete(prompt)
        return payload.split("; ")
