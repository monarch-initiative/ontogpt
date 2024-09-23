

# Slot: treatment_mechanisms


_semicolon-separated list of treatment to asterisk-separated mechanism associations_



URI: [treatment:treatment_mechanisms](http://w3id.org/ontogpt/treatments/treatment_mechanisms)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiseaseTreatmentSummary](DiseaseTreatmentSummary.md) |  |  no  |







## Properties

* Range: [TreatmentMechanism](TreatmentMechanism.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt.separator | * |



### Schema Source


* from schema: http://w3id.org/ontogpt/treatment




## LinkML Source

<details>
```yaml
name: treatment_mechanisms
annotations:
  prompt.separator:
    tag: prompt.separator
    value: '*'
description: semicolon-separated list of treatment to asterisk-separated mechanism
  associations
from_schema: http://w3id.org/ontogpt/treatment
rank: 1000
multivalued: true
alias: treatment_mechanisms
owner: DiseaseTreatmentSummary
domain_of:
- DiseaseTreatmentSummary
range: TreatmentMechanism

```
</details>