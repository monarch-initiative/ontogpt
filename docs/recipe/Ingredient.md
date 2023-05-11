# Class: Ingredient



URI: [FOODON:00004085](http://purl.obolibrary.org/obo/FOODON_00004085)


```mermaid
erDiagram
Ingredient {

}
Quantity {
    string value  
}
Unit {
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

Ingredient ||--|o FoodItem : "food_item"
Ingredient ||--|o Quantity : "amount"
Quantity ||--|o Unit : "unit"
FoodItem ||--|o FoodType : "food"

```




## Inheritance
* [CompoundExpression](CompoundExpression.md)
    * **Ingredient**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [food_item](food_item.md) | 0..1 <br/> [FoodItem](FoodItem.md) | the food item | direct |
| [amount](amount.md) | 0..1 <br/> [Quantity](Quantity.md) | the quantity of the ingredient, e | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Recipe](Recipe.md) | [ingredients](ingredients.md) | range | [Ingredient](Ingredient.md) |






## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| owl | IntersectionOf |



### Schema Source


* from schema: https://w3id.org/ontogpt/recipe





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | FOODON:00004085 |
| native | recipe:Ingredient |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Ingredient
annotations:
  owl:
    tag: owl
    value: IntersectionOf
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
is_a: CompoundExpression
attributes:
  food_item:
    name: food_item
    annotations:
      owl:
        tag: owl
        value: ObjectProperty, ObjectSomeValuesFrom
    description: the food item
    from_schema: https://w3id.org/ontogpt/recipe
    rank: 1000
    range: FoodItem
  amount:
    name: amount
    annotations:
      owl:
        tag: owl
        value: ObjectProperty, ObjectSomeValuesFrom
    description: the quantity of the ingredient, e.g. 2 lbs
    from_schema: https://w3id.org/ontogpt/recipe
    rank: 1000
    range: Quantity
class_uri: FOODON:00004085

```
</details>

### Induced

<details>
```yaml
name: Ingredient
annotations:
  owl:
    tag: owl
    value: IntersectionOf
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
is_a: CompoundExpression
attributes:
  food_item:
    name: food_item
    annotations:
      owl:
        tag: owl
        value: ObjectProperty, ObjectSomeValuesFrom
    description: the food item
    from_schema: https://w3id.org/ontogpt/recipe
    rank: 1000
    alias: food_item
    owner: Ingredient
    domain_of:
    - Ingredient
    range: FoodItem
  amount:
    name: amount
    annotations:
      owl:
        tag: owl
        value: ObjectProperty, ObjectSomeValuesFrom
    description: the quantity of the ingredient, e.g. 2 lbs
    from_schema: https://w3id.org/ontogpt/recipe
    rank: 1000
    alias: amount
    owner: Ingredient
    domain_of:
    - Ingredient
    range: Quantity
class_uri: FOODON:00004085

```
</details>