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


class MendelianDisease(NamedEntity):

    name: Optional[str] = Field(None, description="""the name of the disease""")
    description: Optional[str] = Field(None, description="""a description of the disease""")
    synonyms: Optional[List[str]] = Field(default_factory=list)
    subclass_of: Optional[List[str]] = Field(default_factory=list)
    symptoms: Optional[List[str]] = Field(default_factory=list)
    inheritance: Optional[str] = Field(None)
    genes: Optional[List[str]] = Field(default_factory=list)
    disease_onsets: Optional[List[str]] = Field(default_factory=list)
    publications: Optional[List[Publication]] = Field(default_factory=list)
    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class DiseaseCategory(NamedEntity):

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class Gene(NamedEntity):

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class Symptom(NamedEntity):

    characteristic: Optional[str] = Field(None)
    affects: Optional[str] = Field(None)
    severity: Optional[str] = Field(None)
    onset_of_symptom: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class Onset(NamedEntity):

    years_old: Optional[str] = Field(None)
    decades: Optional[List[str]] = Field(default_factory=list)
    juvenile_or_adult: Optional[str] = Field(None)
    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""The label of the named thing""")


class Inheritance(NamedEntity):

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
MendelianDisease.update_forward_refs()
DiseaseCategory.update_forward_refs()
Gene.update_forward_refs()
Symptom.update_forward_refs()
Onset.update_forward_refs()
Inheritance.update_forward_refs()
CompoundExpression.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
