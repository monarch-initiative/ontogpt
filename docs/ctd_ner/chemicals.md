

# Slot: chemicals


_One or more chemical substances, drugs, or small molecules._



URI: [ctdner:chemicals](http://w3id.org/ontogpt/ctd_nerchemicals)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalToDiseaseDocument](ChemicalToDiseaseDocument.md) | A document that contains chemical and disease entities |  no  |







## Properties

* Range: [Chemical](Chemical.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | A semi-colon separated list of chemical names, for example: Lidocaine; Hydroxychloroquine; Methyldopa; Monosodium Glutamate; Imatinib |



### Schema Source


* from schema: http://w3id.org/ontogpt/ctd_ner




## LinkML Source

<details>
```yaml
name: chemicals
annotations:
  prompt:
    tag: prompt
    value: 'A semi-colon separated list of chemical names, for example: Lidocaine;
      Hydroxychloroquine; Methyldopa; Monosodium Glutamate; Imatinib'
description: One or more chemical substances, drugs, or small molecules.
from_schema: http://w3id.org/ontogpt/ctd_ner
rank: 1000
multivalued: true
alias: chemicals
owner: ChemicalToDiseaseDocument
domain_of:
- ChemicalToDiseaseDocument
range: Chemical

```
</details>