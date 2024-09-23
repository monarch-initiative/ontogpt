

# Slot: inputs


_a semicolon separated list of the inputs of this step_



URI: [RO:0002233](http://purl.obolibrary.org/obo/RO_0002233)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Step](Step.md) |  |  no  |







## Properties

* Range: [FoodItem](FoodItem.md)

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
name: inputs
annotations:
  owl:
    tag: owl
    value: ObjectProperty, ObjectSomeValuesFrom
description: a semicolon separated list of the inputs of this step
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
slot_uri: RO:0002233
multivalued: true
alias: inputs
owner: Step
domain_of:
- Step
range: FoodItem

```
</details>