from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass


class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"


class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    input_id: Optional[str] = Field(None)
    input_title: Optional[str] = Field(None)
    input_text: Optional[str] = Field(None)
    raw_completion_output: Optional[str] = Field(None)
    prompt: Optional[str] = Field(None)
    extracted_object: Optional[Any] = Field(None, description="""The complex objects extracted from the text""")
    named_entities: Optional[List[Any]] = Field(default_factory=list, description="""Named entities extracted from the text""")


class NamedEntity(ConfiguredBaseModel):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CompoundExpression(ConfiguredBaseModel):
    pass


class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""")


class TextWithTriples(ConfiguredBaseModel):
    """
    A text containing one or more relations of the Triple type.
    """
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)


class TextWithEntity(ConfiguredBaseModel):
    """
    A text containing one or more instances of a single type of entity.
    """
    publication: Optional[Publication] = Field(None)
    entities: Optional[List[str]] = Field(default_factory=list)


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


class Document(NamedEntity):
    sections: Optional[List[DocumentSection]] = Field(default_factory=list, description="""A semicolon-separated list of full sections of the document, including the full text of that section alone, beginning with the major division of the document, such as ABSTRACT, INTRODUCTION, METHODS, RESULTS, DISCUSSION, CONCLUSIONS, or a similar heading used by the text. The text should include the section title. If semicolons are present in the section text, they must be replaced with (SEMICOLON) to avoid parsing errors. A single phrase or ID is not a section. Do not format in Markdown.""")
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class DocumentSection(CompoundExpression):
    part_of: Optional[str] = Field(None, description="""The major document division that this section is a part of. Examples are \"introduction\", \"methods\", \"results\", \"discussion\", or \"conclusions\". Do not format in Markdown.""")
    summary: Optional[str] = Field(None, description="""A brief summary of the section, suitable for display in a table of contents or search results. This should be a single sentence or phrase, not a full paragraph. Do not format in Markdown.""")
    taxon: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of taxa or species of organisms mentioned in the section. Where possible, translate to the binomial species name (e.g., change \"mouse\" to \"Mus musculus\"), unless a different species name is provided in the text. If no taxon is mentioned, return NOT FOUND.""")
    diagnostics: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of diagnostic procedures mentioned in the section. If no diagnostic procedures are mentioned, return NOT FOUND.""")
    diseases: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of diseases or conditions mentioned in the section. If no diseases are mentioned, return NOT FOUND.""")
    chemical: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of chemicals, drugs, or other substances mentioned in the section. If no chemicals are mentioned, return NOT FOUND.""")
    environmental_exposures: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of environmental exposures mentioned in the section. These may include exposure to general classes of materials, e.g., \"exposure to pesticides\", or other phenomena, e.g., \"chronic stress\". If no environmental exposures are mentioned, return NOT FOUND.""")
    experimental_metrics_and_indicators: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of of a experimental metrics, signs, symptoms, or outcomes used to measure the progression of Alzheimer's disease and related dementias. These may be quantitative or qualitative measures, including biomolecular assays. In experimental animal models these are analogues of cognitive impairment or indicators of disease progression modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive decline. If no experimental metrics are mentioned, return NOT FOUND.""")
    experimental_metrics_to_taxon_relationships: Optional[List[ExperimentalMetricToTaxonRelationship]] = Field(default_factory=list, description="""Semicolon-separated list of relationships between a specific experimental metric, sign, symptom, or outcome and a taxon, where the relationship is used to measure progression of Alzheimer's disease and related dementias, or an experimental analogue, in the taxon. For example, \"Amyloid beta (Aβ) levels are measured in Mus musculus\" or \"Morris water maze test is measured with Rattus norvegicus\".""")
    experimental_metric_to_disease_relationships: Optional[List[ExperimentalMetricToDiseaseRelationship]] = Field(default_factory=list, description="""Semicolon-separated list of relationships between a specific experimental metric, sign, symptom, or outcome and a disease or condition, where the relationship is used as an experimental model of progression or presence of a disease. For example, \"Amyloid beta (Aβ) levels are used to model Alzheimer's disease\" or \"Morris water maze test is used to model Parkinson's disease\".""")


class MetricOrIndicator(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Diagnostic(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Disease(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Taxon(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Chemical(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class EnvironmentalExposure(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ExperimentalMetricToTaxonRelationship(Triple):
    """
    A triple where the subject is an experimental metric, the object is an taxon, metric, and the predicate describes the relationship between the metric and the taxon, usually MEASURED_IN.
    """
    subject: Optional[str] = Field(None, description="""The name of an experimental metric, sign, symptom, or outcome used to measure the effects of treatments on symptoms or diagnostics, or of the progression of Alzheimer's disease and related dementias. In experimental animal models these are analogues of cognitive impairment or indicators of disease progression modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive decline.""")
    predicate: Optional[str] = Field(None, description="""The relationship type, generally MEASURED_IN to indicate a metric is measured in a taxon.""")
    object: Optional[str] = Field(None, description="""The taxon or species of the model organism in which the experimental metric is measured. For example, Mus musculus, Rattus norvegicus.""")
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the taxon. This may include a strain or genetic background of the model organism.""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the experimental metric. This may include the method of measurement or the specific assay used.""")


class ExperimentalMetricToDiseaseRelationship(Triple):
    """
    A triple where the subject is an experimental metric, the object is a disease or condition, and the predicate describes the relationship between the metric and the disease, usually USED_TO_MODEL.
    """
    subject: Optional[str] = Field(None, description="""The name of an experimental metric, sign, symptom, or outcome used to measure the effects of treatments on symptoms or diagnostics, or of the progression of Alzheimer's disease and related dementias. In experimental animal models these are analogues of cognitive impairment or indicators of disease progression modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive decline.""")
    predicate: Optional[str] = Field(None, description="""The relationship type, generally USED_TO_MODEL to indicate a metric is used to model a disease or condition.""")
    object: Optional[str] = Field(None, description="""The name of a disease or condition. Examples are Alzheimer's disease, Parkinson's disease, Huntington's disease.""")
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the experimental metric. This may include the method of measurement or the specific assay used.""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the disease or condition. This may include the stage or subtype of the disease.""")


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
CompoundExpression.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()
Document.model_rebuild()
DocumentSection.model_rebuild()
MetricOrIndicator.model_rebuild()
Diagnostic.model_rebuild()
Disease.model_rebuild()
Taxon.model_rebuild()
Chemical.model_rebuild()
EnvironmentalExposure.model_rebuild()
ExperimentalMetricToTaxonRelationship.model_rebuild()
ExperimentalMetricToDiseaseRelationship.model_rebuild()

