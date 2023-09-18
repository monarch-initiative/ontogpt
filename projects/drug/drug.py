# Auto generated from drug.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:52:51
# Schema: drug
#
# id: http://w3id.org/ontogpt/drug
# description: A template for Drugs and drug mechanism
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
HGNC = CurieNamespace('HGNC', 'http://example.org/UNKNOWN/HGNC/')
MESH = CurieNamespace('MESH', 'http://example.org/UNKNOWN/MESH/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
DRUG = CurieNamespace('drug', 'http://w3id.org/ontogpt/drug/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
DEFAULT_ = DRUG


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class MechanismElementId(NamedEntityId):
    pass


class DiseaseId(NamedEntityId):
    pass


class DrugId(NamedEntityId):
    pass


class PredicateId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass
class DrugMechanism(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DRUG.DrugMechanism
    class_class_curie: ClassVar[str] = "drug:DrugMechanism"
    class_name: ClassVar[str] = "DrugMechanism"
    class_model_uri: ClassVar[URIRef] = DRUG.DrugMechanism

    disease: Optional[Union[str, DiseaseId]] = None
    drug: Optional[Union[str, DrugId]] = None
    mechanism_links: Optional[Union[Union[dict, "MechanismLink"], List[Union[dict, "MechanismLink"]]]] = empty_list()
    references: Optional[Union[str, List[str]]] = empty_list()
    source_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.disease is not None and not isinstance(self.disease, DiseaseId):
            self.disease = DiseaseId(self.disease)

        if self.drug is not None and not isinstance(self.drug, DrugId):
            self.drug = DrugId(self.drug)

        if not isinstance(self.mechanism_links, list):
            self.mechanism_links = [self.mechanism_links] if self.mechanism_links is not None else []
        self.mechanism_links = [v if isinstance(v, MechanismLink) else MechanismLink(**as_dict(v)) for v in self.mechanism_links]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, str) else str(v) for v in self.references]

        if self.source_text is not None and not isinstance(self.source_text, str):
            self.source_text = str(self.source_text)

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
    class_model_uri: ClassVar[URIRef] = DRUG.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = DRUG.NamedEntity

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
class MechanismElement(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DRUG.MechanismElement
    class_class_curie: ClassVar[str] = "drug:MechanismElement"
    class_name: ClassVar[str] = "MechanismElement"
    class_model_uri: ClassVar[URIRef] = DRUG.MechanismElement

    id: Union[str, MechanismElementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MechanismElementId):
            self.id = MechanismElementId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Disease(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DRUG.Disease
    class_class_curie: ClassVar[str] = "drug:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = DRUG.Disease

    id: Union[str, DiseaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Drug(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DRUG.Drug
    class_class_curie: ClassVar[str] = "drug:Drug"
    class_name: ClassVar[str] = "Drug"
    class_model_uri: ClassVar[URIRef] = DRUG.Drug

    id: Union[str, DrugId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Predicate(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DRUG.Predicate
    class_class_curie: ClassVar[str] = "drug:Predicate"
    class_name: ClassVar[str] = "Predicate"
    class_model_uri: ClassVar[URIRef] = DRUG.Predicate

    id: Union[str, PredicateId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PredicateId):
            self.id = PredicateId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = DRUG.CompoundExpression


@dataclass
class MechanismLink(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DRUG.MechanismLink
    class_class_curie: ClassVar[str] = "drug:MechanismLink"
    class_name: ClassVar[str] = "MechanismLink"
    class_model_uri: ClassVar[URIRef] = DRUG.MechanismLink

    subject: Optional[Union[str, MechanismElementId]] = None
    predicate: Optional[Union[str, PredicateId]] = None
    object: Optional[Union[str, MechanismElementId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, MechanismElementId):
            self.subject = MechanismElementId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, PredicateId):
            self.predicate = PredicateId(self.predicate)

        if self.object is not None and not isinstance(self.object, MechanismElementId):
            self.object = MechanismElementId(self.object)

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
    class_model_uri: ClassVar[URIRef] = DRUG.Triple

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
    class_model_uri: ClassVar[URIRef] = DRUG.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = DRUG.RelationshipType

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
    class_model_uri: ClassVar[URIRef] = DRUG.Publication

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
    class_model_uri: ClassVar[URIRef] = DRUG.AnnotatorResult

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

slots.drugMechanism__disease = Slot(uri=DRUG.disease, name="drugMechanism__disease", curie=DRUG.curie('disease'),
                   model_uri=DRUG.drugMechanism__disease, domain=None, range=Optional[Union[str, DiseaseId]])

slots.drugMechanism__drug = Slot(uri=DRUG.drug, name="drugMechanism__drug", curie=DRUG.curie('drug'),
                   model_uri=DRUG.drugMechanism__drug, domain=None, range=Optional[Union[str, DrugId]])

slots.drugMechanism__mechanism_links = Slot(uri=DRUG.mechanism_links, name="drugMechanism__mechanism_links", curie=DRUG.curie('mechanism_links'),
                   model_uri=DRUG.drugMechanism__mechanism_links, domain=None, range=Optional[Union[Union[dict, MechanismLink], List[Union[dict, MechanismLink]]]])

slots.drugMechanism__references = Slot(uri=DRUG.references, name="drugMechanism__references", curie=DRUG.curie('references'),
                   model_uri=DRUG.drugMechanism__references, domain=None, range=Optional[Union[str, List[str]]])

slots.drugMechanism__source_text = Slot(uri=DRUG.source_text, name="drugMechanism__source_text", curie=DRUG.curie('source_text'),
                   model_uri=DRUG.drugMechanism__source_text, domain=None, range=Optional[str])

slots.mechanismLink__subject = Slot(uri=DRUG.subject, name="mechanismLink__subject", curie=DRUG.curie('subject'),
                   model_uri=DRUG.mechanismLink__subject, domain=None, range=Optional[Union[str, MechanismElementId]])

slots.mechanismLink__predicate = Slot(uri=DRUG.predicate, name="mechanismLink__predicate", curie=DRUG.curie('predicate'),
                   model_uri=DRUG.mechanismLink__predicate, domain=None, range=Optional[Union[str, PredicateId]])

slots.mechanismLink__object = Slot(uri=DRUG.object, name="mechanismLink__object", curie=DRUG.curie('object'),
                   model_uri=DRUG.mechanismLink__object, domain=None, range=Optional[Union[str, MechanismElementId]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=DRUG.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=DRUG.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=DRUG.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=DRUG.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=DRUG.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=DRUG.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=DRUG.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=DRUG.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=DRUG.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=DRUG.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=DRUG.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=DRUG.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=DRUG.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=DRUG.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=DRUG.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=DRUG.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=DRUG.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=DRUG.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=DRUG.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=DRUG.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=DRUG.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=DRUG.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=DRUG.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=DRUG.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=DRUG.annotatorResult__object_text, domain=None, range=Optional[str])