

# Slot: subject

URI: [alzrd:subject](http://w3id.org/ontogpt/alzrd_sectionsubject)



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
| self | alzrd:subject |
| native | alzrd:subject |




## LinkML Source

<details>
```yaml
name: subject
from_schema: http://w3id.org/ontogpt/alzrd_section
rank: 1000
alias: subject
owner: Triple
domain_of:
- Triple
range: NamedEntity

```
</details>