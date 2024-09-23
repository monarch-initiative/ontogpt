

# Slot: keywords


_Keywords associated with the data. These may be provided by the data creator or assigned later in a manual or automated manner._



URI: [dcat:keyword](http://www.w3.org/ns/dcat#keyword)



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

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: keywords
description: Keywords associated with the data. These may be provided by the data
  creator or assigned later in a manual or automated manner.
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
exact_mappings:
- schema:keywords
rank: 1000
singular_name: keyword
slot_uri: dcat:keyword
multivalued: true
alias: keywords
domain_of:
- Information
range: string

```
</details>