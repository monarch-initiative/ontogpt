

# Slot: subject_qualifier


_An optional qualifier or modifier for the subject of the statement, e.g. "high dose" or "intravenously administered"_



URI: [drug:subject_qualifier](http://w3id.org/ontogpt/drug/subject_qualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |  no  |
| [ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md) | A triple where the subject is a chemical and the object is a disease |  yes  |







## Properties

* Range: [NamedEntity](NamedEntity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/ctd




## LinkML Source

<details>
```yaml
name: subject_qualifier
description: An optional qualifier or modifier for the subject of the statement, e.g.
  "high dose" or "intravenously administered"
from_schema: http://w3id.org/ontogpt/ctd
rank: 1000
alias: subject_qualifier
owner: Triple
domain_of:
- Triple
range: NamedEntity

```
</details>