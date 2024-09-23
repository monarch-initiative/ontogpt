

# Slot: environmental_material


_the environmental material that was sampled_



URI: [nmdcsd:environmental_material](http://w3id.org/ontogpt/nmdc-schema-dataenvironmental_material)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) |  |  no  |







## Properties

* Range: [EnvironmentalMaterial](EnvironmentalMaterial.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of environmental materials |



### Schema Source


* from schema: http://w3id.org/ontogpt/nmdc-schema-data




## LinkML Source

<details>
```yaml
name: environmental_material
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of environmental materials
description: the environmental material that was sampled
from_schema: http://w3id.org/ontogpt/nmdc-schema-data
rank: 1000
multivalued: true
alias: environmental_material
owner: Dataset
domain_of:
- Dataset
range: EnvironmentalMaterial

```
</details>