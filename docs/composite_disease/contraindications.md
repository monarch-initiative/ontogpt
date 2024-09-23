

# Slot: contraindications


_semicolon-separated list of therapies and treatments that are contra-indicated for the disease, and should not be used, due to risk of adverse effects._



URI: [composite_disease:contraindications](http://w3id.org/ontogpt/composite_disease/contraindications)



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
| prompt.examples | Beta-blockers, exercise, surgery |



### Schema Source


* from schema: http://w3id.org/ontogpt/composite_disease




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
from_schema: http://w3id.org/ontogpt/composite_disease
rank: 1000
multivalued: true
alias: contraindications
owner: CompositeDisease
domain_of:
- CompositeDisease
range: Treatment

```
</details>