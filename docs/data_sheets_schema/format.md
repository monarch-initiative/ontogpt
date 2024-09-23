

# Slot: format


_The format of the data. This is not the same as the media type. Rather, this is the format of the data in a more specific sense, e.g., CSV, JSON, etc._



URI: [dcterms:format](dcterms:format)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSubset](DataSubset.md) | A subset of a dataset, likely containing multiple files of multiple potential... |  no  |
| [Dataset](Dataset.md) | A single component of related observations and/or information that can be rea... |  no  |







## Properties

* Range: [FormatEnum](FormatEnum.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: format
description: The format of the data. This is not the same as the media type. Rather,
  this is the format of the data in a more specific sense, e.g., CSV, JSON, etc.
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
rank: 1000
slot_uri: dcterms:format
alias: format
domain_of:
- Dataset
range: FormatEnum

```
</details>