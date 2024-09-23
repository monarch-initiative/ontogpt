

# Slot: object_qualifier


_An optional qualifier or modifier for the object of the statement, e.g. "severe" or "with additional complications"_



URI: [maxo_extract:object_qualifier](http://w3id.org/ontogpt/maxoobject_qualifier)



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
| self | maxo_extract:object_qualifier |
| native | maxo_extract:object_qualifier |




## LinkML Source

<details>
```yaml
name: object_qualifier
description: An optional qualifier or modifier for the object of the statement, e.g.
  "severe" or "with additional complications"
from_schema: http://w3id.org/ontogpt/maxo
rank: 1000
alias: object_qualifier
owner: Triple
domain_of:
- Triple
range: NamedEntity

```
</details>