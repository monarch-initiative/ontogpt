

# Slot: ingredients


_a semicolon separated list of the ingredients plus quantities of the recipe_



URI: [FOODON:00002420](http://purl.obolibrary.org/obo/FOODON_00002420)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Recipe](Recipe.md) |  |  no  |







## Properties

* Range: [Ingredient](Ingredient.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| owl | ObjectProperty, ObjectSomeValuesFrom |



### Schema Source


* from schema: https://w3id.org/ontogpt/recipe




## LinkML Source

<details>
```yaml
name: ingredients
annotations:
  owl:
    tag: owl
    value: ObjectProperty, ObjectSomeValuesFrom
description: a semicolon separated list of the ingredients plus quantities of the
  recipe
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
slot_uri: FOODON:00002420
multivalued: true
alias: ingredients
owner: Recipe
domain_of:
- Recipe
range: Ingredient

```
</details>