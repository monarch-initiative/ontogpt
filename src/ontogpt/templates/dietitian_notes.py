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
    
    

class ClinicalObservationSet(ConfiguredBaseModel):
    """
    A set of sets of clinical observations.
    """
    observations: Optional[List[str]] = Field(default_factory=list)
    
    

class MalnutritionObservations(ConfiguredBaseModel):
    
    malnutrition_presence: Optional[str] = Field(None, description="""True if the patient is malnourished, False otherwise. N/A if not provided.""")
    malnutrition_risk: Optional[str] = Field(None, description="""True if the patient has a demonstrable risk for malnutrition, False otherwise. N/A if not provided.""")
    severity: Optional[str] = Field(None, description="""The severity of the patient's malnutrition, if present. This may be Mild, Moderate, or Severe. In general, a patient receiving less than 50% of their estimated energy requirement for greater than 5 days is considered to have severe malnutrition. N/A if not provided.""")
    acute_or_chronic: Optional[str] = Field(None, description="""The duration of the patient's malnutrition, if present. For pediatric patients, acute malnutrition is less than 3 months, and chronic malnutrition is greater than 3 months. This may be Acute or Chronic. N/A if not provided.""")
    diagnosis: Optional[str] = Field(None, description="""The patient's malnutrition diagnosis, if present. This should not include modifiers like 'severe'. N/A if not provided.""")
    etiology: Optional[str] = Field(None, description="""The cause of the patient's malnutrition, if known. This may be due to acute or chronic disease or social/behavioral factors. N/A if not provided.""")
    risk_for_refeeding_syndrome: Optional[str] = Field(None, description="""True if the patient is at risk for refeeding syndrome, False otherwise. N/A if not provided.""")
    
    

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
    is_preterm: Optional[str] = Field(None)
    patient_age: Optional[QuantitativeValue] = Field(None)
    patient_height: Optional[QuantitativeValueWithMetric] = Field(None)
    current_patient_weight: Optional[QuantitativeValueWithMetric] = Field(None)
    usual_patient_weight: Optional[QuantitativeValueWithMetric] = Field(None)
    head_circumference: Optional[QuantitativeValueWithMetric] = Field(None)
    malnutrition_status: Optional[MalnutritionObservations] = Field(None)
    diet_supplementation: Optional[List[DietSupplementation]] = Field(default_factory=list, description="""A semicolon-separated list of the patient's diet supplementation therapies. Split on specific ingredients and their amounts. All acronyms should be expanded, omitting the original acronym. Relevant acronyms: PO: per os/by mouth, TPN: total parenteral nutrition, PN: parenteral nutrition, EN: enteral nutrition, D#%: dextrose percentage (e.g. D5%) for PN infusion, AA # g/kg/d: amino acid provisions (may also be in percentages) for PN infusion, SMOF # g/kg/d: soy MCT olive fish oil emulsion for PN infusion, GIR: glucose infusion rate, SBS: short bowel syndrome, LIS: low intermittent suction, BW: birth weight, EHM: exclusively human milk, RTBW: return to birth weight, Mg: magnesium, Phos: phosphorus, GI: gastrointestinal, PICC: peripherally inserted central catheter, DOL: day of life, TG: triglycerides, KUB: Kidney ureter bladder CT""")
    nutrition_support: Optional[List[NutritionSupport]] = Field(default_factory=list, description="""A semicolon-separated list of the patient's nutrition support therapies, usually enteral or parenteral nutrition. All acronyms should be expanded, omitting the original acronym. Relevant acronyms: PO: per os/by mouth, TPN: total parenteral nutrition, PN: parenteral nutrition, EN: enteral nutrition, D#%: dextrose percentage (e.g. D5%) for PN infusion, AA # g/kg/d: amino acid provisions (may also be in percentages) for PN infusion, SMOF # g/kg/d: soy MCT olive fish oil emulsion for PN infusion, GIR: glucose infusion rate, SBS: short bowel syndrome, LIS: low intermittent suction, BW: birth weight, EHM: exclusively human milk, RTBW: return to birth weight, Mg: magnesium, Phos: phosphorus, GI: gastrointestinal, PICC: peripherally inserted central catheter, DOL: day of life, TG: triglycerides, KUB: Kidney ureter bladder CT""")
    medications: Optional[List[DrugTherapy]] = Field(default_factory=list, description="""A semicolon-separated list of the patient's medications. This should include the medication name, dosage, frequency, and route of administration. Relevant acronyms: PO: per os/by mouth, PRN: pro re nata/as needed. 'Not provided' if not provided.""")
    nil_per_os: Optional[str] = Field(None, description="""True if the patient is not receiving any oral nutrition, False otherwise. NPO means nil per os/nothing by mouth. N/A if not indicated.""")
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class TherapeuticMaterial(NamedEntity):
    """
    A specific material added to a patient's diet or included as part of a nutritional plan.
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class NutritionSupportMethod(NamedEntity):
    """
    A method of nutrition support therapy used to treat or prevent malnutrition. This includes any method of feeding intended to replace or support oral feeding.
    """
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Disease(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Drug(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Unit(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class CompoundExpression(ConfiguredBaseModel):
    
    None
    
    

class QuantitativeValue(CompoundExpression):
    
    value: Optional[str] = Field(None, description="""The value of the quantity, or N/A if not provided.""")
    unit: Optional[str] = Field(None, description="""The unit of the quantity, or N/A if not provided.""")
    
    

class QuantitativeValueWithMetric(QuantitativeValue):
    
    percentile: Optional[str] = Field(None, description="""The reported percentile of the value, as compared to a reference patient population. Always positive, on a scale from 0 to 99%. May be reported as \"X%\", \"X%ile\", or \"Xth percentile\", where X is the value. N/A if not provided.""")
    zscore: Optional[str] = Field(None, description="""The relative standard deviation of the value, as a function of the percentile. May be positive or negative. May be reported as \"z-score\", \"Z-score\", or \"Z\", followed by the value. N/A if not provided.""")
    value: Optional[str] = Field(None, description="""The value of the quantity, or N/A if not provided.""")
    unit: Optional[str] = Field(None, description="""The unit of the quantity, or N/A if not provided.""")
    
    

class QuantitativeValueWithFrequency(QuantitativeValue):
    
    frequency: Optional[str] = Field(None, description="""A phrase describing how often an event or procedure should happen. May include time phrases such as \"per day\", Latin version of the same such as \"per diem\", single words such as \"daily\", or more complex phrases such as \"every 4 hours\". N/A if not provided.""")
    value: Optional[str] = Field(None, description="""The value of the quantity, or N/A if not provided.""")
    unit: Optional[str] = Field(None, description="""The unit of the quantity, or N/A if not provided.""")
    
    

class DietSupplementation(CompoundExpression):
    
    supplement: Optional[str] = Field(None, description="""The name of a specific material added to a patient's diet.""")
    amount: Optional[QuantitativeValueWithFrequency] = Field(None, description="""The quantity or dosage of the therapy, if provided. May include a frequency. N/A if not provided.""")
    dosage_by_unit: Optional[str] = Field(None, description="""The unit of a patient's properties used to determine supplement dosage. Often \"kilogram\". N/A if not provided.""")
    duration: Optional[QuantitativeValue] = Field(None, description="""The duration of the supplementation, if provided. N/A if not provided.""")
    route_of_administration: Optional[str] = Field(None, description="""The route of administration for the supplementation, if provided. N/A if not provided.""")
    
    

class NutritionSupport(CompoundExpression):
    
    method: Optional[str] = Field(None, description="""The name of a method used to provide nutritional support.""")
    components: Optional[List[NutritionSupportComponent]] = Field(default_factory=list, description="""The names of specific components included in a patient's diet.""")
    
    

class NutritionSupportComponent(CompoundExpression):
    
    material: Optional[str] = Field(None, description="""The name of a specific material included in a patient's diet.""")
    amount: Optional[QuantitativeValueWithFrequency] = Field(None, description="""The quantity or dosage of the therapy, if provided. May include a frequency. N/A if not provided.""")
    dosage_by_unit: Optional[str] = Field(None, description="""The unit of a patient's properties used to determine diet amounts. Often \"kilogram\". N/A if not provided.""")
    duration: Optional[QuantitativeValue] = Field(None, description="""The duration of the therapy, if provided. N/A if not provided.""")
    
    

class DrugTherapy(CompoundExpression):
    
    drug: Optional[str] = Field(None, description="""The name of a specific drug for a patient's preventative or therapeutic treatment.""")
    amount: Optional[QuantitativeValueWithFrequency] = Field(None, description="""The quantity or dosage of the drug, if provided. May include a frequency. N/A if not provided.""")
    dosage_by_unit: Optional[str] = Field(None, description="""The unit of a patient's properties used to determine drug dosage. Often \"kilogram\". N/A if not provided.""")
    duration: Optional[QuantitativeValue] = Field(None, description="""The duration of the drug therapy, if provided. N/A if not provided.""")
    route_of_administration: Optional[str] = Field(None, description="""The route of administration for the drug therapy, if provided. N/A if not provided.""")
    
    

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
TherapeuticMaterial.model_rebuild()
NutritionSupportMethod.model_rebuild()
Disease.model_rebuild()
Drug.model_rebuild()
Unit.model_rebuild()
CompoundExpression.model_rebuild()
QuantitativeValue.model_rebuild()
QuantitativeValueWithMetric.model_rebuild()
QuantitativeValueWithFrequency.model_rebuild()
DietSupplementation.model_rebuild()
NutritionSupport.model_rebuild()
NutritionSupportComponent.model_rebuild()
DrugTherapy.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()

