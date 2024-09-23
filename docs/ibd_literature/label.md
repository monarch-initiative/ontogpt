

# Slot: label


_The label (name) of the named thing_



URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](Disease.md) |  |  no  |
| [NamedEntity](NamedEntity.md) |  |  no  |
| [RelationshipType](RelationshipType.md) |  |  no  |
| [Gene](Gene.md) |  |  no  |
| [ChemicalExposure](ChemicalExposure.md) |  |  no  |
| [CellularProcess](CellularProcess.md) |  |  no  |
| [DiseaseToCellularProcessPredicate](DiseaseToCellularProcessPredicate.md) |  |  no  |
| [ChemicalExposureToGenePredicate](ChemicalExposureToGenePredicate.md) |  |  no  |







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


* from schema: http://w3id.org/ontogpt/ibd_literature




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: http://w3id.org/ontogpt/ibd_literature
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