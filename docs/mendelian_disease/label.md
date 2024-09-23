

# Slot: label


_The label (name) of the named thing_



URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Inheritance](Inheritance.md) |  |  no  |
| [Gene](Gene.md) |  |  no  |
| [Symptom](Symptom.md) |  |  no  |
| [RelationshipType](RelationshipType.md) |  |  no  |
| [Onset](Onset.md) |  |  no  |
| [DiseaseCategory](DiseaseCategory.md) |  |  no  |
| [NamedEntity](NamedEntity.md) |  |  no  |
| [MendelianDisease](MendelianDisease.md) |  |  no  |







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


* from schema: http://w3id.org/ontogpt/mendelian_disease




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:label |
| native | mendelian_disease:label |




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: http://w3id.org/ontogpt/mendelian_disease
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