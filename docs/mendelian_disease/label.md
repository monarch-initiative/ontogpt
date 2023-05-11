# Slot: label
_The label (name) of the named thing_


URI: [rdfs:label](rdfs:label)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[MendelianDisease](MendelianDisease.md) | 
[DiseaseCategory](DiseaseCategory.md) | 
[Gene](Gene.md) | 
[Symptom](Symptom.md) | 
[Onset](Onset.md) | 
[Inheritance](Inheritance.md) | 
[NamedEntity](NamedEntity.md) | 
[RelationshipType](RelationshipType.md) | 






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