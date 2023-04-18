"""HALO template."""
from __future__ import annotations

from typing import Any, List, Optional

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


class Ontology(ConfiguredBaseModel):
    elements: Optional[List[OntologyElement]] = Field(default_factory=list)


class OntologyElement(ConfiguredBaseModel):
    name: Optional[str] = Field(None, description="""the name of the entity""")
    context: Optional[str] = Field(
        None, description="""the ontology to which this belongs (single-valued)"""
    )
    description: Optional[str] = Field(
        None, description="""a textual description of the entity (single-valued)"""
    )
    synonyms: Optional[List[str]] = Field(
        default_factory=list, description="""a list of alternative names of the entity"""
    )
    categories: Optional[List[str]] = Field(
        default_factory=list,
        description="""a list of the categories to which this entity belongs""",
    )
    subclass_of: Optional[List[str]] = Field(
        default_factory=list, description="""a list of parent class (superclasses) of this entity"""
    )
    part_of: Optional[List[str]] = Field(
        default_factory=list, description="""a list of things this element is part of"""
    )
    subtypes: Optional[List[str]] = Field(
        default_factory=list, description="""a list of child classes (subclasses) of this entity"""
    )
    parts: Optional[List[str]] = Field(
        default_factory=list,
        description="""a list of names of things this element has as parts (components)""",
    )
    equivalent_to: Optional[str] = Field(
        None,
        description="""an OWL class expression with the necessary and\
            sufficient conditions for this entity to be an instance of this class""",
    )


class Category(OntologyElement):
    name: Optional[str] = Field(None, description="""the name of the entity""")
    context: Optional[str] = Field(
        None, description="""the ontology to which this belongs (single-valued)"""
    )
    description: Optional[str] = Field(
        None, description="""a textual description of the entity (single-valued)"""
    )
    synonyms: Optional[List[str]] = Field(
        default_factory=list, description="""a list of alternative names of the entity"""
    )
    categories: Optional[List[str]] = Field(
        default_factory=list,
        description="""a list of the categories to which this entity belongs""",
    )
    subclass_of: Optional[List[str]] = Field(
        default_factory=list, description="""a list of parent class (superclasses) of this entity"""
    )
    part_of: Optional[List[str]] = Field(
        default_factory=list, description="""a list of things this element is part of"""
    )
    subtypes: Optional[List[str]] = Field(
        default_factory=list, description="""a list of child classes (subclasses) of this entity"""
    )
    parts: Optional[List[str]] = Field(
        default_factory=list,
        description="""a list of names of things this element has as parts (components)""",
    )
    equivalent_to: Optional[str] = Field(
        None,
        description="""an OWL class expression with the necessary and\
            sufficient conditions for this entity to be an instance of this class""",
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


class CompoundExpression(ConfiguredBaseModel):
    pass


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
Ontology.update_forward_refs()
OntologyElement.update_forward_refs()
Category.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
CompoundExpression.update_forward_refs()
Triple.update_forward_refs()
TextWithTriples.update_forward_refs()
RelationshipType.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
