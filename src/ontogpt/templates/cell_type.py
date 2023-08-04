from __future__ import annotations

import sys
from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Union
from linkml_runtime.linkml_model import Decimal
from pydantic.v1 import BaseModel as BaseModel
from pydantic.v1 import Field

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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
    use_enum_values=True,
):
    pass


class BrainRegionIdentifier(str, Enum):
    """
    Brain region (or for now, any nervous system part)
    """

    dummy = "dummy"


class NeurotransmitterIdentifier(str, Enum):
    dummy = "dummy"


class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"

    NOT_APPLICABLE = "NOT_APPLICABLE"

    NOT_MENTIONED = "NOT_MENTIONED"


class CellType(ConfiguredBaseModel):
    """
    Represents a cell type
    """

    id: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""the concise name of the cell type""")
    equivalent_to: Optional[str] = Field(None, description="""the the cell type described""")
    definition: Optional[str] = Field(None)
    parents: Optional[List[str]] = Field(default_factory=list, description="""categorization""")
    subtypes: Optional[List[str]] = Field(default_factory=list)
    localizations: Optional[List[str]] = Field(default_factory=list)
    genes: Optional[List[str]] = Field(default_factory=list)
    diseases: Optional[List[str]] = Field(default_factory=list)
    roles: Optional[List[str]] = Field(default_factory=list)


class ImmuneCell(CellType):
    has_surface_markers: Optional[List[str]] = Field(default_factory=list)
    id: str = Field(...)
    label: Optional[str] = Field(None, description="""the concise name of the cell type""")
    equivalent_to: Optional[str] = Field(None, description="""the the cell type described""")
    definition: Optional[str] = Field(None)
    parents: Optional[List[str]] = Field(default_factory=list, description="""categorization""")
    subtypes: Optional[List[str]] = Field(default_factory=list)
    localizations: Optional[List[str]] = Field(default_factory=list)
    genes: Optional[List[str]] = Field(default_factory=list)
    diseases: Optional[List[str]] = Field(default_factory=list)
    roles: Optional[List[str]] = Field(default_factory=list)


class Neuron(CellType):
    releases_neurotransitter: Optional[List[str]] = Field(default_factory=list)
    id: str = Field(...)
    label: Optional[str] = Field(None, description="""the concise name of the cell type""")
    equivalent_to: Optional[str] = Field(None, description="""the the cell type described""")
    definition: Optional[str] = Field(None)
    parents: Optional[List[str]] = Field(default_factory=list, description="""categorization""")
    subtypes: Optional[List[str]] = Field(default_factory=list)
    localizations: Optional[List[str]] = Field(default_factory=list)
    genes: Optional[List[str]] = Field(default_factory=list)
    diseases: Optional[List[str]] = Field(default_factory=list)
    roles: Optional[List[str]] = Field(default_factory=list)


class Interneuron(Neuron):
    projects_to_or_from: Optional[List[str]] = Field(
        default_factory=list,
        description="""Brain structures from which this cell type projects into or receives projections from""",
    )
    releases_neurotransitter: Optional[List[str]] = Field(default_factory=list)
    id: str = Field(...)
    label: Optional[str] = Field(None, description="""the concise name of the cell type""")
    equivalent_to: Optional[str] = Field(None, description="""the the cell type described""")
    definition: Optional[str] = Field(None)
    parents: Optional[List[str]] = Field(default_factory=list, description="""categorization""")
    subtypes: Optional[List[str]] = Field(default_factory=list)
    localizations: Optional[List[str]] = Field(default_factory=list)
    genes: Optional[List[str]] = Field(default_factory=list)
    diseases: Optional[List[str]] = Field(default_factory=list)
    roles: Optional[List[str]] = Field(default_factory=list)


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
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Gene(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ProteinOrComplex(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class BiologicalProcess(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Pathway(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class AnatomicalStructure(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ChemicalEntity(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Neurotransmitter(ChemicalEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class BrainRegion(AnatomicalStructure):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CellOntologyTerm(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Disease(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Drug(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
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


class TextWithTriples(ConfiguredBaseModel):
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)


class RelationshipType(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
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
CellType.update_forward_refs()
ImmuneCell.update_forward_refs()
Neuron.update_forward_refs()
Interneuron.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
Gene.update_forward_refs()
ProteinOrComplex.update_forward_refs()
BiologicalProcess.update_forward_refs()
Pathway.update_forward_refs()
AnatomicalStructure.update_forward_refs()
ChemicalEntity.update_forward_refs()
Neurotransmitter.update_forward_refs()
BrainRegion.update_forward_refs()
CellOntologyTerm.update_forward_refs()
Disease.update_forward_refs()
Drug.update_forward_refs()
CompoundExpression.update_forward_refs()
Triple.update_forward_refs()
TextWithTriples.update_forward_refs()
RelationshipType.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
