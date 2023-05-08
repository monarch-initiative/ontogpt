"""Reaction template."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel as BaseModel
from pydantic import Field

metamodel_version = "None"
version = "None"


class WeakRefShimBaseModel(BaseModel):
    __slots__ = "__weakref__"


class ConfiguredBaseModel(
    WeakRefShimBaseModel,
    validate_assignment=True,
    validate_all=True,
    underscore_attrs_are_private=True,
    extra="forbid",
    arbitrary_types_allowed=True,
):
    pass


class GeneToReaction(ConfiguredBaseModel):
    gene: Optional[str] = Field(
        None, description="""name of the gene that catalyzes the reaction"""
    )
    reactions: Optional[Dict[str, Reaction]] = Field(
        default_factory=dict,
        description="""semicolon separated list of reaction equations\
            (e.g. A+B = C+D) catalyzed by the gene""",
    )
    organism: Optional[str] = Field(None)


class ReactionDocument(ConfiguredBaseModel):
    genes: Optional[List[str]] = Field(
        default_factory=list,
        description="""semicolon separated list of genes that catalyzes the mentioned reactions""",
    )
    reactions: Optional[Dict[str, Reaction]] = Field(
        default_factory=dict,
        description="""semicolon separated list of reaction equations\
            (e.g. A+B = C+D) catalyzed by the gene""",
    )
    gene_reaction_pairings: Optional[List[GeneReactionPairing]] = Field(
        default_factory=list,
        description="""semicolon separated list of gene to reaction pairings""",
    )
    organism: Optional[str] = Field(None)
    has_evidence: Optional[List[str]] = Field(
        default_factory=list, description="""evidence for the reaction"""
    )


class ExtractionResult(ConfiguredBaseModel):
    """A result of extracting knowledge on text."""

    input_id: Optional[str] = Field(None)
    input_title: Optional[str] = Field(None)
    input_text: Optional[str] = Field(None)
    raw_completion_output: Optional[str] = Field(None)
    prompt: Optional[str] = Field(None)
    extracted_object: Optional[Any] = Field(
        None, description="""The complex objects extracted from the text"""
    )
    named_entities: Optional[List[Any]] = Field(
        default_factory=list, description="""Named entities extracted from the text"""
    )


class NamedEntity(ConfiguredBaseModel):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Reaction(NamedEntity):
    label: Optional[str] = Field(None, description="""the name of the reaction""")
    description: Optional[str] = Field(
        None, description="""a textual description of the reaction"""
    )
    synonyms: Optional[List[str]] = Field(
        default_factory=list, description="""alternative names of the reaction"""
    )
    subclass_of: Optional[str] = Field(
        None, description="""the category to which this biological process belongs"""
    )
    left_side: Optional[List[str]] = Field(
        default_factory=list,
        description="""semicolon separated list of chemical entities on the left side""",
    )
    right_side: Optional[List[str]] = Field(
        default_factory=list,
        description="""semicolon separated list of chemical entities on the right side""",
    )
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")


class ReactionGrouping(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ChemicalEntity(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Evidence(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Gene(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Organism(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CompoundExpression(ConfiguredBaseModel):
    pass


class GeneReactionPairing(CompoundExpression):
    gene: Optional[str] = Field(
        None, description="""name of the gene that catalyzes the reaction"""
    )
    reaction: Optional[str] = Field(
        None,
        description="""equation describing the reaction (e.g. A+B = C+D) catalyzed by the gene""",
    )


class Triple(CompoundExpression):
    """Abstract parent for Relation Extraction tasks."""

    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    qualifier: Optional[str] = Field(
        None, description="""A qualifier for the statements, e.g. \"NOT\" for negation"""
    )
    subject_qualifier: Optional[str] = Field(
        None,
        description="""An optional qualifier or modifier for the subject of the statement,\
            e.g. \"high dose\" or \"intravenously administered\"""",
    )
    object_qualifier: Optional[str] = Field(
        None,
        description="""An optional qualifier or modifier for the object of the statement,\
            e.g. \"severe\" or \"with additional complications\"""",
    )


class TextWithTriples(ConfiguredBaseModel):
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)


class RelationshipType(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Publication(ConfiguredBaseModel):
    id: Optional[str] = Field(None, description="""The publication identifier""")
    title: Optional[str] = Field(None, description="""The title of the publication""")
    abstract: Optional[str] = Field(None, description="""The abstract of the publication""")
    combined_text: Optional[str] = Field(None)
    full_text: Optional[str] = Field(None, description="""The full text of the publication""")


class AnnotatorResult(ConfiguredBaseModel):
    subject_text: Optional[str] = Field(None)
    object_id: Optional[str] = Field(None)
    object_text: Optional[str] = Field(None)


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
GeneToReaction.update_forward_refs()
ReactionDocument.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
Reaction.update_forward_refs()
ReactionGrouping.update_forward_refs()
ChemicalEntity.update_forward_refs()
Evidence.update_forward_refs()
Gene.update_forward_refs()
Organism.update_forward_refs()
CompoundExpression.update_forward_refs()
GeneReactionPairing.update_forward_refs()
Triple.update_forward_refs()
TextWithTriples.update_forward_refs()
RelationshipType.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
