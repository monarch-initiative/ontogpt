# Auto generated from composite_disease.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:51:59
# Schema: composite_disease
#
# id: http://w3id.org/ontogpt/composite_disease
# description: A template for representing composite disease concepts
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
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
COMPOSITE_DISEASE = CurieNamespace('composite_disease', 'http://w3id.org/ontogpt/composite_disease/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
DEFAULT_ = COMPOSITE_DISEASE


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class GeneId(NamedEntityId):
    pass


class SymptomId(NamedEntityId):
    pass


class DiseaseId(NamedEntityId):
    pass


class AdverseEffectId(NamedEntityId):
    pass


class TreatmentId(NamedEntityId):
    pass


class MechanismId(NamedEntityId):
    pass


class DrugId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass
class CompositeDisease(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.CompositeDisease
    class_class_curie: ClassVar[str] = "composite_disease:CompositeDisease"
    class_name: ClassVar[str] = "CompositeDisease"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.CompositeDisease

    main_disease: Optional[Union[str, DiseaseId]] = None
    drugs: Optional[Union[Union[str, DrugId], List[Union[str, DrugId]]]] = empty_list()
    treatments: Optional[Union[Union[str, TreatmentId], List[Union[str, TreatmentId]]]] = empty_list()
    contraindications: Optional[Union[Union[str, TreatmentId], List[Union[str, TreatmentId]]]] = empty_list()
    treatment_mechanisms: Optional[Union[Union[dict, "TreatmentMechanism"], List[Union[dict, "TreatmentMechanism"]]]] = empty_list()
    treatment_efficacies: Optional[Union[Union[dict, "TreatmentEfficacy"], List[Union[dict, "TreatmentEfficacy"]]]] = empty_list()
    treatment_adverse_effects: Optional[Union[Union[dict, "TreatmentAdverseEffect"], List[Union[dict, "TreatmentAdverseEffect"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.main_disease is not None and not isinstance(self.main_disease, DiseaseId):
            self.main_disease = DiseaseId(self.main_disease)

        if not isinstance(self.drugs, list):
            self.drugs = [self.drugs] if self.drugs is not None else []
        self.drugs = [v if isinstance(v, DrugId) else DrugId(v) for v in self.drugs]

        if not isinstance(self.treatments, list):
            self.treatments = [self.treatments] if self.treatments is not None else []
        self.treatments = [v if isinstance(v, TreatmentId) else TreatmentId(v) for v in self.treatments]

        if not isinstance(self.contraindications, list):
            self.contraindications = [self.contraindications] if self.contraindications is not None else []
        self.contraindications = [v if isinstance(v, TreatmentId) else TreatmentId(v) for v in self.contraindications]

        if not isinstance(self.treatment_mechanisms, list):
            self.treatment_mechanisms = [self.treatment_mechanisms] if self.treatment_mechanisms is not None else []
        self.treatment_mechanisms = [v if isinstance(v, TreatmentMechanism) else TreatmentMechanism(**as_dict(v)) for v in self.treatment_mechanisms]

        if not isinstance(self.treatment_efficacies, list):
            self.treatment_efficacies = [self.treatment_efficacies] if self.treatment_efficacies is not None else []
        self.treatment_efficacies = [v if isinstance(v, TreatmentEfficacy) else TreatmentEfficacy(**as_dict(v)) for v in self.treatment_efficacies]

        if not isinstance(self.treatment_adverse_effects, list):
            self.treatment_adverse_effects = [self.treatment_adverse_effects] if self.treatment_adverse_effects is not None else []
        self.treatment_adverse_effects = [v if isinstance(v, TreatmentAdverseEffect) else TreatmentAdverseEffect(**as_dict(v)) for v in self.treatment_adverse_effects]

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
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.NamedEntity

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
class Gene(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Gene
    class_class_curie: ClassVar[str] = "composite_disease:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Gene

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

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Symptom
    class_class_curie: ClassVar[str] = "composite_disease:Symptom"
    class_name: ClassVar[str] = "Symptom"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Symptom

    id: Union[str, SymptomId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SymptomId):
            self.id = SymptomId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Disease(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Disease
    class_class_curie: ClassVar[str] = "composite_disease:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Disease

    id: Union[str, DiseaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class AdverseEffect(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.AdverseEffect
    class_class_curie: ClassVar[str] = "composite_disease:AdverseEffect"
    class_name: ClassVar[str] = "AdverseEffect"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.AdverseEffect

    id: Union[str, AdverseEffectId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AdverseEffectId):
            self.id = AdverseEffectId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Treatment(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Treatment
    class_class_curie: ClassVar[str] = "composite_disease:Treatment"
    class_name: ClassVar[str] = "Treatment"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Treatment

    id: Union[str, TreatmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TreatmentId):
            self.id = TreatmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Mechanism(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Mechanism
    class_class_curie: ClassVar[str] = "composite_disease:Mechanism"
    class_name: ClassVar[str] = "Mechanism"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Mechanism

    id: Union[str, MechanismId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MechanismId):
            self.id = MechanismId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Drug(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Drug
    class_class_curie: ClassVar[str] = "composite_disease:Drug"
    class_name: ClassVar[str] = "Drug"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Drug

    id: Union[str, DrugId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DrugId):
            self.id = DrugId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.CompoundExpression


@dataclass
class TreatmentMechanism(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.TreatmentMechanism
    class_class_curie: ClassVar[str] = "composite_disease:TreatmentMechanism"
    class_name: ClassVar[str] = "TreatmentMechanism"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.TreatmentMechanism

    treatment: Optional[Union[str, TreatmentId]] = None
    mechanism: Optional[Union[str, MechanismId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.treatment is not None and not isinstance(self.treatment, TreatmentId):
            self.treatment = TreatmentId(self.treatment)

        if self.mechanism is not None and not isinstance(self.mechanism, MechanismId):
            self.mechanism = MechanismId(self.mechanism)

        super().__post_init__(**kwargs)


@dataclass
class TreatmentAdverseEffect(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.TreatmentAdverseEffect
    class_class_curie: ClassVar[str] = "composite_disease:TreatmentAdverseEffect"
    class_name: ClassVar[str] = "TreatmentAdverseEffect"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.TreatmentAdverseEffect

    treatment: Optional[Union[str, TreatmentId]] = None
    adverse_effects: Optional[Union[Union[str, AdverseEffectId], List[Union[str, AdverseEffectId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.treatment is not None and not isinstance(self.treatment, TreatmentId):
            self.treatment = TreatmentId(self.treatment)

        if not isinstance(self.adverse_effects, list):
            self.adverse_effects = [self.adverse_effects] if self.adverse_effects is not None else []
        self.adverse_effects = [v if isinstance(v, AdverseEffectId) else AdverseEffectId(v) for v in self.adverse_effects]

        super().__post_init__(**kwargs)


@dataclass
class TreatmentEfficacy(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.TreatmentEfficacy
    class_class_curie: ClassVar[str] = "composite_disease:TreatmentEfficacy"
    class_name: ClassVar[str] = "TreatmentEfficacy"
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.TreatmentEfficacy

    treatment: Optional[Union[str, TreatmentId]] = None
    efficacy: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.treatment is not None and not isinstance(self.treatment, TreatmentId):
            self.treatment = TreatmentId(self.treatment)

        if self.efficacy is not None and not isinstance(self.efficacy, str):
            self.efficacy = str(self.efficacy)

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
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Triple

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
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.RelationshipType

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
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.Publication

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
    class_model_uri: ClassVar[URIRef] = COMPOSITE_DISEASE.AnnotatorResult

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
class NCITDrugType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NCITDrugType",
    )

class NCITTreatmentType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NCITTreatmentType",
    )

class NCITTActivityType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NCITTActivityType",
    )

class MAXOActionType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MAXOActionType",
    )

class MESHTherapeuticType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MESHTherapeuticType",
    )

class CHEBIDrugType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CHEBIDrugType",
    )

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

slots.compositeDisease__main_disease = Slot(uri=COMPOSITE_DISEASE.main_disease, name="compositeDisease__main_disease", curie=COMPOSITE_DISEASE.curie('main_disease'),
                   model_uri=COMPOSITE_DISEASE.compositeDisease__main_disease, domain=None, range=Optional[Union[str, DiseaseId]])

slots.compositeDisease__drugs = Slot(uri=COMPOSITE_DISEASE.drugs, name="compositeDisease__drugs", curie=COMPOSITE_DISEASE.curie('drugs'),
                   model_uri=COMPOSITE_DISEASE.compositeDisease__drugs, domain=None, range=Optional[Union[Union[str, DrugId], List[Union[str, DrugId]]]])

slots.compositeDisease__treatments = Slot(uri=COMPOSITE_DISEASE.treatments, name="compositeDisease__treatments", curie=COMPOSITE_DISEASE.curie('treatments'),
                   model_uri=COMPOSITE_DISEASE.compositeDisease__treatments, domain=None, range=Optional[Union[Union[str, TreatmentId], List[Union[str, TreatmentId]]]])

slots.compositeDisease__contraindications = Slot(uri=COMPOSITE_DISEASE.contraindications, name="compositeDisease__contraindications", curie=COMPOSITE_DISEASE.curie('contraindications'),
                   model_uri=COMPOSITE_DISEASE.compositeDisease__contraindications, domain=None, range=Optional[Union[Union[str, TreatmentId], List[Union[str, TreatmentId]]]])

slots.compositeDisease__treatment_mechanisms = Slot(uri=COMPOSITE_DISEASE.treatment_mechanisms, name="compositeDisease__treatment_mechanisms", curie=COMPOSITE_DISEASE.curie('treatment_mechanisms'),
                   model_uri=COMPOSITE_DISEASE.compositeDisease__treatment_mechanisms, domain=None, range=Optional[Union[Union[dict, TreatmentMechanism], List[Union[dict, TreatmentMechanism]]]])

slots.compositeDisease__treatment_efficacies = Slot(uri=COMPOSITE_DISEASE.treatment_efficacies, name="compositeDisease__treatment_efficacies", curie=COMPOSITE_DISEASE.curie('treatment_efficacies'),
                   model_uri=COMPOSITE_DISEASE.compositeDisease__treatment_efficacies, domain=None, range=Optional[Union[Union[dict, TreatmentEfficacy], List[Union[dict, TreatmentEfficacy]]]])

slots.compositeDisease__treatment_adverse_effects = Slot(uri=COMPOSITE_DISEASE.treatment_adverse_effects, name="compositeDisease__treatment_adverse_effects", curie=COMPOSITE_DISEASE.curie('treatment_adverse_effects'),
                   model_uri=COMPOSITE_DISEASE.compositeDisease__treatment_adverse_effects, domain=None, range=Optional[Union[Union[dict, TreatmentAdverseEffect], List[Union[dict, TreatmentAdverseEffect]]]])

slots.treatmentMechanism__treatment = Slot(uri=COMPOSITE_DISEASE.treatment, name="treatmentMechanism__treatment", curie=COMPOSITE_DISEASE.curie('treatment'),
                   model_uri=COMPOSITE_DISEASE.treatmentMechanism__treatment, domain=None, range=Optional[Union[str, TreatmentId]])

slots.treatmentMechanism__mechanism = Slot(uri=COMPOSITE_DISEASE.mechanism, name="treatmentMechanism__mechanism", curie=COMPOSITE_DISEASE.curie('mechanism'),
                   model_uri=COMPOSITE_DISEASE.treatmentMechanism__mechanism, domain=None, range=Optional[Union[str, MechanismId]])

slots.treatmentAdverseEffect__treatment = Slot(uri=COMPOSITE_DISEASE.treatment, name="treatmentAdverseEffect__treatment", curie=COMPOSITE_DISEASE.curie('treatment'),
                   model_uri=COMPOSITE_DISEASE.treatmentAdverseEffect__treatment, domain=None, range=Optional[Union[str, TreatmentId]])

slots.treatmentAdverseEffect__adverse_effects = Slot(uri=COMPOSITE_DISEASE.adverse_effects, name="treatmentAdverseEffect__adverse_effects", curie=COMPOSITE_DISEASE.curie('adverse_effects'),
                   model_uri=COMPOSITE_DISEASE.treatmentAdverseEffect__adverse_effects, domain=None, range=Optional[Union[Union[str, AdverseEffectId], List[Union[str, AdverseEffectId]]]])

slots.treatmentEfficacy__treatment = Slot(uri=COMPOSITE_DISEASE.treatment, name="treatmentEfficacy__treatment", curie=COMPOSITE_DISEASE.curie('treatment'),
                   model_uri=COMPOSITE_DISEASE.treatmentEfficacy__treatment, domain=None, range=Optional[Union[str, TreatmentId]])

slots.treatmentEfficacy__efficacy = Slot(uri=COMPOSITE_DISEASE.efficacy, name="treatmentEfficacy__efficacy", curie=COMPOSITE_DISEASE.curie('efficacy'),
                   model_uri=COMPOSITE_DISEASE.treatmentEfficacy__efficacy, domain=None, range=Optional[str])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=COMPOSITE_DISEASE.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=COMPOSITE_DISEASE.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=COMPOSITE_DISEASE.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=COMPOSITE_DISEASE.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=COMPOSITE_DISEASE.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=COMPOSITE_DISEASE.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=COMPOSITE_DISEASE.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=COMPOSITE_DISEASE.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=COMPOSITE_DISEASE.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=COMPOSITE_DISEASE.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=COMPOSITE_DISEASE.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=COMPOSITE_DISEASE.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=COMPOSITE_DISEASE.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=COMPOSITE_DISEASE.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=COMPOSITE_DISEASE.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=COMPOSITE_DISEASE.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=COMPOSITE_DISEASE.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=COMPOSITE_DISEASE.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=COMPOSITE_DISEASE.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=COMPOSITE_DISEASE.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=COMPOSITE_DISEASE.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=COMPOSITE_DISEASE.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=COMPOSITE_DISEASE.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=COMPOSITE_DISEASE.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=COMPOSITE_DISEASE.annotatorResult__object_text, domain=None, range=Optional[str])