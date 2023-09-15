# Auto generated from reaction.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:56:03
# Schema: reaction-template
#
# id: https://w3id.org/ontogpt/reaction
# description: A template for reactions
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
ECO = CurieNamespace('ECO', 'http://example.org/UNKNOWN/ECO/')
GO = CurieNamespace('GO', 'http://example.org/UNKNOWN/GO/')
HGNC = CurieNamespace('HGNC', 'http://example.org/UNKNOWN/HGNC/')
MS = CurieNamespace('MS', 'http://example.org/UNKNOWN/MS/')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://example.org/UNKNOWN/NCBITaxon/')
OBI = CurieNamespace('OBI', 'http://example.org/UNKNOWN/OBI/')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
REACTION = CurieNamespace('reaction', 'http://w3id.org/ontogpt/reaction/')
DEFAULT_ = REACTION


# Types

# Class references
class NamedEntityId(extended_str):
    pass


class ReactionId(NamedEntityId):
    pass


class ReactionGroupingId(NamedEntityId):
    pass


class ChemicalEntityId(NamedEntityId):
    pass


class EvidenceId(NamedEntityId):
    pass


class GeneId(NamedEntityId):
    pass


class OrganismId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass
class GeneToReaction(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTION.GeneToReaction
    class_class_curie: ClassVar[str] = "reaction:GeneToReaction"
    class_name: ClassVar[str] = "GeneToReaction"
    class_model_uri: ClassVar[URIRef] = REACTION.GeneToReaction

    gene: Optional[Union[str, GeneId]] = None
    reactions: Optional[Union[Dict[Union[str, ReactionId], Union[dict, Reaction]], List[Union[dict, Reaction]]]] = empty_dict()
    organism: Optional[Union[str, OrganismId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        self._normalize_inlined_as_dict(slot_name="reactions", slot_type=Reaction, key_name="id", keyed=True)

        if self.organism is not None and not isinstance(self.organism, OrganismId):
            self.organism = OrganismId(self.organism)

        super().__post_init__(**kwargs)


@dataclass
class ReactionDocument(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTION.ReactionDocument
    class_class_curie: ClassVar[str] = "reaction:ReactionDocument"
    class_name: ClassVar[str] = "ReactionDocument"
    class_model_uri: ClassVar[URIRef] = REACTION.ReactionDocument

    genes: Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]] = empty_list()
    reactions: Optional[Union[Dict[Union[str, ReactionId], Union[dict, Reaction]], List[Union[dict, Reaction]]]] = empty_dict()
    gene_reaction_pairings: Optional[Union[Union[dict, "GeneReactionPairing"], List[Union[dict, "GeneReactionPairing"]]]] = empty_list()
    organism: Optional[Union[str, OrganismId]] = None
    has_evidence: Optional[Union[Union[str, EvidenceId], List[Union[str, EvidenceId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.genes, list):
            self.genes = [self.genes] if self.genes is not None else []
        self.genes = [v if isinstance(v, GeneId) else GeneId(v) for v in self.genes]

        self._normalize_inlined_as_dict(slot_name="reactions", slot_type=Reaction, key_name="id", keyed=True)

        if not isinstance(self.gene_reaction_pairings, list):
            self.gene_reaction_pairings = [self.gene_reaction_pairings] if self.gene_reaction_pairings is not None else []
        self.gene_reaction_pairings = [v if isinstance(v, GeneReactionPairing) else GeneReactionPairing(**as_dict(v)) for v in self.gene_reaction_pairings]

        if self.organism is not None and not isinstance(self.organism, OrganismId):
            self.organism = OrganismId(self.organism)

        if not isinstance(self.has_evidence, list):
            self.has_evidence = [self.has_evidence] if self.has_evidence is not None else []
        self.has_evidence = [v if isinstance(v, EvidenceId) else EvidenceId(v) for v in self.has_evidence]

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
    class_model_uri: ClassVar[URIRef] = REACTION.ExtractionResult

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
    class_model_uri: ClassVar[URIRef] = REACTION.NamedEntity

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
class Reaction(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTION.Reaction
    class_class_curie: ClassVar[str] = "reaction:Reaction"
    class_name: ClassVar[str] = "Reaction"
    class_model_uri: ClassVar[URIRef] = REACTION.Reaction

    id: Union[str, ReactionId] = None
    label: Optional[str] = None
    description: Optional[str] = None
    synonyms: Optional[Union[str, List[str]]] = empty_list()
    subclass_of: Optional[Union[str, ReactionGroupingId]] = None
    left_side: Optional[Union[Union[str, ChemicalEntityId], List[Union[str, ChemicalEntityId]]]] = empty_list()
    right_side: Optional[Union[Union[str, ChemicalEntityId], List[Union[str, ChemicalEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionId):
            self.id = ReactionId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.synonyms, list):
            self.synonyms = [self.synonyms] if self.synonyms is not None else []
        self.synonyms = [v if isinstance(v, str) else str(v) for v in self.synonyms]

        if self.subclass_of is not None and not isinstance(self.subclass_of, ReactionGroupingId):
            self.subclass_of = ReactionGroupingId(self.subclass_of)

        if not isinstance(self.left_side, list):
            self.left_side = [self.left_side] if self.left_side is not None else []
        self.left_side = [v if isinstance(v, ChemicalEntityId) else ChemicalEntityId(v) for v in self.left_side]

        if not isinstance(self.right_side, list):
            self.right_side = [self.right_side] if self.right_side is not None else []
        self.right_side = [v if isinstance(v, ChemicalEntityId) else ChemicalEntityId(v) for v in self.right_side]

        super().__post_init__(**kwargs)


@dataclass
class ReactionGrouping(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTION.ReactionGrouping
    class_class_curie: ClassVar[str] = "reaction:ReactionGrouping"
    class_name: ClassVar[str] = "ReactionGrouping"
    class_model_uri: ClassVar[URIRef] = REACTION.ReactionGrouping

    id: Union[str, ReactionGroupingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionGroupingId):
            self.id = ReactionGroupingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ChemicalEntity(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTION.ChemicalEntity
    class_class_curie: ClassVar[str] = "reaction:ChemicalEntity"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = REACTION.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Evidence(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTION.Evidence
    class_class_curie: ClassVar[str] = "reaction:Evidence"
    class_name: ClassVar[str] = "Evidence"
    class_model_uri: ClassVar[URIRef] = REACTION.Evidence

    id: Union[str, EvidenceId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvidenceId):
            self.id = EvidenceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Gene(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTION.Gene
    class_class_curie: ClassVar[str] = "reaction:Gene"
    class_name: ClassVar[str] = "Gene"
    class_model_uri: ClassVar[URIRef] = REACTION.Gene

    id: Union[str, GeneId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneId):
            self.id = GeneId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Organism(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTION.Organism
    class_class_curie: ClassVar[str] = "reaction:Organism"
    class_name: ClassVar[str] = "Organism"
    class_model_uri: ClassVar[URIRef] = REACTION.Organism

    id: Union[str, OrganismId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganismId):
            self.id = OrganismId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = REACTION.CompoundExpression


@dataclass
class GeneReactionPairing(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = REACTION.GeneReactionPairing
    class_class_curie: ClassVar[str] = "reaction:GeneReactionPairing"
    class_name: ClassVar[str] = "GeneReactionPairing"
    class_model_uri: ClassVar[URIRef] = REACTION.GeneReactionPairing

    gene: Optional[Union[str, GeneId]] = None
    reaction: Optional[Union[str, ReactionId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gene is not None and not isinstance(self.gene, GeneId):
            self.gene = GeneId(self.gene)

        if self.reaction is not None and not isinstance(self.reaction, ReactionId):
            self.reaction = ReactionId(self.reaction)

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
    class_model_uri: ClassVar[URIRef] = REACTION.Triple

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
    class_model_uri: ClassVar[URIRef] = REACTION.TextWithTriples

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
    class_model_uri: ClassVar[URIRef] = REACTION.RelationshipType

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
    class_model_uri: ClassVar[URIRef] = REACTION.Publication

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
    class_model_uri: ClassVar[URIRef] = REACTION.AnnotatorResult

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

slots.reaction__label = Slot(uri=REACTION.label, name="reaction__label", curie=REACTION.curie('label'),
                   model_uri=REACTION.reaction__label, domain=None, range=Optional[str])

slots.reaction__description = Slot(uri=REACTION.description, name="reaction__description", curie=REACTION.curie('description'),
                   model_uri=REACTION.reaction__description, domain=None, range=Optional[str])

slots.reaction__synonyms = Slot(uri=REACTION.synonyms, name="reaction__synonyms", curie=REACTION.curie('synonyms'),
                   model_uri=REACTION.reaction__synonyms, domain=None, range=Optional[Union[str, List[str]]])

slots.reaction__subclass_of = Slot(uri=REACTION.subclass_of, name="reaction__subclass_of", curie=REACTION.curie('subclass_of'),
                   model_uri=REACTION.reaction__subclass_of, domain=None, range=Optional[Union[str, ReactionGroupingId]])

slots.reaction__left_side = Slot(uri=REACTION.left_side, name="reaction__left_side", curie=REACTION.curie('left_side'),
                   model_uri=REACTION.reaction__left_side, domain=None, range=Optional[Union[Union[str, ChemicalEntityId], List[Union[str, ChemicalEntityId]]]])

slots.reaction__right_side = Slot(uri=REACTION.right_side, name="reaction__right_side", curie=REACTION.curie('right_side'),
                   model_uri=REACTION.reaction__right_side, domain=None, range=Optional[Union[Union[str, ChemicalEntityId], List[Union[str, ChemicalEntityId]]]])

slots.geneToReaction__gene = Slot(uri=REACTION.gene, name="geneToReaction__gene", curie=REACTION.curie('gene'),
                   model_uri=REACTION.geneToReaction__gene, domain=None, range=Optional[Union[str, GeneId]])

slots.geneToReaction__reactions = Slot(uri=REACTION.reactions, name="geneToReaction__reactions", curie=REACTION.curie('reactions'),
                   model_uri=REACTION.geneToReaction__reactions, domain=None, range=Optional[Union[Dict[Union[str, ReactionId], Union[dict, Reaction]], List[Union[dict, Reaction]]]])

slots.geneToReaction__organism = Slot(uri=REACTION.organism, name="geneToReaction__organism", curie=REACTION.curie('organism'),
                   model_uri=REACTION.geneToReaction__organism, domain=None, range=Optional[Union[str, OrganismId]])

slots.reactionDocument__genes = Slot(uri=REACTION.genes, name="reactionDocument__genes", curie=REACTION.curie('genes'),
                   model_uri=REACTION.reactionDocument__genes, domain=None, range=Optional[Union[Union[str, GeneId], List[Union[str, GeneId]]]])

slots.reactionDocument__reactions = Slot(uri=REACTION.reactions, name="reactionDocument__reactions", curie=REACTION.curie('reactions'),
                   model_uri=REACTION.reactionDocument__reactions, domain=None, range=Optional[Union[Dict[Union[str, ReactionId], Union[dict, Reaction]], List[Union[dict, Reaction]]]])

slots.reactionDocument__gene_reaction_pairings = Slot(uri=REACTION.gene_reaction_pairings, name="reactionDocument__gene_reaction_pairings", curie=REACTION.curie('gene_reaction_pairings'),
                   model_uri=REACTION.reactionDocument__gene_reaction_pairings, domain=None, range=Optional[Union[Union[dict, GeneReactionPairing], List[Union[dict, GeneReactionPairing]]]])

slots.reactionDocument__organism = Slot(uri=REACTION.organism, name="reactionDocument__organism", curie=REACTION.curie('organism'),
                   model_uri=REACTION.reactionDocument__organism, domain=None, range=Optional[Union[str, OrganismId]])

slots.reactionDocument__has_evidence = Slot(uri=REACTION.has_evidence, name="reactionDocument__has_evidence", curie=REACTION.curie('has_evidence'),
                   model_uri=REACTION.reactionDocument__has_evidence, domain=None, range=Optional[Union[Union[str, EvidenceId], List[Union[str, EvidenceId]]]])

slots.geneReactionPairing__gene = Slot(uri=REACTION.gene, name="geneReactionPairing__gene", curie=REACTION.curie('gene'),
                   model_uri=REACTION.geneReactionPairing__gene, domain=None, range=Optional[Union[str, GeneId]])

slots.geneReactionPairing__reaction = Slot(uri=REACTION.reaction, name="geneReactionPairing__reaction", curie=REACTION.curie('reaction'),
                   model_uri=REACTION.geneReactionPairing__reaction, domain=None, range=Optional[Union[str, ReactionId]])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=REACTION.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=REACTION.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=REACTION.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=REACTION.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=REACTION.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=REACTION.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=REACTION.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=REACTION.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=REACTION.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=REACTION.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=REACTION.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=REACTION.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=REACTION.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=REACTION.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=REACTION.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=REACTION.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=REACTION.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=REACTION.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=REACTION.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=REACTION.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=REACTION.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=REACTION.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=REACTION.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=REACTION.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=REACTION.annotatorResult__object_text, domain=None, range=Optional[str])