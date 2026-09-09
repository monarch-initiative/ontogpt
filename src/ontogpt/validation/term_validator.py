"""Validate grounded terms in an extraction result and repair invalid ones.

After SPIRES has produced a full extraction result, every identifier that
grounding placed into the extracted object is checked with
linkml-term-validator: does the term exist in its ontology, is it obsolete,
and does the label the model extracted agree with the ontology's label or one
of its synonyms. Invalid identifiers are repaired by, in order, following an
obsolete term's replacement, re-grounding the extracted label through the
template's annotators, and searching the annotators' ontologies for the label.
When nothing valid turns up the identifier is rewritten with the engine's auto
prefix so that no invalid identifier is left in the output. Every decision is
recorded in a TermValidationReport attached to the result.
"""

import logging
from dataclasses import dataclass, field
from importlib import metadata
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, Iterator, List, Optional, Tuple, Union
from urllib.parse import quote

import pydantic
from linkml_runtime.linkml_model import ClassDefinition

from ontogpt.templates.core import (
    ExtractionResult,
    TermValidationReport,
    TermValidationResult,
    TermValidationStatus,
)

if TYPE_CHECKING:
    from ontogpt.engines.knowledge_engine import KnowledgeEngine

logger = logging.getLogger(__name__)

try:
    VALIDATOR_NAME = f"linkml-term-validator {metadata.version('linkml-term-validator')}"
except metadata.PackageNotFoundError:  # pragma: no cover
    VALIDATOR_NAME = "linkml-term-validator"

# The identifier of the "term replaced by" annotation property in OBO ontologies.
REPLACED_BY = "IAO:0100001"

# Prefixes whose sqlite:obo: builds are known to exist, used when a template's
# annotators do not name the prefix's own ontology. Keys are lower-case.
KNOWN_SQLITE_BUILDS = {
    "biolink",
    "chebi",
    "cl",
    "doid",
    "drugbank",
    "efo",
    "emapa",
    "envo",
    "fbbt",
    "foodon",
    "go",
    "hgnc",
    "hp",
    "maxo",
    "mesh",
    "mondo",
    "mp",
    "nbo",
    "ncbitaxon",
    "ncit",
    "oba",
    "obi",
    "opmi",
    "pato",
    "peco",
    "po",
    "pr",
    "pw",
    "ro",
    "so",
    "to",
    "uberon",
    "uo",
    "vbo",
    "wbbt",
    "zfa",
}

# Annotator selectors that expose label lookup and can serve as validation adapters.
CHECKABLE_SELECTOR_SCHEMES = ("sqlite:", "bioportal:", "ols:", "ubergraph:", "obo:", "pronto:")


def _normalize(text: str) -> str:
    from linkml_term_validator.utils import normalize_string

    return normalize_string(text)


def _selector_slug(selector: str) -> str:
    """Return the ontology name part of an OAK selector, e.g. 'mondo' for sqlite:obo:mondo."""
    slug = selector.split(":")[-1]
    return Path(slug).stem.lower() if "/" in slug or slug.endswith(".db") else slug.lower()


@dataclass
class EntityRef:
    """A grounded identifier found in the extracted object, with where it lives."""

    container: Any
    key: Union[str, int]
    curie: str
    class_name: str

    def set(self, new_id: str) -> None:
        if isinstance(self.key, int):
            self.container[self.key] = new_id
        else:
            setattr(self.container, self.key, new_id)


@dataclass
class TermValidator:
    """Validate and repair grounded terms in an ExtractionResult."""

    engine: "KnowledgeEngine"
    """The engine that produced the result; supplies the schema, annotators, and grounding."""

    max_attempts: int = 8
    """Maximum number of candidate replacements to examine per invalid term."""

    prefix_adapters: Dict[str, Any] = field(default_factory=dict)
    """Explicit prefix to OAK selector (or adapter object) overrides."""

    cache_dir: Optional[Path] = None
    """Where linkml-term-validator caches labels; defaults to a pystow directory."""

    _access: Any = field(default=None, init=False, repr=False)
    _validator: Any = field(default=None, init=False, repr=False)
    _prefix_map: Dict[str, str] = field(default_factory=dict, init=False, repr=False)
    _resolved: Dict[str, str] = field(default_factory=dict, init=False, repr=False)
    """CURIE as produced by grounding to the spelling the adapter resolved."""

    # ------------------------------------------------------------------
    # Setup
    # ------------------------------------------------------------------

    def _ensure_validator(self) -> None:
        if self._validator is not None:
            return
        from linkml_term_validator.models import ValidationConfig
        from linkml_term_validator.validator import EnumValidator

        if self.cache_dir is None:
            import pystow

            self.cache_dir = pystow.join("ontogpt", "term-validator-cache")
        config = ValidationConfig(
            oak_adapter_string="sqlite:obo:",
            strict_mode=True,
            cache_labels=True,
            cache_dir=Path(self.cache_dir),
        )
        self._validator = EnumValidator(config)
        self._access = self._validator.ontology
        self._prefix_map = self._build_prefix_map()
        # The validator resolves adapters per prefix from this mapping. Prefixes
        # absent from it are reported as unresolvable, never guessed.
        self._access.oak_config = dict(self._prefix_map)
        for prefix, selector in self._prefix_map.items():
            override = self.prefix_adapters.get(prefix)
            if override is not None and not isinstance(override, str):
                self._access._adapter_cache[prefix] = override
            elif self.engine.annotators and selector in self.engine.annotators:
                # Reuse an adapter the engine already opened.
                self._access._adapter_cache[prefix] = self.engine.annotators[selector]

    def _entity_classes(self) -> List[ClassDefinition]:
        sv = self.engine.schemaview
        if sv is None:
            return []
        return [
            c
            for c in sv.all_classes().values()
            if c.name != "NamedEntity" and "NamedEntity" in sv.class_ancestors(c.name)
        ]

    def _class_selectors(self, cls: ClassDefinition) -> List[str]:
        value = self.engine._annotation_value(cls.annotations, "annotators")
        if not value:
            return []
        return [a.strip() for a in value.split(",") if a.strip()]

    def _build_prefix_map(self) -> Dict[str, str]:
        """Map each identifier prefix used by the template to an OAK selector.

        A prefix maps to the annotator whose ontology name matches it (MONDO to
        sqlite:obo:mondo). Prefixes without such an annotator fall back to a
        known sqlite:obo: build. Anything else is left unmapped and skipped.
        """
        mapping: Dict[str, str] = {}
        for prefix, override in self.prefix_adapters.items():
            mapping[prefix] = override if isinstance(override, str) else f"override:{prefix}"
        for cls in self._entity_classes():
            selectors = [
                s for s in self._class_selectors(cls) if s.startswith(CHECKABLE_SELECTOR_SCHEMES)
            ]
            for prefix in cls.id_prefixes or []:
                if prefix in mapping:
                    continue
                for selector in selectors:
                    if _selector_slug(selector) == prefix.lower():
                        mapping[prefix] = selector
                        break
        for cls in self._entity_classes():
            for prefix in cls.id_prefixes or []:
                if prefix not in mapping and prefix.lower() in KNOWN_SQLITE_BUILDS:
                    mapping[prefix] = f"sqlite:obo:{prefix.lower()}"
        return mapping

    # ------------------------------------------------------------------
    # Walking the extracted object
    # ------------------------------------------------------------------

    def _is_entity_class(self, name: Optional[str]) -> bool:
        sv = self.engine.schemaview
        if sv is None or not name or name not in sv.all_classes():
            return False
        return "NamedEntity" in sv.class_ancestors(name)

    def iter_entity_refs(self, obj: Any, class_name: str) -> Iterator[EntityRef]:
        """Yield every grounded identifier in obj with its template class."""
        sv = self.engine.schemaview
        if sv is None or obj is None or not isinstance(obj, pydantic.BaseModel):
            return
        if class_name not in sv.all_classes():
            return
        for slot in sv.class_induced_slots(class_name):
            value = getattr(obj, slot.name, None)
            if value is None:
                continue
            rng = slot.range
            if self._is_entity_class(rng):
                if isinstance(value, list):
                    for i, item in enumerate(value):
                        if isinstance(item, str):
                            yield EntityRef(value, i, item, str(rng))
                        elif isinstance(item, pydantic.BaseModel):
                            yield from self.iter_entity_refs(item, str(rng))
                elif isinstance(value, str):
                    yield EntityRef(obj, slot.name, value, str(rng))
                elif isinstance(value, pydantic.BaseModel):
                    yield from self.iter_entity_refs(value, str(rng))
            elif rng and rng in sv.all_classes():
                if isinstance(value, list):
                    for item in value:
                        yield from self.iter_entity_refs(item, str(rng))
                else:
                    yield from self.iter_entity_refs(value, str(rng))

    # ------------------------------------------------------------------
    # Checking one term
    # ------------------------------------------------------------------

    def _is_checkable(self, curie: str) -> bool:
        if ":" not in curie or curie.startswith("LIKELY HALLUCINATION"):
            return False
        prefix = curie.split(":", 1)[0]
        auto = self.engine.auto_prefix or "AUTO"
        return prefix not in (auto, "AUTO") and bool(prefix)

    def _label_for(self, result: ExtractionResult, curie: str) -> Optional[str]:
        for ne in result.named_entities or []:
            if getattr(ne, "id", None) == curie:
                return getattr(ne, "label", None)
        return None

    def _adapter_for(self, curie: str) -> Any:
        return self._access.get_adapter(curie.split(":", 1)[0])

    def _aliases(self, curie: str) -> List[str]:
        adapter = self._adapter_for(curie)
        if adapter is None:
            return []
        try:
            return [a for a in adapter.entity_aliases(self._resolved.get(curie, curie)) if a]
        except Exception as e:  # noqa: BLE001
            logger.debug(f"Could not fetch aliases for {curie}: {e}")
            return []

    @staticmethod
    def _prefix_variants(curie: str) -> List[str]:
        """Spellings of a CURIE's prefix that an ontology build may use for its own ids."""
        prefix, local = curie.split(":", 1)
        variants = [curie, f"{prefix.lower()}:{local}", f"{prefix.upper()}:{local}"]
        return list(dict.fromkeys(variants))

    def _term_ok(self, curie: str) -> Tuple[bool, Optional[str], str]:
        """Return (is_valid, ontology_label, reason) for a CURIE.

        Some builds store their identifiers with a differently cased prefix
        than the one OntoGPT normalizes to (drugbank:DB01136 versus
        DRUGBANK:DB01136), so a miss is retried with prefix case variants
        against the same adapter before the term is called missing.
        """
        label = self._access.get_label(curie)
        resolved = curie
        adapter = self._adapter_for(curie)
        if label is None and adapter is not None:
            for variant in self._prefix_variants(curie)[1:]:
                try:
                    label = adapter.label(variant)
                except Exception as e:  # noqa: BLE001
                    logger.debug(f"Label lookup for {variant} failed: {e}")
                    label = None
                if label:
                    resolved = variant
                    break
        if label is None:
            return False, None, "not found in ontology"
        self._resolved[curie] = resolved
        if resolved == curie:
            obsolete = self._access.is_obsolete(curie)
        else:
            obsoletes = self._access._get_obsoletes_set(curie.split(":", 1)[0], adapter)
            obsolete = bool(obsoletes and resolved in obsoletes)
        if obsolete:
            return False, label, "obsolete"
        return True, label, ""

    def _label_agrees(self, curie: str, extracted: Optional[str], ontology_label: str) -> bool:
        if not extracted:
            return True
        wanted = _normalize(extracted)
        if wanted == _normalize(ontology_label):
            return True
        return any(_normalize(a) == wanted for a in self._aliases(curie))

    # ------------------------------------------------------------------
    # Finding replacements
    # ------------------------------------------------------------------

    def _candidates(self, curie: str, label: Optional[str], cls: ClassDefinition) -> Iterator[str]:
        """Yield replacement candidates in priority order."""
        prefix = curie.split(":", 1)[0]
        adapter = self._access.get_adapter(prefix)
        # 1. An obsolete term names its successor.
        if adapter is not None:
            try:
                resolved = self._resolved.get(curie, curie)
                replaced_by = adapter.entity_metadata_map(resolved).get(REPLACED_BY) or []
                if isinstance(replaced_by, str):
                    replaced_by = [replaced_by]
                for rep in replaced_by:
                    yield str(rep)
            except Exception as e:  # noqa: BLE001
                logger.debug(f"No replacement metadata for {curie}: {e}")
        if not label:
            return
        # 2. Ground the extracted label again through the template's annotators.
        try:
            for grounded in self.engine.groundings(label, cls):
                for normalized in self.engine.normalize_identifier(grounded, cls):
                    yield normalized
        except Exception as e:  # noqa: BLE001
            logger.debug(f"Re-grounding {label!r} failed: {e}")
        # 3. Search the class's ontologies for the label.
        for search_adapter in self._search_adapters(cls):
            try:
                for hit in list(search_adapter.basic_search(label))[:5]:
                    yield str(hit)
            except Exception as e:  # noqa: BLE001
                logger.debug(f"Search for {label!r} failed: {e}")

    def _search_adapters(self, cls: ClassDefinition) -> List[Any]:
        """Adapters to search for a class: engine overrides first, else its annotators."""
        if self.engine.annotators and cls.name in self.engine.annotators:
            return [a for a in self.engine.annotators[cls.name] if not isinstance(a, str)]
        adapters: List[Any] = []
        for selector in self._class_selectors(cls):
            if not selector.startswith(CHECKABLE_SELECTOR_SCHEMES):
                continue
            try:
                if self.engine.annotators is None:
                    self.engine.annotators = {}
                if selector not in self.engine.annotators:
                    from oaklib import get_adapter

                    self.engine.annotators[selector] = get_adapter(selector)
                adapters.append(self.engine.annotators[selector])
            except Exception as e:  # noqa: BLE001
                logger.debug(f"Could not open {selector} for search: {e}")
        return adapters

    def _find_replacement(
        self, curie: str, label: Optional[str], cls: ClassDefinition, require_label_match: bool
    ) -> Tuple[Optional[str], Optional[str], List[str]]:
        """Return (replacement_id, replacement_label, attempts)."""
        attempts: List[str] = []
        seen = {curie}
        for candidate in self._candidates(curie, label, cls):
            if candidate in seen:
                continue
            seen.add(candidate)
            if len(attempts) >= self.max_attempts:
                break
            attempts.append(candidate)
            if not self._is_checkable(candidate):
                continue
            if cls.id_prefixes and not self.engine.is_valid_identifier(candidate, cls):
                continue
            ok, cand_label, _ = self._term_ok(candidate)
            if not ok or cand_label is None:
                continue
            if require_label_match and not self._label_agrees(candidate, label, cand_label):
                continue
            return candidate, cand_label, attempts
        return None, None, attempts

    # ------------------------------------------------------------------
    # Main entry point
    # ------------------------------------------------------------------

    def validate(
        self, result: ExtractionResult, root_class: Optional[str] = None
    ) -> TermValidationReport:
        """Validate every grounded term in result, repairing in place, and attach a report."""
        self._ensure_validator()
        sv = self.engine.schemaview
        if root_class is None:
            root_class = type(result.extracted_object).__name__ if result.extracted_object else None
        report = TermValidationReport(
            validator=VALIDATOR_NAME,
            total_terms=0,
            valid_terms=0,
            replaced_terms=0,
            unresolved_terms=0,
            label_mismatches=0,
            skipped_terms=0,
            results=[],
        )
        if sv is None or result.extracted_object is None or root_class is None:
            result.validation = report
            return report

        refs = list(self.iter_entity_refs(result.extracted_object, root_class))
        decisions: Dict[Tuple[str, str], TermValidationResult] = {}
        for ref in refs:
            if not self._is_checkable(ref.curie):
                continue
            key = (ref.curie, ref.class_name)
            if key not in decisions:
                decisions[key] = self._decide(result, ref.curie, ref.class_name)
            decision = decisions[key]
            if decision.replacement_id:
                ref.set(decision.replacement_id)

        # Apply replacements to the named entity list as well.
        for decision in decisions.values():
            if not decision.replacement_id:
                continue
            for ne in result.named_entities or []:
                if getattr(ne, "id", None) == decision.original_id:
                    ne.id = decision.replacement_id

        for decision in decisions.values():
            report.results.append(decision)
            report.total_terms += 1
            if decision.status == TermValidationStatus.VALID:
                report.valid_terms += 1
            elif decision.status == TermValidationStatus.REPLACED:
                report.replaced_terms += 1
            elif decision.status == TermValidationStatus.UNRESOLVED:
                report.unresolved_terms += 1
            elif decision.status == TermValidationStatus.LABEL_DIFFERS:
                report.label_mismatches += 1
            else:
                report.skipped_terms += 1
        result.validation = report
        logger.info(
            f"Term validation: {report.total_terms} checked, {report.valid_terms} valid, "
            f"{report.replaced_terms} replaced, {report.unresolved_terms} unresolved, "
            f"{report.label_mismatches} label mismatches, {report.skipped_terms} skipped"
        )
        return report

    def _decide(
        self, result: ExtractionResult, curie: str, class_name: str
    ) -> TermValidationResult:
        sv = self.engine.schemaview
        cls = sv.get_class(class_name) if sv else None
        label = self._label_for(result, curie)
        prefix = curie.split(":", 1)[0]
        outcome = TermValidationResult(
            original_id=curie, label=label, entity_class=class_name, attempts=[]
        )
        if prefix not in self._prefix_map or cls is None:
            outcome.status = TermValidationStatus.SKIPPED
            outcome.message = f"No ontology adapter available for prefix {prefix}"
            return outcome
        try:
            ok, ontology_label, reason = self._term_ok(curie)
        except Exception as e:  # noqa: BLE001
            outcome.status = TermValidationStatus.SKIPPED
            outcome.message = f"Could not check {curie}: {e}"
            return outcome
        outcome.ontology_label = ontology_label

        if ok and ontology_label is not None:
            if self._label_agrees(curie, label, ontology_label):
                outcome.status = TermValidationStatus.VALID
                outcome.message = (
                    "Label matches"
                    if not label or _normalize(label) == _normalize(ontology_label)
                    else "Label matches a synonym"
                )
                return outcome
            # Resolves, but the extracted label is not this term. Only swap it
            # for a term whose label or synonym is exactly the extracted label.
            rep, rep_label, attempts = self._find_replacement(curie, label, cls, True)
            outcome.attempts = attempts
            if rep:
                outcome.status = TermValidationStatus.REPLACED
                outcome.replacement_id = rep
                outcome.replacement_label = rep_label
                outcome.message = (
                    f"Extracted label {label!r} is not a label or synonym of {curie} "
                    f"({ontology_label!r}); replaced with an exact match"
                )
            else:
                outcome.status = TermValidationStatus.LABEL_DIFFERS
                outcome.message = (
                    f"Extracted label {label!r} is not a label or synonym of {curie} "
                    f"({ontology_label!r}); kept"
                )
            return outcome

        # Invalid: missing or obsolete. Take any valid substitute.
        rep, rep_label, attempts = self._find_replacement(curie, label, cls, False)
        outcome.attempts = attempts
        if rep:
            outcome.status = TermValidationStatus.REPLACED
            outcome.replacement_id = rep
            outcome.replacement_label = rep_label
            outcome.message = f"{curie} is {reason}; replaced"
            return outcome
        auto = self.engine.auto_prefix or "AUTO"
        outcome.status = TermValidationStatus.UNRESOLVED
        outcome.replacement_id = f"{auto}:{quote(label or curie)}"
        outcome.message = (
            f"{curie} is {reason} and no valid replacement was found after "
            f"{len(attempts)} candidate(s); value rewritten with the {auto} prefix"
        )
        return outcome
