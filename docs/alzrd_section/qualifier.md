

# Slot: qualifier


_A qualifier for the statements, e.g. "NOT" for negation_



URI: [alzrd:qualifier](http://w3id.org/ontogpt/alzrd_sectionqualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalMetricToDiseaseRelationship](ExperimentalMetricToDiseaseRelationship.md) | A triple where the subject is an experimental metric, the object is a disease... |  no  |
| [ExperimentalMetricToTaxonRelationship](ExperimentalMetricToTaxonRelationship.md) | A triple where the subject is an experimental metric, the object is an taxon,... |  no  |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd_section




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:qualifier |
| native | alzrd:qualifier |




## LinkML Source

<details>
```yaml
name: qualifier
description: A qualifier for the statements, e.g. "NOT" for negation
from_schema: http://w3id.org/ontogpt/alzrd_section
rank: 1000
alias: qualifier
owner: Triple
domain_of:
- Triple
range: string

```
</details>