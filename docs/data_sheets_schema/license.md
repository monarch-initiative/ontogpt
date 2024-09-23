

# Slot: license


_license for the data_



URI: [dcterms:license](dcterms:license)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | A single component of related observations and/or information that can be rea... |  no  |
| [Information](Information.md) | Grouping for datasets and data files |  no  |
| [Software](Software.md) | A software program or library |  no  |
| [DataSubset](DataSubset.md) | A subset of a dataset, likely containing multiple files of multiple potential... |  no  |
| [DatasetCollection](DatasetCollection.md) | A collection of related datasets, likely containing multiple files of multipl... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: license
description: license for the data
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
exact_mappings:
- frictionless:licenses
rank: 1000
slot_uri: dcterms:license
alias: license
domain_of:
- Information
- Software
range: string

```
</details>