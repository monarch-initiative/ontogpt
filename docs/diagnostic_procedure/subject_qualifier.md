

# Slot: subject_qualifier


_An optional qualifier or modifier for the subject of the statement, e.g. "high dose" or "intravenously administered"_



URI: [diag:subject_qualifier](http://w3id.org/ontogpt/diagnostic_procedure/subject_qualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |  no  |
| [DiagnosticProceduretoAttributeAssociation](DiagnosticProceduretoAttributeAssociation.md) | A triple representing a relationship between a diagnostic procedure and a mea... |  yes  |
| [DiagnosticProceduretoPhenotypeAssociation](DiagnosticProceduretoPhenotypeAssociation.md) | A triple representing a relationship between a diagnostic procedure and an as... |  yes  |







## Properties

* Range: [NamedEntity](NamedEntity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/diagnostic_procedure




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | diag:subject_qualifier |
| native | diag:subject_qualifier |




## LinkML Source

<details>
```yaml
name: subject_qualifier
description: An optional qualifier or modifier for the subject of the statement, e.g.
  "high dose" or "intravenously administered"
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
rank: 1000
alias: subject_qualifier
owner: Triple
domain_of:
- Triple
range: NamedEntity

```
</details>