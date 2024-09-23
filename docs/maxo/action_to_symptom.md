# Slot: action_to_symptom

URI: [maxo_extract:action_to_symptom](http://w3id.org/ontogpt/maxoaction_to_symptom)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MaxoAnnotations](MaxoAnnotations.md) |  |  no  |







## Properties

* Range: [ActionToSymptomRelationship](ActionToSymptomRelationship.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | A triple representing a relationship between a medical action (A clinically prescribed procedure, therapy, intervention, or recommendation) and a symptom, for example, a chest X-ray IS USED TO DIAGNOSE pleural effusion. |



### Schema Source


* from schema: http://w3id.org/ontogpt/maxo




## LinkML Source

<details>
```yaml
name: action_to_symptom
annotations:
  prompt:
    tag: prompt
    value: A triple representing a relationship between a medical action (A clinically
      prescribed procedure, therapy, intervention, or recommendation) and a symptom,
      for example, a chest X-ray IS USED TO DIAGNOSE pleural effusion.
from_schema: http://w3id.org/ontogpt/maxo
rank: 1000
multivalued: true
alias: action_to_symptom
owner: MaxoAnnotations
domain_of:
- MaxoAnnotations
range: ActionToSymptomRelationship

```
</details>