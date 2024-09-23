

# Slot: experimental_metric_to_disease_relationships


_Semicolon-separated list of relationships between a specific experimental metric, sign, symptom, or outcome and a disease or condition, as described in the input text. These are cases in which the relationship is used as an experimental model of progression or presence of a disease. For example, "Amyloid beta (Aβ) levels are used to model Alzheimer's disease" or "Morris water maze test is used to model Parkinson's disease".  Include all qualifiers, whether the relationship was direct or indirect, and any observed associations, including whether the association was positive, negative, or inconclusive._



URI: [alzrd:experimental_metric_to_disease_relationships](http://w3id.org/ontogpt/alzrdexperimental_metric_to_disease_relationships)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) |  |  no  |







## Properties

* Range: [ExperimentalMetricToDiseaseRelationship](ExperimentalMetricToDiseaseRelationship.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:experimental_metric_to_disease_relationships |
| native | alzrd:experimental_metric_to_disease_relationships |




## LinkML Source

<details>
```yaml
name: experimental_metric_to_disease_relationships
description: Semicolon-separated list of relationships between a specific experimental
  metric, sign, symptom, or outcome and a disease or condition, as described in the
  input text. These are cases in which the relationship is used as an experimental
  model of progression or presence of a disease. For example, "Amyloid beta (Aβ) levels
  are used to model Alzheimer's disease" or "Morris water maze test is used to model
  Parkinson's disease".  Include all qualifiers, whether the relationship was direct
  or indirect, and any observed associations, including whether the association was
  positive, negative, or inconclusive.
from_schema: http://w3id.org/ontogpt/alzrd
rank: 1000
alias: experimental_metric_to_disease_relationships
owner: Document
domain_of:
- Document
range: ExperimentalMetricToDiseaseRelationship
multivalued: true

```
</details>