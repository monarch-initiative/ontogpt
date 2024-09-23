

# Slot: label


_The label (name) of the named thing_



URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnvironmentalCondition](EnvironmentalCondition.md) |  |  no  |
| [Taxon](Taxon.md) |  |  no  |
| [Trait](Trait.md) |  |  no  |
| [EntityContainingDocument](EntityContainingDocument.md) |  |  no  |
| [NamedEntity](NamedEntity.md) |  |  no  |
| [RelationshipType](RelationshipType.md) |  |  no  |







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


* from schema: http://w3id.org/ontogpt/desiccation




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: http://w3id.org/ontogpt/desiccation
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