# Auto generated from biotic_interaction.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:51:35
# Schema: biotic-interaction-template
#
# id: https://w3id.org/ontogpt/biotic_interaction
# description: A template for biotic interactions
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
COL = CurieNamespace('COL', 'https://www.catalogueoflife.org/data/taxon/')
GBIF = CurieNamespace('GBIF', 'https://www.gbif.org/species/')
ITIS = CurieNamespace('ITIS', 'https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=')
MESH = CurieNamespace('MESH', 'http://example.org/UNKNOWN/MESH/')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITAXON_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
BP = CurieNamespace('bp', 'http://w3id.org/ontogpt/biotic-interaction-template')
COL = CurieNamespace('col', 'https://www.catalogueoflife.org/data/taxon/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
GBIF = CurieNamespace('gbif', 'https://www.gbif.org/species/')
ITIS = CurieNamespace('itis', 'https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
DEFAULT_ = BP


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class TaxonId(NamedEntityId):
    pass


class InteractionTypeId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BP.Container
    class_class_curie: ClassVar[str] = "bp:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = BP.Container

    interactions: Optional[Union[Union[dict, "BioticInteraction"], List[Union[dict, "BioticInteraction"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.interactions, list):
            self.interactions = [self.interactions] if self.interactions is not None else []
        self.interactions = [v if isinstance(v, BioticInteraction) else BioticInteraction(**as_dict(v)) for v in self.interactions]

        super().__post_init__(**kwargs)


@dataclass
class BioticInteraction(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BP.BioticInteraction
    class_class_curie: ClassVar[str] = "bp:BioticInteraction"
    class_name: ClassVar[str] = "BioticInteraction"
    class_model_uri: ClassVar[URIRef] = BP.BioticInteraction

    source_taxon: Optional[Union[str, TaxonId]] = None
    target_taxon: Optional[Union[str, TaxonId]] = None
    interaction_type: Optional[Union[str, InteractionTypeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.source_taxon is not None and not isinstance(self.source_taxon, TaxonId):
            self.source_taxon = TaxonId(self.source_taxon)

        if self.target_taxon is not None and not isinstance(self.target_taxon, TaxonId):
            self.target_taxon = TaxonId(self.target_taxon)

        if self.interaction_type is not None and not isinstance(self.interaction_type, InteractionTypeId):
            self.interaction_type = InteractionTypeId(self.interaction_type)

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
    class_model_uri: ClassVar[URIRef] = BP.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = BP.NamedEntity

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
class Taxon(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BP.Taxon
    class_class_curie: ClassVar[str] = "bp:Taxon"
    class_name: ClassVar[str] = "Taxon"
    class_model_uri: ClassVar[URIRef] = BP.Taxon

    id: Union[str, TaxonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TaxonId):
            self.id = TaxonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class InteractionType(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BP.InteractionType
    class_class_curie: ClassVar[str] = "bp:InteractionType"
    class_name: ClassVar[str] = "InteractionType"
    class_model_uri: ClassVar[URIRef] = BP.InteractionType

    id: Union[str, InteractionTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InteractionTypeId):
            self.id = InteractionTypeId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = BP.CompoundExpression


@dataclass
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Triple
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = BP.Triple

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
    class_model_uri: ClassVar[URIRef] = BP.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = BP.RelationshipType

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
    class_model_uri: ClassVar[URIRef] = BP.Publication

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
    class_model_uri: ClassVar[URIRef] = BP.AnnotatorResult

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

slots.container__interactions = Slot(uri=BP.interactions, name="container__interactions", curie=BP.curie('interactions'),
                   model_uri=BP.container__interactions, domain=None, range=Optional[Union[Union[dict, BioticInteraction], List[Union[dict, BioticInteraction]]]])

slots.bioticInteraction__source_taxon = Slot(uri=BP.source_taxon, name="bioticInteraction__source_taxon", curie=BP.curie('source_taxon'),
                   model_uri=BP.bioticInteraction__source_taxon, domain=None, range=Optional[Union[str, TaxonId]])

slots.bioticInteraction__target_taxon = Slot(uri=BP.target_taxon, name="bioticInteraction__target_taxon", curie=BP.curie('target_taxon'),
                   model_uri=BP.bioticInteraction__target_taxon, domain=None, range=Optional[Union[str, TaxonId]])

slots.bioticInteraction__interaction_type = Slot(uri=BP.interaction_type, name="bioticInteraction__interaction_type", curie=BP.curie('interaction_type'),
                   model_uri=BP.bioticInteraction__interaction_type, domain=None, range=Optional[Union[str, InteractionTypeId]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=BP.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=BP.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=BP.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=BP.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=BP.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=BP.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=BP.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=BP.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=BP.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=BP.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=BP.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=BP.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=BP.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=BP.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=BP.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=BP.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=BP.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=BP.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=BP.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=BP.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=BP.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=BP.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=BP.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=BP.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=BP.annotatorResult__object_text, domain=None, range=Optional[str])