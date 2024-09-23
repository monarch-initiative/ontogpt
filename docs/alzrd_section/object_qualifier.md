

# Slot: object_qualifier


_An optional qualifier or modifier for the object of the statement, e.g. "severe" or "with additional complications"_



URI: [alzrd:object_qualifier](http://w3id.org/ontogpt/alzrd_sectionobject_qualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalMetricToDiseaseRelationship](ExperimentalMetricToDiseaseRelationship.md) | A triple where the subject is an experimental metric, the object is a disease... |  yes  |
| [ExperimentalMetricToTaxonRelationship](ExperimentalMetricToTaxonRelationship.md) | A triple where the subject is an experimental metric, the object is an taxon,... |  yes  |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |  no  |







## Properties

* Range: [NamedEntity](NamedEntity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd_section




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:object_qualifier |
| native | alzrd:object_qualifier |




## LinkML Source

<details>
```yaml
name: object_qualifier
description: An optional qualifier or modifier for the object of the statement, e.g.
  "severe" or "with additional complications"
from_schema: http://w3id.org/ontogpt/alzrd_section
rank: 1000
alias: object_qualifier
owner: Triple
domain_of:
- Triple
range: NamedEntity

```
</details>