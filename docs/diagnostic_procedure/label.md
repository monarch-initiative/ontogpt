

# Slot: label


_The label (name) of the named thing_



URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RelationshipType](RelationshipType.md) |  |  no  |
| [Phenotype](Phenotype.md) |  |  no  |
| [Unit](Unit.md) |  |  no  |
| [ClinicalAttribute](ClinicalAttribute.md) |  |  no  |
| [Quality](Quality.md) |  |  no  |
| [ProcedureToAttributePredicate](ProcedureToAttributePredicate.md) | A predicate for procedure to attribute relationships, defining "this procedur... |  no  |
| [NamedEntity](NamedEntity.md) |  |  no  |
| [ProcedureToPhenotypePredicate](ProcedureToPhenotypePredicate.md) | A predicate for procedure to phenotype relationships, defining "this procedur... |  no  |
| [DiagnosticProcedure](DiagnosticProcedure.md) |  |  no  |







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


* from schema: http://w3id.org/ontogpt/diagnostic_procedure




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:label |
| native | diag:label |




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
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