

# Slot: modified_by


_agent that modified the element_



URI: [oslc:modifiedBy](oslc:modifiedBy)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DatasetCollection](DatasetCollection.md) | A collection of related datasets, likely containing multiple files of multipl... |  no  |
| [Information](Information.md) | Grouping for datasets and data files |  no  |
| [DataSubset](DataSubset.md) | A subset of a dataset, likely containing multiple files of multiple potential... |  no  |
| [Dataset](Dataset.md) | A single component of related observations and/or information that can be rea... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: modified_by
description: agent that modified the element
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
rank: 1000
slot_uri: oslc:modifiedBy
alias: modified_by
domain_of:
- Information
range: string

```
</details>