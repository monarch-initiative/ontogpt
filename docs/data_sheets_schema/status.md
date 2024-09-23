

# Slot: status


_Status of the element in terms of its maturity or life cycle_



URI: [bibo:status](bibo:status)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DatasetCollection](DatasetCollection.md) | A collection of related datasets, likely containing multiple files of multipl... |  no  |
| [Information](Information.md) | Grouping for datasets and data files |  no  |
| [DataSubset](DataSubset.md) | A subset of a dataset, likely containing multiple files of multiple potential... |  no  |
| [Dataset](Dataset.md) | A single component of related observations and/or information that can be rea... |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)






## Examples

| Value |
| --- |
| bibo:draft |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: status
description: Status of the element in terms of its maturity or life cycle
examples:
- value: bibo:draft
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
rank: 1000
slot_uri: bibo:status
alias: status
domain_of:
- Information
range: uriorcurie

```
</details>