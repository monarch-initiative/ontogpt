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


class DiagnosticProcedure(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Phenotype(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ClinicalAttribute(NamedEntity):
    unit: Optional[str] = Field(None, description="""the unit used to measure the attribute""")
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Quality(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Unit(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CompoundExpression(ConfiguredBaseModel):
    None


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


class DiagnosticProceduretoPhenotypeAssociation(Triple):
    """
    A triple representing a relationship between a diagnostic procedure and an associated phenotype, e.g., \"blood pressure measurement\" is associated with \"high blood pressure\".
    """

    subject: Optional[str] = Field(
        None,
        description="""A diagnostic procedure yielding a result, which in turn may be interpreted as a phenotype. Procedures include \"heart rate measurement\", \"blood pressure measurement\", \"oxygen saturation measurement\", etc. In practice, procedures may be named based on what they measure, with the \"measurement\" part left implicit.""",
    )
    predicate: Optional[str] = Field(None, description="""The relationship type, e.g. RELATED_TO""")
    object: Optional[List[str]] = Field(
        default_factory=list,
        description="""The observable physical or biochemical characteristics of a patient. Not equivalent to a disease state, but may contribute to a diagnosis.""",
    )
    qualifier: Optional[str] = Field(
        None, description="""A qualifier for the statements, e.g. \"NOT\" for negation"""
    )
    subject_qualifier: Optional[str] = Field(
        None, description="""An optional qualifier or modifier for the procedure."""
    )
    object_qualifier: Optional[str] = Field(
        None, description="""An optional qualifier or modifier for the phenotype."""
    )


class DiagnosticProceduretoAttributeAssociation(Triple):
    """
    A triple representing a relationship between a diagnostic procedure and a measured attribute, e.g., \"blood pressure measurement\" is associated with \"blood pressure\" (or in OBA, something like OBA:VT0000183, \"blood pressure trait\").
    """

    subject: Optional[str] = Field(
        None,
        description="""A diagnostic procedure yielding a result, which in turn may be interpreted as a phenotype. Procedures include \"heart rate measurement\", \"blood pressure measurement\", \"oxygen saturation measurement\", etc. In practice, procedures may be named based on what they measure, with the \"measurement\" part left implicit.""",
    )
    predicate: Optional[str] = Field(None, description="""The relationship type, e.g. RELATED_TO""")
    object: Optional[List[str]] = Field(
        default_factory=list, description="""Any measurable clinical attribute."""
    )
    qualifier: Optional[str] = Field(
        None, description="""A qualifier for the statements, e.g. \"NOT\" for negation"""
    )
    subject_qualifier: Optional[str] = Field(
        None, description="""An optional qualifier or modifier for the procedure."""
    )
    object_qualifier: Optional[str] = Field(
        None, description="""An optional qualifier or modifier for the phenotype."""
    )


class TextWithTriples(ConfiguredBaseModel):
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)


class RelationshipType(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ProcedureToPhenotypePredicate(RelationshipType):
    """
    A predicate for procedure to phenotype relationships, defining \"this procedure is intended to provide support for/against this phenotype\".
    """

    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ProcedureToAttributePredicate(RelationshipType):
    """
    A predicate for procedure to attribute relationships, defining \"this procedure is a measurement of this attribute\".
    """

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
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
DiagnosticProcedure.update_forward_refs()
Phenotype.update_forward_refs()
ClinicalAttribute.update_forward_refs()
Quality.update_forward_refs()
Unit.update_forward_refs()
CompoundExpression.update_forward_refs()
Triple.update_forward_refs()
DiagnosticProceduretoPhenotypeAssociation.update_forward_refs()
DiagnosticProceduretoAttributeAssociation.update_forward_refs()
TextWithTriples.update_forward_refs()
RelationshipType.update_forward_refs()
ProcedureToPhenotypePredicate.update_forward_refs()
ProcedureToAttributePredicate.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
