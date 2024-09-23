

# Slot: contraindications


_semicolon-separated list of therapies and treatments that are contra-indicated for the disease, and should not be used, due to risk of adverse effects._



URI: [treatment:contraindications](http://w3id.org/ontogpt/treatments/contraindications)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DiseaseTreatmentSummary](DiseaseTreatmentSummary.md) |  |  no  |







## Properties

* Range: [Treatment](Treatment.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt.examples | Beta-blockers, exercise, surgery |



### Schema Source


* from schema: http://w3id.org/ontogpt/treatment




## LinkML Source

<details>
```yaml
name: contraindications
annotations:
  prompt.examples:
    tag: prompt.examples
    value: Beta-blockers, exercise, surgery
description: semicolon-separated list of therapies and treatments that are contra-indicated
  for the disease, and should not be used, due to risk of adverse effects.
from_schema: http://w3id.org/ontogpt/treatment
rank: 1000
multivalued: true
alias: contraindications
owner: DiseaseTreatmentSummary
domain_of:
- DiseaseTreatmentSummary
range: Treatment

```
</details>