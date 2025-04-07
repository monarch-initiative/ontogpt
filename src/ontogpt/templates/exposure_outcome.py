# Auto generated from exposure_outcome.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-04-07T12:42:29
# Schema: exposure_outcome
#
# id: http://w3id.org/ontogpt/exposure_outcome
# description: Schema to represent metadata associated with exposure-outcome modeling
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
EXPOSURE_OUTCOME = CurieNamespace('exposure_outcome', 'http://w3id.org/ontogpt/exposure_outcome')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = EXPOSURE_OUTCOME


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class ExposureEventId(NamedThingId):
    pass


class ChemicalEntityId(NamedThingId):
    pass


class PhenotypeId(NamedThingId):
    pass


class NamedEntityId(extended_str):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic class for named entities. Often used to anchor identifiers and human-readable labels for ontology
    classes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["NamedThing"]
    class_class_curie: ClassVar[str] = "exposure_outcome:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureEvent(NamedThing):
    """
    A record of a toxicological exposure, usually representing a chemical or environmental factor impacting an
    organism. Can be mapped to ontology concepts from ECTO.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ExposureEvent"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ExposureEvent"
    class_name: ClassVar[str] = "ExposureEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ExposureEvent

    id: Union[str, ExposureEventId] = None
    exposure_substance: Optional[Union[str, URIorCURIE]] = None
    exposure_type: Optional[Union[str, "ExposureTypeEnum"]] = None
    concentration: Optional[str] = None
    duration: Optional[Union[dict, "QuantityValue"]] = None
    frequency: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExposureEventId):
            self.id = ExposureEventId(self.id)

        if self.exposure_substance is not None and not isinstance(self.exposure_substance, URIorCURIE):
            self.exposure_substance = URIorCURIE(self.exposure_substance)

        if self.concentration is not None and not isinstance(self.concentration, str):
            self.concentration = str(self.concentration)

        if self.duration is not None and not isinstance(self.duration, QuantityValue):
            self.duration = QuantityValue()

        if self.frequency is not None and not isinstance(self.frequency, QuantityValue):
            self.frequency = QuantityValue()

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntity(NamedThing):
    """
    A chemical compound or drug used as a toxicant in an exposure study. Should ideally map to a CHEBI class.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ChemicalEntity"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ChemicalEntity"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Phenotype(NamedThing):
    """
    A phenotypic abnormality or observable feature resulting from a toxicant exposure. Should be mapped to Human
    Phenotype Ontology (HPO) where possible.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["Phenotype"]
    class_class_curie: ClassVar[str] = "exposure_outcome:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Phenotype

    id: Union[str, PhenotypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeId):
            self.id = PhenotypeId(self.id)

        super().__post_init__(**kwargs)


class Annotation(YAMLRoot):
    """
    Abstract class used to group annotation-like records, including quantitative values.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["Annotation"]
    class_class_curie: ClassVar[str] = "exposure_outcome:Annotation"
    class_name: ClassVar[str] = "Annotation"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Annotation


class QuantityValue(Annotation):
    """
    A measurement represented as a numeric value and an associated unit (e.g. 5 mg/L). Useful for concentration,
    frequency, and duration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["QuantityValue"]
    class_class_curie: ClassVar[str] = "exposure_outcome:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.QuantityValue


class Concentration(QuantityValue):
    """
    A numeric concentration (e.g. 3.5 µg/mL) of a toxicant used in an exposure.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["Concentration"]
    class_class_curie: ClassVar[str] = "exposure_outcome:Concentration"
    class_name: ClassVar[str] = "Concentration"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Concentration


@dataclass(repr=False)
class ExposureOutcomeEvent(YAMLRoot):
    """
    A specific linkage between an exposure and the resulting phenotypes. A document that contains exposure to outcome
    relations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ExposureOutcomeEvent"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ExposureOutcomeEvent"
    class_name: ClassVar[str] = "ExposureOutcomeEvent"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ExposureOutcomeEvent

    exposure_event: Optional[Union[str, ExposureEventId]] = None
    outcome: Optional[Union[Union[str, PhenotypeId], List[Union[str, PhenotypeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.exposure_event is not None and not isinstance(self.exposure_event, ExposureEventId):
            self.exposure_event = ExposureEventId(self.exposure_event)

        if not isinstance(self.outcome, list):
            self.outcome = [self.outcome] if self.outcome is not None else []
        self.outcome = [v if isinstance(v, PhenotypeId) else PhenotypeId(v) for v in self.outcome]

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class ExtractionResult(YAMLRoot):
    """
    A result of extracting knowledge on text
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["ExtractionResult"]
    class_class_curie: ClassVar[str] = "core:ExtractionResult"
    class_name: ClassVar[str] = "ExtractionResult"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ExtractionResult

    input_id: Optional[str] = None
    input_title: Optional[str] = None
    input_text: Optional[str] = None
    raw_completion_output: Optional[str] = None
    prompt: Optional[str] = None
    extracted_object: Optional[Union[dict, Any]] = None
    named_entities: Optional[Union[Union[dict, Any], List[Union[dict, Any]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.input_id is not None and not isinstance(self.input_id, str):
            self.input_id = str(self.input_id)

        if self.input_title is not None and not isinstance(self.input_title, str):
            self.input_title = str(self.input_title)

        if self.input_text is not None and not isinstance(self.input_text, str):
            self.input_text = str(self.input_text)

        if self.raw_completion_output is not None and not isinstance(self.raw_completion_output, str):
            self.raw_completion_output = str(self.raw_completion_output)

        if self.prompt is not None and not isinstance(self.prompt, str):
            self.prompt = str(self.prompt)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedEntity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["NamedEntity"]
    class_class_curie: ClassVar[str] = "core:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.NamedEntity

    id: Union[str, NamedEntityId] = None
    label: Optional[str] = None
    original_spans: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if not isinstance(self.original_spans, list):
            self.original_spans = [self.original_spans] if self.original_spans is not None else []
        self.original_spans = [v if isinstance(v, str) else str(v) for v in self.original_spans]

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["CompoundExpression"]
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.CompoundExpression


@dataclass(repr=False)
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Triple"]
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Triple

    subject: Optional[Union[str, NamedEntityId]] = None
    predicate: Optional[Union[str, RelationshipTypeId]] = None
    object: Optional[Union[str, NamedEntityId]] = None
    qualifier: Optional[str] = None
    subject_qualifier: Optional[Union[str, NamedEntityId]] = None
    object_qualifier: Optional[Union[str, NamedEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NamedEntityId):
            self.subject = NamedEntityId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, RelationshipTypeId):
            self.predicate = RelationshipTypeId(self.predicate)

        if self.object is not None and not isinstance(self.object, NamedEntityId):
            self.object = NamedEntityId(self.object)

        if self.qualifier is not None and not isinstance(self.qualifier, str):
            self.qualifier = str(self.qualifier)

        if self.subject_qualifier is not None and not isinstance(self.subject_qualifier, NamedEntityId):
            self.subject_qualifier = NamedEntityId(self.subject_qualifier)

        if self.object_qualifier is not None and not isinstance(self.object_qualifier, NamedEntityId):
            self.object_qualifier = NamedEntityId(self.object_qualifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextWithTriples(YAMLRoot):
    """
    A text containing one or more relations of the Triple type.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["TextWithTriples"]
    class_class_curie: ClassVar[str] = "core:TextWithTriples"
    class_name: ClassVar[str] = "TextWithTriples"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.TextWithTriples

    publication: Optional[Union[dict, "Publication"]] = None
    triples: Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.publication is not None and not isinstance(self.publication, Publication):
            self.publication = Publication(**as_dict(self.publication))

        if not isinstance(self.triples, list):
            self.triples = [self.triples] if self.triples is not None else []
        self.triples = [v if isinstance(v, Triple) else Triple(**as_dict(v)) for v in self.triples]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExposureEventOutcomeCollection(TextWithTriples):
    """
    A collection of exposure events and their associated outcomes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME["ExposureEventOutcomeCollection"]
    class_class_curie: ClassVar[str] = "exposure_outcome:ExposureEventOutcomeCollection"
    class_name: ClassVar[str] = "ExposureEventOutcomeCollection"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.ExposureEventOutcomeCollection

    exposure_event: Optional[Union[str, ExposureEventId]] = None
    outcome: Optional[Union[Union[str, PhenotypeId], List[Union[str, PhenotypeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.exposure_event is not None and not isinstance(self.exposure_event, ExposureEventId):
            self.exposure_event = ExposureEventId(self.exposure_event)

        if not isinstance(self.outcome, list):
            self.outcome = [self.outcome] if self.outcome is not None else []
        self.outcome = [v if isinstance(v, PhenotypeId) else PhenotypeId(v) for v in self.outcome]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextWithEntity(YAMLRoot):
    """
    A text containing one or more instances of a single type of entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["TextWithEntity"]
    class_class_curie: ClassVar[str] = "core:TextWithEntity"
    class_name: ClassVar[str] = "TextWithEntity"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.TextWithEntity

    publication: Optional[Union[dict, "Publication"]] = None
    entities: Optional[Union[Union[str, NamedEntityId], List[Union[str, NamedEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.publication is not None and not isinstance(self.publication, Publication):
            self.publication = Publication(**as_dict(self.publication))

        if not isinstance(self.entities, list):
            self.entities = [self.entities] if self.entities is not None else []
        self.entities = [v if isinstance(v, NamedEntityId) else NamedEntityId(v) for v in self.entities]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RelationshipType(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["RelationshipType"]
    class_class_curie: ClassVar[str] = "core:RelationshipType"
    class_name: ClassVar[str] = "RelationshipType"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.RelationshipType

    id: Union[str, RelationshipTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Publication(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Publication"]
    class_class_curie: ClassVar[str] = "core:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.Publication

    id: Optional[str] = None
    title: Optional[str] = None
    abstract: Optional[str] = None
    combined_text: Optional[str] = None
    full_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.combined_text is not None and not isinstance(self.combined_text, str):
            self.combined_text = str(self.combined_text)

        if self.full_text is not None and not isinstance(self.full_text, str):
            self.full_text = str(self.full_text)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnnotatorResult(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["AnnotatorResult"]
    class_class_curie: ClassVar[str] = "core:AnnotatorResult"
    class_name: ClassVar[str] = "AnnotatorResult"
    class_model_uri: ClassVar[URIRef] = EXPOSURE_OUTCOME.AnnotatorResult

    subject_text: Optional[str] = None
    object_id: Optional[str] = None
    object_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_text is not None and not isinstance(self.subject_text, str):
            self.subject_text = str(self.subject_text)

        if self.object_id is not None and not isinstance(self.object_id, str):
            self.object_id = str(self.object_id)

        if self.object_text is not None and not isinstance(self.object_text, str):
            self.object_text = str(self.object_text)

        super().__post_init__(**kwargs)


# Enumerations
class ExposureTypeEnum(EnumDefinitionImpl):
    """
    Enumeration of exposure types derived from the ECTO ontology. Free-text values should be mapped to ECTO subclasses
    of 'exposure event' where possible.
    """
    _defn = EnumDefinition(
        name="ExposureTypeEnum",
        description="""Enumeration of exposure types derived from the ECTO ontology. Free-text values should be mapped to ECTO subclasses of 'exposure event' where possible.""",
    )

class NullDataOptions(EnumDefinitionImpl):

    UNSPECIFIED_METHOD_OF_ADMINISTRATION = PermissibleValue(
        text="UNSPECIFIED_METHOD_OF_ADMINISTRATION",
        meaning=NCIT["C149701"])
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        meaning=NCIT["C18902"])
    NOT_MENTIONED = PermissibleValue(text="NOT_MENTIONED")

    _defn = EnumDefinition(
        name="NullDataOptions",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=EXPOSURE_OUTCOME.id, name="id", curie=EXPOSURE_OUTCOME.curie('id'),
                   model_uri=EXPOSURE_OUTCOME.id, domain=None, range=URIRef)

slots.name = Slot(uri=EXPOSURE_OUTCOME.name, name="name", curie=EXPOSURE_OUTCOME.curie('name'),
                   model_uri=EXPOSURE_OUTCOME.name, domain=None, range=Optional[str])

slots.exposure_type = Slot(uri=EXPOSURE_OUTCOME.exposure_type, name="exposure_type", curie=EXPOSURE_OUTCOME.curie('exposure_type'),
                   model_uri=EXPOSURE_OUTCOME.exposure_type, domain=None, range=Optional[Union[str, "ExposureTypeEnum"]])

slots.has_unit = Slot(uri=EXPOSURE_OUTCOME.has_unit, name="has_unit", curie=EXPOSURE_OUTCOME.curie('has_unit'),
                   model_uri=EXPOSURE_OUTCOME.has_unit, domain=None, range=Optional[str])

slots.has_numeric_value = Slot(uri=EXPOSURE_OUTCOME.has_numeric_value, name="has_numeric_value", curie=EXPOSURE_OUTCOME.curie('has_numeric_value'),
                   model_uri=EXPOSURE_OUTCOME.has_numeric_value, domain=None, range=Optional[str])

slots.treated_with = Slot(uri=EXPOSURE_OUTCOME.treated_with, name="treated_with", curie=EXPOSURE_OUTCOME.curie('treated_with'),
                   model_uri=EXPOSURE_OUTCOME.treated_with, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.exposure_substance = Slot(uri=EXPOSURE_OUTCOME.exposure_substance, name="exposure_substance", curie=EXPOSURE_OUTCOME.curie('exposure_substance'),
                   model_uri=EXPOSURE_OUTCOME.exposure_substance, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.concentration = Slot(uri=EXPOSURE_OUTCOME.concentration, name="concentration", curie=EXPOSURE_OUTCOME.curie('concentration'),
                   model_uri=EXPOSURE_OUTCOME.concentration, domain=None, range=Optional[str])

slots.duration = Slot(uri=EXPOSURE_OUTCOME.duration, name="duration", curie=EXPOSURE_OUTCOME.curie('duration'),
                   model_uri=EXPOSURE_OUTCOME.duration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.exposure_event = Slot(uri=EXPOSURE_OUTCOME.exposure_event, name="exposure_event", curie=EXPOSURE_OUTCOME.curie('exposure_event'),
                   model_uri=EXPOSURE_OUTCOME.exposure_event, domain=None, range=Optional[Union[str, ExposureEventId]])

slots.outcome = Slot(uri=EXPOSURE_OUTCOME.outcome, name="outcome", curie=EXPOSURE_OUTCOME.curie('outcome'),
                   model_uri=EXPOSURE_OUTCOME.outcome, domain=None, range=Optional[Union[Union[str, PhenotypeId], List[Union[str, PhenotypeId]]]])

slots.frequency = Slot(uri=EXPOSURE_OUTCOME.frequency, name="frequency", curie=EXPOSURE_OUTCOME.curie('frequency'),
                   model_uri=EXPOSURE_OUTCOME.frequency, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=EXPOSURE_OUTCOME.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=EXPOSURE_OUTCOME.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=EXPOSURE_OUTCOME.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=EXPOSURE_OUTCOME.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=EXPOSURE_OUTCOME.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=EXPOSURE_OUTCOME.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=EXPOSURE_OUTCOME.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=EXPOSURE_OUTCOME.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=EXPOSURE_OUTCOME.namedEntity__label, domain=None, range=Optional[str])

slots.namedEntity__original_spans = Slot(uri=CORE.original_spans, name="namedEntity__original_spans", curie=CORE.curie('original_spans'),
                   model_uri=EXPOSURE_OUTCOME.namedEntity__original_spans, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^\d+:\d+$'))

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=EXPOSURE_OUTCOME.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=EXPOSURE_OUTCOME.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=EXPOSURE_OUTCOME.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=EXPOSURE_OUTCOME.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=EXPOSURE_OUTCOME.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=EXPOSURE_OUTCOME.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=EXPOSURE_OUTCOME.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=EXPOSURE_OUTCOME.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.textWithEntity__publication = Slot(uri=CORE.publication, name="textWithEntity__publication", curie=CORE.curie('publication'),
                   model_uri=EXPOSURE_OUTCOME.textWithEntity__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithEntity__entities = Slot(uri=CORE.entities, name="textWithEntity__entities", curie=CORE.curie('entities'),
                   model_uri=EXPOSURE_OUTCOME.textWithEntity__entities, domain=None, range=Optional[Union[Union[str, NamedEntityId], List[Union[str, NamedEntityId]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=EXPOSURE_OUTCOME.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=EXPOSURE_OUTCOME.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=EXPOSURE_OUTCOME.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=EXPOSURE_OUTCOME.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=EXPOSURE_OUTCOME.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=EXPOSURE_OUTCOME.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=EXPOSURE_OUTCOME.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=EXPOSURE_OUTCOME.annotatorResult__object_text, domain=None, range=Optional[str])
