

# Slot: entities

URI: [ctdner:entities](http://w3id.org/ontogpt/ctd_nerentities)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextWithEntity](TextWithEntity.md) | A text containing one or more instances of a single type of entity |  no  |
| [ChemicalToDiseaseDocument](ChemicalToDiseaseDocument.md) | A document that contains chemical and disease entities |  no  |







## Properties

* Range: [NamedEntity](NamedEntity.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/ctd_ner




## LinkML Source

<details>
```yaml
name: entities
from_schema: http://w3id.org/ontogpt/ctd_ner
rank: 1000
multivalued: true
alias: entities
owner: TextWithEntity
domain_of:
- TextWithEntity
range: NamedEntity

```
</details>