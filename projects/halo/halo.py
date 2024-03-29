# Auto generated from halo.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:54:01
# Schema: ontology-class
#
# id: https://w3id.org/ontogpt/halo
# description: A template for Ontology Classes
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
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OC = CurieNamespace('oc', 'http://w3id.org/ontogpt/ontology-class-template')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
DEFAULT_ = OC


# Types

# Class references
class OntologyElementName(extended_str):
    pass


class CategoryName(OntologyElementName):
    pass


class NamedEntityId(extended_str):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass
class Ontology(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OC.Ontology
    class_class_curie: ClassVar[str] = "oc:Ontology"
    class_name: ClassVar[str] = "Ontology"
    class_model_uri: ClassVar[URIRef] = OC.Ontology

    elements: Optional[Union[Dict[Union[str, OntologyElementName], Union[dict, "OntologyElement"]], List[Union[dict, "OntologyElement"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="elements", slot_type=OntologyElement, key_name="name", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class OntologyElement(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OC.OntologyElement
    class_class_curie: ClassVar[str] = "oc:OntologyElement"
    class_name: ClassVar[str] = "OntologyElement"
    class_model_uri: ClassVar[URIRef] = OC.OntologyElement

    name: Union[str, OntologyElementName] = None
    context: Optional[str] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    categories: Optional[Union[Union[str, CategoryName], List[Union[str, CategoryName]]]] = empty_list()
    subclass_of: Optional[Union[Union[str, OntologyElementName], List[Union[str, OntologyElementName]]]] = empty_list()
    part_of: Optional[Union[Union[str, OntologyElementName], List[Union[str, OntologyElementName]]]] = empty_list()
    subtypes: Optional[Union[Union[str, OntologyElementName], List[Union[str, OntologyElementName]]]] = empty_list()
    parts: Optional[Union[Union[str, OntologyElementName], List[Union[str, OntologyElementName]]]] = empty_list()
    equivalent_to: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, OntologyElementName):
            self.name = OntologyElementName(self.name)

        if self.context is not None and not isinstance(self.context, str):
            self.context = str(self.context)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, CategoryName) else CategoryName(v) for v in self.categories]

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, OntologyElementName) else OntologyElementName(v) for v in self.subclass_of]

        if not isinstance(self.part_of, list):
            self.part_of = [self.part_of] if self.part_of is not None else []
        self.part_of = [v if isinstance(v, OntologyElementName) else OntologyElementName(v) for v in self.part_of]

        if not isinstance(self.subtypes, list):
            self.subtypes = [self.subtypes] if self.subtypes is not None else []
        self.subtypes = [v if isinstance(v, OntologyElementName) else OntologyElementName(v) for v in self.subtypes]

        if not isinstance(self.parts, list):
            self.parts = [self.parts] if self.parts is not None else []
        self.parts = [v if isinstance(v, OntologyElementName) else OntologyElementName(v) for v in self.parts]

        if self.equivalent_to is not None and not isinstance(self.equivalent_to, str):
            self.equivalent_to = str(self.equivalent_to)

        super().__post_init__(**kwargs)


@dataclass
class Category(OntologyElement):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OC.Category
    class_class_curie: ClassVar[str] = "oc:Category"
    class_name: ClassVar[str] = "Category"
    class_model_uri: ClassVar[URIRef] = OC.Category

    name: Union[str, CategoryName] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, CategoryName):
            self.name = CategoryName(self.name)

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
    class_model_uri: ClassVar[URIRef] = OC.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = OC.NamedEntity

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


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = OC.CompoundExpression


@dataclass
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Triple
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = OC.Triple

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
    class_model_uri: ClassVar[URIRef] = OC.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = OC.RelationshipType

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
    class_model_uri: ClassVar[URIRef] = OC.Publication

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
    class_model_uri: ClassVar[URIRef] = OC.AnnotatorResult

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

slots.subclass_of = Slot(uri=RDFS.subClassOf, name="subclass_of", curie=RDFS.curie('subClassOf'),
                   model_uri=OC.subclass_of, domain=OntologyElement, range=Optional[Union[Union[str, OntologyElementName], List[Union[str, OntologyElementName]]]])

slots.part_of = Slot(uri=BFO['0000050'], name="part_of", curie=BFO.curie('0000050'),
                   model_uri=OC.part_of, domain=OntologyElement, range=Optional[Union[Union[str, OntologyElementName], List[Union[str, OntologyElementName]]]])

slots.ontology__elements = Slot(uri=OC.elements, name="ontology__elements", curie=OC.curie('elements'),
                   model_uri=OC.ontology__elements, domain=None, range=Optional[Union[Dict[Union[str, OntologyElementName], Union[dict, OntologyElement]], List[Union[dict, OntologyElement]]]])

slots.ontologyElement__name = Slot(uri=OC.name, name="ontologyElement__name", curie=OC.curie('name'),
                   model_uri=OC.ontologyElement__name, domain=None, range=URIRef)

slots.ontologyElement__context = Slot(uri=OC.context, name="ontologyElement__context", curie=OC.curie('context'),
                   model_uri=OC.ontologyElement__context, domain=None, range=Optional[str])

slots.ontologyElement__description = Slot(uri=OC.description, name="ontologyElement__description", curie=OC.curie('description'),
                   model_uri=OC.ontologyElement__description, domain=None, range=Optional[str])

slots.ontologyElement__synonyms = Slot(uri=OC.synonyms, name="ontologyElement__synonyms", curie=OC.curie('synonyms'),
                   model_uri=OC.ontologyElement__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.ontologyElement__categories = Slot(uri=OC.categories, name="ontologyElement__categories", curie=OC.curie('categories'),
                   model_uri=OC.ontologyElement__categories, domain=None, range=Optional[Union[Union[str, CategoryName], List[Union[str, CategoryName]]]])

slots.ontologyElement__subclass_of = Slot(uri=RDFS.subClassOf, name="ontologyElement__subclass_of", curie=RDFS.curie('subClassOf'),
                   model_uri=OC.ontologyElement__subclass_of, domain=None, range=Optional[Union[Union[str, OntologyElementName], List[Union[str, OntologyElementName]]]])

slots.ontologyElement__part_of = Slot(uri=BFO['0000050'], name="ontologyElement__part_of", curie=BFO.curie('0000050'),
                   model_uri=OC.ontologyElement__part_of, domain=None, range=Optional[Union[Union[str, OntologyElementName], List[Union[str, OntologyElementName]]]])

slots.ontologyElement__subtypes = Slot(uri=OC.subtypes, name="ontologyElement__subtypes", curie=OC.curie('subtypes'),
                   model_uri=OC.ontologyElement__subtypes, domain=None, range=Optional[Union[Union[str, OntologyElementName], List[Union[str, OntologyElementName]]]])

slots.ontologyElement__parts = Slot(uri=OC.parts, name="ontologyElement__parts", curie=OC.curie('parts'),
                   model_uri=OC.ontologyElement__parts, domain=None, range=Optional[Union[Union[str, OntologyElementName], List[Union[str, OntologyElementName]]]])

slots.ontologyElement__equivalent_to = Slot(uri=OC.equivalent_to, name="ontologyElement__equivalent_to", curie=OC.curie('equivalent_to'),
                   model_uri=OC.ontologyElement__equivalent_to, domain=None, range=Optional[str])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=OC.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=OC.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=OC.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=OC.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=OC.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=OC.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=OC.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=OC.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=OC.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=OC.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=OC.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=OC.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=OC.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=OC.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=OC.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=OC.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=OC.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=OC.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=OC.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=OC.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=OC.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=OC.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=OC.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=OC.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=OC.annotatorResult__object_text, domain=None, range=Optional[str])