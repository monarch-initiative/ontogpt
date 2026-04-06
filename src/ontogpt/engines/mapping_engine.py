"""
Mapping engine.

This module provides the `MappingEngine` class,
which is responsible for generating and resolving
mappings between concepts in different ontologies.
It utilizes various classes and enums to represent
mapping tasks, categorized mappings, and confidence levels.

Classes:
    MappingPredicate: Enum representing different types of mapping predicates.
    Confidence: Enum representing different levels of confidence.
    CategorizedMapping: Model representing a categorized mapping with various attributes.
    MappingTask: Model representing a mapping task with various attributes.
    MappingTaskCollection: Model representing a collection of mapping tasks.
    Relationship: Model representing a relationship between concepts.
    Concept: Model representing a concept with various attributes.
    MappingEngine: Engine class for generating and resolving mappings.

Functions:
    categorize_mapping: Categorizes a mapping between a subject
    and an object using a template.
    _parse: Parses the payload from the categorization process into a `CategorizedMapping`.
    categorize_mappings: Categorizes multiple mappings between subjects and object sources.
    run_tasks: Runs a collection of mapping tasks and categorizes the results.
    generate_tasks: Generates mapping tasks from a collection or
    specified subjects and object sources.
    from_sssom: Generates tasks from an SSSOM file.
    categorize_sssom_mapping: Categorizes a single SSSOM mapping.
    _concept: Retrieves a concept from an ontology adapter.
"""

import logging
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Callable, Dict, Iterator, List, Optional, Tuple, Union, cast

from jinja2 import Template
from oaklib import BasicOntologyInterface, get_adapter
from oaklib.datamodels.vocabulary import IS_A, SKOS_RELATED_MATCH
from oaklib.interfaces import MappingProviderInterface
from oaklib.types import CURIE
from pydantic import BaseModel
from sssom.parsers import parse_sssom_table, to_mapping_set_document
from sssom_schema import Mapping

from ontogpt.engines.knowledge_engine import KnowledgeEngine
from ontogpt.io.utils import read_text_with_fallbacks
from ontogpt.prompts.mapping import DEFAULT_MAPPING_EVAL_PROMPT

logger = logging.getLogger(__name__)

MAX_TOKENS = 300


class MappingPredicate(str, Enum):
    """Mapping predicates."""

    EXACT_MATCH = "exact_match"
    CLOSE_MATCH = "close_match"
    BROADER_THAN = "broader_than"
    NARROWER_THAN = "narrower_than"
    RELATED_TO = "related_to"
    DIFFERENT_FROM = "different_from"
    UNCATEGORIZED = "uncategorized"

    def mappings(self) -> Dict[str, str]:
        """Return the mappings for this predicate."""
        return {
            "skos:exactMatch": "exact_match",
            "skos:closeMatch": "close_match",
            "skos:broadMatch": "broader_than",
            "skos:narrowMatch": "narrower_than",
            "skos:relatedMatch": "related_to",
            "owl:differentFrom": "different",
        }


class Confidence(str, Enum):
    """Confidence levels."""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class CategorizedMapping(BaseModel):
    subject: Optional[CURIE] = None
    object: Optional[CURIE] = None
    completion: Optional[str] = None
    predicate: Optional[Union[MappingPredicate, str]] = None
    confidence: Optional[Union[Confidence, str]] = None
    similarities: Optional[List[str]] = None
    differences: Optional[List[str]] = None


class MappingTask(BaseModel):
    subject: CURIE
    object: CURIE
    subject_label: Optional[str] = None
    object_label: Optional[str] = None
    subject_source: Optional[str] = None
    object_source: Optional[str] = None
    subject_adapter: Optional[str] = None
    object_adapter: Optional[str] = None
    predicate: Optional[Union[str, MappingPredicate]] = None
    difficulty: Optional[Confidence] = None
    score: Optional[float] = None


class MappingTaskCollection(BaseModel):
    name: Optional[str] = None
    predicates: List[MappingPredicate] = []
    subjects: Optional[List[CURIE]] = None
    object_sources: Optional[List[str]] = None
    source_adapters: Optional[Dict[str, str]] = None
    tasks: List[MappingTask] = []


class Relationship(BaseModel):
    predicate: CURIE
    predicate_label: str
    object: CURIE
    object_label: str


class Concept(BaseModel):
    id: CURIE
    label: str
    definition: Optional[str] = None
    synonyms: List[str] = []
    parents: List[str] = []
    relationships: List[Relationship] = []
    categories: List[str] = []


@dataclass
class MappingEngine(KnowledgeEngine):
    """Engine for generating and resolving mappings."""

    subject_adapter: Optional[BasicOntologyInterface] = None
    object_adapter: Optional[BasicOntologyInterface] = None

    @staticmethod
    def _require_curie(value: object, field_name: str) -> CURIE:
        if isinstance(value, str) and value:
            return value
        raise ValueError(f"Expected {field_name} to be a non-empty CURIE string, got {value!r}")

    def _source_from_curie(self, value: object, field_name: str) -> str:
        curie = self._require_curie(value, field_name)
        return curie.split(":", 1)[0]

    def categorize_mapping(
        self, subject: CURIE, object: CURIE, template_path: Optional[str] = None
    ) -> CategorizedMapping:
        if template_path is None:
            template_path = str(DEFAULT_MAPPING_EVAL_PROMPT)
        if len(template_path) == 0:
            template_path = str(DEFAULT_MAPPING_EVAL_PROMPT)
        if isinstance(template_path, Path):
            template_path = str(template_path)
        if not isinstance(template_path, str):
            raise TypeError(f"Unsupported template path type: {type(template_path)}")
        template_txt = read_text_with_fallbacks(Path(template_path))
        template = Template(template_txt)
        subject_concept = self._concept(subject, self.subject_adapter)
        object_concept = self._concept(object, self.object_adapter)
        prompt = template.render(
            subject=subject_concept,
            object=object_concept,
        )
        payload = self._require_client().complete(prompt, max_tokens=MAX_TOKENS)
        cm = self._parse(payload)
        cm.subject = str(subject)
        cm.object = str(object)
        if cm.predicate is None:
            cm.predicate = MappingPredicate.UNCATEGORIZED.value
        return cm

    def _parse(self, payload: str):
        cm = CategorizedMapping(
            completion=payload,
        )

        def _split(s: str, sep: str = ";") -> List[str]:
            if s is None:
                return []
            return [s.strip() for s in s.split(sep)]

        lines = payload.split("\n")
        for line in lines:
            if ":" not in line:
                logger.warning(f"Invalid line {line} in mapping response")
                continue
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if key == "category":
                cm.predicate = value
                # try:
                #    cm.predicate = MappingPredicate[value]
                # except KeyError:
                #    cm.predicate = value
            elif key == "confidence":
                cm.confidence = value
                # try:
                #    cm.confidence = Confidence[value]
                # except KeyError:
                #    cm.confidence = value
            elif key == "similarities":
                cm.similarities = _split(value)
            elif key == "differences":
                cm.differences = _split(value)
            else:
                logger.warning(f"Unknown key {key} in mapping response")
        return cm

    def categorize_mappings(
        self, subjects: List[CURIE], object_sources: Optional[List[str]] = None
    ) -> Iterator[CategorizedMapping]:
        sa = self.subject_adapter
        if not isinstance(sa, MappingProviderInterface):
            raise TypeError(f"subject adapter {sa} must implement MappingProviderInterface")
        mapping_provider = cast(MappingProviderInterface, sa)
        for object_source in object_sources or []:
            print(f"EVAL: {object_source} x {subjects}")
            for mapping in mapping_provider.sssom_mappings(subjects, source=object_source):
                print(f" MAP: {mapping}")
                subject_id = self._require_curie(getattr(mapping, "subject_id", None), "subject_id")
                object_id = self._require_curie(getattr(mapping, "object_id", None), "object_id")
                yield self.categorize_mapping(subject_id, object_id)

    def run_tasks(
        self, task_collection: MappingTaskCollection, evaluate: bool = False
    ) -> Iterator[CategorizedMapping]:
        for task in task_collection.tasks:
            if task.subject_adapter:
                # TODO: do not mutate.
                self.subject_adapter = get_adapter(task.subject_adapter)
            if task.object_adapter:
                # TODO: do not mutate.
                self.object_adapter = get_adapter(task.object_adapter)
            cm = self.categorize_mapping(task.subject, task.object)
            yield cm

    def generate_tasks(
        self,
        task_collection: Optional[MappingTaskCollection] = None,
        subjects: Optional[List[CURIE]] = None,
        object_sources: Optional[List[str]] = None,
    ) -> Iterator[MappingTask]:
        sa = self.subject_adapter
        if task_collection:
            if task_collection.object_sources:
                if object_sources:
                    raise ValueError("object_sources specified twice")
                object_sources = task_collection.object_sources
            if task_collection.subjects:
                if subjects:
                    raise ValueError(
                        "subjects cannot be specified in both task_collection and as an argument"
                    )
                subjects = task_collection.subjects
        if not isinstance(sa, MappingProviderInterface):
            raise TypeError(f"subject adapter {sa} must implement MappingProviderInterface")
        mapping_provider = cast(MappingProviderInterface, sa)
        for object_source in object_sources or []:
            for mapping in mapping_provider.sssom_mappings(subjects or [], source=object_source):
                subject_id = self._require_curie(getattr(mapping, "subject_id", None), "subject_id")
                object_id = self._require_curie(getattr(mapping, "object_id", None), "object_id")
                subject_source = self._source_from_curie(subject_id, "subject_id")
                object_source_name = self._source_from_curie(object_id, "object_id")
                yield MappingTask(
                    subject=subject_id,
                    object=object_id,
                    subject_source=subject_source,
                    object_source=object_source_name,
                    subject_adapter=f"sqlite:obo:{subject_source.lower()}",
                    object_adapter=f"sqlite:obo:{object_source_name.lower()}",
                )

    def from_sssom(
        self, path: Union[str, Path], exclude_functions: Optional[List[Callable]] = None
    ) -> MappingTaskCollection:
        """Generate tasks from an SSSOM file."""
        msdf = parse_sssom_table(path)
        msd = to_mapping_set_document(msdf)
        mappings = msd.mapping_set.mappings or []
        tasks = []
        for mapping in mappings:
            if not isinstance(mapping, Mapping):
                logger.warning(f"Skipping unexpected SSSOM mapping entry: {type(mapping)}")
                continue
            exclude = False
            if exclude_functions:
                for exclude_function in exclude_functions:
                    if exclude_function(mapping):
                        exclude = True
                        break
            if exclude:
                continue
            subject_id = self._require_curie(mapping.subject_id, "subject_id")
            object_id = self._require_curie(mapping.object_id, "object_id")
            subject_source = self._source_from_curie(subject_id, "subject_id")
            object_source = self._source_from_curie(object_id, "object_id")
            mp = MappingPredicate.EXACT_MATCH
            task = MappingTask(
                subject=subject_id,
                object=object_id,
                predicate=mp.mappings().get(mapping.predicate_id),
                subject_label=mapping.subject_label,
                object_label=mapping.object_label,
                subject_source=subject_source,
                object_source=object_source,
                subject_adapter=f"sqlite:obo:{subject_source.lower()}",
                object_adapter=f"sqlite:obo:{object_source.lower()}",
            )
            tasks.append(task)
        return MappingTaskCollection(
            tasks=tasks,
        )

    def categorize_sssom_mapping(
        self,
        mapping: Mapping,
    ) -> Tuple[Mapping, CategorizedMapping]:
        mapping = deepcopy(mapping)

        def _get_adapter(src: str):
            return get_adapter(f"sqlite:obo:{src.lower()}")
        subject_id = self._require_curie(mapping.subject_id, "subject_id")
        object_id = self._require_curie(mapping.object_id, "object_id")
        subject_source = self._source_from_curie(subject_id, "subject_id")
        object_source = self._source_from_curie(object_id, "object_id")
        self.subject_adapter = _get_adapter(subject_source)
        self.object_adapter = _get_adapter(object_source)
        cm = self.categorize_mapping(subject_id, object_id)
        mp = MappingPredicate.EXACT_MATCH
        revmap = {v.upper(): k for k, v in mp.mappings().items()}
        predicate = str(cm.predicate or MappingPredicate.UNCATEGORIZED.value)
        if predicate.upper() not in revmap:
            logger.warning(f"Unknown predicate {predicate}")
        mapping.predicate_id = revmap.get(predicate.upper(), SKOS_RELATED_MATCH)
        return mapping, cm

    def _concept(self, curie: CURIE, adapter: Optional[BasicOntologyInterface]) -> Concept:
        """Get a concept."""
        if adapter is None:
            raise ValueError(f"No adapter configured for {curie}")

        def _label(curie: CURIE) -> str:
            return adapter.label(curie) or str(curie)

        def _relationship(p, o) -> Relationship:
            return Relationship(
                predicate=p,
                predicate_label=_label(p),
                object=o,
                object_label=_label(o),
            )

        parents = [
            _label(rel[2])
            for rel in sorted(list(adapter.relationships([curie], predicates=[IS_A])))
        ]
        rels = [
            _relationship(p, o)
            for _, p, o in sorted(list(adapter.relationships([curie])))
            if p != IS_A
        ]
        label = adapter.label(curie)
        if not label:
            logger.warning(f"Could not find label for {curie} in {adapter}")
            label = str(curie)
        return Concept(
            id=str(curie),
            label=label,
            synonyms=sorted(list(adapter.entity_aliases(curie))),
            definition=adapter.definition(curie),
            parents=parents,
            relationships=rels,
        )
