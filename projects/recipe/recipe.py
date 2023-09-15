# Auto generated from recipe.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-08-07T10:56:18
# Schema: recipe-template
#
# id: https://w3id.org/ontogpt/recipe
# description: A template for food recipes
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AUTO = CurieNamespace('AUTO', 'http://example.org/auto/')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
FOODON = CurieNamespace('FOODON', 'http://purl.obolibrary.org/obo/FOODON_')
HANCESTRO = CurieNamespace('HANCESTRO', 'http://purl.obolibrary.org/obo/HANCESTRO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
BIOLINK = CurieNamespace('biolink', 'http://example.org/UNKNOWN/biolink/')
CORE = CurieNamespace('core', 'http://w3id.org/ontogpt/core/')
DBPEDIAONT = CurieNamespace('dbpediaont', 'http://dbpedia.org/ontology/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
RDF = CurieNamespace('rdf', 'http://example.org/UNKNOWN/rdf/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
RECIPE = CurieNamespace('recipe', 'http://w3id.org/ontogpt/recipe/')
DEFAULT_ = RECIPE


# Types

# Class references
class RecipeUrl(URIorCURIE):
    pass


class NamedEntityId(extended_str):
    pass


class FoodTypeId(NamedEntityId):
    pass


class RecipeCategoryId(NamedEntityId):
    pass


class ActionId(NamedEntityId):
    pass


class UtensilTypeId(NamedEntityId):
    pass


class UnitId(NamedEntityId):
    pass


class RelationshipTypeId(NamedEntityId):
    pass


@dataclass
class Recipe(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RECIPE.Recipe
    class_class_curie: ClassVar[str] = "recipe:Recipe"
    class_name: ClassVar[str] = "Recipe"
    class_model_uri: ClassVar[URIRef] = RECIPE.Recipe

    url: Union[str, RecipeUrl] = None
    label: Optional[str] = None
    description: Optional[str] = None
    categories: Optional[Union[Union[str, RecipeCategoryId], List[Union[str, RecipeCategoryId]]]] = empty_list()
    ingredients: Optional[Union[Union[dict, "Ingredient"], List[Union[dict, "Ingredient"]]]] = empty_list()
    steps: Optional[Union[Union[dict, "Step"], List[Union[dict, "Step"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, RecipeUrl):
            self.url = RecipeUrl(self.url)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.categories, list):
            self.categories = [self.categories] if self.categories is not None else []
        self.categories = [v if isinstance(v, RecipeCategoryId) else RecipeCategoryId(v) for v in self.categories]

        if not isinstance(self.ingredients, list):
            self.ingredients = [self.ingredients] if self.ingredients is not None else []
        self.ingredients = [v if isinstance(v, Ingredient) else Ingredient(**as_dict(v)) for v in self.ingredients]

        if not isinstance(self.steps, list):
            self.steps = [self.steps] if self.steps is not None else []
        self.steps = [v if isinstance(v, Step) else Step(**as_dict(v)) for v in self.steps]

        super().__post_init__(**kwargs)


Any = Any

@dataclass
class ExtractionResult(YAMLRoot):
    """
    A result of extracting knowledge on text
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.ExtractionResult
    class_class_curie: ClassVar[str] = "core:ExtractionResult"
    class_name: ClassVar[str] = "ExtractionResult"
    class_model_uri: ClassVar[URIRef] = RECIPE.ExtractionResult

    input_id: Optional[str] = None
    input_title: Optional[str] = None
    input_text: Optional[str] = None
    raw_completion_output: Optional[str] = None
    prompt: Optional[str] = None
    extracted_object: Optional[Union[dict, Any]] = None
    named_entities: Optional[Union[Union[dict, Any], List[Union[dict, Any]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.input_id is not None and not isinstance(self.input_id, str):
            self.input_id = str(self.input_id)

        if self.input_title is not None and not isinstance(self.input_title, str):
            self.input_title = str(self.input_title)

        if self.input_text is not None and not isinstance(self.input_text, str):
            self.input_text = str(self.input_text)

        if self.raw_completion_output is not None and not isinstance(self.raw_completion_output, str):
            self.raw_completion_output = str(self.raw_completion_output)

        if self.prompt is not None and not isinstance(self.prompt, str):
            self.prompt = str(self.prompt)

        super().__post_init__(**kwargs)


@dataclass
class NamedEntity(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.NamedEntity
    class_class_curie: ClassVar[str] = "core:NamedEntity"
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = RECIPE.NamedEntity

    id: Union[str, NamedEntityId] = None
    label: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass
class FoodType(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RECIPE.FoodType
    class_class_curie: ClassVar[str] = "recipe:FoodType"
    class_name: ClassVar[str] = "FoodType"
    class_model_uri: ClassVar[URIRef] = RECIPE.FoodType

    id: Union[str, FoodTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FoodTypeId):
            self.id = FoodTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class RecipeCategory(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RECIPE.RecipeCategory
    class_class_curie: ClassVar[str] = "recipe:RecipeCategory"
    class_name: ClassVar[str] = "RecipeCategory"
    class_model_uri: ClassVar[URIRef] = RECIPE.RecipeCategory

    id: Union[str, RecipeCategoryId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecipeCategoryId):
            self.id = RecipeCategoryId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Action(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RECIPE.Action
    class_class_curie: ClassVar[str] = "recipe:Action"
    class_name: ClassVar[str] = "Action"
    class_model_uri: ClassVar[URIRef] = RECIPE.Action

    id: Union[str, ActionId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActionId):
            self.id = ActionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class UtensilType(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RECIPE.UtensilType
    class_class_curie: ClassVar[str] = "recipe:UtensilType"
    class_name: ClassVar[str] = "UtensilType"
    class_model_uri: ClassVar[URIRef] = RECIPE.UtensilType

    id: Union[str, UtensilTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UtensilTypeId):
            self.id = UtensilTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Unit(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RECIPE.Unit
    class_class_curie: ClassVar[str] = "recipe:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = RECIPE.Unit

    id: Union[str, UnitId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UnitId):
            self.id = UnitId(self.id)

        super().__post_init__(**kwargs)


class CompoundExpression(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.CompoundExpression
    class_class_curie: ClassVar[str] = "core:CompoundExpression"
    class_name: ClassVar[str] = "CompoundExpression"
    class_model_uri: ClassVar[URIRef] = RECIPE.CompoundExpression


@dataclass
class Ingredient(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOODON["00004085"]
    class_class_curie: ClassVar[str] = "FOODON:00004085"
    class_name: ClassVar[str] = "Ingredient"
    class_model_uri: ClassVar[URIRef] = RECIPE.Ingredient

    food_item: Optional[Union[dict, "FoodItem"]] = None
    amount: Optional[Union[dict, "Quantity"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.food_item is not None and not isinstance(self.food_item, FoodItem):
            self.food_item = FoodItem(**as_dict(self.food_item))

        if self.amount is not None and not isinstance(self.amount, Quantity):
            self.amount = Quantity(**as_dict(self.amount))

        super().__post_init__(**kwargs)


@dataclass
class Quantity(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RECIPE.Quantity
    class_class_curie: ClassVar[str] = "recipe:Quantity"
    class_name: ClassVar[str] = "Quantity"
    class_model_uri: ClassVar[URIRef] = RECIPE.Quantity

    value: Optional[str] = None
    unit: Optional[Union[str, UnitId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.unit is not None and not isinstance(self.unit, UnitId):
            self.unit = UnitId(self.unit)

        super().__post_init__(**kwargs)


@dataclass
class Step(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOODON["00004087"]
    class_class_curie: ClassVar[str] = "FOODON:00004087"
    class_name: ClassVar[str] = "Step"
    class_model_uri: ClassVar[URIRef] = RECIPE.Step

    action: Optional[Union[str, ActionId]] = None
    inputs: Optional[Union[Union[dict, "FoodItem"], List[Union[dict, "FoodItem"]]]] = empty_list()
    outputs: Optional[Union[Union[dict, "FoodItem"], List[Union[dict, "FoodItem"]]]] = empty_list()
    utensils: Optional[Union[Union[str, UtensilTypeId], List[Union[str, UtensilTypeId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.action is not None and not isinstance(self.action, ActionId):
            self.action = ActionId(self.action)

        if not isinstance(self.inputs, list):
            self.inputs = [self.inputs] if self.inputs is not None else []
        self.inputs = [v if isinstance(v, FoodItem) else FoodItem(**as_dict(v)) for v in self.inputs]

        if not isinstance(self.outputs, list):
            self.outputs = [self.outputs] if self.outputs is not None else []
        self.outputs = [v if isinstance(v, FoodItem) else FoodItem(**as_dict(v)) for v in self.outputs]

        if not isinstance(self.utensils, list):
            self.utensils = [self.utensils] if self.utensils is not None else []
        self.utensils = [v if isinstance(v, UtensilTypeId) else UtensilTypeId(v) for v in self.utensils]

        super().__post_init__(**kwargs)


@dataclass
class FoodItem(CompoundExpression):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RECIPE.FoodItem
    class_class_curie: ClassVar[str] = "recipe:FoodItem"
    class_name: ClassVar[str] = "FoodItem"
    class_model_uri: ClassVar[URIRef] = RECIPE.FoodItem

    food: Optional[Union[str, FoodTypeId]] = None
    state: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.food is not None and not isinstance(self.food, FoodTypeId):
            self.food = FoodTypeId(self.food)

        if self.state is not None and not isinstance(self.state, str):
            self.state = str(self.state)

        super().__post_init__(**kwargs)


@dataclass
class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Triple
    class_class_curie: ClassVar[str] = "core:Triple"
    class_name: ClassVar[str] = "Triple"
    class_model_uri: ClassVar[URIRef] = RECIPE.Triple

    subject: Optional[Union[str, NamedEntityId]] = None
    predicate: Optional[Union[str, RelationshipTypeId]] = None
    object: Optional[Union[str, NamedEntityId]] = None
    qualifier: Optional[str] = None
    subject_qualifier: Optional[Union[str, NamedEntityId]] = None
    object_qualifier: Optional[Union[str, NamedEntityId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject is not None and not isinstance(self.subject, NamedEntityId):
            self.subject = NamedEntityId(self.subject)

        if self.predicate is not None and not isinstance(self.predicate, RelationshipTypeId):
            self.predicate = RelationshipTypeId(self.predicate)

        if self.object is not None and not isinstance(self.object, NamedEntityId):
            self.object = NamedEntityId(self.object)

        if self.qualifier is not None and not isinstance(self.qualifier, str):
            self.qualifier = str(self.qualifier)

        if self.subject_qualifier is not None and not isinstance(self.subject_qualifier, NamedEntityId):
            self.subject_qualifier = NamedEntityId(self.subject_qualifier)

        if self.object_qualifier is not None and not isinstance(self.object_qualifier, NamedEntityId):
            self.object_qualifier = NamedEntityId(self.object_qualifier)

        super().__post_init__(**kwargs)


@dataclass
class TextWithTriples(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.TextWithTriples
    class_class_curie: ClassVar[str] = "core:TextWithTriples"
    class_name: ClassVar[str] = "TextWithTriples"
    class_model_uri: ClassVar[URIRef] = RECIPE.TextWithTriples

    publication: Optional[Union[dict, "Publication"]] = None
    triples: Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.publication is not None and not isinstance(self.publication, Publication):
            self.publication = Publication(**as_dict(self.publication))

        if not isinstance(self.triples, list):
            self.triples = [self.triples] if self.triples is not None else []
        self.triples = [v if isinstance(v, Triple) else Triple(**as_dict(v)) for v in self.triples]

        super().__post_init__(**kwargs)


@dataclass
class RelationshipType(NamedEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.RelationshipType
    class_class_curie: ClassVar[str] = "core:RelationshipType"
    class_name: ClassVar[str] = "RelationshipType"
    class_model_uri: ClassVar[URIRef] = RECIPE.RelationshipType

    id: Union[str, RelationshipTypeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RelationshipTypeId):
            self.id = RelationshipTypeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Publication(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.Publication
    class_class_curie: ClassVar[str] = "core:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = RECIPE.Publication

    id: Optional[str] = None
    title: Optional[str] = None
    abstract: Optional[str] = None
    combined_text: Optional[str] = None
    full_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.abstract is not None and not isinstance(self.abstract, str):
            self.abstract = str(self.abstract)

        if self.combined_text is not None and not isinstance(self.combined_text, str):
            self.combined_text = str(self.combined_text)

        if self.full_text is not None and not isinstance(self.full_text, str):
            self.full_text = str(self.full_text)

        super().__post_init__(**kwargs)


@dataclass
class AnnotatorResult(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE.AnnotatorResult
    class_class_curie: ClassVar[str] = "core:AnnotatorResult"
    class_name: ClassVar[str] = "AnnotatorResult"
    class_model_uri: ClassVar[URIRef] = RECIPE.AnnotatorResult

    subject_text: Optional[str] = None
    object_id: Optional[str] = None
    object_text: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.subject_text is not None and not isinstance(self.subject_text, str):
            self.subject_text = str(self.subject_text)

        if self.object_id is not None and not isinstance(self.object_id, str):
            self.object_id = str(self.object_id)

        if self.object_text is not None and not isinstance(self.object_text, str):
            self.object_text = str(self.object_text)

        super().__post_init__(**kwargs)


# Enumerations
class NullDataOptions(EnumDefinitionImpl):

    UNSPECIFIED_METHOD_OF_ADMINISTRATION = PermissibleValue(text="UNSPECIFIED_METHOD_OF_ADMINISTRATION",
                                                                                               meaning=NCIT.C149701)
    NOT_APPLICABLE = PermissibleValue(text="NOT_APPLICABLE",
                                                   meaning=NCIT.C18902)
    NOT_MENTIONED = PermissibleValue(text="NOT_MENTIONED")

    _defn = EnumDefinition(
        name="NullDataOptions",
    )

# Slots
class slots:
    pass

slots.recipe__url = Slot(uri=RDF.Resource, name="recipe__url", curie=RDF.curie('Resource'),
                   model_uri=RECIPE.recipe__url, domain=None, range=URIRef)

slots.recipe__label = Slot(uri=RDFS.label, name="recipe__label", curie=RDFS.curie('label'),
                   model_uri=RECIPE.recipe__label, domain=None, range=Optional[str])

slots.recipe__description = Slot(uri=DCTERMS.description, name="recipe__description", curie=DCTERMS.curie('description'),
                   model_uri=RECIPE.recipe__description, domain=None, range=Optional[str])

slots.recipe__categories = Slot(uri=DCTERMS.subject, name="recipe__categories", curie=DCTERMS.curie('subject'),
                   model_uri=RECIPE.recipe__categories, domain=None, range=Optional[Union[Union[str, RecipeCategoryId], List[Union[str, RecipeCategoryId]]]])

slots.recipe__ingredients = Slot(uri=FOODON['00002420'], name="recipe__ingredients", curie=FOODON.curie('00002420'),
                   model_uri=RECIPE.recipe__ingredients, domain=None, range=Optional[Union[Union[dict, Ingredient], List[Union[dict, Ingredient]]]])

slots.recipe__steps = Slot(uri=RECIPE.steps, name="recipe__steps", curie=RECIPE.curie('steps'),
                   model_uri=RECIPE.recipe__steps, domain=None, range=Optional[Union[Union[dict, Step], List[Union[dict, Step]]]])

slots.ingredient__food_item = Slot(uri=RECIPE.food_item, name="ingredient__food_item", curie=RECIPE.curie('food_item'),
                   model_uri=RECIPE.ingredient__food_item, domain=None, range=Optional[Union[dict, FoodItem]])

slots.ingredient__amount = Slot(uri=RECIPE.amount, name="ingredient__amount", curie=RECIPE.curie('amount'),
                   model_uri=RECIPE.ingredient__amount, domain=None, range=Optional[Union[dict, Quantity]])

slots.quantity__value = Slot(uri=RECIPE.value, name="quantity__value", curie=RECIPE.curie('value'),
                   model_uri=RECIPE.quantity__value, domain=None, range=Optional[str])

slots.quantity__unit = Slot(uri=QUDT.unit, name="quantity__unit", curie=QUDT.curie('unit'),
                   model_uri=RECIPE.quantity__unit, domain=None, range=Optional[Union[str, UnitId]])

slots.step__action = Slot(uri=RECIPE.action, name="step__action", curie=RECIPE.curie('action'),
                   model_uri=RECIPE.step__action, domain=None, range=Optional[Union[str, ActionId]])

slots.step__inputs = Slot(uri=RO['0002233'], name="step__inputs", curie=RO.curie('0002233'),
                   model_uri=RECIPE.step__inputs, domain=None, range=Optional[Union[Union[dict, FoodItem], List[Union[dict, FoodItem]]]])

slots.step__outputs = Slot(uri=RO['0002234'], name="step__outputs", curie=RO.curie('0002234'),
                   model_uri=RECIPE.step__outputs, domain=None, range=Optional[Union[Union[dict, FoodItem], List[Union[dict, FoodItem]]]])

slots.step__utensils = Slot(uri=RO['0002500'], name="step__utensils", curie=RO.curie('0002500'),
                   model_uri=RECIPE.step__utensils, domain=None, range=Optional[Union[Union[str, UtensilTypeId], List[Union[str, UtensilTypeId]]]])

slots.foodItem__food = Slot(uri=BFO['0000051'], name="foodItem__food", curie=BFO.curie('0000051'),
                   model_uri=RECIPE.foodItem__food, domain=None, range=Optional[Union[str, FoodTypeId]])

slots.foodItem__state = Slot(uri=RECIPE.state, name="foodItem__state", curie=RECIPE.curie('state'),
                   model_uri=RECIPE.foodItem__state, domain=None, range=Optional[str])

slots.extractionResult__input_id = Slot(uri=CORE.input_id, name="extractionResult__input_id", curie=CORE.curie('input_id'),
                   model_uri=RECIPE.extractionResult__input_id, domain=None, range=Optional[str])

slots.extractionResult__input_title = Slot(uri=CORE.input_title, name="extractionResult__input_title", curie=CORE.curie('input_title'),
                   model_uri=RECIPE.extractionResult__input_title, domain=None, range=Optional[str])

slots.extractionResult__input_text = Slot(uri=CORE.input_text, name="extractionResult__input_text", curie=CORE.curie('input_text'),
                   model_uri=RECIPE.extractionResult__input_text, domain=None, range=Optional[str])

slots.extractionResult__raw_completion_output = Slot(uri=CORE.raw_completion_output, name="extractionResult__raw_completion_output", curie=CORE.curie('raw_completion_output'),
                   model_uri=RECIPE.extractionResult__raw_completion_output, domain=None, range=Optional[str])

slots.extractionResult__prompt = Slot(uri=CORE.prompt, name="extractionResult__prompt", curie=CORE.curie('prompt'),
                   model_uri=RECIPE.extractionResult__prompt, domain=None, range=Optional[str])

slots.extractionResult__extracted_object = Slot(uri=CORE.extracted_object, name="extractionResult__extracted_object", curie=CORE.curie('extracted_object'),
                   model_uri=RECIPE.extractionResult__extracted_object, domain=None, range=Optional[Union[dict, Any]])

slots.extractionResult__named_entities = Slot(uri=CORE.named_entities, name="extractionResult__named_entities", curie=CORE.curie('named_entities'),
                   model_uri=RECIPE.extractionResult__named_entities, domain=None, range=Optional[Union[Union[dict, Any], List[Union[dict, Any]]]])

slots.namedEntity__id = Slot(uri=CORE.id, name="namedEntity__id", curie=CORE.curie('id'),
                   model_uri=RECIPE.namedEntity__id, domain=None, range=URIRef)

slots.namedEntity__label = Slot(uri=RDFS.label, name="namedEntity__label", curie=RDFS.curie('label'),
                   model_uri=RECIPE.namedEntity__label, domain=None, range=Optional[str])

slots.triple__subject = Slot(uri=CORE.subject, name="triple__subject", curie=CORE.curie('subject'),
                   model_uri=RECIPE.triple__subject, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__predicate = Slot(uri=CORE.predicate, name="triple__predicate", curie=CORE.curie('predicate'),
                   model_uri=RECIPE.triple__predicate, domain=None, range=Optional[Union[str, RelationshipTypeId]])

slots.triple__object = Slot(uri=CORE.object, name="triple__object", curie=CORE.curie('object'),
                   model_uri=RECIPE.triple__object, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__qualifier = Slot(uri=CORE.qualifier, name="triple__qualifier", curie=CORE.curie('qualifier'),
                   model_uri=RECIPE.triple__qualifier, domain=None, range=Optional[str])

slots.triple__subject_qualifier = Slot(uri=CORE.subject_qualifier, name="triple__subject_qualifier", curie=CORE.curie('subject_qualifier'),
                   model_uri=RECIPE.triple__subject_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.triple__object_qualifier = Slot(uri=CORE.object_qualifier, name="triple__object_qualifier", curie=CORE.curie('object_qualifier'),
                   model_uri=RECIPE.triple__object_qualifier, domain=None, range=Optional[Union[str, NamedEntityId]])

slots.textWithTriples__publication = Slot(uri=CORE.publication, name="textWithTriples__publication", curie=CORE.curie('publication'),
                   model_uri=RECIPE.textWithTriples__publication, domain=None, range=Optional[Union[dict, Publication]])

slots.textWithTriples__triples = Slot(uri=CORE.triples, name="textWithTriples__triples", curie=CORE.curie('triples'),
                   model_uri=RECIPE.textWithTriples__triples, domain=None, range=Optional[Union[Union[dict, Triple], List[Union[dict, Triple]]]])

slots.publication__id = Slot(uri=CORE.id, name="publication__id", curie=CORE.curie('id'),
                   model_uri=RECIPE.publication__id, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=CORE.title, name="publication__title", curie=CORE.curie('title'),
                   model_uri=RECIPE.publication__title, domain=None, range=Optional[str])

slots.publication__abstract = Slot(uri=CORE.abstract, name="publication__abstract", curie=CORE.curie('abstract'),
                   model_uri=RECIPE.publication__abstract, domain=None, range=Optional[str])

slots.publication__combined_text = Slot(uri=CORE.combined_text, name="publication__combined_text", curie=CORE.curie('combined_text'),
                   model_uri=RECIPE.publication__combined_text, domain=None, range=Optional[str])

slots.publication__full_text = Slot(uri=CORE.full_text, name="publication__full_text", curie=CORE.curie('full_text'),
                   model_uri=RECIPE.publication__full_text, domain=None, range=Optional[str])

slots.annotatorResult__subject_text = Slot(uri=CORE.subject_text, name="annotatorResult__subject_text", curie=CORE.curie('subject_text'),
                   model_uri=RECIPE.annotatorResult__subject_text, domain=None, range=Optional[str])

slots.annotatorResult__object_id = Slot(uri=CORE.object_id, name="annotatorResult__object_id", curie=CORE.curie('object_id'),
                   model_uri=RECIPE.annotatorResult__object_id, domain=None, range=Optional[str])

slots.annotatorResult__object_text = Slot(uri=CORE.object_text, name="annotatorResult__object_text", curie=CORE.curie('object_text'),
                   model_uri=RECIPE.annotatorResult__object_text, domain=None, range=Optional[str])