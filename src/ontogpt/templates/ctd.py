"""CTD template."""
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


class MeshChemicalIdentifier(str, Enum):
    dummy = "dummy"


class MeshDiseaseIdentifier(str, Enum):
    dummy = "dummy"


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


class Disease(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Chemical(NamedEntity):
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


class ChemicalToDiseaseRelationship(Triple):
    """A triple where the subject is a chemical and the object is a disease."""

    subject: Optional[str] = Field(
        None,
        description="""The chemical substance, drug, or small molecule.\
            or example: Lidocaine, Monosodium Glutamate, Imatinib.""",
    )
    predicate: Optional[str] = Field(
        None, description="""The relationship type, e.g. INDUCES, TREATS."""
    )
    object: Optional[str] = Field(
        None,
        description="""The disease or condition that is being treated or induced by the chemical.\
            For example, asthma, cancer, covid-19, cardiac asystole, Hypotension, Headache.""",
    )
    qualifier: Optional[str] = Field(
        None, description="""A qualifier for the statements, e.g. \"NOT\" for negation"""
    )
    subject_qualifier: Optional[str] = Field(
        None,
        description="""An optional qualifier or modifier for the chemical,\
            e.g. \"high dose\" or \"intravenously administered\"""",
    )
    object_qualifier: Optional[str] = Field(
        None,
        description="""An optional qualifier or modifier for the disease,\
            e.g. \"severe\" or \"with additional complications\"""",
    )


class TextWithTriples(ConfiguredBaseModel):
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)


class ChemicalToDiseaseDocument(TextWithTriples):
    """A document that contains chemical to disease relations."""

    publication: Optional[Publication] = Field(None)
    triples: Optional[List[ChemicalToDiseaseRelationship]] = Field(default_factory=list)


class RelationshipType(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ChemicalToDiseasePredicate(RelationshipType):
    """A predicate for chemical to disease relationships."""

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
Disease.update_forward_refs()
Chemical.update_forward_refs()
CompoundExpression.update_forward_refs()
Triple.update_forward_refs()
ChemicalToDiseaseRelationship.update_forward_refs()
TextWithTriples.update_forward_refs()
ChemicalToDiseaseDocument.update_forward_refs()
RelationshipType.update_forward_refs()
ChemicalToDiseasePredicate.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
