# Slot: action_to_disease

URI: [maxo_extract:action_to_disease](http://w3id.org/ontogpt/maxoaction_to_disease)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MaxoAnnotations](MaxoAnnotations.md) |  |  no  |







## Properties

* Range: [ActionToDiseaseRelationship](ActionToDiseaseRelationship.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | Semicolon-separated list of medical action to disease relationships, where each is a triple representing a relationship between a medical action and a disease, for example, radiation therapy TREATS cancer, or PET scan IS USED TO DIAGNOSE myocarditis. |



### Schema Source


* from schema: http://w3id.org/ontogpt/maxo




## LinkML Source

<details>
```yaml
name: action_to_disease
annotations:
  prompt:
    tag: prompt
    value: Semicolon-separated list of medical action to disease relationships, where
      each is a triple representing a relationship between a medical action and a
      disease, for example, radiation therapy TREATS cancer, or PET scan IS USED TO
      DIAGNOSE myocarditis.
from_schema: http://w3id.org/ontogpt/maxo
rank: 1000
multivalued: true
alias: action_to_disease
owner: MaxoAnnotations
domain_of:
- MaxoAnnotations
range: ActionToDiseaseRelationship

```
</details>