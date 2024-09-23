

# Slot: diseases


_One or more diseases or conditions._



URI: [ctdner:diseases](http://w3id.org/ontogpt/ctd_nerdiseases)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalToDiseaseDocument](ChemicalToDiseaseDocument.md) | A document that contains chemical and disease entities |  no  |







## Properties

* Range: [Disease](Disease.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | A semi-colon separated list of disease names, for example: cardiac asystole; COVID-19; Hypotension; Headache; cancer |



### Schema Source


* from schema: http://w3id.org/ontogpt/ctd_ner




## LinkML Source

<details>
```yaml
name: diseases
annotations:
  prompt:
    tag: prompt
    value: 'A semi-colon separated list of disease names, for example: cardiac asystole;
      COVID-19; Hypotension; Headache; cancer'
description: One or more diseases or conditions.
from_schema: http://w3id.org/ontogpt/ctd_ner
rank: 1000
multivalued: true
alias: diseases
owner: ChemicalToDiseaseDocument
domain_of:
- ChemicalToDiseaseDocument
range: Disease

```
</details>