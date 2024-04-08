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
    
    

class MaxoAnnotations(ConfiguredBaseModel):
    
    primary_disease: Optional[str] = Field(None, description="""The main disease the text is about, or its central disease topic. This is often the disease mentioned in an article's title or in its first few sentences.""")
    medical_actions: Optional[List[str]] = Field(default_factory=list, description="""Semicolon-separated list of medical actions.""")
    symptoms: Optional[List[str]] = Field(default_factory=list, description="""Semicolon-separated list of signs or symptoms.""")
    chemicals: Optional[List[str]] = Field(default_factory=list, description="""Semicolon-separated list of chemicals or drugs""")
    action_annotation_relationships: Optional[List[ActionAnnotationRelationship]] = Field(default_factory=list, description="""Semicolon-separated list of relationships between a disease, the mentioned signs and symptoms associated with that disease, the medical actions relating to each symptom, and the type of relationship between each action and symptom (usually TREATS or PREVENTS). The disease name must be included in the relationship, for example, \"treatment TREATS symptom IN disease\". If the medical action includes a specific chemical or drug, include the chemical or drug name in the relationship, for example, \"treatment (with chemical) TREATS symptom IN disease\".""")
    
    

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
    
    

class MedicalAction(NamedEntity):
    """
    A clinically prescribed procedure, therapy, intervention, or recommendation. For example: blood transfusion, radiation therapy, cardiac catheterization, pulse oximetry, otoscopy
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Disease(NamedEntity):
    """
    A disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism. For example: Beck-Fahrner syndrome, hereditary retinoblastoma, progeria, diabetes mellitus, infectious otitis media
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Symptom(NamedEntity):
    """
    A condition or phenotype resulting from an abnormal health state. For example: Low serum calcitriol, hypoplasia of the thymus, chronic cough, aortic stiffness, low pulse pressure
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Chemical(NamedEntity):
    """
    A substance that has a defined molecular structure and is produced by or used in a chemical process. Includes drugs used as part of medical actions. For example: corticosteroid, folic acid, opioid analgesic
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
    
    

class ExtendedTriple(Triple):
    """
    Abstract parent for Relation Extraction tasks, with additional support for an extension term describing some aspect of the subject and object.
    """
    subject_extension: Optional[str] = Field(None, description="""An optional term describing some specific aspect of the subject, e.g. \"analgesic agent therapy\" has the aspect \"analgesic\"""")
    object_extension: Optional[str] = Field(None, description="""An optional term describing some specific aspect of the object, e.g. \"analgesic agent therapy\" has the aspect \"analgesic\"""")
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""")
    
    

class ActionAnnotationRelationship(ExtendedTriple):
    """
    An association representing a relationships between a disease, the mentioned signs and symptoms associated with that disease, the medical actions relating to each symptom, and the type of relationship between each action and symptom (usually TREATS or PREVENTS).
    """
    subject_extension: Optional[str] = Field(None, description="""A chemical or drug mentioned in the relationship between the medical action and the symptom, for example, \"analgesic agent therapy\" has the aspect \"analgesic\"""")
    object_extension: Optional[str] = Field(None, description="""An optional term describing some specific aspect of the object, e.g. \"analgesic agent therapy\" has the aspect \"analgesic\"""")
    subject: Optional[str] = Field(None, description="""The medical action. For example: blood transfusion, radiation therapy, cardiac catheterization, pulse oximetry, otoscopy""")
    predicate: Optional[str] = Field(None, description="""The relationship type between the medical action and the symptom, usually TREATS or PREVENTS.""")
    object: Optional[str] = Field(None, description="""A sign or symptom associated with the disease and targeted by the medical action. For example, Low serum calcitriol, hypoplasia of the thymus, chronic cough, aortic stiffness, low pulse pressure""")
    qualifier: Optional[str] = Field(None, description="""The primary disease the relationship is about, or specifically the disease the symptom is related to. For example, Beck-Fahrner syndrome, hereditary retinoblastoma, progeria, diabetes mellitus, infectious otitis media""")
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
MaxoAnnotations.model_rebuild()
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
MedicalAction.model_rebuild()
Disease.model_rebuild()
Symptom.model_rebuild()
Chemical.model_rebuild()
CompoundExpression.model_rebuild()
Triple.model_rebuild()
ExtendedTriple.model_rebuild()
ActionAnnotationRelationship.model_rebuild()
TextWithTriples.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()

