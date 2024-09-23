

# Slot: label


_The label (name) of the named thing_



URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Disease](Disease.md) | A disposition to undergo pathological processes that exists in an organism be... |  no  |
| [Chemical](Chemical.md) | A substance that has a defined molecular structure and is produced by or used... |  no  |
| [MedicalAction](MedicalAction.md) | A clinically prescribed procedure, therapy, intervention, or recommendation |  no  |
| [Symptom](Symptom.md) | A condition or phenotype resulting from an abnormal health state |  no  |
| [RelationshipType](RelationshipType.md) |  |  no  |
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


* from schema: http://w3id.org/ontogpt/maxo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:label |
| native | maxo_extract:label |




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: http://w3id.org/ontogpt/maxo
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