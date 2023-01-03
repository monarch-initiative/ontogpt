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


class DrugMechanism(ConfiguredBaseModel):

    disease: Optional[str] = Field(None, description="""the name of the disease that is treated""")
    drug: Optional[str] = Field(
        None, description="""the name of the drug that treats the disease"""
    )
    mechanism_links: Optional[List[MechanismLink]] = Field(
        default_factory=list,
        description="""semicolon-separated list of links, where each link is a triple connecting two entities via a relationship type""",
    )
    references: Optional[List[str]] = Field(default_factory=list)
    source_text: Optional[str] = Field(None)


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


class MechanismElement(NamedEntity):

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class Disease(NamedEntity):

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class Drug(NamedEntity):

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class Predicate(NamedEntity):

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class CompoundExpression(ConfiguredBaseModel):

    None


class MechanismLink(CompoundExpression):

    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)


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
DrugMechanism.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
MechanismElement.update_forward_refs()
Disease.update_forward_refs()
Drug.update_forward_refs()
Predicate.update_forward_refs()
CompoundExpression.update_forward_refs()
MechanismLink.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
