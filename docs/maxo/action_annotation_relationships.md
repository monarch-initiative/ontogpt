

# Slot: action_annotation_relationships


_Semicolon-separated list of relationships between a disease, the mentioned signs and symptoms associated with that disease, the medical actions relating to each symptom, and the type of relationship between each action and symptom (usually TREATS or PREVENTS). The disease name must be included in the relationship, for example, "treatment TREATS symptom IN disease". If the medical action includes a specific chemical or drug, include the chemical or drug name in the relationship, for example, "treatment (with chemical) TREATS symptom IN disease"._



URI: [maxo_extract:action_annotation_relationships](http://w3id.org/ontogpt/maxoaction_annotation_relationships)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MaxoAnnotations](MaxoAnnotations.md) |  |  no  |







## Properties

* Range: [ActionAnnotationRelationship](ActionAnnotationRelationship.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/maxo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | maxo_extract:action_annotation_relationships |
| native | maxo_extract:action_annotation_relationships |




## LinkML Source

<details>
```yaml
name: action_annotation_relationships
description: Semicolon-separated list of relationships between a disease, the mentioned
  signs and symptoms associated with that disease, the medical actions relating to
  each symptom, and the type of relationship between each action and symptom (usually
  TREATS or PREVENTS). The disease name must be included in the relationship, for
  example, "treatment TREATS symptom IN disease". If the medical action includes a
  specific chemical or drug, include the chemical or drug name in the relationship,
  for example, "treatment (with chemical) TREATS symptom IN disease".
from_schema: http://w3id.org/ontogpt/maxo
rank: 1000
alias: action_annotation_relationships
owner: MaxoAnnotations
domain_of:
- MaxoAnnotations
range: ActionAnnotationRelationship
multivalued: true

```
</details>