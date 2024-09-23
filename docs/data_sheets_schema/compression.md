

# Slot: compression


_The compression format of the data. This is not the same as the media type. Rather, this is the compression format of the data in a more specific sense, e.g., zip, gzip, etc._



URI: [data_sheets_schema:compression](https://w3id.org/bridge2ai/data-sheets-schema/compression)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DatasetCollection](DatasetCollection.md) | A collection of related datasets, likely containing multiple files of multipl... |  no  |
| [Information](Information.md) | Grouping for datasets and data files |  no  |
| [DataSubset](DataSubset.md) | A subset of a dataset, likely containing multiple files of multiple potential... |  no  |
| [Dataset](Dataset.md) | A single component of related observations and/or information that can be rea... |  no  |







## Properties

* Range: [CompressionEnum](CompressionEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: compression
description: The compression format of the data. This is not the same as the media
  type. Rather, this is the compression format of the data in a more specific sense,
  e.g., zip, gzip, etc.
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
rank: 1000
alias: compression
domain_of:
- Information
range: CompressionEnum

```
</details>