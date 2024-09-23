

# Slot: predicate

URI: [alzrd:predicate](http://w3id.org/ontogpt/alzrdpredicate)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalMetricToEnvironmentRelationship](ExperimentalMetricToEnvironmentRelationship.md) | A triple where the subject is an experimental metric, the object is an enviro... |  no  |
| [ExperimentalMetricToDiseaseRelationship](ExperimentalMetricToDiseaseRelationship.md) | A triple where the subject is an experimental metric, the object is a disease... |  no  |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |  no  |
| [ExperimentalMetricToChemicalRelationship](ExperimentalMetricToChemicalRelationship.md) | A triple where the subject is an experimental metric, the object is a chemica... |  no  |
| [ExperimentalMetricToTaxonRelationship](ExperimentalMetricToTaxonRelationship.md) | A triple where the subject is an experimental metric, the object is an taxon,... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:predicate |
| native | alzrd:predicate |




## LinkML Source

<details>
```yaml
name: predicate
alias: predicate
domain_of:
- ExperimentalMetricToTaxonRelationship
- ExperimentalMetricToDiseaseRelationship
- ExperimentalMetricToEnvironmentRelationship
- ExperimentalMetricToChemicalRelationship
- Triple
range: string

```
</details>