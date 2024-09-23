

# Slot: treatment_mechanisms


_semicolon-separated list of treatment to asterisk-separated mechanism associations_



URI: [composite_disease:treatment_mechanisms](http://w3id.org/ontogpt/composite_disease/treatment_mechanisms)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CompositeDisease](CompositeDisease.md) |  |  no  |







## Properties

* Range: [TreatmentMechanism](TreatmentMechanism.md)

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
name: treatment_mechanisms
annotations:
  prompt.separator:
    tag: prompt.separator
    value: '*'
description: semicolon-separated list of treatment to asterisk-separated mechanism
  associations
from_schema: http://w3id.org/ontogpt/composite_disease
rank: 1000
multivalued: true
alias: treatment_mechanisms
owner: CompositeDisease
domain_of:
- CompositeDisease
range: TreatmentMechanism

```
</details>