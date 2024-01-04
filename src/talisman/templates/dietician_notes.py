from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, ConfigDict,  Field, field_validator
import re
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        validate_default=True,
        extra = 'forbid',
        arbitrary_types_allowed=True,
        use_enum_values = True)


class NullDataOptions(str, Enum):
    
    
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    
    NOT_APPLICABLE = "NOT_APPLICABLE"
    
    NOT_MENTIONED = "NOT_MENTIONED"
    
    

class ClinicalObservationSet(ConfiguredBaseModel):
    """
    A set of sets of clinical observations.
    """
    observations: Optional[List[str]] = Field(default_factory=list)
    
        

class MalnutritionObservations(ConfiguredBaseModel):
    
    malnutrition_presence: Optional[str] = Field(None, description="""True if the patient is malnourished, False otherwise.""")
    severity: Optional[str] = Field(None, description="""The severity of the patient's malnutrition, if present.""")
    diagnosis: Optional[str] = Field(None, description="""The patient's malnutrition diagnosis, if present.""")
    
        

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
    
        

class ClinicalObservations(NamedEntity):
    """
    A set of clinical observations about a single patient at a single time.
    """
    is_pediatric: Optional[str] = Field(None)
    patient_height: Optional[QuantitativeValue] = Field(None)
    patient_weight: Optional[QuantitativeValue] = Field(None)
    malnutrition_status: Optional[MalnutritionObservations] = Field(None)
    diet_supplementation: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of the patient's diet supplementation therapies.""")
    nutrition_support: Optional[List[str]] = Field(default_factory=list, description="""A semicolon-separated list of the patient's nutrition support therapies, usually enteral or parenteral nutrition.""")
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
        

class DietSupplementation(NamedEntity):
    """
    A diet supplementation therapy.
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
        

class NutritionSupport(NamedEntity):
    """
    A nutrition support therapy used to treat or prevent malnutrition.
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
        

class Disease(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
        

class Unit(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
        

class CompoundExpression(ConfiguredBaseModel):
    
    None
    
        

class QuantitativeValue(CompoundExpression):
    
    value: Optional[float] = Field(None, description="""The value of the quantity.""")
    unit: Optional[str] = Field(None, description="""The unit of the quantity.""")
    
        

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
    
        


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ClinicalObservationSet.model_rebuild()
MalnutritionObservations.model_rebuild()
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
ClinicalObservations.model_rebuild()
DietSupplementation.model_rebuild()
NutritionSupport.model_rebuild()
Disease.model_rebuild()
Unit.model_rebuild()
CompoundExpression.model_rebuild()
QuantitativeValue.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()

