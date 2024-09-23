

# Slot: environmental_material


_the environmental material that was sampled_



URI: [sample:environmental_material](http://w3id.org/ontogpt/environmental-sample-ungrounded/environmental_material)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) |  |  no  |







## Properties

* Range: [EnvironmentalMaterial](EnvironmentalMaterial.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of environmental materials |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample-ungrounded




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sample:environmental_material |
| native | sample:environmental_material |




## LinkML Source

<details>
```yaml
name: environmental_material
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of environmental materials
description: the environmental material that was sampled
from_schema: http://w3id.org/ontogpt/environmental-sample-ungrounded
rank: 1000
alias: environmental_material
owner: Study
domain_of:
- Study
range: EnvironmentalMaterial
multivalued: true

```
</details>