# Slot: label
_The label (name) of the named thing_


URI: [rdfs:label](rdfs:label)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
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


* from schema: https://w3id.org/ontogpt/halo




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: https://w3id.org/ontogpt/halo
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