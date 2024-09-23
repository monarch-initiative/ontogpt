

# Slot: label


_The label (name) of the named thing_



URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](Disease.md) |  |  no  |
| [Taxon](Taxon.md) |  |  no  |
| [NamedEntity](NamedEntity.md) |  |  no  |
| [Document](Document.md) |  |  no  |
| [Chemical](Chemical.md) |  |  no  |
| [Diagnostic](Diagnostic.md) |  |  no  |
| [MetricOrIndicator](MetricOrIndicator.md) |  |  no  |
| [EnvironmentalExposure](EnvironmentalExposure.md) |  |  no  |
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


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:label |
| native | alzrd:label |




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: http://w3id.org/ontogpt/alzrd
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