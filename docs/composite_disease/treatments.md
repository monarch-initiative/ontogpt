

# Slot: treatments


_semicolon-separated list of therapies and treatments are indicated for treating the disease._



URI: [composite_disease:treatments](http://w3id.org/ontogpt/composite_disease/treatments)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CompositeDisease](CompositeDisease.md) |  |  no  |







## Properties

* Range: [Treatment](Treatment.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt.examples | Imatinib, exercise, surgery |



### Schema Source


* from schema: http://w3id.org/ontogpt/composite_disease




## LinkML Source

<details>
```yaml
name: treatments
annotations:
  prompt.examples:
    tag: prompt.examples
    value: Imatinib, exercise, surgery
description: semicolon-separated list of therapies and treatments are indicated for
  treating the disease.
from_schema: http://w3id.org/ontogpt/composite_disease
rank: 1000
multivalued: true
alias: treatments
owner: CompositeDisease
domain_of:
- CompositeDisease
range: Treatment

```
</details>