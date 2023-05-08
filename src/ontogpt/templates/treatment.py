"""Treatment template."""
from __future__ import annotations

from enum import Enum
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


class NCITDrugType(str, Enum):
    dummy = "dummy"


class NCITTreatmentType(str, Enum):
    dummy = "dummy"


class NCITTActivityType(str, Enum):
    dummy = "dummy"


class MAXOActionType(str, Enum):
    dummy = "dummy"


class MESHTherapeuticType(str, Enum):
    dummy = "dummy"


class CHEBIDrugType(str, Enum):
    dummy = "dummy"


class DiseaseTreatmentSummary(ConfiguredBaseModel):
    disease: Optional[str] = Field(None, description="""the name of the disease that is treated""")
    drugs: Optional[List[str]] = Field(
        default_factory=list,
        description="""semicolon-separated list of named small molecule drugs""",
    )
    treatments: Optional[List[str]] = Field(
        default_factory=list,
        description="""semicolon-separated list of therapies and treatments are\
            indicated for treating the disease.""",
    )
    contraindications: Optional[List[str]] = Field(
        default_factory=list,
        description="""semicolon-separated list of therapies and treatments that are\
            contra-indicated for the disease, and should not be used,\
            due to risk of adverse effects.""",
    )
    treatment_mechanisms: Optional[List[TreatmentMechanism]] = Field(
        default_factory=list,
        description="""semicolon-separated list of treatment to asterisk-separated\
            mechanism associations""",
    )
    treatment_efficacies: Optional[List[TreatmentEfficacy]] = Field(
        default_factory=list,
        description="""semicolon-separated list of treatment to efficacy associations,\
            e.g. Imatinib*effective""",
    )
    treatment_adverse_effects: Optional[List[TreatmentAdverseEffect]] = Field(
        default_factory=list,
        description="""semicolon-separated list of treatment to adverse effect associations,\
            e.g. Imatinib*nausea""",
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


class Gene(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Symptom(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Disease(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class AdverseEffect(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Treatment(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Mechanism(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Drug(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CompoundExpression(ConfiguredBaseModel):
    pass


class TreatmentMechanism(CompoundExpression):
    treatment: Optional[str] = Field(None)
    mechanism: Optional[str] = Field(None)


class TreatmentAdverseEffect(CompoundExpression):
    treatment: Optional[str] = Field(None)
    adverse_effects: Optional[List[str]] = Field(default_factory=list)


class TreatmentEfficacy(CompoundExpression):
    treatment: Optional[str] = Field(None)
    efficacy: Optional[str] = Field(None)


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
DiseaseTreatmentSummary.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
Gene.update_forward_refs()
Symptom.update_forward_refs()
Disease.update_forward_refs()
AdverseEffect.update_forward_refs()
Treatment.update_forward_refs()
Mechanism.update_forward_refs()
Drug.update_forward_refs()
CompoundExpression.update_forward_refs()
TreatmentMechanism.update_forward_refs()
TreatmentAdverseEffect.update_forward_refs()
TreatmentEfficacy.update_forward_refs()
Triple.update_forward_refs()
TextWithTriples.update_forward_refs()
RelationshipType.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
