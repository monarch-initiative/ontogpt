

# Slot: qualifier


_A qualifier for the statements, e.g. "NOT" for negation_



URI: [maxo_extract:qualifier](http://w3id.org/ontogpt/maxoqualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ActionAnnotationRelationship](ActionAnnotationRelationship.md) | An association representing a relationships between a disease, the mentioned ... |  yes  |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |  no  |
| [ExtendedTriple](ExtendedTriple.md) | Abstract parent for Relation Extraction tasks, with additional support for an... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/maxo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | maxo_extract:qualifier |
| native | maxo_extract:qualifier |




## LinkML Source

<details>
```yaml
name: qualifier
description: A qualifier for the statements, e.g. "NOT" for negation
from_schema: http://w3id.org/ontogpt/maxo
rank: 1000
alias: qualifier
owner: Triple
domain_of:
- Triple
range: string

```
</details>