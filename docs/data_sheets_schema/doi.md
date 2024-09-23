

# Slot: doi


_The Digital Object Identifier of the data, with the doi prefix._



URI: [data_sheets_schema:doi](https://w3id.org/bridge2ai/data-sheets-schema/doi)



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
| doi:10.48550/arXiv.2310.03666 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: doi
description: The Digital Object Identifier of the data, with the doi prefix.
examples:
- value: doi:10.48550/arXiv.2310.03666
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
rank: 1000
alias: doi
domain_of:
- Information
range: uriorcurie

```
</details>