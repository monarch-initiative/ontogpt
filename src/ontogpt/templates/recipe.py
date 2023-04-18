"""Recipe template."""
from __future__ import annotations

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


class Recipe(ConfiguredBaseModel):
    url: Optional[str] = Field(None)
    label: Optional[str] = Field(None, description="""the name of the recipe""")
    description: Optional[str] = Field(
        None, description="""a brief textual description of the recipe"""
    )
    categories: Optional[List[str]] = Field(
        default_factory=list,
        description="""a semicolon separated list of the categories to which this recipe belongs""",
    )
    ingredients: Optional[List[Ingredient]] = Field(
        default_factory=list,
        description="""a semicolon separated list of the\
            ingredients plus quantities of the recipe""",
    )
    steps: Optional[List[Step]] = Field(
        default_factory=list,
        description="""a semicolon separated list of the\
            individual steps involved in this recipe""",
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


class FoodType(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class RecipeCategory(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Action(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class UtensilType(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Unit(NamedEntity):
    id: Optional[str] = Field(None, description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CompoundExpression(ConfiguredBaseModel):
    pass


class Ingredient(CompoundExpression):
    food_item: Optional[FoodItem] = Field(None, description="""the food item""")
    amount: Optional[Quantity] = Field(
        None, description="""the quantity of the ingredient, e.g. 2 lbs"""
    )


class Quantity(CompoundExpression):
    value: Optional[str] = Field(None, description="""the value of the quantity""")
    unit: Optional[str] = Field(
        None, description="""the unit of the quantity, e.g. grams, cups, etc."""
    )


class Step(CompoundExpression):
    action: Optional[str] = Field(
        None, description="""the action taken in this step (e.g. mix, add)"""
    )
    inputs: Optional[List[FoodItem]] = Field(
        default_factory=list,
        description="""a semicolon separated list of the inputs of this step""",
    )
    outputs: Optional[List[FoodItem]] = Field(
        default_factory=list,
        description="""a semicolon separated list of the outputs of this step""",
    )
    utensils: Optional[List[str]] = Field(
        default_factory=list,
        description="""the kitchen utensil used in this step (e.g. pan, bowl)""",
    )


class FoodItem(CompoundExpression):
    food: Optional[str] = Field(None, description="""the food item""")
    state: Optional[str] = Field(
        None, description="""the state of the food item (e.g. chopped, diced)"""
    )


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
        description="""An optional qualifier or modifier for the subject of the\
            statement, e.g. \"high dose\" or \"intravenously administered\"""",
    )
    object_qualifier: Optional[str] = Field(
        None,
        description="""An optional qualifier or modifier for the object of\
            the statement, e.g. \"severe\" or \"with additional complications\"""",
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
Recipe.update_forward_refs()
ExtractionResult.update_forward_refs()
NamedEntity.update_forward_refs()
FoodType.update_forward_refs()
RecipeCategory.update_forward_refs()
Action.update_forward_refs()
UtensilType.update_forward_refs()
Unit.update_forward_refs()
CompoundExpression.update_forward_refs()
Ingredient.update_forward_refs()
Quantity.update_forward_refs()
Step.update_forward_refs()
FoodItem.update_forward_refs()
Triple.update_forward_refs()
TextWithTriples.update_forward_refs()
RelationshipType.update_forward_refs()
Publication.update_forward_refs()
AnnotatorResult.update_forward_refs()
