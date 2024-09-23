

# Slot: label


_The label (name) of the named thing_



URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RelationshipType](RelationshipType.md) |  |  no  |
| [Taxon](Taxon.md) |  |  no  |
| [InteractionType](InteractionType.md) |  |  no  |
| [NamedEntity](NamedEntity.md) |  |  no  |







## Properties

* Range: [String](String.md)



## Aliases


* name



## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| owl | AnnotationProperty, AnnotationAssertion |



### Schema Source


* from schema: https://w3id.org/ontogpt/biotic_interaction




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:label |
| native | bp:label |




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: https://w3id.org/ontogpt/biotic_interaction
aliases:
- name
rank: 1000
slot_uri: rdfs:label
alias: label
owner: NamedEntity
domain_of:
- NamedEntity
range: string

```
</details>