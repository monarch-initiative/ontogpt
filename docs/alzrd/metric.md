

# Slot: metric

URI: [alzrd:metric](http://w3id.org/ontogpt/alzrdmetric)



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
| self | alzrd:metric |
| native | alzrd:metric |




## LinkML Source

<details>
```yaml
name: metric
alias: metric
domain_of:
- ExperimentalMetricToTaxonRelationship
- ExperimentalMetricToDiseaseRelationship
- ExperimentalMetricToEnvironmentRelationship
- ExperimentalMetricToChemicalRelationship
range: string

```
</details>