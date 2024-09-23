

# Slot: treatment_efficacies


_semicolon-separated list of treatment to efficacy associations, e.g. Imatinib*effective_



URI: [composite_disease:treatment_efficacies](http://w3id.org/ontogpt/composite_disease/treatment_efficacies)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CompositeDisease](CompositeDisease.md) |  |  no  |







## Properties

* Range: [TreatmentEfficacy](TreatmentEfficacy.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt.separator | * |



### Schema Source


* from schema: http://w3id.org/ontogpt/composite_disease




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
from_schema: http://w3id.org/ontogpt/composite_disease
rank: 1000
multivalued: true
alias: treatment_efficacies
owner: CompositeDisease
domain_of:
- CompositeDisease
range: TreatmentEfficacy

```
</details>