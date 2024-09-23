

# Slot: subsets

URI: [dcat:distribution](http://www.w3.org/ns/dcat#distribution)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSubset](DataSubset.md) | A subset of a dataset, likely containing multiple files of multiple potential... |  no  |
| [Dataset](Dataset.md) | A single component of related observations and/or information that can be rea... |  no  |







## Properties

* Range: [DataSubset](DataSubset.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: subsets
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
exact_mappings:
- schema:distribution
rank: 1000
slot_uri: dcat:distribution
multivalued: true
alias: subsets
owner: Dataset
domain_of:
- Dataset
range: DataSubset

```
</details>