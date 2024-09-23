

# Slot: chemical_qualifier


_An optional qualifier or modifier for the chemical, drug, or other substance, as described in the input text. This may include the dose or route of administration._



URI: [alzrd:chemical_qualifier](http://w3id.org/ontogpt/alzrdchemical_qualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalMetricToChemicalRelationship](ExperimentalMetricToChemicalRelationship.md) | A triple where the subject is an experimental metric, the object is a chemica... |  no  |







## Properties

* Range: [NamedEntity](NamedEntity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:chemical_qualifier |
| native | alzrd:chemical_qualifier |




## LinkML Source

<details>
```yaml
name: chemical_qualifier
description: An optional qualifier or modifier for the chemical, drug, or other substance,
  as described in the input text. This may include the dose or route of administration.
from_schema: http://w3id.org/ontogpt/alzrd
rank: 1000
alias: chemical_qualifier
owner: ExperimentalMetricToChemicalRelationship
domain_of:
- ExperimentalMetricToChemicalRelationship
range: NamedEntity

```
</details>