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
    
    

class Recipe(ConfiguredBaseModel):
    
    url: str = Field(...)
    label: Optional[str] = Field(None, description="""the name of the recipe""")
    description: Optional[str] = Field(None, description="""a brief textual description of the recipe""")
    categories: Optional[List[str]] = Field(default_factory=list, description="""a semicolon separated list of the categories to which this recipe belongs""")
    ingredients: Optional[List[Ingredient]] = Field(default_factory=list, description="""a semicolon separated list of the ingredients plus quantities of the recipe""")
    steps: Optional[List[Step]] = Field(default_factory=list, description="""a semicolon separated list of the individual steps involved in this recipe""")
    
    

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
    
    

class FoodType(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class RecipeCategory(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Action(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class UtensilType(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class Unit(NamedEntity):
    
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")
    
    

class CompoundExpression(ConfiguredBaseModel):
    
    None
    
    

class Ingredient(CompoundExpression):
    
    food_item: Optional[FoodItem] = Field(None, description="""the food item""")
    amount: Optional[Quantity] = Field(None, description="""the quantity of the ingredient, e.g. 2 lbs""")
    
    

class Quantity(CompoundExpression):
    
    value: Optional[str] = Field(None, description="""the value of the quantity""")
    unit: Optional[str] = Field(None, description="""the unit of the quantity, e.g. grams, cups, etc.""")
    
    

class Step(CompoundExpression):
    
    action: Optional[str] = Field(None, description="""the action taken in this step (e.g. mix, add)""")
    inputs: Optional[List[FoodItem]] = Field(default_factory=list, description="""a semicolon separated list of the inputs of this step""")
    outputs: Optional[List[FoodItem]] = Field(default_factory=list, description="""a semicolon separated list of the outputs of this step""")
    utensils: Optional[List[str]] = Field(default_factory=list, description="""the kitchen utensil used in this step (e.g. pan, bowl)""")
    
    

class FoodItem(CompoundExpression):
    
    food: Optional[str] = Field(None, description="""the food item""")
    state: Optional[str] = Field(None, description="""the state of the food item (e.g. chopped, diced)""")
    
    

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
Recipe.model_rebuild()
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
FoodType.model_rebuild()
RecipeCategory.model_rebuild()
Action.model_rebuild()
UtensilType.model_rebuild()
Unit.model_rebuild()
CompoundExpression.model_rebuild()
Ingredient.model_rebuild()
Quantity.model_rebuild()
Step.model_rebuild()
FoodItem.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()

