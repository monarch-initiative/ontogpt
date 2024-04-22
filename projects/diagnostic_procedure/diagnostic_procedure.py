# Auto generated from diagnostic_procedure.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:52:38
# Schema: diagnostic_procedure
#
# id: http://w3id.org/ontogpt/diagnostic_procedure
# description: A template for clinical diagnostic procedures and the phenotypes they may contribute to.
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
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
LOINC = CurieNamespace('LOINC', 'http://loinc.org/rdf/')
OBA = CurieNamespace('OBA', 'http://purl.obolibrary.org/obo/OBA_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
UO = CurieNamespace('UO', 'http://example.org/UNKNOWN/UO/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
DIAG = CurieNamespace('diag', 'http://w3id.org/ontogpt/diagnostic_procedure/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
DEFAULT_ = DIAG


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class DiagnosticProcedureId(NamedEntityId):
    pass


class PhenotypeId(NamedEntityId):
    pass


class ClinicalAttributeId(NamedEntityId):
    pass


class QualityId(NamedEntityId):
    pass


class UnitId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


class ProcedureToPhenotypePredicateId(RelationshipTypeId):
    pass


class ProcedureToAttributePredicateId(RelationshipTypeId):
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
    class_model_uri: ClassVar[URIRef] = DIAG.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = DIAG.NamedEntity

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
class DiagnosticProcedure(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DIAG.DiagnosticProcedure
    class_class_curie: ClassVar[str] = "diag:DiagnosticProcedure"
    class_name: ClassVar[str] = "DiagnosticProcedure"
    class_model_uri: ClassVar[URIRef] = DIAG.DiagnosticProcedure

    id: Union[str, DiagnosticProcedureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiagnosticProcedureId):
            self.id = DiagnosticProcedureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Phenotype(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DIAG.Phenotype
    class_class_curie: ClassVar[str] = "diag:Phenotype"
    class_name: ClassVar[str] = "Phenotype"
    class_model_uri: ClassVar[URIRef] = DIAG.Phenotype

    id: Union[str, PhenotypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhenotypeId):
            self.id = PhenotypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ClinicalAttribute(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DIAG.ClinicalAttribute
    class_class_curie: ClassVar[str] = "diag:ClinicalAttribute"
    class_name: ClassVar[str] = "ClinicalAttribute"
    class_model_uri: ClassVar[URIRef] = DIAG.ClinicalAttribute

    id: Union[str, ClinicalAttributeId] = None
    unit: Optional[Union[str, UnitId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ClinicalAttributeId):
            self.id = ClinicalAttributeId(self.id)

        if self.unit is not None and not isinstance(self.unit, UnitId):
            self.unit = UnitId(self.unit)

        super().__post_init__(**kwargs)


@dataclass
class Quality(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DIAG.Quality
    class_class_curie: ClassVar[str] = "diag:Quality"
    class_name: ClassVar[str] = "Quality"
    class_model_uri: ClassVar[URIRef] = DIAG.Quality

    id: Union[str, QualityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QualityId):
            self.id = QualityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Unit(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DIAG.Unit
    class_class_curie: ClassVar[str] = "diag:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = DIAG.Unit

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
    class_model_uri: ClassVar[URIRef] = DIAG.CompoundExpression


@dataclass
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Triple
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = DIAG.Triple

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
class DiagnosticProceduretoPhenotypeAssociation(Triple):
    """
    A triple representing a relationship between a diagnostic procedure and an associated phenotype, e.g., "blood
    pressure measurement" is associated with "high blood pressure".
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DIAG.DiagnosticProceduretoPhenotypeAssociation
    class_class_curie: ClassVar[str] = "diag:DiagnosticProceduretoPhenotypeAssociation"
    class_name: ClassVar[str] = "DiagnosticProceduretoPhenotypeAssociation"
    class_model_uri: ClassVar[URIRef] = DIAG.DiagnosticProceduretoPhenotypeAssociation

    subject: Optional[Union[str, DiagnosticProcedureId]] = None
    object: Optional[Union[Union[str, PhenotypeId], List[Union[str, PhenotypeId]]]] = empty_list()
    predicate: Optional[Union[str, ProcedureToPhenotypePredicateId]] = None
    subject_qualifier: Optional[Union[str, NamedEntityId]] = None
    object_qualifier: Optional[Union[str, NamedEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, DiagnosticProcedureId):
            self.subject = DiagnosticProcedureId(self.subject)

        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, PhenotypeId) else PhenotypeId(v) for v in self.object]

        if self.predicate is not None and not isinstance(self.predicate, ProcedureToPhenotypePredicateId):
            self.predicate = ProcedureToPhenotypePredicateId(self.predicate)

        if self.subject_qualifier is not None and not isinstance(self.subject_qualifier, NamedEntityId):
            self.subject_qualifier = NamedEntityId(self.subject_qualifier)

        if self.object_qualifier is not None and not isinstance(self.object_qualifier, NamedEntityId):
            self.object_qualifier = NamedEntityId(self.object_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class DiagnosticProceduretoAttributeAssociation(Triple):
    """
    A triple representing a relationship between a diagnostic procedure and a measured attribute, e.g., "blood
    pressure measurement" is associated with "blood pressure" (or in OBA, something like OBA:VT0000183, "blood
    pressure trait").
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DIAG.DiagnosticProceduretoAttributeAssociation
    class_class_curie: ClassVar[str] = "diag:DiagnosticProceduretoAttributeAssociation"
    class_name: ClassVar[str] = "DiagnosticProceduretoAttributeAssociation"
    class_model_uri: ClassVar[URIRef] = DIAG.DiagnosticProceduretoAttributeAssociation

    subject: Optional[Union[str, DiagnosticProcedureId]] = None
    object: Optional[Union[Union[str, ClinicalAttributeId], List[Union[str, ClinicalAttributeId]]]] = empty_list()
    predicate: Optional[Union[str, ProcedureToAttributePredicateId]] = None
    subject_qualifier: Optional[Union[str, NamedEntityId]] = None
    object_qualifier: Optional[Union[str, QualityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, DiagnosticProcedureId):
            self.subject = DiagnosticProcedureId(self.subject)

        if not isinstance(self.object, list):
            self.object = [self.object] if self.object is not None else []
        self.object = [v if isinstance(v, ClinicalAttributeId) else ClinicalAttributeId(v) for v in self.object]

        if self.predicate is not None and not isinstance(self.predicate, ProcedureToAttributePredicateId):
            self.predicate = ProcedureToAttributePredicateId(self.predicate)

        if self.subject_qualifier is not None and not isinstance(self.subject_qualifier, NamedEntityId):
            self.subject_qualifier = NamedEntityId(self.subject_qualifier)

        if self.object_qualifier is not None and not isinstance(self.object_qualifier, QualityId):
            self.object_qualifier = QualityId(self.object_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class TextWithTriples(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.TextWithTriples
    class_class_curie: ClassVar[str] = "core:TextWithTriples"
    class_name: ClassVar[str] = "TextWithTriples"
    class_model_uri: ClassVar[URIRef] = DIAG.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = DIAG.RelationshipType

    id: Union[str, RelationshipTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ProcedureToPhenotypePredicate(RelationshipType):
    """
    A predicate for procedure to phenotype relationships, defining "this procedure is intended to provide support
    for/against this phenotype".
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DIAG.ProcedureToPhenotypePredicate
    class_class_curie: ClassVar[str] = "diag:ProcedureToPhenotypePredicate"
    class_name: ClassVar[str] = "ProcedureToPhenotypePredicate"
    class_model_uri: ClassVar[URIRef] = DIAG.ProcedureToPhenotypePredicate

    id: Union[str, ProcedureToPhenotypePredicateId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcedureToPhenotypePredicateId):
            self.id = ProcedureToPhenotypePredicateId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ProcedureToAttributePredicate(RelationshipType):
    """
    A predicate for procedure to attribute relationships, defining "this procedure is a measurement of this attribute".
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DIAG.ProcedureToAttributePredicate
    class_class_curie: ClassVar[str] = "diag:ProcedureToAttributePredicate"
    class_name: ClassVar[str] = "ProcedureToAttributePredicate"
    class_model_uri: ClassVar[URIRef] = DIAG.ProcedureToAttributePredicate

    id: Union[str, ProcedureToAttributePredicateId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcedureToAttributePredicateId):
            self.id = ProcedureToAttributePredicateId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Publication
    class_class_curie: ClassVar[str] = "core:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = DIAG.Publication

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
    class_model_uri: ClassVar[URIRef] = DIAG.AnnotatorResult

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

slots.clinicalAttribute__unit = Slot(uri=DIAG.unit, name="clinicalAttribute__unit", curie=DIAG.curie('unit'),
                   model_uri=DIAG.clinicalAttribute__unit, domain=None, range=Optional[Union[str, UnitId]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=DIAG.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=DIAG.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=DIAG.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=DIAG.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=DIAG.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=DIAG.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=DIAG.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=DIAG.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=DIAG.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=DIAG.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=DIAG.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=DIAG.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=DIAG.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=DIAG.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=DIAG.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=DIAG.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=DIAG.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=DIAG.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=DIAG.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=DIAG.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=DIAG.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=DIAG.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=DIAG.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=DIAG.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=DIAG.annotatorResult__object_text, domain=None, range=Optional[str])

slots.DiagnosticProceduretoPhenotypeAssociation_subject = Slot(uri=DIAG.subject, name="DiagnosticProceduretoPhenotypeAssociation_subject", curie=DIAG.curie('subject'),
                   model_uri=DIAG.DiagnosticProceduretoPhenotypeAssociation_subject, domain=DiagnosticProceduretoPhenotypeAssociation, range=Optional[Union[str, DiagnosticProcedureId]])

slots.DiagnosticProceduretoPhenotypeAssociation_object = Slot(uri=DIAG.object, name="DiagnosticProceduretoPhenotypeAssociation_object", curie=DIAG.curie('object'),
                   model_uri=DIAG.DiagnosticProceduretoPhenotypeAssociation_object, domain=DiagnosticProceduretoPhenotypeAssociation, range=Optional[Union[Union[str, PhenotypeId], List[Union[str, PhenotypeId]]]])

slots.DiagnosticProceduretoPhenotypeAssociation_predicate = Slot(uri=DIAG.predicate, name="DiagnosticProceduretoPhenotypeAssociation_predicate", curie=DIAG.curie('predicate'),
                   model_uri=DIAG.DiagnosticProceduretoPhenotypeAssociation_predicate, domain=DiagnosticProceduretoPhenotypeAssociation, range=Optional[Union[str, ProcedureToPhenotypePredicateId]])

slots.DiagnosticProceduretoPhenotypeAssociation_subject_qualifier = Slot(uri=DIAG.subject_qualifier, name="DiagnosticProceduretoPhenotypeAssociation_subject_qualifier", curie=DIAG.curie('subject_qualifier'),
                   model_uri=DIAG.DiagnosticProceduretoPhenotypeAssociation_subject_qualifier, domain=DiagnosticProceduretoPhenotypeAssociation, range=Optional[Union[str, NamedEntityId]])

slots.DiagnosticProceduretoPhenotypeAssociation_object_qualifier = Slot(uri=DIAG.object_qualifier, name="DiagnosticProceduretoPhenotypeAssociation_object_qualifier", curie=DIAG.curie('object_qualifier'),
                   model_uri=DIAG.DiagnosticProceduretoPhenotypeAssociation_object_qualifier, domain=DiagnosticProceduretoPhenotypeAssociation, range=Optional[Union[str, NamedEntityId]])

slots.DiagnosticProceduretoAttributeAssociation_subject = Slot(uri=DIAG.subject, name="DiagnosticProceduretoAttributeAssociation_subject", curie=DIAG.curie('subject'),
                   model_uri=DIAG.DiagnosticProceduretoAttributeAssociation_subject, domain=DiagnosticProceduretoAttributeAssociation, range=Optional[Union[str, DiagnosticProcedureId]])

slots.DiagnosticProceduretoAttributeAssociation_object = Slot(uri=DIAG.object, name="DiagnosticProceduretoAttributeAssociation_object", curie=DIAG.curie('object'),
                   model_uri=DIAG.DiagnosticProceduretoAttributeAssociation_object, domain=DiagnosticProceduretoAttributeAssociation, range=Optional[Union[Union[str, ClinicalAttributeId], List[Union[str, ClinicalAttributeId]]]])

slots.DiagnosticProceduretoAttributeAssociation_predicate = Slot(uri=DIAG.predicate, name="DiagnosticProceduretoAttributeAssociation_predicate", curie=DIAG.curie('predicate'),
                   model_uri=DIAG.DiagnosticProceduretoAttributeAssociation_predicate, domain=DiagnosticProceduretoAttributeAssociation, range=Optional[Union[str, ProcedureToAttributePredicateId]])

slots.DiagnosticProceduretoAttributeAssociation_subject_qualifier = Slot(uri=DIAG.subject_qualifier, name="DiagnosticProceduretoAttributeAssociation_subject_qualifier", curie=DIAG.curie('subject_qualifier'),
                   model_uri=DIAG.DiagnosticProceduretoAttributeAssociation_subject_qualifier, domain=DiagnosticProceduretoAttributeAssociation, range=Optional[Union[str, NamedEntityId]])

slots.DiagnosticProceduretoAttributeAssociation_object_qualifier = Slot(uri=DIAG.object_qualifier, name="DiagnosticProceduretoAttributeAssociation_object_qualifier", curie=DIAG.curie('object_qualifier'),
                   model_uri=DIAG.DiagnosticProceduretoAttributeAssociation_object_qualifier, domain=DiagnosticProceduretoAttributeAssociation, range=Optional[Union[str, QualityId]])