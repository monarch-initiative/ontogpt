# Auto generated from ibd.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:54:16
# Schema: gocam-template
#
# id: http://w3id.org/ontogpt/gocam
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
CHEBI = CurieNamespace('CHEBI', 'http://example.org/UNKNOWN/CHEBI/')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
EFO = CurieNamespace('EFO', 'http://example.org/UNKNOWN/EFO/')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
HGNC = CurieNamespace('HGNC', 'http://example.org/UNKNOWN/HGNC/')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://example.org/UNKNOWN/NCBITaxon/')
PR = CurieNamespace('PR', 'http://example.org/UNKNOWN/PR/')
PW = CurieNamespace('PW', 'http://example.org/UNKNOWN/PW/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
UBERON = CurieNamespace('UBERON', 'http://example.org/UNKNOWN/UBERON/')
UNIPROTKB = CurieNamespace('UniProtKB', 'http://example.org/UNKNOWN/UniProtKB/')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
GOCAM = CurieNamespace('gocam', 'http://w3id.org/ontogpt/gocam/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
DEFAULT_ = GOCAM


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class GeneId(NamedEntityId):
    pass


class PathwayId(NamedEntityId):
    pass


class CellularProcessId(NamedEntityId):
    pass


class MolecularActivityId(NamedEntityId):
    pass


class GeneLocationId(NamedEntityId):
    pass


class OrganismId(NamedEntityId):
    pass


class MoleculeId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass
class IBDAnnotations(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.IBDAnnotations
    class_class_curie: ClassVar[str] = "gocam:IBDAnnotations"
    class_name: ClassVar[str] = "IBDAnnotations"
    class_model_uri: ClassVar[URIRef] = GOCAM.IBDAnnotations

    genes: Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]] = empty_list()
    organisms: Optional[Union[Union[str, OrganismId], List[Union[str, OrganismId]]]] = empty_list()
    gene_organisms: Optional[Union[Union[dict, "GeneOrganismRelationship"], List[Union[dict, "GeneOrganismRelationship"]]]] = empty_list()
    activities: Optional[Union[Union[str, MolecularActivityId], List[Union[str, MolecularActivityId]]]] = empty_list()
    gene_functions: Optional[Union[Union[dict, "GeneMolecularActivityRelationship"], List[Union[dict, "GeneMolecularActivityRelationship"]]]] = empty_list()
    cellular_processes: Optional[Union[Union[str, CellularProcessId], List[Union[str, CellularProcessId]]]] = empty_list()
    pathways: Optional[Union[Union[str, PathwayId], List[Union[str, PathwayId]]]] = empty_list()
    gene_gene_interactions: Optional[Union[Union[dict, "GeneGeneInteraction"], List[Union[dict, "GeneGeneInteraction"]]]] = empty_list()
    gene_localizations: Optional[Union[Union[dict, "GeneSubcellularLocalizationRelationship"], List[Union[dict, "GeneSubcellularLocalizationRelationship"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneId) else GeneId(v) for v in self.genes]

        if not isinstance(self.organisms, list):
            self.organisms = [self.organisms] if self.organisms is not None else []
        self.organisms = [v if isinstance(v, OrganismId) else OrganismId(v) for v in self.organisms]

        if not isinstance(self.gene_organisms, list):
            self.gene_organisms = [self.gene_organisms] if self.gene_organisms is not None else []
        self.gene_organisms = [v if isinstance(v, GeneOrganismRelationship) else GeneOrganismRelationship(**as_dict(v)) for v in self.gene_organisms]

        if not isinstance(self.activities, list):
            self.activities = [self.activities] if self.activities is not None else []
        self.activities = [v if isinstance(v, MolecularActivityId) else MolecularActivityId(v) for v in self.activities]

        if not isinstance(self.gene_functions, list):
            self.gene_functions = [self.gene_functions] if self.gene_functions is not None else []
        self.gene_functions = [v if isinstance(v, GeneMolecularActivityRelationship) else GeneMolecularActivityRelationship(**as_dict(v)) for v in self.gene_functions]

        if not isinstance(self.cellular_processes, list):
            self.cellular_processes = [self.cellular_processes] if self.cellular_processes is not None else []
        self.cellular_processes = [v if isinstance(v, CellularProcessId) else CellularProcessId(v) for v in self.cellular_processes]

        if not isinstance(self.pathways, list):
            self.pathways = [self.pathways] if self.pathways is not None else []
        self.pathways = [v if isinstance(v, PathwayId) else PathwayId(v) for v in self.pathways]

        if not isinstance(self.gene_gene_interactions, list):
            self.gene_gene_interactions = [self.gene_gene_interactions] if self.gene_gene_interactions is not None else []
        self.gene_gene_interactions = [v if isinstance(v, GeneGeneInteraction) else GeneGeneInteraction(**as_dict(v)) for v in self.gene_gene_interactions]

        if not isinstance(self.gene_localizations, list):
            self.gene_localizations = [self.gene_localizations] if self.gene_localizations is not None else []
        self.gene_localizations = [v if isinstance(v, GeneSubcellularLocalizationRelationship) else GeneSubcellularLocalizationRelationship(**as_dict(v)) for v in self.gene_localizations]

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
    class_model_uri: ClassVar[URIRef] = GOCAM.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = GOCAM.NamedEntity

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

    class_class_uri: ClassVar[URIRef] = GOCAM.Gene
    class_class_curie: ClassVar[str] = "gocam:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = GOCAM.Gene

    id: Union[str, GeneId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Pathway(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Pathway
    class_class_curie: ClassVar[str] = "gocam:Pathway"
    class_name: ClassVar[str] = "Pathway"
    class_model_uri: ClassVar[URIRef] = GOCAM.Pathway

    id: Union[str, PathwayId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PathwayId):
            self.id = PathwayId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CellularProcess(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.CellularProcess
    class_class_curie: ClassVar[str] = "gocam:CellularProcess"
    class_name: ClassVar[str] = "CellularProcess"
    class_model_uri: ClassVar[URIRef] = GOCAM.CellularProcess

    id: Union[str, CellularProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellularProcessId):
            self.id = CellularProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MolecularActivity(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.MolecularActivity
    class_class_curie: ClassVar[str] = "gocam:MolecularActivity"
    class_name: ClassVar[str] = "MolecularActivity"
    class_model_uri: ClassVar[URIRef] = GOCAM.MolecularActivity

    id: Union[str, MolecularActivityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularActivityId):
            self.id = MolecularActivityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GeneLocation(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.GeneLocation
    class_class_curie: ClassVar[str] = "gocam:GeneLocation"
    class_name: ClassVar[str] = "GeneLocation"
    class_model_uri: ClassVar[URIRef] = GOCAM.GeneLocation

    id: Union[str, GeneLocationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneLocationId):
            self.id = GeneLocationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Organism(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Organism
    class_class_curie: ClassVar[str] = "gocam:Organism"
    class_name: ClassVar[str] = "Organism"
    class_model_uri: ClassVar[URIRef] = GOCAM.Organism

    id: Union[str, OrganismId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismId):
            self.id = OrganismId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Molecule(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.Molecule
    class_class_curie: ClassVar[str] = "gocam:Molecule"
    class_name: ClassVar[str] = "Molecule"
    class_model_uri: ClassVar[URIRef] = GOCAM.Molecule

    id: Union[str, MoleculeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoleculeId):
            self.id = MoleculeId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = GOCAM.CompoundExpression


@dataclass
class GeneOrganismRelationship(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.GeneOrganismRelationship
    class_class_curie: ClassVar[str] = "gocam:GeneOrganismRelationship"
    class_name: ClassVar[str] = "GeneOrganismRelationship"
    class_model_uri: ClassVar[URIRef] = GOCAM.GeneOrganismRelationship

    gene: Optional[Union[str, GeneId]] = None
    organism: Optional[Union[str, OrganismId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        if self.organism is not None and not isinstance(self.organism, OrganismId):
            self.organism = OrganismId(self.organism)

        super().__post_init__(**kwargs)


@dataclass
class GeneMolecularActivityRelationship(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.GeneMolecularActivityRelationship
    class_class_curie: ClassVar[str] = "gocam:GeneMolecularActivityRelationship"
    class_name: ClassVar[str] = "GeneMolecularActivityRelationship"
    class_model_uri: ClassVar[URIRef] = GOCAM.GeneMolecularActivityRelationship

    gene: Optional[Union[str, GeneId]] = None
    molecular_activity: Optional[Union[str, MolecularActivityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        if self.molecular_activity is not None and not isinstance(self.molecular_activity, MolecularActivityId):
            self.molecular_activity = MolecularActivityId(self.molecular_activity)

        super().__post_init__(**kwargs)


@dataclass
class GeneMolecularActivityRelationship2(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.GeneMolecularActivityRelationship2
    class_class_curie: ClassVar[str] = "gocam:GeneMolecularActivityRelationship2"
    class_name: ClassVar[str] = "GeneMolecularActivityRelationship2"
    class_model_uri: ClassVar[URIRef] = GOCAM.GeneMolecularActivityRelationship2

    gene: Optional[Union[str, GeneId]] = None
    molecular_activity: Optional[Union[str, MolecularActivityId]] = None
    target: Optional[Union[str, MoleculeId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        if self.molecular_activity is not None and not isinstance(self.molecular_activity, MolecularActivityId):
            self.molecular_activity = MolecularActivityId(self.molecular_activity)

        if self.target is not None and not isinstance(self.target, MoleculeId):
            self.target = MoleculeId(self.target)

        super().__post_init__(**kwargs)


@dataclass
class GeneSubcellularLocalizationRelationship(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.GeneSubcellularLocalizationRelationship
    class_class_curie: ClassVar[str] = "gocam:GeneSubcellularLocalizationRelationship"
    class_name: ClassVar[str] = "GeneSubcellularLocalizationRelationship"
    class_model_uri: ClassVar[URIRef] = GOCAM.GeneSubcellularLocalizationRelationship

    gene: Optional[Union[str, GeneId]] = None
    location: Optional[Union[str, GeneLocationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        if self.location is not None and not isinstance(self.location, GeneLocationId):
            self.location = GeneLocationId(self.location)

        super().__post_init__(**kwargs)


@dataclass
class GeneGeneInteraction(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GOCAM.GeneGeneInteraction
    class_class_curie: ClassVar[str] = "gocam:GeneGeneInteraction"
    class_name: ClassVar[str] = "GeneGeneInteraction"
    class_model_uri: ClassVar[URIRef] = GOCAM.GeneGeneInteraction

    gene1: Optional[Union[str, GeneId]] = None
    gene2: Optional[Union[str, GeneId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gene1 is not None and not isinstance(self.gene1, GeneId):
            self.gene1 = GeneId(self.gene1)

        if self.gene2 is not None and not isinstance(self.gene2, GeneId):
            self.gene2 = GeneId(self.gene2)

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
    class_model_uri: ClassVar[URIRef] = GOCAM.Triple

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
    class_model_uri: ClassVar[URIRef] = GOCAM.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = GOCAM.RelationshipType

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
    class_model_uri: ClassVar[URIRef] = GOCAM.Publication

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
    class_model_uri: ClassVar[URIRef] = GOCAM.AnnotatorResult

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
class GeneLocationEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GeneLocationEnum",
    )

class GOCellComponentType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GOCellComponentType",
    )

class CellType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="CellType",
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

slots.iBDAnnotations__genes = Slot(uri=GOCAM.genes, name="iBDAnnotations__genes", curie=GOCAM.curie('genes'),
                   model_uri=GOCAM.iBDAnnotations__genes, domain=None, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.iBDAnnotations__organisms = Slot(uri=GOCAM.organisms, name="iBDAnnotations__organisms", curie=GOCAM.curie('organisms'),
                   model_uri=GOCAM.iBDAnnotations__organisms, domain=None, range=Optional[Union[Union[str, OrganismId], List[Union[str, OrganismId]]]])

slots.iBDAnnotations__gene_organisms = Slot(uri=GOCAM.gene_organisms, name="iBDAnnotations__gene_organisms", curie=GOCAM.curie('gene_organisms'),
                   model_uri=GOCAM.iBDAnnotations__gene_organisms, domain=None, range=Optional[Union[Union[dict, GeneOrganismRelationship], List[Union[dict, GeneOrganismRelationship]]]])

slots.iBDAnnotations__activities = Slot(uri=GOCAM.activities, name="iBDAnnotations__activities", curie=GOCAM.curie('activities'),
                   model_uri=GOCAM.iBDAnnotations__activities, domain=None, range=Optional[Union[Union[str, MolecularActivityId], List[Union[str, MolecularActivityId]]]])

slots.iBDAnnotations__gene_functions = Slot(uri=GOCAM.gene_functions, name="iBDAnnotations__gene_functions", curie=GOCAM.curie('gene_functions'),
                   model_uri=GOCAM.iBDAnnotations__gene_functions, domain=None, range=Optional[Union[Union[dict, GeneMolecularActivityRelationship], List[Union[dict, GeneMolecularActivityRelationship]]]])

slots.iBDAnnotations__cellular_processes = Slot(uri=GOCAM.cellular_processes, name="iBDAnnotations__cellular_processes", curie=GOCAM.curie('cellular_processes'),
                   model_uri=GOCAM.iBDAnnotations__cellular_processes, domain=None, range=Optional[Union[Union[str, CellularProcessId], List[Union[str, CellularProcessId]]]])

slots.iBDAnnotations__pathways = Slot(uri=GOCAM.pathways, name="iBDAnnotations__pathways", curie=GOCAM.curie('pathways'),
                   model_uri=GOCAM.iBDAnnotations__pathways, domain=None, range=Optional[Union[Union[str, PathwayId], List[Union[str, PathwayId]]]])

slots.iBDAnnotations__gene_gene_interactions = Slot(uri=GOCAM.gene_gene_interactions, name="iBDAnnotations__gene_gene_interactions", curie=GOCAM.curie('gene_gene_interactions'),
                   model_uri=GOCAM.iBDAnnotations__gene_gene_interactions, domain=None, range=Optional[Union[Union[dict, GeneGeneInteraction], List[Union[dict, GeneGeneInteraction]]]])

slots.iBDAnnotations__gene_localizations = Slot(uri=GOCAM.gene_localizations, name="iBDAnnotations__gene_localizations", curie=GOCAM.curie('gene_localizations'),
                   model_uri=GOCAM.iBDAnnotations__gene_localizations, domain=None, range=Optional[Union[Union[dict, GeneSubcellularLocalizationRelationship], List[Union[dict, GeneSubcellularLocalizationRelationship]]]])

slots.geneOrganismRelationship__gene = Slot(uri=GOCAM.gene, name="geneOrganismRelationship__gene", curie=GOCAM.curie('gene'),
                   model_uri=GOCAM.geneOrganismRelationship__gene, domain=None, range=Optional[Union[str, GeneId]])

slots.geneOrganismRelationship__organism = Slot(uri=GOCAM.organism, name="geneOrganismRelationship__organism", curie=GOCAM.curie('organism'),
                   model_uri=GOCAM.geneOrganismRelationship__organism, domain=None, range=Optional[Union[str, OrganismId]])

slots.geneMolecularActivityRelationship__gene = Slot(uri=GOCAM.gene, name="geneMolecularActivityRelationship__gene", curie=GOCAM.curie('gene'),
                   model_uri=GOCAM.geneMolecularActivityRelationship__gene, domain=None, range=Optional[Union[str, GeneId]])

slots.geneMolecularActivityRelationship__molecular_activity = Slot(uri=GOCAM.molecular_activity, name="geneMolecularActivityRelationship__molecular_activity", curie=GOCAM.curie('molecular_activity'),
                   model_uri=GOCAM.geneMolecularActivityRelationship__molecular_activity, domain=None, range=Optional[Union[str, MolecularActivityId]])

slots.geneMolecularActivityRelationship2__gene = Slot(uri=GOCAM.gene, name="geneMolecularActivityRelationship2__gene", curie=GOCAM.curie('gene'),
                   model_uri=GOCAM.geneMolecularActivityRelationship2__gene, domain=None, range=Optional[Union[str, GeneId]])

slots.geneMolecularActivityRelationship2__molecular_activity = Slot(uri=GOCAM.molecular_activity, name="geneMolecularActivityRelationship2__molecular_activity", curie=GOCAM.curie('molecular_activity'),
                   model_uri=GOCAM.geneMolecularActivityRelationship2__molecular_activity, domain=None, range=Optional[Union[str, MolecularActivityId]])

slots.geneMolecularActivityRelationship2__target = Slot(uri=GOCAM.target, name="geneMolecularActivityRelationship2__target", curie=GOCAM.curie('target'),
                   model_uri=GOCAM.geneMolecularActivityRelationship2__target, domain=None, range=Optional[Union[str, MoleculeId]])

slots.geneSubcellularLocalizationRelationship__gene = Slot(uri=GOCAM.gene, name="geneSubcellularLocalizationRelationship__gene", curie=GOCAM.curie('gene'),
                   model_uri=GOCAM.geneSubcellularLocalizationRelationship__gene, domain=None, range=Optional[Union[str, GeneId]])

slots.geneSubcellularLocalizationRelationship__location = Slot(uri=GOCAM.location, name="geneSubcellularLocalizationRelationship__location", curie=GOCAM.curie('location'),
                   model_uri=GOCAM.geneSubcellularLocalizationRelationship__location, domain=None, range=Optional[Union[str, GeneLocationId]])

slots.geneGeneInteraction__gene1 = Slot(uri=GOCAM.gene1, name="geneGeneInteraction__gene1", curie=GOCAM.curie('gene1'),
                   model_uri=GOCAM.geneGeneInteraction__gene1, domain=None, range=Optional[Union[str, GeneId]])

slots.geneGeneInteraction__gene2 = Slot(uri=GOCAM.gene2, name="geneGeneInteraction__gene2", curie=GOCAM.curie('gene2'),
                   model_uri=GOCAM.geneGeneInteraction__gene2, domain=None, range=Optional[Union[str, GeneId]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=GOCAM.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=GOCAM.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=GOCAM.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=GOCAM.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=GOCAM.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=GOCAM.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=GOCAM.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=GOCAM.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=GOCAM.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=GOCAM.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=GOCAM.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=GOCAM.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=GOCAM.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=GOCAM.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=GOCAM.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=GOCAM.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=GOCAM.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=GOCAM.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=GOCAM.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=GOCAM.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=GOCAM.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=GOCAM.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=GOCAM.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=GOCAM.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=GOCAM.annotatorResult__object_text, domain=None, range=Optional[str])

slots.GeneLocation_id = Slot(uri=GOCAM.id, name="GeneLocation_id", curie=GOCAM.curie('id'),
                   model_uri=GOCAM.GeneLocation_id, domain=GeneLocation, range=Union[str, GeneLocationId])