# Auto generated from environmental_sample.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:53:18
# Schema: environmental-sample
#
# id: http://w3id.org/ontogpt/environmental-sample
# description: A template for Environmental Samples
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ENVO = CurieNamespace('ENVO', 'http://example.org/UNKNOWN/ENVO/')
ENVTHES = CurieNamespace('ENVTHES', 'http://example.org/UNKNOWN/ENVTHES/')
GAZ = CurieNamespace('GAZ', 'http://example.org/UNKNOWN/GAZ/')
MIXS = CurieNamespace('MIXS', 'http://example.org/UNKNOWN/MIXS/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
PATO = CurieNamespace('PATO', 'http://example.org/UNKNOWN/PATO/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
UO = CurieNamespace('UO', 'http://example.org/UNKNOWN/UO/')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
SAMPLE = CurieNamespace('sample', 'http://w3id.org/ontogpt/environmental-sample/')
DEFAULT_ = SAMPLE


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class LocationId(NamedEntityId):
    pass


class EnvironmentalMaterialId(NamedEntityId):
    pass


class EnvironmentId(NamedEntityId):
    pass


class VariableId(NamedEntityId):
    pass


class UnitId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass
class Study(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE.Study
    class_class_curie: ClassVar[str] = "sample:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Study

    location: Optional[Union[Union[str, LocationId], List[Union[str, LocationId]]]] = empty_list()
    environmental_material: Optional[Union[Union[str, EnvironmentalMaterialId], List[Union[str, EnvironmentalMaterialId]]]] = empty_list()
    environments: Optional[Union[Union[str, EnvironmentId], List[Union[str, EnvironmentId]]]] = empty_list()
    causal_relationships: Optional[Union[Union[dict, "CausalRelationship"], List[Union[dict, "CausalRelationship"]]]] = empty_list()
    variables: Optional[Union[Union[str, VariableId], List[Union[str, VariableId]]]] = empty_list()
    measurements: Optional[Union[Union[dict, "Measurement"], List[Union[dict, "Measurement"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.location, list):
            self.location = [self.location] if self.location is not None else []
        self.location = [v if isinstance(v, LocationId) else LocationId(v) for v in self.location]

        if not isinstance(self.environmental_material, list):
            self.environmental_material = [self.environmental_material] if self.environmental_material is not None else []
        self.environmental_material = [v if isinstance(v, EnvironmentalMaterialId) else EnvironmentalMaterialId(v) for v in self.environmental_material]

        if not isinstance(self.environments, list):
            self.environments = [self.environments] if self.environments is not None else []
        self.environments = [v if isinstance(v, EnvironmentId) else EnvironmentId(v) for v in self.environments]

        if not isinstance(self.causal_relationships, list):
            self.causal_relationships = [self.causal_relationships] if self.causal_relationships is not None else []
        self.causal_relationships = [v if isinstance(v, CausalRelationship) else CausalRelationship(**as_dict(v)) for v in self.causal_relationships]

        if not isinstance(self.variables, list):
            self.variables = [self.variables] if self.variables is not None else []
        self.variables = [v if isinstance(v, VariableId) else VariableId(v) for v in self.variables]

        if not isinstance(self.measurements, list):
            self.measurements = [self.measurements] if self.measurements is not None else []
        self.measurements = [v if isinstance(v, Measurement) else Measurement(**as_dict(v)) for v in self.measurements]

        super().__post_init__(**kwargs)


Any = Any

@dataclass
class ExtractionResult(YAMLRoot):
    """
    A result of extracting knowledge on text
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ExtractionResult
    class_class_curie: ClassVar[str] = "core:ExtractionResult"
    class_name: ClassVar[str] = "ExtractionResult"
    class_model_uri: ClassVar[URIRef] = SAMPLE.ExtractionResult

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


@dataclass
class NamedEntity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.NamedEntity
    class_class_curie: ClassVar[str] = "core:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = SAMPLE.NamedEntity

    id: Union[str, NamedEntityId] = None
    label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass
class Location(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE.Location
    class_class_curie: ClassVar[str] = "sample:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Location

    id: Union[str, LocationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LocationId):
            self.id = LocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalMaterial(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE.EnvironmentalMaterial
    class_class_curie: ClassVar[str] = "sample:EnvironmentalMaterial"
    class_name: ClassVar[str] = "EnvironmentalMaterial"
    class_model_uri: ClassVar[URIRef] = SAMPLE.EnvironmentalMaterial

    id: Union[str, EnvironmentalMaterialId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentalMaterialId):
            self.id = EnvironmentalMaterialId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Environment(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE.Environment
    class_class_curie: ClassVar[str] = "sample:Environment"
    class_name: ClassVar[str] = "Environment"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Environment

    id: Union[str, EnvironmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentId):
            self.id = EnvironmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Variable(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE.Variable
    class_class_curie: ClassVar[str] = "sample:Variable"
    class_name: ClassVar[str] = "Variable"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Variable

    id: Union[str, VariableId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VariableId):
            self.id = VariableId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Unit(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE.Unit
    class_class_curie: ClassVar[str] = "sample:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Unit

    id: Union[str, UnitId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnitId):
            self.id = UnitId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = SAMPLE.CompoundExpression


@dataclass
class Measurement(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE.Measurement
    class_class_curie: ClassVar[str] = "sample:Measurement"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Measurement

    value: Optional[str] = None
    unit: Optional[Union[str, UnitId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, UnitId):
            self.unit = UnitId(self.unit)

        super().__post_init__(**kwargs)


@dataclass
class CausalRelationship(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SAMPLE.CausalRelationship
    class_class_curie: ClassVar[str] = "sample:CausalRelationship"
    class_name: ClassVar[str] = "CausalRelationship"
    class_model_uri: ClassVar[URIRef] = SAMPLE.CausalRelationship

    cause: Optional[Union[str, VariableId]] = None
    effect: Optional[Union[str, VariableId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.cause is not None and not isinstance(self.cause, VariableId):
            self.cause = VariableId(self.cause)

        if self.effect is not None and not isinstance(self.effect, VariableId):
            self.effect = VariableId(self.effect)

        super().__post_init__(**kwargs)


@dataclass
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Triple
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Triple

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


@dataclass
class TextWithTriples(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.TextWithTriples
    class_class_curie: ClassVar[str] = "core:TextWithTriples"
    class_name: ClassVar[str] = "TextWithTriples"
    class_model_uri: ClassVar[URIRef] = SAMPLE.TextWithTriples

    publication: Optional[Union[dict, "Publication"]] = None
    triples: Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.publication is not None and not isinstance(self.publication, Publication):
            self.publication = Publication(**as_dict(self.publication))

        if not isinstance(self.triples, list):
            self.triples = [self.triples] if self.triples is not None else []
        self.triples = [v if isinstance(v, Triple) else Triple(**as_dict(v)) for v in self.triples]

        super().__post_init__(**kwargs)


@dataclass
class RelationshipType(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.RelationshipType
    class_class_curie: ClassVar[str] = "core:RelationshipType"
    class_name: ClassVar[str] = "RelationshipType"
    class_model_uri: ClassVar[URIRef] = SAMPLE.RelationshipType

    id: Union[str, RelationshipTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Publication
    class_class_curie: ClassVar[str] = "core:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = SAMPLE.Publication

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


@dataclass
class AnnotatorResult(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.AnnotatorResult
    class_class_curie: ClassVar[str] = "core:AnnotatorResult"
    class_name: ClassVar[str] = "AnnotatorResult"
    class_model_uri: ClassVar[URIRef] = SAMPLE.AnnotatorResult

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
class NullDataOptions(EnumDefinitionImpl):

    UNSPECIFIED_METHOD_OF_ADMINISTRATION = PermissibleValue(text="UNSPECIFIED_METHOD_OF_ADMINISTRATION",
                                                                                               meaning=NCIT.C149701)
    NOT_APPLICABLE = PermissibleValue(text="NOT_APPLICABLE",
                                                   meaning=NCIT.C18902)
    NOT_MENTIONED = PermissibleValue(text="NOT_MENTIONED")

    _defn = EnumDefinition(
        name="NullDataOptions",
    )

# Slots
class slots:
    pass

slots.study__location = Slot(uri=SAMPLE.location, name="study__location", curie=SAMPLE.curie('location'),
                   model_uri=SAMPLE.study__location, domain=None, range=Optional[Union[Union[str, LocationId], List[Union[str, LocationId]]]])

slots.study__environmental_material = Slot(uri=SAMPLE.environmental_material, name="study__environmental_material", curie=SAMPLE.curie('environmental_material'),
                   model_uri=SAMPLE.study__environmental_material, domain=None, range=Optional[Union[Union[str, EnvironmentalMaterialId], List[Union[str, EnvironmentalMaterialId]]]])

slots.study__environments = Slot(uri=SAMPLE.environments, name="study__environments", curie=SAMPLE.curie('environments'),
                   model_uri=SAMPLE.study__environments, domain=None, range=Optional[Union[Union[str, EnvironmentId], List[Union[str, EnvironmentId]]]])

slots.study__causal_relationships = Slot(uri=SAMPLE.causal_relationships, name="study__causal_relationships", curie=SAMPLE.curie('causal_relationships'),
                   model_uri=SAMPLE.study__causal_relationships, domain=None, range=Optional[Union[Union[dict, CausalRelationship], List[Union[dict, CausalRelationship]]]])

slots.study__variables = Slot(uri=SAMPLE.variables, name="study__variables", curie=SAMPLE.curie('variables'),
                   model_uri=SAMPLE.study__variables, domain=None, range=Optional[Union[Union[str, VariableId], List[Union[str, VariableId]]]])

slots.study__measurements = Slot(uri=SAMPLE.measurements, name="study__measurements", curie=SAMPLE.curie('measurements'),
                   model_uri=SAMPLE.study__measurements, domain=None, range=Optional[Union[Union[dict, Measurement], List[Union[dict, Measurement]]]])

slots.measurement__value = Slot(uri=SAMPLE.value, name="measurement__value", curie=SAMPLE.curie('value'),
                   model_uri=SAMPLE.measurement__value, domain=None, range=Optional[str])

slots.measurement__unit = Slot(uri=SAMPLE.unit, name="measurement__unit", curie=SAMPLE.curie('unit'),
                   model_uri=SAMPLE.measurement__unit, domain=None, range=Optional[Union[str, UnitId]])

slots.causalRelationship__cause = Slot(uri=SAMPLE.cause, name="causalRelationship__cause", curie=SAMPLE.curie('cause'),
                   model_uri=SAMPLE.causalRelationship__cause, domain=None, range=Optional[Union[str, VariableId]])

slots.causalRelationship__effect = Slot(uri=SAMPLE.effect, name="causalRelationship__effect", curie=SAMPLE.curie('effect'),
                   model_uri=SAMPLE.causalRelationship__effect, domain=None, range=Optional[Union[str, VariableId]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=SAMPLE.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=SAMPLE.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=SAMPLE.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=SAMPLE.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=SAMPLE.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=SAMPLE.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=SAMPLE.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=SAMPLE.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=SAMPLE.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=SAMPLE.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=SAMPLE.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=SAMPLE.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=SAMPLE.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=SAMPLE.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=SAMPLE.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=SAMPLE.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=SAMPLE.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=SAMPLE.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=SAMPLE.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=SAMPLE.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=SAMPLE.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=SAMPLE.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=SAMPLE.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=SAMPLE.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=SAMPLE.annotatorResult__object_text, domain=None, range=Optional[str])