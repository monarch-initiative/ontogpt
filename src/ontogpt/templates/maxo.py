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
    
    

class Action(NamedEntity):
    """
    A clinically prescribed procedure, therapy, intervention, or recommendation.
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Disease(NamedEntity):
    """
    A disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism.
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Symptom(NamedEntity):
    """
    A condition or phenotype resulting from an abnormal health state.
    """
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
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""")
    
    

class ActionToDiseaseRelationship(Triple):
    """
    A triple representing a relationship between a medical action (A clinically prescribed procedure, therapy, intervention, or recommendation) and a disease, for example, radiation therapy TREATS cancer, or PET scan IS USED TO DIAGNOSE myocarditis.
    """
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None, description="""The relationship type, usually TREATS or IS USED TO DIAGNOSE""")
    object: Optional[List[str]] = Field(default_factory=list)
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the medical action.""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the disease.""")
    
    

class ActionToSymptomRelationship(Triple):
    """
    A triple representing a relationship between a medical action (A clinically prescribed procedure, therapy, intervention, or recommendation) and a symptom, for example, a chest X-ray IS USED TO DIAGNOSE pleural effusion.
    """
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None, description="""The relationship type, usually IS USED TO DIAGNOSE""")
    object: Optional[List[str]] = Field(default_factory=list)
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the medical action.""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the symptom.""")
    
    

class TextWithTriples(ConfiguredBaseModel):
    """
    A text containing one or more relations of the Triple type.
    """
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)
    
    

class MaxoAnnotations(TextWithTriples):
    
    action: Optional[List[str]] = Field(default_factory=list, description="""Semicolon-separated list of medical actions.""")
    disease: Optional[List[str]] = Field(default_factory=list, description="""Semicolon-separated list of diseases.""")
    symptom: Optional[List[str]] = Field(default_factory=list, description="""Semicolon-separated list of symptoms.""")
    action_to_disease: Optional[List[ActionToDiseaseRelationship]] = Field(default_factory=list)
    action_to_symptom: Optional[List[ActionToSymptomRelationship]] = Field(default_factory=list)
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
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
Action.model_rebuild()
Disease.model_rebuild()
Symptom.model_rebuild()
CompoundExpression.model_rebuild()
Triple.model_rebuild()
ActionToDiseaseRelationship.model_rebuild()
ActionToSymptomRelationship.model_rebuild()
TextWithTriples.model_rebuild()
MaxoAnnotations.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()

