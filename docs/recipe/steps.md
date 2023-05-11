# Slot: steps
_a semicolon separated list of the individual steps involved in this recipe_


URI: [recipe:steps](http://w3id.org/ontogpt/recipe/steps)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Recipe](Recipe.md) | 






## Properties

* Range: [Step](Step.md)
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
name: steps
annotations:
  owl:
    tag: owl
    value: ObjectProperty, ObjectSomeValuesFrom
description: a semicolon separated list of the individual steps involved in this recipe
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
multivalued: true
alias: steps
owner: Recipe
domain_of:
- Recipe
range: Step

```
</details>