

# Slot: metric_qualifier

URI: [alzrd:metric_qualifier](http://w3id.org/ontogpt/alzrdmetric_qualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalMetricToDiseaseRelationship](ExperimentalMetricToDiseaseRelationship.md) | A triple where the subject is an experimental metric, the object is a disease... |  no  |
| [ExperimentalMetricToEnvironmentRelationship](ExperimentalMetricToEnvironmentRelationship.md) | A triple where the subject is an experimental metric, the object is an enviro... |  no  |
| [ExperimentalMetricToChemicalRelationship](ExperimentalMetricToChemicalRelationship.md) | A triple where the subject is an experimental metric, the object is a chemica... |  no  |
| [ExperimentalMetricToTaxonRelationship](ExperimentalMetricToTaxonRelationship.md) | A triple where the subject is an experimental metric, the object is an taxon,... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information








## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:metric_qualifier |
| native | alzrd:metric_qualifier |




## LinkML Source

<details>
```yaml
name: metric_qualifier
alias: metric_qualifier
domain_of:
- ExperimentalMetricToTaxonRelationship
- ExperimentalMetricToDiseaseRelationship
- ExperimentalMetricToEnvironmentRelationship
- ExperimentalMetricToChemicalRelationship
range: string

```
</details>