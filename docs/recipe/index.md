# Food Recipe Template

A template for food recipes

URI: https://w3id.org/ontogpt/recipe
Name: recipe-template



## Schema Diagram

```mermaid
erDiagram
Recipe {
    uriorcurie url  
    string label  
    string description  
}
Step {

}
UtensilType {
    string id  
    string label  
}
FoodItem {
    string state  
}
FoodType {
    string id  
    string label  
}
Action {
    string id  
    string label  
}
Ingredient {

}
Quantity {
    string value  
}
Unit {
    string id  
    string label  
}
RecipeCategory {
    string id  
    string label  
}

Recipe ||--}o RecipeCategory : "categories"
Recipe ||--}o Ingredient : "ingredients"
Recipe ||--}o Step : "steps"
Step ||--|o Action : "action"
Step ||--}o FoodItem : "inputs"
Step ||--}o FoodItem : "outputs"
Step ||--}o UtensilType : "utensils"
FoodItem ||--|o FoodType : "food"
Ingredient ||--|o FoodItem : "food_item"
Ingredient ||--|o Quantity : "amount"
Quantity ||--|o Unit : "unit"

```


## Classes

| Class | Description |
| --- | --- |
| [Action](Action.md) |  |
| [AnnotatorResult](AnnotatorResult.md) |  |
| [Any](Any.md) |  |
| [CompoundExpression](CompoundExpression.md) |  |
| [ExtractionResult](ExtractionResult.md) | A result of extracting knowledge on text |
| [FoodItem](FoodItem.md) |  |
| [FoodType](FoodType.md) |  |
| [Ingredient](Ingredient.md) |  |
| [NamedEntity](NamedEntity.md) |  |
| [Publication](Publication.md) |  |
| [Quantity](Quantity.md) |  |
| [Recipe](Recipe.md) |  |
| [RecipeCategory](RecipeCategory.md) |  |
| [RelationshipType](RelationshipType.md) |  |
| [Step](Step.md) |  |
| [TextWithTriples](TextWithTriples.md) |  |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |
| [Unit](Unit.md) |  |
| [UtensilType](UtensilType.md) |  |


## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) | The abstract of the publication |
| [action](action.md) | the action taken in this step (e |
| [amount](amount.md) | the quantity of the ingredient, e |
| [categories](categories.md) | a semicolon separated list of the categories to which this recipe belongs |
| [combined_text](combined_text.md) |  |
| [description](description.md) | a brief textual description of the recipe |
| [extracted_object](extracted_object.md) | The complex objects extracted from the text |
| [food](food.md) | the food item |
| [food_item](food_item.md) | the food item |
| [full_text](full_text.md) | The full text of the publication |
| [id](id.md) | A unique identifier for the named entity |
| [ingredients](ingredients.md) | a semicolon separated list of the ingredients plus quantities of the recipe |
| [input_id](input_id.md) |  |
| [input_text](input_text.md) |  |
| [input_title](input_title.md) |  |
| [inputs](inputs.md) | a semicolon separated list of the inputs of this step |
| [label](label.md) | the name of the recipe |
| [named_entities](named_entities.md) | Named entities extracted from the text |
| [object](object.md) |  |
| [object_id](object_id.md) |  |
| [object_qualifier](object_qualifier.md) | An optional qualifier or modifier for the object of the statement, e |
| [object_text](object_text.md) |  |
| [outputs](outputs.md) | a semicolon separated list of the outputs of this step |
| [predicate](predicate.md) |  |
| [prompt](prompt.md) |  |
| [publication](publication.md) |  |
| [qualifier](qualifier.md) | A qualifier for the statements, e |
| [raw_completion_output](raw_completion_output.md) |  |
| [state](state.md) | the state of the food item (e |
| [steps](steps.md) | a semicolon separated list of the individual steps involved in this recipe |
| [subject](subject.md) |  |
| [subject_qualifier](subject_qualifier.md) | An optional qualifier or modifier for the subject of the statement, e |
| [subject_text](subject_text.md) |  |
| [title](title.md) | The title of the publication |
| [triples](triples.md) |  |
| [unit](unit.md) | the unit of the quantity, e |
| [url](url.md) |  |
| [utensils](utensils.md) | the kitchen utensil used in this step (e |
| [value](value.md) | the value of the quantity |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
