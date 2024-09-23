

# Slot: object_qualifier


_An optional qualifier or modifier for the object of the statement, e.g. "severe" or "with additional complications"_



URI: [diag:object_qualifier](http://w3id.org/ontogpt/diagnostic_procedure/object_qualifier)



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
| self | diag:object_qualifier |
| native | diag:object_qualifier |




## LinkML Source

<details>
```yaml
name: object_qualifier
description: An optional qualifier or modifier for the object of the statement, e.g.
  "severe" or "with additional complications"
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
rank: 1000
alias: object_qualifier
owner: Triple
domain_of:
- Triple
range: NamedEntity

```
</details>