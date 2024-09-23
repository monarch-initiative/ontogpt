

# Slot: label


_The label (name) of the named thing_



URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalObservations](ClinicalObservations.md) | A set of clinical observations about a single patient at a single time |  no  |
| [Disease](Disease.md) |  |  no  |
| [Drug](Drug.md) |  |  no  |
| [Unit](Unit.md) |  |  no  |
| [RelationshipType](RelationshipType.md) |  |  no  |
| [NutritionSupportMethod](NutritionSupportMethod.md) | A method of nutrition support therapy used to treat or prevent malnutrition |  no  |
| [NamedEntity](NamedEntity.md) |  |  no  |
| [TherapeuticMaterial](TherapeuticMaterial.md) | A specific material added to a patient's diet or included as part of a nutrit... |  no  |







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


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:label |
| native | dietitian_notes:label |




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: http://w3id.org/ontogpt/dietician_notes
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