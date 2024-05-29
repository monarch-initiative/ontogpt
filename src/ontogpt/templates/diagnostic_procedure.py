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


class DiagnosticProceduretoPhenotypeAssociation(Triple):
    """
    A triple representing a relationship between a diagnostic procedure and an associated phenotype, e.g., \"blood pressure measurement\" is associated with \"high blood pressure\".
    """
    subject: Optional[str] = Field(None, description="""A diagnostic procedure yielding a result, which in turn may be interpreted as a phenotype. Procedures include \"heart rate measurement\", \"blood pressure measurement\", \"oxygen saturation measurement\", etc. In practice, procedures may be named based on what they measure, with the \"measurement\" part left implicit.""")
    predicate: Optional[str] = Field(None, description="""The relationship type, e.g. RELATED_TO""")
    object: Optional[List[str]] = Field(default_factory=list, description="""The observable physical or biochemical characteristics of a patient. Not equivalent to a disease state, but may contribute to a diagnosis.""")
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the procedure.""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the phenotype.""")


class DiagnosticProceduretoAttributeAssociation(Triple):
    """
    A triple representing a relationship between a diagnostic procedure and a measured attribute, e.g., \"blood pressure measurement\" is associated with \"blood pressure\" (or in OBA, something like OBA:VT0000183, \"blood pressure trait\").
    """
    subject: Optional[str] = Field(None, description="""A diagnostic procedure yielding a result, which in turn may be interpreted as a phenotype. Procedures include \"heart rate measurement\", \"blood pressure measurement\", \"oxygen saturation measurement\", etc. In practice, procedures may be named based on what they measure, with the \"measurement\" part left implicit.""")
    predicate: Optional[str] = Field(None, description="""The relationship type, e.g. RELATED_TO""")
    object: Optional[List[str]] = Field(default_factory=list, description="""Any measurable clinical attribute.""")
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the procedure.""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the phenotype.""")


class DiagnosticProcedure(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Phenotype(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ClinicalAttribute(NamedEntity):
    unit: Optional[str] = Field(None, description="""the unit used to measure the attribute""")
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Quality(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ProcedureToPhenotypePredicate(RelationshipType):
    """
    A predicate for procedure to phenotype relationships, defining \"this procedure is intended to provide support for/against this phenotype\".
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class ProcedureToAttributePredicate(RelationshipType):
    """
    A predicate for procedure to attribute relationships, defining \"this procedure is a measurement of this attribute\".
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Unit(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


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
DiagnosticProceduretoPhenotypeAssociation.model_rebuild()
DiagnosticProceduretoAttributeAssociation.model_rebuild()
DiagnosticProcedure.model_rebuild()
Phenotype.model_rebuild()
ClinicalAttribute.model_rebuild()
Quality.model_rebuild()
ProcedureToPhenotypePredicate.model_rebuild()
ProcedureToAttributePredicate.model_rebuild()
Unit.model_rebuild()

