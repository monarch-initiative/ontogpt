# Auto generated from ibd_literature.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T11:00:44
# Schema: ibd-literature-template
#
# id: http://w3id.org/ontogpt/ibd_literature
# description: A template for extracting information from IBD literature
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
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
ECTO = CurieNamespace('ECTO', 'http://purl.obolibrary.org/obo/ECTO_')
EXO = CurieNamespace('ExO', 'http://purl.obolibrary.org/obo/ExO_')
GO = CurieNamespace('GO', 'http://example.org/UNKNOWN/GO/')
HGNC = CurieNamespace('HGNC', 'http://identifiers.org/hgnc/')
MONDO = CurieNamespace('MONDO', 'http://example.org/UNKNOWN/MONDO/')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
IBDLIT = CurieNamespace('ibdlit', 'http://w3id.org/ontogpt/ibd_literature/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
DEFAULT_ = IBDLIT


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class GeneId(NamedEntityId):
    pass


class DiseaseId(NamedEntityId):
    pass


class CellularProcessId(NamedEntityId):
    pass


class ChemicalExposureId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


class DiseaseToCellularProcessPredicateId(RelationshipTypeId):
    pass


class ChemicalExposureToGenePredicateId(RelationshipTypeId):
    pass


@dataclass
class IBDAnnotations(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IBDLIT.IBDAnnotations
    class_class_curie: ClassVar[str] = "ibdlit:IBDAnnotations"
    class_name: ClassVar[str] = "IBDAnnotations"
    class_model_uri: ClassVar[URIRef] = IBDLIT.IBDAnnotations

    genes: Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]] = empty_list()
    exposures: Optional[Union[Union[str, ChemicalExposureId], List[Union[str, ChemicalExposureId]]]] = empty_list()
    gene_exposures_relationships: Optional[Union[Union[dict, "GeneExposureRelationship"], List[Union[dict, "GeneExposureRelationship"]]]] = empty_list()
    diseases: Optional[Union[Union[str, DiseaseId], List[Union[str, DiseaseId]]]] = empty_list()
    cellular_process: Optional[Union[Union[str, CellularProcessId], List[Union[str, CellularProcessId]]]] = empty_list()
    disease_cellular_process_relationships: Optional[Union[Union[dict, "DiseaseCellularProcessRelationship"], List[Union[dict, "DiseaseCellularProcessRelationship"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneId) else GeneId(v) for v in self.genes]

        if not isinstance(self.exposures, list):
            self.exposures = [self.exposures] if self.exposures is not None else []
        self.exposures = [v if isinstance(v, ChemicalExposureId) else ChemicalExposureId(v) for v in self.exposures]

        if not isinstance(self.gene_exposures_relationships, list):
            self.gene_exposures_relationships = [self.gene_exposures_relationships] if self.gene_exposures_relationships is not None else []
        self.gene_exposures_relationships = [v if isinstance(v, GeneExposureRelationship) else GeneExposureRelationship(**as_dict(v)) for v in self.gene_exposures_relationships]

        if not isinstance(self.diseases, list):
            self.diseases = [self.diseases] if self.diseases is not None else []
        self.diseases = [v if isinstance(v, DiseaseId) else DiseaseId(v) for v in self.diseases]

        if not isinstance(self.cellular_process, list):
            self.cellular_process = [self.cellular_process] if self.cellular_process is not None else []
        self.cellular_process = [v if isinstance(v, CellularProcessId) else CellularProcessId(v) for v in self.cellular_process]

        if not isinstance(self.disease_cellular_process_relationships, list):
            self.disease_cellular_process_relationships = [self.disease_cellular_process_relationships] if self.disease_cellular_process_relationships is not None else []
        self.disease_cellular_process_relationships = [v if isinstance(v, DiseaseCellularProcessRelationship) else DiseaseCellularProcessRelationship(**as_dict(v)) for v in self.disease_cellular_process_relationships]

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
    class_model_uri: ClassVar[URIRef] = IBDLIT.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = IBDLIT.NamedEntity

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

    class_class_uri: ClassVar[URIRef] = IBDLIT.Gene
    class_class_curie: ClassVar[str] = "ibdlit:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = IBDLIT.Gene

    id: Union[str, GeneId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Disease(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IBDLIT.Disease
    class_class_curie: ClassVar[str] = "ibdlit:Disease"
    class_name: ClassVar[str] = "Disease"
    class_model_uri: ClassVar[URIRef] = IBDLIT.Disease

    id: Union[str, DiseaseId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseId):
            self.id = DiseaseId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CellularProcess(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IBDLIT.CellularProcess
    class_class_curie: ClassVar[str] = "ibdlit:CellularProcess"
    class_name: ClassVar[str] = "CellularProcess"
    class_model_uri: ClassVar[URIRef] = IBDLIT.CellularProcess

    id: Union[str, CellularProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellularProcessId):
            self.id = CellularProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalExposure(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IBDLIT.ChemicalExposure
    class_class_curie: ClassVar[str] = "ibdlit:ChemicalExposure"
    class_name: ClassVar[str] = "ChemicalExposure"
    class_model_uri: ClassVar[URIRef] = IBDLIT.ChemicalExposure

    id: Union[str, ChemicalExposureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalExposureId):
            self.id = ChemicalExposureId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = IBDLIT.CompoundExpression


@dataclass
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Triple
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = IBDLIT.Triple

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
class DiseaseCellularProcessRelationship(Triple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IBDLIT.DiseaseCellularProcessRelationship
    class_class_curie: ClassVar[str] = "ibdlit:DiseaseCellularProcessRelationship"
    class_name: ClassVar[str] = "DiseaseCellularProcessRelationship"
    class_model_uri: ClassVar[URIRef] = IBDLIT.DiseaseCellularProcessRelationship

    subject: Optional[Union[str, DiseaseId]] = None
    predicate: Optional[Union[str, DiseaseToCellularProcessPredicateId]] = None
    object: Optional[Union[str, CellularProcessId]] = None
    subject_qualifier: Optional[Union[str, NamedEntityId]] = None
    object_qualifier: Optional[Union[str, NamedEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, DiseaseId):
            self.subject = DiseaseId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, DiseaseToCellularProcessPredicateId):
            self.predicate = DiseaseToCellularProcessPredicateId(self.predicate)

        if self.object is not None and not isinstance(self.object, CellularProcessId):
            self.object = CellularProcessId(self.object)

        if self.subject_qualifier is not None and not isinstance(self.subject_qualifier, NamedEntityId):
            self.subject_qualifier = NamedEntityId(self.subject_qualifier)

        if self.object_qualifier is not None and not isinstance(self.object_qualifier, NamedEntityId):
            self.object_qualifier = NamedEntityId(self.object_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class GeneExposureRelationship(Triple):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IBDLIT.GeneExposureRelationship
    class_class_curie: ClassVar[str] = "ibdlit:GeneExposureRelationship"
    class_name: ClassVar[str] = "GeneExposureRelationship"
    class_model_uri: ClassVar[URIRef] = IBDLIT.GeneExposureRelationship

    subject: Optional[Union[str, ChemicalExposureId]] = None
    predicate: Optional[Union[str, ChemicalExposureToGenePredicateId]] = None
    object: Optional[Union[str, GeneId]] = None
    subject_qualifier: Optional[Union[str, NamedEntityId]] = None
    object_qualifier: Optional[Union[str, NamedEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, ChemicalExposureId):
            self.subject = ChemicalExposureId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, ChemicalExposureToGenePredicateId):
            self.predicate = ChemicalExposureToGenePredicateId(self.predicate)

        if self.object is not None and not isinstance(self.object, GeneId):
            self.object = GeneId(self.object)

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
    class_model_uri: ClassVar[URIRef] = IBDLIT.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = IBDLIT.RelationshipType

    id: Union[str, RelationshipTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DiseaseToCellularProcessPredicate(RelationshipType):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IBDLIT.DiseaseToCellularProcessPredicate
    class_class_curie: ClassVar[str] = "ibdlit:DiseaseToCellularProcessPredicate"
    class_name: ClassVar[str] = "DiseaseToCellularProcessPredicate"
    class_model_uri: ClassVar[URIRef] = IBDLIT.DiseaseToCellularProcessPredicate

    id: Union[str, DiseaseToCellularProcessPredicateId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DiseaseToCellularProcessPredicateId):
            self.id = DiseaseToCellularProcessPredicateId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalExposureToGenePredicate(RelationshipType):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = IBDLIT.ChemicalExposureToGenePredicate
    class_class_curie: ClassVar[str] = "ibdlit:ChemicalExposureToGenePredicate"
    class_name: ClassVar[str] = "ChemicalExposureToGenePredicate"
    class_model_uri: ClassVar[URIRef] = IBDLIT.ChemicalExposureToGenePredicate

    id: Union[str, ChemicalExposureToGenePredicateId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalExposureToGenePredicateId):
            self.id = ChemicalExposureToGenePredicateId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Publication
    class_class_curie: ClassVar[str] = "core:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = IBDLIT.Publication

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
    class_model_uri: ClassVar[URIRef] = IBDLIT.AnnotatorResult

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

slots.iBDAnnotations__genes = Slot(uri=IBDLIT.genes, name="iBDAnnotations__genes", curie=IBDLIT.curie('genes'),
                   model_uri=IBDLIT.iBDAnnotations__genes, domain=None, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.iBDAnnotations__exposures = Slot(uri=IBDLIT.exposures, name="iBDAnnotations__exposures", curie=IBDLIT.curie('exposures'),
                   model_uri=IBDLIT.iBDAnnotations__exposures, domain=None, range=Optional[Union[Union[str, ChemicalExposureId], List[Union[str, ChemicalExposureId]]]])

slots.iBDAnnotations__gene_exposures_relationships = Slot(uri=IBDLIT.gene_exposures_relationships, name="iBDAnnotations__gene_exposures_relationships", curie=IBDLIT.curie('gene_exposures_relationships'),
                   model_uri=IBDLIT.iBDAnnotations__gene_exposures_relationships, domain=None, range=Optional[Union[Union[dict, GeneExposureRelationship], List[Union[dict, GeneExposureRelationship]]]])

slots.iBDAnnotations__diseases = Slot(uri=IBDLIT.diseases, name="iBDAnnotations__diseases", curie=IBDLIT.curie('diseases'),
                   model_uri=IBDLIT.iBDAnnotations__diseases, domain=None, range=Optional[Union[Union[str, DiseaseId], List[Union[str, DiseaseId]]]])

slots.iBDAnnotations__cellular_process = Slot(uri=IBDLIT.cellular_process, name="iBDAnnotations__cellular_process", curie=IBDLIT.curie('cellular_process'),
                   model_uri=IBDLIT.iBDAnnotations__cellular_process, domain=None, range=Optional[Union[Union[str, CellularProcessId], List[Union[str, CellularProcessId]]]])

slots.iBDAnnotations__disease_cellular_process_relationships = Slot(uri=IBDLIT.disease_cellular_process_relationships, name="iBDAnnotations__disease_cellular_process_relationships", curie=IBDLIT.curie('disease_cellular_process_relationships'),
                   model_uri=IBDLIT.iBDAnnotations__disease_cellular_process_relationships, domain=None, range=Optional[Union[Union[dict, DiseaseCellularProcessRelationship], List[Union[dict, DiseaseCellularProcessRelationship]]]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=IBDLIT.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=IBDLIT.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=IBDLIT.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=IBDLIT.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=IBDLIT.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=IBDLIT.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=IBDLIT.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=IBDLIT.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=IBDLIT.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=IBDLIT.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=IBDLIT.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=IBDLIT.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=IBDLIT.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=IBDLIT.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=IBDLIT.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=IBDLIT.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=IBDLIT.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=IBDLIT.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=IBDLIT.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=IBDLIT.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=IBDLIT.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=IBDLIT.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=IBDLIT.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=IBDLIT.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=IBDLIT.annotatorResult__object_text, domain=None, range=Optional[str])

slots.DiseaseCellularProcessRelationship_subject = Slot(uri=IBDLIT.subject, name="DiseaseCellularProcessRelationship_subject", curie=IBDLIT.curie('subject'),
                   model_uri=IBDLIT.DiseaseCellularProcessRelationship_subject, domain=DiseaseCellularProcessRelationship, range=Optional[Union[str, DiseaseId]])

slots.DiseaseCellularProcessRelationship_predicate = Slot(uri=IBDLIT.predicate, name="DiseaseCellularProcessRelationship_predicate", curie=IBDLIT.curie('predicate'),
                   model_uri=IBDLIT.DiseaseCellularProcessRelationship_predicate, domain=DiseaseCellularProcessRelationship, range=Optional[Union[str, DiseaseToCellularProcessPredicateId]])

slots.DiseaseCellularProcessRelationship_object = Slot(uri=IBDLIT.object, name="DiseaseCellularProcessRelationship_object", curie=IBDLIT.curie('object'),
                   model_uri=IBDLIT.DiseaseCellularProcessRelationship_object, domain=DiseaseCellularProcessRelationship, range=Optional[Union[str, CellularProcessId]])

slots.DiseaseCellularProcessRelationship_subject_qualifier = Slot(uri=IBDLIT.subject_qualifier, name="DiseaseCellularProcessRelationship_subject_qualifier", curie=IBDLIT.curie('subject_qualifier'),
                   model_uri=IBDLIT.DiseaseCellularProcessRelationship_subject_qualifier, domain=DiseaseCellularProcessRelationship, range=Optional[Union[str, NamedEntityId]])

slots.DiseaseCellularProcessRelationship_object_qualifier = Slot(uri=IBDLIT.object_qualifier, name="DiseaseCellularProcessRelationship_object_qualifier", curie=IBDLIT.curie('object_qualifier'),
                   model_uri=IBDLIT.DiseaseCellularProcessRelationship_object_qualifier, domain=DiseaseCellularProcessRelationship, range=Optional[Union[str, NamedEntityId]])

slots.GeneExposureRelationship_subject = Slot(uri=IBDLIT.subject, name="GeneExposureRelationship_subject", curie=IBDLIT.curie('subject'),
                   model_uri=IBDLIT.GeneExposureRelationship_subject, domain=GeneExposureRelationship, range=Optional[Union[str, ChemicalExposureId]])

slots.GeneExposureRelationship_predicate = Slot(uri=IBDLIT.predicate, name="GeneExposureRelationship_predicate", curie=IBDLIT.curie('predicate'),
                   model_uri=IBDLIT.GeneExposureRelationship_predicate, domain=GeneExposureRelationship, range=Optional[Union[str, ChemicalExposureToGenePredicateId]])

slots.GeneExposureRelationship_object = Slot(uri=IBDLIT.object, name="GeneExposureRelationship_object", curie=IBDLIT.curie('object'),
                   model_uri=IBDLIT.GeneExposureRelationship_object, domain=GeneExposureRelationship, range=Optional[Union[str, GeneId]])

slots.GeneExposureRelationship_subject_qualifier = Slot(uri=IBDLIT.subject_qualifier, name="GeneExposureRelationship_subject_qualifier", curie=IBDLIT.curie('subject_qualifier'),
                   model_uri=IBDLIT.GeneExposureRelationship_subject_qualifier, domain=GeneExposureRelationship, range=Optional[Union[str, NamedEntityId]])

slots.GeneExposureRelationship_object_qualifier = Slot(uri=IBDLIT.object_qualifier, name="GeneExposureRelationship_object_qualifier", curie=IBDLIT.curie('object_qualifier'),
                   model_uri=IBDLIT.GeneExposureRelationship_object_qualifier, domain=GeneExposureRelationship, range=Optional[Union[str, NamedEntityId]])