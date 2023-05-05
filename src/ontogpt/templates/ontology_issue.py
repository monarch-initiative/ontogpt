from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union

from linkml_runtime.linkml_model import Decimal
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


class ProblemType(str, Enum):
    UNKNOWN = "UNKNOWN"
    TYPO = "TYPO"
    BAD_XREF = "BAD_XREF"
    MISSING_DEFINITION = "MISSING_DEFINITION"
    MISSING_PARENT = "MISSING_PARENT"
    BAD_RELATIONSHIP = "BAD_RELATIONSHIP"
    OTHER = "OTHER"


class ChangeType(str, Enum):
    UNKNOWN = "UNKNOWN"
    CHANGE_DEFINITION = "CHANGE_DEFINITION"
    CHANGE_LABEL = "CHANGE_LABEL"
    CHANGE_XREF = "CHANGE_XREF"
    MOVE_TERM = "MOVE_TERM"


class OntologyIssue(ConfiguredBaseModel):
    title: Optional[str] = Field(None, description="""the title of the issue""")
    summary: Optional[str] = Field(None, description="""a high level summary""")
    status: Optional[str] = Field(None)
    domains: Optional[List[str]] = Field(
        default_factory=list, description="""What part of the ontology does this pertain to."""
    )
    problem_list: Optional[List[OntologyProblem]] = Field(
        default_factory=list, description="""A list of problems stated at a high level"""
    )
    proposed_changes: Optional[List[OntologyChange]] = Field(
        default_factory=list, description="""What part of the ontology does this pertain to."""
    )


class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """

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


class OntologyClass(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CompoundExpression(ConfiguredBaseModel):
    None


class OntologyProblem(CompoundExpression):
    description: Optional[str] = Field(
        None, description="""A succinct description of the problem"""
    )
    severity: Optional[str] = Field(None, description="""How severe is this problem?""")
    category: Optional[ProblemType] = Field(
        None, description="""What category does this problem fall into?"""
    )
    about: Optional[List[str]] = Field(
        default_factory=list, description="""What terms in the ontology is this problem about?"""
    )


class OntologyChange(CompoundExpression):
    description: Optional[str] = Field(
        None, description="""A succinct description of the proposed change"""
    )
    category: Optional[ChangeType] = Field(None, description="""What kind of change?""")
    about: Optional[List[str]] = Field(
        default_factory=list, description="""What terms in the ontology will this change affect?"""
    )


class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """

    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    qualifier: Optional[str] = Field(
        None, description="""A qualifier for the statements, e.g. \"NOT\" for negation"""
    )
    subject_qualifier: Optional[str] = Field(
        None,
        description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""",
    )
    object_qualifier: Optional[str] = Field(
        None,
        description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""",
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
OntologyIssue.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
OntologyClass.update_forward_refs()
CompoundExpression.update_forward_refs()
OntologyProblem.update_forward_refs()
OntologyChange.update_forward_refs()
Triple.update_forward_refs()
TextWithTriples.update_forward_refs()
RelationshipType.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
