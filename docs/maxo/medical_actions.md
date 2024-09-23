

# Slot: medical_actions


_Semicolon-separated list of medical actions._



URI: [maxo_extract:medical_actions](http://w3id.org/ontogpt/maxomedical_actions)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MaxoAnnotations](MaxoAnnotations.md) |  |  no  |







## Properties

* Range: [MedicalAction](MedicalAction.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | Semicolon-separated list of medical actions, where each is a clinically prescribed procedure, therapy, intervention, or recommendation. |



### Schema Source


* from schema: http://w3id.org/ontogpt/maxo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | maxo_extract:medical_actions |
| native | maxo_extract:medical_actions |




## LinkML Source

<details>
```yaml
name: medical_actions
annotations:
  prompt:
    tag: prompt
    value: Semicolon-separated list of medical actions, where each is a clinically
      prescribed procedure, therapy, intervention, or recommendation.
description: Semicolon-separated list of medical actions.
from_schema: http://w3id.org/ontogpt/maxo
rank: 1000
alias: medical_actions
owner: MaxoAnnotations
domain_of:
- MaxoAnnotations
range: MedicalAction
multivalued: true

```
</details>