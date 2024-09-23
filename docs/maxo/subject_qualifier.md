

# Slot: subject_qualifier


_An optional qualifier or modifier for the subject of the statement, e.g. "high dose" or "intravenously administered"_



URI: [maxo_extract:subject_qualifier](http://w3id.org/ontogpt/maxosubject_qualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ActionAnnotationRelationship](ActionAnnotationRelationship.md) | An association representing a relationships between a disease, the mentioned ... |  no  |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |  no  |
| [ExtendedTriple](ExtendedTriple.md) | Abstract parent for Relation Extraction tasks, with additional support for an... |  no  |







## Properties

* Range: [NamedEntity](NamedEntity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/maxo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | maxo_extract:subject_qualifier |
| native | maxo_extract:subject_qualifier |




## LinkML Source

<details>
```yaml
name: subject_qualifier
description: An optional qualifier or modifier for the subject of the statement, e.g.
  "high dose" or "intravenously administered"
from_schema: http://w3id.org/ontogpt/maxo
rank: 1000
alias: subject_qualifier
owner: Triple
domain_of:
- Triple
range: NamedEntity

```
</details>