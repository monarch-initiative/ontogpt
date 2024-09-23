

# Slot: outputs


_a semicolon separated list of the outputs of this step_



URI: [RO:0002234](http://purl.obolibrary.org/obo/RO_0002234)



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
name: outputs
annotations:
  owl:
    tag: owl
    value: ObjectProperty, ObjectSomeValuesFrom
description: a semicolon separated list of the outputs of this step
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
slot_uri: RO:0002234
multivalued: true
alias: outputs
owner: Step
domain_of:
- Step
range: FoodItem

```
</details>