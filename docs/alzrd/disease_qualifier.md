

# Slot: disease_qualifier


_An optional qualifier or modifier for the disease or condition, as described in the input text. This may include the stage or subtype of the disease._



URI: [alzrd:disease_qualifier](http://w3id.org/ontogpt/alzrddisease_qualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalMetricToDiseaseRelationship](ExperimentalMetricToDiseaseRelationship.md) | A triple where the subject is an experimental metric, the object is a disease... |  no  |







## Properties

* Range: [NamedEntity](NamedEntity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:disease_qualifier |
| native | alzrd:disease_qualifier |




## LinkML Source

<details>
```yaml
name: disease_qualifier
description: An optional qualifier or modifier for the disease or condition, as described
  in the input text. This may include the stage or subtype of the disease.
from_schema: http://w3id.org/ontogpt/alzrd
rank: 1000
alias: disease_qualifier
owner: ExperimentalMetricToDiseaseRelationship
domain_of:
- ExperimentalMetricToDiseaseRelationship
range: NamedEntity

```
</details>