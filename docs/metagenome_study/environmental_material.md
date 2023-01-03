# Slot: environmental_material
_the environmental material that was sampled_


URI: [eg:environmental_material](http://w3id.org/ontogpt/environmental-metagenome/environmental_material)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Study](Study.md) | 






## Properties

* Range: [EnvironmentalMaterial](EnvironmentalMaterial.md)
* Multivalued: True








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of environmental materials |



### Schema Source


* from schema: http://w3id.org/ontogpt/metagenome




## LinkML Source

<details>
```yaml
name: environmental_material
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of environmental materials
description: the environmental material that was sampled
from_schema: http://w3id.org/ontogpt/metagenome
rank: 1000
multivalued: true
alias: environmental_material
owner: Study
domain_of:
- Study
range: EnvironmentalMaterial

```
</details>