# Slot: anatomical_entity
_The anatomical location that the chemical entity is measured in_


URI: [phenotype:anatomical_entity](http://w3id.org/ontogpt/phenotype/anatomical_entity)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Trait](Trait.md) | 






## Properties

* Range: [AnatomicalEntity](AnatomicalEntity.md)







## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt.example | liver, heart, brain, finger |



### Schema Source


* from schema: http://w3id.org/ontogpt/eq




## LinkML Source

<details>
```yaml
name: anatomical_entity
annotations:
  prompt.example:
    tag: prompt.example
    value: liver, heart, brain, finger
description: The anatomical location that the chemical entity is measured in
from_schema: http://w3id.org/ontogpt/eq
rank: 1000
alias: anatomical_entity
owner: Trait
domain_of:
- Trait
range: AnatomicalEntity

```
</details>