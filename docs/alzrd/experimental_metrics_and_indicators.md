

# Slot: experimental_metrics_and_indicators


_A semicolon-separated list of of experimental metrics, signs, symptoms, or outcomes used to measure the progression of Alzheimer's disease and related dementias, mentioned in the input text. These may be quantitative or qualitative measures, including biomolecular assays. In experimental animal models these are analogues of cognitive impairment or indicators of disease progression modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive decline. If no experimental metrics are mentioned, return NOT FOUND._



URI: [alzrd:experimental_metrics_and_indicators](http://w3id.org/ontogpt/alzrdexperimental_metrics_and_indicators)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) |  |  no  |







## Properties

* Range: [MetricOrIndicator](MetricOrIndicator.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:experimental_metrics_and_indicators |
| native | alzrd:experimental_metrics_and_indicators |




## LinkML Source

<details>
```yaml
name: experimental_metrics_and_indicators
description: A semicolon-separated list of of experimental metrics, signs, symptoms,
  or outcomes used to measure the progression of Alzheimer's disease and related dementias,
  mentioned in the input text. These may be quantitative or qualitative measures,
  including biomolecular assays. In experimental animal models these are analogues
  of cognitive impairment or indicators of disease progression modeling those observed
  in humans. Examples are Amyloid beta (Aβ) levels, Morris water maze test, tau phosphorylation,
  neurofibrillary tangles, and cognitive decline. If no experimental metrics are mentioned,
  return NOT FOUND.
from_schema: http://w3id.org/ontogpt/alzrd
rank: 1000
alias: experimental_metrics_and_indicators
owner: Document
domain_of:
- Document
range: MetricOrIndicator
multivalued: true

```
</details>