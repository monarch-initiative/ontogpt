# Slot: utensils
_the kitchen utensil used in this step (e.g. pan, bowl)_


URI: [RO:0002500](http://purl.obolibrary.org/obo/RO_0002500)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Step](Step.md) | 






## Properties

* Range: [UtensilType](UtensilType.md)
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
name: utensils
annotations:
  owl:
    tag: owl
    value: ObjectProperty, ObjectSomeValuesFrom
description: the kitchen utensil used in this step (e.g. pan, bowl)
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
slot_uri: RO:0002500
multivalued: true
alias: utensils
owner: Step
domain_of:
- Step
range: UtensilType

```
</details>