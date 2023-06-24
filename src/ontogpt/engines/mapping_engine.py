"""Synonym engine."""
import logging
from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Callable, Dict, Iterator, List, Optional, Tuple, Union

from jinja2 import Template
from oaklib import BasicOntologyInterface, get_adapter
from oaklib.datamodels.vocabulary import IS_A, SKOS_RELATED_MATCH
from oaklib.interfaces import MappingProviderInterface
from oaklib.types import CURIE
from pydantic import BaseModel
from sssom.parsers import parse_sssom_table, to_mapping_set_document
from sssom_schema import Mapping

from ontogpt.engines.knowledge_engine import KnowledgeEngine
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

    def mappings() -> Dict[str, str]:
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
    subject: CURIE = None
    object: CURIE = None
    completion: str = None
    predicate: Union[MappingPredicate, str] = None
    confidence: Union[Confidence, str] = None
    similarities: List[str] = None
    differences: List[str] = None


class MappingTask(BaseModel):
    subject: CURIE
    object: CURIE
    subject_label: str = None
    object_label: str = None
    subject_source: str = None
    object_source: str = None
    subject_adapter: str = None
    object_adapter: str = None
    predicate: Union[str, MappingPredicate] = None
    difficulty: Confidence = None
    score: float = None


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
    definition: str = None
    synonyms: List[str] = []
    parents: List[str] = []
    relationships: List[Relationship] = []
    categories: List[str] = []


@dataclass
class MappingEngine(KnowledgeEngine):
    """Engine for generating and resolving mappings."""

    subject_adapter: BasicOntologyInterface = None
    object_adapter: BasicOntologyInterface = None

    def categorize_mapping(
        self, subject: CURIE, object: CURIE, template_path: str = None
    ) -> CategorizedMapping:
        if template_path is None:
            template_path = DEFAULT_MAPPING_EVAL_PROMPT
        if isinstance(template_path, Path):
            template_path = str(template_path)
        if isinstance(template_path, str):
            # create a Jinja2 template object
            with open(template_path) as file:
                template_txt = file.read()
                template = Template(template_txt)
        subject_concept = self._concept(subject, self.subject_adapter)
        object_concept = self._concept(object, self.object_adapter)
        prompt = template.render(
            subject=subject_concept,
            object=object_concept,
        )
        payload = self.client.complete(prompt, max_tokens=MAX_TOKENS)
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
        self, subjects: List[CURIE], object_sources: List[CURIE] = None
    ) -> Iterator[CategorizedMapping]:
        sa = self.subject_adapter
        if not isinstance(sa, MappingProviderInterface):
            raise TypeError(f"subject adapter {sa} must implement MappingProviderInterface")
        for object_source in object_sources:
            print(f"EVAL: {object_source} x {subjects}")
            for mapping in sa.sssom_mappings(subjects, source=object_source):
                print(f" MAP: {mapping}")
                yield self.categorize_mapping(mapping.subject_id, mapping.object_id)

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
        task_collection: MappingTaskCollection = None,
        subjects: List[CURIE] = None,
        object_sources: List[CURIE] = None,
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
        for object_source in object_sources:
            for mapping in sa.sssom_mappings(subjects, source=object_source):
                yield MappingTask(
                    subject=mapping.subject_id,
                    object=mapping.object_id,
                    subject_source=mapping.subject_source,
                    object_source=mapping.object_source,
                    subject_adapter=f"sqlite:obo:{mapping.subject_source.lower()}",
                    object_adapter=f"sqlite:obo:{mapping.object_source.lower()}",
                )

    def from_sssom(
        self, path: Union[str, Path], exclude_functions: Optional[List[Callable]] = None
    ) -> MappingTaskCollection:
        """Generate tasks from an SSSOM file."""
        msdf = parse_sssom_table(path)
        msd = to_mapping_set_document(msdf)
        mappings = msd.mapping_set.mappings
        tasks = []
        for mapping in mappings:
            exclude = False
            if exclude_functions:
                for exclude_function in exclude_functions:
                    if exclude_function(mapping):
                        exclude = True
                        break
            if exclude:
                continue

            def _get_source(curie: CURIE) -> str:
                return curie.split(":")[0]

            mapping.subject_source = _get_source(mapping.subject_id)
            mapping.object_source = _get_source(mapping.object_id)
            task = MappingTask(
                subject=mapping.subject_id,
                object=mapping.object_id,
                predicate=MappingPredicate.mappings().get(mapping.predicate_id),
                subject_label=mapping.subject_label,
                object_label=mapping.object_label,
                subject_source=mapping.subject_source,
                object_source=mapping.object_source,
                subject_adapter=f"sqlite:obo:{mapping.subject_source.lower()}",
                object_adapter=f"sqlite:obo:{mapping.object_source.lower()}",
            )
            tasks.append(task)
        return MappingTaskCollection(
            tasks=tasks,
        )

    def categorize_sssom_mapping(
        self,
        mapping: Mapping,
    ) -> Iterator[Tuple[Mapping, CategorizedMapping]]:
        mapping = deepcopy(mapping)

        def _get_source(curie: CURIE) -> str:
            return curie.split(":")[0]

        def _get_adapter(src: str):
            return get_adapter(f"sqlite:obo:{src.lower()}")

        mapping.subject_source = _get_source(mapping.subject_id)
        mapping.object_source = _get_source(mapping.object_id)
        self.subject_adapter = _get_adapter(mapping.subject_source)
        self.object_adapter = _get_adapter(mapping.object_source)
        cm = self.categorize_mapping(mapping.subject_id, mapping.object_id)
        revmap = {v.upper(): k for k, v in MappingPredicate.mappings().items()}
        if cm.predicate.upper() not in revmap:
            logger.warning(f"Unknown predicate {cm.predicate}")
        mapping.predicate_id = revmap.get(cm.predicate.upper(), SKOS_RELATED_MATCH)
        return mapping, cm

    def _concept(self, curie: CURIE, adapter: BasicOntologyInterface) -> Concept:
        """Get a concept."""

        def _label(curie: CURIE) -> str:
            return adapter.label(curie)

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
        return Concept(
            id=str(curie),
            label=label,
            synonyms=sorted(list(adapter.aliases_by_curie(curie))),
            definition=adapter.definition(curie),
            parents=parents,
            relationships=rels,
        )
