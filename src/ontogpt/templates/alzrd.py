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
    summary: Optional[str] = Field(None, description="""A brief summary of the input text, suitable for display in a table of contents or search results. This should be no more than three sentences. Do not format in Markdown.""")
    article_type: Optional[str] = Field(None, description="""The type of article, e.g., \"research article\", \"review\", \"case report\".""")
    modeling_approach: Optional[str] = Field(None, description="""A brief description of the modeling approach used in the input text, e.g., \"experimental\", \"observational\", \"computational\", \"review\".""")
    modeling_summary: Optional[str] = Field(None, description="""A brief summary of the modeling approach used in the input text, suitable for display in a table of contents or search results. Include any details about how a model of disease is defined, including the use of model organisms, cell lines, or in silico models, as well as the experimental metrics used to model human disease. If this is a study of human subjects, include details about the study design and the human subjects involved. This should be no more than three sentences. Do not format in Markdown.""")
    taxa: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of taxa or species of organisms mentioned in the input text. Where possible, translate to the binomial species name (e.g., change \"mouse\" to \"Mus musculus\"), unless a different species name is provided in the text. If no taxon is mentioned, return NOT FOUND.""")
    diagnostics: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of diagnostic procedures mentioned in the input text. If no diagnostic procedures are mentioned, return NOT FOUND.""")
    diseases: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of diseases or conditions mentioned in the input text. If no diseases are mentioned, return NOT FOUND.""")
    chemical: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of chemicals, drugs, or other substances mentioned in the input text. If no chemicals are mentioned, return NOT FOUND.""")
    environmental_exposures: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of environmental exposures mentioned in the input text. These may include exposure to general classes of materials, e.g., \"exposure to pesticides\", or other phenomena, e.g., \"chronic stress\". If no environmental exposures are mentioned, return NOT FOUND.""")
    experimental_metrics_and_indicators: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of of experimental metrics, signs, symptoms, or outcomes used to measure the progression of Alzheimer's disease and related dementias, mentioned in the input text. These may be quantitative or qualitative measures, including biomolecular assays. In experimental animal models these are analogues of cognitive impairment or indicators of disease progression modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive decline. If no experimental metrics are mentioned, return NOT FOUND.""")
    experimental_metrics_to_taxon_relationships: Optional[List[ExperimentalMetricToTaxonRelationship]] = Field(default_factory=list, description="""Semicolon-separated list of relationships between a specific experimental metric, sign, symptom, or outcome and a taxon, as described in the input text. These are cases in which the relationship is used to measure progression of Alzheimer's disease and related dementias, or an experimental analogue, in the taxon. For example, \"Amyloid beta (Aβ) levels are measured in Mus musculus\" or \"Morris water maze test is measured with Rattus norvegicus\".  Include all qualifiers and whether the relationship is direct or indirect.""")
    experimental_metric_to_disease_relationships: Optional[List[ExperimentalMetricToDiseaseRelationship]] = Field(default_factory=list, description="""Semicolon-separated list of relationships between a specific experimental metric, sign, symptom, or outcome and a disease or condition, as described in the input text. These are cases in which the relationship is used as an experimental model of progression or presence of a disease. For example, \"Amyloid beta (Aβ) levels are used to model Alzheimer's disease\" or \"Morris water maze test is used to model Parkinson's disease\".  Include all qualifiers, whether the relationship was direct or indirect, and any observed associations, including whether the association was positive, negative, or inconclusive.""")
    experimental_metric_to_environment_relationships: Optional[List[ExperimentalMetricToEnvironmentRelationship]] = Field(default_factory=list, description="""Semicolon-separated list of relationships between a specific experimental metric, sign, symptom, or outcome and an environmental exposure or condition, as described in the input text. These are cases in which the relationship is used to measure the effects of an environmental exposure on the progression of Alzheimer's disease and related dementias, or an experimental analogue. For example, \"Amyloid beta (Aβ) levels are measured in response to chronic stress\" or \"Morris water maze test is measured in response to air pollution\". Include all qualifiers, whether the relationship was direct or indirect, and any observed associations, including whether the association was positive, negative, or inconclusive.""")
    experimental_metric_to_chemical_relationships: Optional[List[ExperimentalMetricToChemicalRelationship]] = Field(default_factory=list, description="""Semicolon-separated list of relationships between a specific experimental metric, sign, symptom, or outcome and a chemical, drug, or other substance, as described in the input text. These are cases in which the relationship is used to measure the effects of a chemical on the progression of Alzheimer's disease and related dementias, or an experimental analogue. For example, \"Amyloid beta (Aβ) levels are measured in response to donepezil\" or \"Morris water maze test is measured in response to caffeine\". Include all qualifiers, whether the relationship was direct or indirect, and any observed associations, including whether the association was positive, negative, or inconclusive.""")
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


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


class ExperimentalMetricToTaxonRelationship(CompoundExpression):
    """
    A triple where the subject is an experimental metric, the object is an taxon, metric, and the predicate describes the relationship between the metric and the taxon, usually MEASURED_IN.
    """
    metric: Optional[str] = Field(None, description="""The name of an experimental metric, sign, symptom, or outcome used to measure the effects of treatments on symptoms or diagnostics, or of the progression of Alzheimer's disease and related dementias. In experimental animal models these are analogues of cognitive impairment or indicators of disease progression modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive decline.""")
    taxon: Optional[str] = Field(None, description="""The taxon or species of the model organism in which the experimental metric is measured. For example, Mus musculus, Rattus norvegicus.""")
    predicate: Optional[str] = Field(None, description="""The relationship type, generally MEASURED_IN to indicate a metric is measured in a taxon.""")
    metric_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the experimental metric, as described in the input text. This may include the method of measurement or the specific assay used.""")
    taxon_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the taxon, as described
 in the input text.
 This may include a strain or genetic background of the model organism.""")
    direct_or_indirect: Optional[str] = Field(None, description="""Whether the relationship between the metric and the taxon is direct or indirect. UNKNOWN if this is not specified in the text or is unclear.""")


class ExperimentalMetricToDiseaseRelationship(CompoundExpression):
    """
    A triple where the subject is an experimental metric, the object is a disease or condition, and the predicate describes the relationship between the metric and the disease, usually USED_TO_MODEL.
    """
    metric: Optional[str] = Field(None, description="""The name of an experimental metric, sign, symptom, or outcome used to measure the effects of treatments on symptoms or diagnostics, or of the progression of Alzheimer's disease and related dementias. In experimental animal models these are analogues of cognitive impairment or indicators of disease progression modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive decline.""")
    disease: Optional[str] = Field(None, description="""The name of a disease or condition. Examples are Alzheimer's disease, Parkinson's disease, Huntington's disease.""")
    predicate: Optional[str] = Field(None, description="""The relationship type, generally USED_TO_MODEL to indicate a metric is used to model a disease or condition.""")
    metric_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the experimental metric, as described in the input text. This may include the method of measurement or the specific assay used.""")
    disease_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the disease or condition, as described in the input text. This may include the stage or subtype of the disease.""")
    direct_or_indirect: Optional[str] = Field(None, description="""Whether the relationship between the metric and the disease is direct or indirect. UNKNOWN if this is not specified in the text or is unclear.""")
    association: Optional[str] = Field(None, description="""The type of any observed association between the value of the metric and the disease. May be \"positive\", \"negative\", \"inconclusive\", or UNKNOWN if this is not specified in the text or is unclear.""")


class ExperimentalMetricToEnvironmentRelationship(CompoundExpression):
    """
    A triple where the subject is an experimental metric, the object is an environmental exposure or condition, and the predicate describes the relationship between the metric and the environmental exposure, usually MEASURED_IN_RESPONSE_TO.
    """
    metric: Optional[str] = Field(None, description="""The name of an experimental metric, sign, symptom, or outcome used to measure the effects of treatments on symptoms or diagnostics, or of the progression of Alzheimer's disease and related dementias. In experimental animal models these are analogues of cognitive impairment or indicators of disease progression modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive decline.""")
    environment: Optional[str] = Field(None, description="""The name of an environmental exposure or condition. Examples are \"pesticides\", \"chronic stress\", \"air pollution\", \"heavy metals\", \"radiation\", \"heat stress\".""")
    predicate: Optional[str] = Field(None, description="""The relationship type, generally MEASURED_IN_RESPONSE_TO to indicate a metric is measured in response to an environmental exposure.""")
    metric_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the experimental metric, as described in the input text. This may include the method of measurement or the specific assay used.""")
    environment_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the environmental exposure, as described in the input text. This may include the duration or intensity of the exposure.""")
    direct_or_indirect: Optional[str] = Field(None, description="""Whether the relationship between the metric and the environmental exposure is direct or indirect. UNKNOWN if this is not specified in the text or is unclear.""")
    association: Optional[str] = Field(None, description="""The type of any observed association between the value of the metric and the environmental exposure. May be \"positive\", \"negative\", \"inconclusive\", or UNKNOWN if this is not specified in the text or is unclear.""")


class ExperimentalMetricToChemicalRelationship(CompoundExpression):
    """
    A triple where the subject is an experimental metric, the object is a chemical, drug, or other substance, and the predicate describes the relationship between the metric and the chemical, usually MEASURED_IN_RESPONSE_TO.
    """
    metric: Optional[str] = Field(None, description="""The name of an experimental metric, sign, symptom, or outcome used to measure the effects of treatments on symptoms or diagnostics, or of the progression of Alzheimer's disease and related dementias. In experimental animal models these are analogues of cognitive impairment or indicators of disease progression modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive decline.""")
    chemical: Optional[str] = Field(None, description="""The name of a chemical, drug, or other substance. Examples are \"donepezil\", \"Aβ42\", \"Aβ40\", \"tau\", \"insulin\", \"caffeine\", \"nicotine\", \"alcohol\".""")
    predicate: Optional[str] = Field(None, description="""The relationship type, generally MEASURED_IN_RESPONSE_TO to indicate a metric is measured in response to a chemical.""")
    metric_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the experimental metric, as described in the input text. This may include the method of measurement or the specific assay used.""")
    chemical_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the chemical, drug, or other substance, as described in the input text. This may include the dose or route of administration.""")
    direct_or_indirect: Optional[str] = Field(None, description="""Whether the relationship between the metric and the chemical is direct or indirect. UNKNOWN if this is not specified in the text or is unclear.""")
    association: Optional[str] = Field(None, description="""The type of any observed association between the value of the metric and the chemical. May be \"positive\", \"negative\", \"inconclusive\", or UNKNOWN if this is not specified in the text or is unclear.""")


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
MetricOrIndicator.model_rebuild()
Diagnostic.model_rebuild()
Disease.model_rebuild()
Taxon.model_rebuild()
Chemical.model_rebuild()
EnvironmentalExposure.model_rebuild()
ExperimentalMetricToTaxonRelationship.model_rebuild()
ExperimentalMetricToDiseaseRelationship.model_rebuild()
ExperimentalMetricToEnvironmentRelationship.model_rebuild()
ExperimentalMetricToChemicalRelationship.model_rebuild()

