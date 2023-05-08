"""Similarity engine."""
import logging
from dataclasses import dataclass
from typing import Iterable, List

from oaklib import BasicOntologyInterface
from oaklib.datamodels.vocabulary import IS_A

from ontogpt.clients import OpenAIClient
from ontogpt.engines.knowledge_engine import KnowledgeEngine

logger = logging.getLogger(__name__)


@dataclass
class EmbeddingSimilarity:
    subject_id: str = None
    subject_label: str = None
    object_id: str = None
    object_label: str = None
    embedding_cosine_similarity: float = None
    object_rank_for_subject: int = None


@dataclass
class SimilarityEngine(KnowledgeEngine):
    """Engine for generating synonyms."""

    adapter: BasicOntologyInterface = None
    autolabel: bool = True
    definitions: bool = True
    parents: bool = True
    ancestors: bool = True
    synonyms: bool = True
    logical_definitions: bool = False

    def similarity(self, entity1: str, entity2: str) -> EmbeddingSimilarity:
        """Get similarity."""
        t1 = self.entity_text(entity1)
        t2 = self.entity_text(entity2)
        client = OpenAIClient()
        score = client.similarity(t1, t2)
        obj = EmbeddingSimilarity(
            subject_id=entity1, object_id=entity2, embedding_cosine_similarity=score
        )
        if self.autolabel:
            obj.subject_label = self.adapter.label(entity1)
            obj.object_label = self.adapter.label(entity2)
        return obj

    def search(self, entity1: str, entities: List[str]) -> Iterable[EmbeddingSimilarity]:
        """Get similarity."""
        client = OpenAIClient()
        t1 = self.entity_text(entity1)
        sims = []
        for entity2 in entities:
            t2 = self.entity_text(entity2)
            score = client.similarity(t1, t2)
            sim = EmbeddingSimilarity(
                subject_id=entity1, object_id=entity2, embedding_cosine_similarity=score
            )
            if self.autolabel:
                sim.subject_label = self.adapter.label(entity1)
                sim.object_label = self.adapter.label(entity2)
            sims.append(sim)
        sims = sorted(sims, key=lambda x: x.embedding_cosine_similarity, reverse=True)
        for i, sim in enumerate(sims):
            sim.object_rank_for_subject = i
        yield from sims

    def entity_text(self, entity: str) -> str:
        """Get text for an entity."""
        adapter = self.adapter
        s = f"{adapter.label(entity)}"
        if self.definitions:
            s += f"\ndefinition: {adapter.definition(entity)}"
        if self.parents:
            parent_labels = [
                adapter.label(o) for _s, _p, o in adapter.relationships([entity], [IS_A])
            ]
            s += f"\nparents: {'; '.join(parent_labels)}"
        if self.ancestors:
            ancestor_labels = [
                adapter.label(a) for a in adapter.ancestors([entity], [IS_A], reflexive=False)
            ]
            s += f"\nancestors: {'; '.join(ancestor_labels)}"
        if self.synonyms:
            s += f"\nsynonyms: {'; '.join(adapter.entity_aliases(entity))}"
        if self.logical_definitions:
            for ldef in adapter.logical_definitions(entity):
                genus_labels = [adapter.label(g) for g in ldef.genusIds]
                restriction_labels = [
                    f"{adapter.label(r.propertyId)} {adapter.label(r.valueId)}"
                    for r in ldef.restrictions
                ]
                s += f"\nlogical definition: A {', '.join(genus_labels)} that\
                    {' and '.join(restriction_labels)}"
            s += f"\nlogical definitions: {'; '.join(adapter.logical_definitions(entity))}"
        logger.info(f"Entity text for {entity}: {s}")
        return s
