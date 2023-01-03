# Slot: disease_onsets

URI: [mendelian_disease:disease_onsets](http://w3id.org/ontogpt/mendelian_disease/disease_onsets)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[MendelianDisease](MendelianDisease.md) | 






## Properties

* Range: [Onset](Onset.md)
* Multivalued: True








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semi-colon separated list of onsets at which the disease occurs, for example: adult; juvenile; first decade |



### Schema Source


* from schema: http://w3id.org/ontogpt/mendelian_disease




## LinkML Source

<details>
```yaml
name: disease_onsets
annotations:
  prompt:
    tag: prompt
    value: 'semi-colon separated list of onsets at which the disease occurs, for example:
      adult; juvenile; first decade'
from_schema: http://w3id.org/ontogpt/mendelian_disease
rank: 1000
multivalued: true
alias: disease_onsets
owner: MendelianDisease
domain_of:
- MendelianDisease
range: Onset

```
</details>