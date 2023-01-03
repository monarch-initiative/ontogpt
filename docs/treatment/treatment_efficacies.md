# Slot: treatment_efficacies
_semicolon-separated list of treatment to efficacy associations, e.g. Imatinib*effective_


URI: [treatment:treatment_efficacies](http://w3id.org/ontogpt/treatments/treatment_efficacies)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[DiseaseTreatmentSummary](DiseaseTreatmentSummary.md) | 






## Properties

* Range: [TreatmentEfficacy](TreatmentEfficacy.md)
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
name: treatment_efficacies
annotations:
  prompt.separator:
    tag: prompt.separator
    value: '*'
description: semicolon-separated list of treatment to efficacy associations, e.g.
  Imatinib*effective
from_schema: http://w3id.org/ontogpt/treatment
rank: 1000
multivalued: true
alias: treatment_efficacies
owner: DiseaseTreatmentSummary
domain_of:
- DiseaseTreatmentSummary
range: TreatmentEfficacy

```
</details>