

# Slot: treatment_adverse_effects


_semicolon-separated list of treatment to adverse effect associations, e.g. Imatinib*nausea_



URI: [composite_disease:treatment_adverse_effects](http://w3id.org/ontogpt/composite_disease/treatment_adverse_effects)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CompositeDisease](CompositeDisease.md) |  |  no  |







## Properties

* Range: [TreatmentAdverseEffect](TreatmentAdverseEffect.md)

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
name: treatment_adverse_effects
annotations:
  prompt.separator:
    tag: prompt.separator
    value: '*'
description: semicolon-separated list of treatment to adverse effect associations,
  e.g. Imatinib*nausea
from_schema: http://w3id.org/ontogpt/composite_disease
rank: 1000
multivalued: true
alias: treatment_adverse_effects
owner: CompositeDisease
domain_of:
- CompositeDisease
range: TreatmentAdverseEffect

```
</details>