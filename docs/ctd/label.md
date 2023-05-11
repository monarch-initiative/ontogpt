# Slot: label
_The label (name) of the named thing_


URI: [rdfs:label](rdfs:label)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Disease](Disease.md) | 
[Chemical](Chemical.md) | 
[ChemicalToDiseasePredicate](ChemicalToDiseasePredicate.md) | A predicate for chemical to disease relationships
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


* from schema: http://w3id.org/ontogpt/ctd




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: http://w3id.org/ontogpt/ctd
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