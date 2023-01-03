from __future__ import annotations

from datetime import date, datetime
from enum import Enum
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


class LogicalDefinition(ConfiguredBaseModel):

    genus: Optional[List[str]] = Field(default_factory=list)
    differentiating_characteristic_relationship: Optional[str] = Field(None)
    differentiating_characteristic_parents: Optional[List[str]] = Field(default_factory=list)


class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """

    input_id: Optional[str] = Field(None)
    input_title: Optional[str] = Field(None)
    input_text: Optional[str] = Field(None)
    raw_completion_output: Optional[str] = Field(None)
    prompt: Optional[str] = Field(None)
    results: Optional[Any] = Field(None)
    named_entities: Optional[List[Any]] = Field(default_factory=list)


class NamedEntity(ConfiguredBaseModel):

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class OntologyClass(NamedEntity):

    label: Optional[str] = Field(None, description="""the name of the entity""")
    description: Optional[str] = Field(None, description="""a textual description of the entity""")
    synonyms: Optional[List[str]] = Field(
        default_factory=list, description="""alternative names of the entity"""
    )
    categories: Optional[List[str]] = Field(
        default_factory=list, description="""the categories to which this entity belongs"""
    )
    subclass_of: Optional[List[str]] = Field(default_factory=list)
    logical_definition: Optional[LogicalDefinition] = Field(
        None,
        description="""the necessary and sufficient conditions for this entity to be an instance of this class""",
    )
    id: Optional[str] = Field(None)


class Relation(NamedEntity):

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class CompoundExpression(ConfiguredBaseModel):

    None


class Publication(ConfiguredBaseModel):

    id: Optional[str] = Field(None, description="""The publication identifier""")
    title: Optional[str] = Field(None, description="""The title of the publication""")
    abstract: Optional[str] = Field(None, description="""The abstract of the publication""")
    full_text: Optional[str] = Field(None, description="""The full text of the publication""")


class AnnotatorResult(ConfiguredBaseModel):

    subject_text: Optional[str] = Field(None)
    object_id: Optional[str] = Field(None)
    object_text: Optional[str] = Field(None)


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
LogicalDefinition.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
OntologyClass.update_forward_refs()
Relation.update_forward_refs()
CompoundExpression.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
