"""Environmental sample template."""
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


class Study(ConfiguredBaseModel):
    location: Optional[List[str]] = Field(
        default_factory=list, description="""the sites at which the study was conducted"""
    )
    environmental_material: Optional[List[str]] = Field(
        default_factory=list, description="""the environmental material that was sampled"""
    )
    environments: Optional[List[str]] = Field(default_factory=list)
    causal_relationships: Optional[List[CausalRelationship]] = Field(default_factory=list)
    variables: Optional[List[str]] = Field(default_factory=list)
    measurements: Optional[List[Measurement]] = Field(default_factory=list)


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


class Location(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class EnvironmentalMaterial(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Environment(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Variable(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Unit(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CompoundExpression(ConfiguredBaseModel):
    pass


class Measurement(CompoundExpression):
    value: Optional[str] = Field(None, description="""the value of the measurement""")
    unit: Optional[str] = Field(None, description="""the unit of the measurement""")


class CausalRelationship(CompoundExpression):
    cause: Optional[str] = Field(
        None, description="""the variable that is the cause of the effect"""
    )
    effect: Optional[str] = Field(None, description="""the things that is affected""")


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
        description="""An optional qualifier or modifier for the subject of\
            the statement, e.g. \"high dose\" or \"intravenously administered\"""",
    )
    object_qualifier: Optional[str] = Field(
        None,
        description="""An optional qualifier or modifier for the object of\
            the statement, e.g. \"severe\" or \"with additional complications\"""",
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
Study.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
Location.update_forward_refs()
EnvironmentalMaterial.update_forward_refs()
Environment.update_forward_refs()
Variable.update_forward_refs()
Unit.update_forward_refs()
CompoundExpression.update_forward_refs()
Measurement.update_forward_refs()
CausalRelationship.update_forward_refs()
Triple.update_forward_refs()
TextWithTriples.update_forward_refs()
RelationshipType.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
