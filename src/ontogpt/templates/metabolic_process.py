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


class MetabolicProcess(NamedEntity):

    label: Optional[str] = Field(None, description="""the name of the metabolic process""")
    description: Optional[str] = Field(
        None, description="""a textual description of the metabolic process"""
    )
    synonyms: Optional[List[str]] = Field(
        default_factory=list, description="""alternative names of the metabolic process"""
    )
    subclass_of: Optional[List[str]] = Field(
        default_factory=list,
        description="""a semicolon separated list of broader metabolic processes which this is a subclass of""",
    )
    category: Optional[str] = Field(
        None,
        description="""the category of metabolic process, e.g metabolic process, catabolic process, biosynthetic process, small molecule sensor activity""",
    )
    inputs: Optional[List[str]] = Field(
        default_factory=list, description="""the inputs of the metabolic process"""
    )
    outputs: Optional[List[str]] = Field(
        default_factory=list, description="""the outputs of the metabolic process"""
    )
    id: Optional[str] = Field(None)


class MetabolicProcessCategory(NamedEntity):

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class ChemicalEntity(NamedEntity):

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
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
MetabolicProcess.update_forward_refs()
MetabolicProcessCategory.update_forward_refs()
ChemicalEntity.update_forward_refs()
CompoundExpression.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
