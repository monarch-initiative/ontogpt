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
    sections: Optional[List[DocumentSection]] = Field(default_factory=list, description="""A semicolon-separated list of full sections of the document. If semicolons are present in the section text, they should be replaced with (SEMICOLON) to avoid parsing errors. A section is a major division of the document, such as an abstract, introduction, methods, results, discussion, or conclusion, or a subsection of one of these. The text should include the section title. A single phrase or ID is not a section. Do not format in Markdown.""")
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class DocumentSection(CompoundExpression):
    taxon: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of taxa or species of organisms mentioned in the section. Where possible, translate to the binomial species name (e.g., change \"mouse\" to \"Mus musculus\"), unless a different species name is provided in the text.""")
    summary: Optional[str] = Field(None, description="""A brief summary of the section, suitable for display in a table of contents or search results. This should be a single sentence or phrase, not a full paragraph. Do not format in Markdown.""")
    symptoms: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of symptoms mentioned in the section. These are signs of disease or other conditions that are experienced by a human or experimental model organism. They may include physical or behavioral signs. If no symptoms are mentioned, return NONE.""")
    diagnostics: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of diagnostic procedures mentioned in the section. If no diagnostic procedures are mentioned, return NONE.""")
    experimental_metrics: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of experimental metrics or outcomes mentioned in the section. These may be quantitative or qualitative measures, including biomolecular assays. They measure the effects of treatments on symptoms or diagnostics, or of the progression of Alzheimer's disease and related dementias. For example, Amyloid beta (Aβ) levels are a frequently used metric for assessing the progression of Alzheimer's disease. If no experimental metrics are mentioned, return NONE.""")
    taxon_experimental_metrics: Optional[List[TaxonToExperimentalMetricRelationship]] = Field(default_factory=list, description="""Semicolon-separated list of relationships between a specific taxon and an experimental metric used to measure progression of Alzheimer's disease and related dementias, or an experimental analogue, in the taxon. For example, synaptic density MEASURED_IN Mus musculus.""")


class Metric(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Symptom(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Diagnostic(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Taxon(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class TaxonToExperimentalMetricRelationship(Triple):
    """
    A triple where the subject is a taxon, the object is an experimental metric, and the predicate describes the relationship between the taxon and the metric, usually MEASURED_IN.
    """
    subject: Optional[str] = Field(None, description="""The taxon or species of the model organism in which the experimental metric is measured. For example, Mus musculus, Rattus norvegicus.""")
    predicate: Optional[str] = Field(None, description="""The relationship type, generally MEASURED_IN""")
    object: Optional[str] = Field(None, description="""The experimental metric or outcome used to measure the effects of treatments on symptoms or diagnostics, or of the progression of Alzheimer's disease and related dementias.""")
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the taxon. This may include a strain or genetic background of the model organism.""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the experimental metric. This may include the method of measurement or the specific assay used.""")


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
Metric.model_rebuild()
Symptom.model_rebuild()
Diagnostic.model_rebuild()
Taxon.model_rebuild()
TaxonToExperimentalMetricRelationship.model_rebuild()

