"""GO-CAM template."""
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


class GeneLocationEnum(str, Enum):
    dummy = "dummy"


class GOCellComponentType(str, Enum):
    dummy = "dummy"


class CellType(str, Enum):
    dummy = "dummy"


class GoCamAnnotations(ConfiguredBaseModel):
    genes: Optional[List[str]] = Field(
        default_factory=list, description="""semicolon-separated list of genes"""
    )
    organisms: Optional[List[str]] = Field(
        default_factory=list, description="""semicolon-separated list of organism taxons"""
    )
    gene_organisms: Optional[List[GeneOrganismRelationship]] = Field(default_factory=list)
    activities: Optional[List[str]] = Field(
        default_factory=list, description="""semicolon-separated list of molecular activities"""
    )
    gene_functions: Optional[List[GeneMolecularActivityRelationship]] = Field(
        default_factory=list,
        description="""semicolon-separated list of gene to molecular activity relationships""",
    )
    cellular_processes: Optional[List[str]] = Field(
        default_factory=list, description="""semicolon-separated list of cellular processes"""
    )
    pathways: Optional[List[str]] = Field(
        default_factory=list, description="""semicolon-separated list of pathways"""
    )
    gene_gene_interactions: Optional[List[GeneGeneInteraction]] = Field(
        default_factory=list,
        description="""semicolon-separated list of gene to gene interactions""",
    )
    gene_localizations: Optional[List[GeneSubcellularLocalizationRelationship]] = Field(
        default_factory=list,
        description="""semicolon-separated list of genes plus their location in the cell;\
            for example, \"gene1 / cytoplasm; gene2 / mitochondrion\"""",
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


class Pathway(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CellularProcess(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class MolecularActivity(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class GeneLocation(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Organism(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Molecule(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CompoundExpression(ConfiguredBaseModel):
    pass


class GeneOrganismRelationship(CompoundExpression):
    gene: Optional[str] = Field(None)
    organism: Optional[str] = Field(None)


class GeneMolecularActivityRelationship(CompoundExpression):
    gene: Optional[str] = Field(None)
    molecular_activity: Optional[str] = Field(None)


class GeneMolecularActivityRelationship2(CompoundExpression):
    gene: Optional[str] = Field(None)
    molecular_activity: Optional[str] = Field(None)
    target: Optional[str] = Field(None)


class GeneSubcellularLocalizationRelationship(CompoundExpression):
    gene: Optional[str] = Field(None)
    location: Optional[str] = Field(None)


class GeneGeneInteraction(CompoundExpression):
    gene1: Optional[str] = Field(None)
    gene2: Optional[str] = Field(None)


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
GoCamAnnotations.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
Gene.update_forward_refs()
Pathway.update_forward_refs()
CellularProcess.update_forward_refs()
MolecularActivity.update_forward_refs()
GeneLocation.update_forward_refs()
Organism.update_forward_refs()
Molecule.update_forward_refs()
CompoundExpression.update_forward_refs()
GeneOrganismRelationship.update_forward_refs()
GeneMolecularActivityRelationship.update_forward_refs()
GeneMolecularActivityRelationship2.update_forward_refs()
GeneSubcellularLocalizationRelationship.update_forward_refs()
GeneGeneInteraction.update_forward_refs()
Triple.update_forward_refs()
TextWithTriples.update_forward_refs()
RelationshipType.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
