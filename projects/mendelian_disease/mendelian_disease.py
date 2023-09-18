# Auto generated from mendelian_disease.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:54:43
# Schema: mendelian_disease-template
#
# id: http://w3id.org/ontogpt/mendelian_disease
# description: A template for GO-CAMs
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
HP = CurieNamespace('HP', 'http://example.org/UNKNOWN/HP/')
MONDO = CurieNamespace('MONDO', 'http://example.org/UNKNOWN/MONDO/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MENDELIAN_DISEASE = CurieNamespace('mendelian_disease', 'http://w3id.org/ontogpt/mendelian_disease/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
DEFAULT_ = MENDELIAN_DISEASE


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class MendelianDiseaseId(NamedEntityId):
    pass


class DiseaseCategoryId(NamedEntityId):
    pass


class GeneId(NamedEntityId):
    pass


class SymptomId(NamedEntityId):
    pass


class OnsetId(NamedEntityId):
    pass


class InheritanceId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


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
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.NamedEntity

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
class MendelianDisease(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.MendelianDisease
    class_class_curie: ClassVar[str] = "mendelian_disease:MendelianDisease"
    class_name: ClassVar[str] = "MendelianDisease"
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.MendelianDisease

    id: Union[str, MendelianDiseaseId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    subclass_of: Optional[Union[Union[str, DiseaseCategoryId], List[Union[str, DiseaseCategoryId]]]] = empty_list()
    symptoms: Optional[Union[Union[str, SymptomId], List[Union[str, SymptomId]]]] = empty_list()
    inheritance: Optional[Union[str, InheritanceId]] = None
    genes: Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]] = empty_list()
    disease_onsets: Optional[Union[Union[str, OnsetId], List[Union[str, OnsetId]]]] = empty_list()
    publications: Optional[Union[Union[dict, "Publication"], List[Union[dict, "Publication"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MendelianDiseaseId):
            self.id = MendelianDiseaseId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if not isinstance(self.subclass_of, list):
            self.subclass_of = [self.subclass_of] if self.subclass_of is not None else []
        self.subclass_of = [v if isinstance(v, DiseaseCategoryId) else DiseaseCategoryId(v) for v in self.subclass_of]

        if not isinstance(self.symptoms, list):
            self.symptoms = [self.symptoms] if self.symptoms is not None else []
        self.symptoms = [v if isinstance(v, SymptomId) else SymptomId(v) for v in self.symptoms]

        if self.inheritance is not None and not isinstance(self.inheritance, InheritanceId):
            self.inheritance = InheritanceId(self.inheritance)

        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneId) else GeneId(v) for v in self.genes]

        if not isinstance(self.disease_onsets, list):
            self.disease_onsets = [self.disease_onsets] if self.disease_onsets is not None else []
        self.disease_onsets = [v if isinstance(v, OnsetId) else OnsetId(v) for v in self.disease_onsets]

        if not isinstance(self.publications, list):
            self.publications = [self.publications] if self.publications is not None else []
        self.publications = [v if isinstance(v, Publication) else Publication(**as_dict(v)) for v in self.publications]

        super().__post_init__(**kwargs)


@dataclass
class DiseaseCategory(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.DiseaseCategory
    class_class_curie: ClassVar[str] = "mendelian_disease:DiseaseCategory"
    class_name: ClassVar[str] = "DiseaseCategory"
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.DiseaseCategory

    id: Union[str, DiseaseCategoryId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseCategoryId):
            self.id = DiseaseCategoryId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Gene(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.Gene
    class_class_curie: ClassVar[str] = "mendelian_disease:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.Gene

    id: Union[str, GeneId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Symptom(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.Symptom
    class_class_curie: ClassVar[str] = "mendelian_disease:Symptom"
    class_name: ClassVar[str] = "Symptom"
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.Symptom

    id: Union[str, SymptomId] = None
    characteristic: Optional[str] = None
    affects: Optional[str] = None
    severity: Optional[str] = None
    onset_of_symptom: Optional[Union[str, OnsetId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SymptomId):
            self.id = SymptomId(self.id)

        if self.characteristic is not None and not isinstance(self.characteristic, str):
            self.characteristic = str(self.characteristic)

        if self.affects is not None and not isinstance(self.affects, str):
            self.affects = str(self.affects)

        if self.severity is not None and not isinstance(self.severity, str):
            self.severity = str(self.severity)

        if self.onset_of_symptom is not None and not isinstance(self.onset_of_symptom, OnsetId):
            self.onset_of_symptom = OnsetId(self.onset_of_symptom)

        super().__post_init__(**kwargs)


@dataclass
class Onset(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.Onset
    class_class_curie: ClassVar[str] = "mendelian_disease:Onset"
    class_name: ClassVar[str] = "Onset"
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.Onset

    id: Union[str, OnsetId] = None
    years_old: Optional[str] = None
    decades: Optional[Union[str, List[str]]] = empty_list()
    juvenile_or_adult: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OnsetId):
            self.id = OnsetId(self.id)

        if self.years_old is not None and not isinstance(self.years_old, str):
            self.years_old = str(self.years_old)

        if not isinstance(self.decades, list):
            self.decades = [self.decades] if self.decades is not None else []
        self.decades = [v if isinstance(v, str) else str(v) for v in self.decades]

        if self.juvenile_or_adult is not None and not isinstance(self.juvenile_or_adult, str):
            self.juvenile_or_adult = str(self.juvenile_or_adult)

        super().__post_init__(**kwargs)


@dataclass
class Inheritance(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.Inheritance
    class_class_curie: ClassVar[str] = "mendelian_disease:Inheritance"
    class_name: ClassVar[str] = "Inheritance"
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.Inheritance

    id: Union[str, InheritanceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InheritanceId):
            self.id = InheritanceId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.CompoundExpression


@dataclass
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Triple
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.Triple

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
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.RelationshipType

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
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.Publication

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
    class_model_uri: ClassVar[URIRef] = MENDELIAN_DISEASE.AnnotatorResult

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

slots.mendelianDisease__name = Slot(uri=MENDELIAN_DISEASE.name, name="mendelianDisease__name", curie=MENDELIAN_DISEASE.curie('name'),
                   model_uri=MENDELIAN_DISEASE.mendelianDisease__name, domain=None, range=Optional[str])

slots.mendelianDisease__description = Slot(uri=MENDELIAN_DISEASE.description, name="mendelianDisease__description", curie=MENDELIAN_DISEASE.curie('description'),
                   model_uri=MENDELIAN_DISEASE.mendelianDisease__description, domain=None, range=Optional[str])

slots.mendelianDisease__synonyms = Slot(uri=MENDELIAN_DISEASE.synonyms, name="mendelianDisease__synonyms", curie=MENDELIAN_DISEASE.curie('synonyms'),
                   model_uri=MENDELIAN_DISEASE.mendelianDisease__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.mendelianDisease__subclass_of = Slot(uri=MENDELIAN_DISEASE.subclass_of, name="mendelianDisease__subclass_of", curie=MENDELIAN_DISEASE.curie('subclass_of'),
                   model_uri=MENDELIAN_DISEASE.mendelianDisease__subclass_of, domain=None, range=Optional[Union[Union[str, DiseaseCategoryId], List[Union[str, DiseaseCategoryId]]]])

slots.mendelianDisease__symptoms = Slot(uri=MENDELIAN_DISEASE.symptoms, name="mendelianDisease__symptoms", curie=MENDELIAN_DISEASE.curie('symptoms'),
                   model_uri=MENDELIAN_DISEASE.mendelianDisease__symptoms, domain=None, range=Optional[Union[Union[str, SymptomId], List[Union[str, SymptomId]]]])

slots.mendelianDisease__inheritance = Slot(uri=MENDELIAN_DISEASE.inheritance, name="mendelianDisease__inheritance", curie=MENDELIAN_DISEASE.curie('inheritance'),
                   model_uri=MENDELIAN_DISEASE.mendelianDisease__inheritance, domain=None, range=Optional[Union[str, InheritanceId]])

slots.mendelianDisease__genes = Slot(uri=MENDELIAN_DISEASE.genes, name="mendelianDisease__genes", curie=MENDELIAN_DISEASE.curie('genes'),
                   model_uri=MENDELIAN_DISEASE.mendelianDisease__genes, domain=None, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.mendelianDisease__disease_onsets = Slot(uri=MENDELIAN_DISEASE.disease_onsets, name="mendelianDisease__disease_onsets", curie=MENDELIAN_DISEASE.curie('disease_onsets'),
                   model_uri=MENDELIAN_DISEASE.mendelianDisease__disease_onsets, domain=None, range=Optional[Union[Union[str, OnsetId], List[Union[str, OnsetId]]]])

slots.mendelianDisease__publications = Slot(uri=MENDELIAN_DISEASE.publications, name="mendelianDisease__publications", curie=MENDELIAN_DISEASE.curie('publications'),
                   model_uri=MENDELIAN_DISEASE.mendelianDisease__publications, domain=None, range=Optional[Union[Union[dict, Publication], List[Union[dict, Publication]]]])

slots.symptom__characteristic = Slot(uri=MENDELIAN_DISEASE.characteristic, name="symptom__characteristic", curie=MENDELIAN_DISEASE.curie('characteristic'),
                   model_uri=MENDELIAN_DISEASE.symptom__characteristic, domain=None, range=Optional[str])

slots.symptom__affects = Slot(uri=MENDELIAN_DISEASE.affects, name="symptom__affects", curie=MENDELIAN_DISEASE.curie('affects'),
                   model_uri=MENDELIAN_DISEASE.symptom__affects, domain=None, range=Optional[str])

slots.symptom__severity = Slot(uri=MENDELIAN_DISEASE.severity, name="symptom__severity", curie=MENDELIAN_DISEASE.curie('severity'),
                   model_uri=MENDELIAN_DISEASE.symptom__severity, domain=None, range=Optional[str])

slots.symptom__onset_of_symptom = Slot(uri=MENDELIAN_DISEASE.onset_of_symptom, name="symptom__onset_of_symptom", curie=MENDELIAN_DISEASE.curie('onset_of_symptom'),
                   model_uri=MENDELIAN_DISEASE.symptom__onset_of_symptom, domain=None, range=Optional[Union[str, OnsetId]])

slots.onset__years_old = Slot(uri=MENDELIAN_DISEASE.years_old, name="onset__years_old", curie=MENDELIAN_DISEASE.curie('years_old'),
                   model_uri=MENDELIAN_DISEASE.onset__years_old, domain=None, range=Optional[str])

slots.onset__decades = Slot(uri=MENDELIAN_DISEASE.decades, name="onset__decades", curie=MENDELIAN_DISEASE.curie('decades'),
                   model_uri=MENDELIAN_DISEASE.onset__decades, domain=None, range=Optional[Union[str, List[str]]])

slots.onset__juvenile_or_adult = Slot(uri=MENDELIAN_DISEASE.juvenile_or_adult, name="onset__juvenile_or_adult", curie=MENDELIAN_DISEASE.curie('juvenile_or_adult'),
                   model_uri=MENDELIAN_DISEASE.onset__juvenile_or_adult, domain=None, range=Optional[str])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=MENDELIAN_DISEASE.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=MENDELIAN_DISEASE.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=MENDELIAN_DISEASE.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=MENDELIAN_DISEASE.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=MENDELIAN_DISEASE.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=MENDELIAN_DISEASE.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=MENDELIAN_DISEASE.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=MENDELIAN_DISEASE.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=MENDELIAN_DISEASE.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=MENDELIAN_DISEASE.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=MENDELIAN_DISEASE.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=MENDELIAN_DISEASE.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=MENDELIAN_DISEASE.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=MENDELIAN_DISEASE.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=MENDELIAN_DISEASE.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=MENDELIAN_DISEASE.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=MENDELIAN_DISEASE.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=MENDELIAN_DISEASE.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=MENDELIAN_DISEASE.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=MENDELIAN_DISEASE.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=MENDELIAN_DISEASE.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=MENDELIAN_DISEASE.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=MENDELIAN_DISEASE.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=MENDELIAN_DISEASE.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=MENDELIAN_DISEASE.annotatorResult__object_text, domain=None, range=Optional[str])