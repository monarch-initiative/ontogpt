# Auto generated from traits.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:56:31
# Schema: traits
#
# id: http://w3id.org/ontogpt/traits
# description: A template for Traits
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
BIODIVTHES = CurieNamespace('BIODIVTHES', 'http://example.org/UNKNOWN/BIODIVTHES/')
ECOCORE = CurieNamespace('ECOCORE', 'http://example.org/UNKNOWN/ECOCORE/')
GO = CurieNamespace('GO', 'http://example.org/UNKNOWN/GO/')
OBA = CurieNamespace('OBA', 'http://example.org/UNKNOWN/OBA/')
PATO = CurieNamespace('PATO', 'http://example.org/UNKNOWN/PATO/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
TRAITS = CurieNamespace('traits', 'http://w3id.org/ontogpt/traits/')
DEFAULT_ = TRAITS


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class TraitId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass
class Taxon(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TRAITS.Taxon
    class_class_curie: ClassVar[str] = "traits:Taxon"
    class_name: ClassVar[str] = "Taxon"
    class_model_uri: ClassVar[URIRef] = TRAITS.Taxon

    metabolic_traits: Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]] = empty_list()
    morphological_traits: Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]] = empty_list()
    genetic_traits: Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]] = empty_list()
    cellular_traits: Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]] = empty_list()
    ecological_traits: Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]] = empty_list()
    reproductive_traits: Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]] = empty_list()
    survival_traits: Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]] = empty_list()
    phenotypic_plasticiticy_traits: Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]] = empty_list()
    preferred_environments: Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.metabolic_traits, list):
            self.metabolic_traits = [self.metabolic_traits] if self.metabolic_traits is not None else []
        self.metabolic_traits = [v if isinstance(v, TraitId) else TraitId(v) for v in self.metabolic_traits]

        if not isinstance(self.morphological_traits, list):
            self.morphological_traits = [self.morphological_traits] if self.morphological_traits is not None else []
        self.morphological_traits = [v if isinstance(v, TraitId) else TraitId(v) for v in self.morphological_traits]

        if not isinstance(self.genetic_traits, list):
            self.genetic_traits = [self.genetic_traits] if self.genetic_traits is not None else []
        self.genetic_traits = [v if isinstance(v, TraitId) else TraitId(v) for v in self.genetic_traits]

        if not isinstance(self.cellular_traits, list):
            self.cellular_traits = [self.cellular_traits] if self.cellular_traits is not None else []
        self.cellular_traits = [v if isinstance(v, TraitId) else TraitId(v) for v in self.cellular_traits]

        if not isinstance(self.ecological_traits, list):
            self.ecological_traits = [self.ecological_traits] if self.ecological_traits is not None else []
        self.ecological_traits = [v if isinstance(v, TraitId) else TraitId(v) for v in self.ecological_traits]

        if not isinstance(self.reproductive_traits, list):
            self.reproductive_traits = [self.reproductive_traits] if self.reproductive_traits is not None else []
        self.reproductive_traits = [v if isinstance(v, TraitId) else TraitId(v) for v in self.reproductive_traits]

        if not isinstance(self.survival_traits, list):
            self.survival_traits = [self.survival_traits] if self.survival_traits is not None else []
        self.survival_traits = [v if isinstance(v, TraitId) else TraitId(v) for v in self.survival_traits]

        if not isinstance(self.phenotypic_plasticiticy_traits, list):
            self.phenotypic_plasticiticy_traits = [self.phenotypic_plasticiticy_traits] if self.phenotypic_plasticiticy_traits is not None else []
        self.phenotypic_plasticiticy_traits = [v if isinstance(v, TraitId) else TraitId(v) for v in self.phenotypic_plasticiticy_traits]

        if not isinstance(self.preferred_environments, list):
            self.preferred_environments = [self.preferred_environments] if self.preferred_environments is not None else []
        self.preferred_environments = [v if isinstance(v, TraitId) else TraitId(v) for v in self.preferred_environments]

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
    class_model_uri: ClassVar[URIRef] = TRAITS.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = TRAITS.NamedEntity

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
class Trait(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TRAITS.Trait
    class_class_curie: ClassVar[str] = "traits:Trait"
    class_name: ClassVar[str] = "Trait"
    class_model_uri: ClassVar[URIRef] = TRAITS.Trait

    id: Union[str, TraitId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TraitId):
            self.id = TraitId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = TRAITS.CompoundExpression


@dataclass
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Triple
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = TRAITS.Triple

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
    class_model_uri: ClassVar[URIRef] = TRAITS.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = TRAITS.RelationshipType

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
    class_model_uri: ClassVar[URIRef] = TRAITS.Publication

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
    class_model_uri: ClassVar[URIRef] = TRAITS.AnnotatorResult

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

slots.taxon__metabolic_traits = Slot(uri=TRAITS.metabolic_traits, name="taxon__metabolic_traits", curie=TRAITS.curie('metabolic_traits'),
                   model_uri=TRAITS.taxon__metabolic_traits, domain=None, range=Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]])

slots.taxon__morphological_traits = Slot(uri=TRAITS.morphological_traits, name="taxon__morphological_traits", curie=TRAITS.curie('morphological_traits'),
                   model_uri=TRAITS.taxon__morphological_traits, domain=None, range=Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]])

slots.taxon__genetic_traits = Slot(uri=TRAITS.genetic_traits, name="taxon__genetic_traits", curie=TRAITS.curie('genetic_traits'),
                   model_uri=TRAITS.taxon__genetic_traits, domain=None, range=Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]])

slots.taxon__cellular_traits = Slot(uri=TRAITS.cellular_traits, name="taxon__cellular_traits", curie=TRAITS.curie('cellular_traits'),
                   model_uri=TRAITS.taxon__cellular_traits, domain=None, range=Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]])

slots.taxon__ecological_traits = Slot(uri=TRAITS.ecological_traits, name="taxon__ecological_traits", curie=TRAITS.curie('ecological_traits'),
                   model_uri=TRAITS.taxon__ecological_traits, domain=None, range=Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]])

slots.taxon__reproductive_traits = Slot(uri=TRAITS.reproductive_traits, name="taxon__reproductive_traits", curie=TRAITS.curie('reproductive_traits'),
                   model_uri=TRAITS.taxon__reproductive_traits, domain=None, range=Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]])

slots.taxon__survival_traits = Slot(uri=TRAITS.survival_traits, name="taxon__survival_traits", curie=TRAITS.curie('survival_traits'),
                   model_uri=TRAITS.taxon__survival_traits, domain=None, range=Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]])

slots.taxon__phenotypic_plasticiticy_traits = Slot(uri=TRAITS.phenotypic_plasticiticy_traits, name="taxon__phenotypic_plasticiticy_traits", curie=TRAITS.curie('phenotypic_plasticiticy_traits'),
                   model_uri=TRAITS.taxon__phenotypic_plasticiticy_traits, domain=None, range=Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]])

slots.taxon__preferred_environments = Slot(uri=TRAITS.preferred_environments, name="taxon__preferred_environments", curie=TRAITS.curie('preferred_environments'),
                   model_uri=TRAITS.taxon__preferred_environments, domain=None, range=Optional[Union[Union[str, TraitId], List[Union[str, TraitId]]]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=TRAITS.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=TRAITS.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=TRAITS.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=TRAITS.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=TRAITS.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=TRAITS.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=TRAITS.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=TRAITS.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=TRAITS.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=TRAITS.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=TRAITS.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=TRAITS.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=TRAITS.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=TRAITS.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=TRAITS.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=TRAITS.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=TRAITS.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=TRAITS.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=TRAITS.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=TRAITS.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=TRAITS.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=TRAITS.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=TRAITS.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=TRAITS.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=TRAITS.annotatorResult__object_text, domain=None, range=Optional[str])