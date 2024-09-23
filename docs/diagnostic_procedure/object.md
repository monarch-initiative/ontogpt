

# Slot: object

URI: [diag:object](http://w3id.org/ontogpt/diagnostic_procedure/object)



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
| self | diag:object |
| native | diag:object |




## LinkML Source

<details>
```yaml
name: object
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
rank: 1000
alias: object
owner: Triple
domain_of:
- Triple
range: NamedEntity

```
</details>