

# Slot: was_derived_from


_A derivation is a transformation of an entity into another, an update of an entity resulting in a new one, or the construction of a new entity based on a pre-existing entity.@en_



URI: [prov:wasDerivedFrom](prov:wasDerivedFrom)



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
name: was_derived_from
description: A derivation is a transformation of an entity into another, an update
  of an entity resulting in a new one, or the construction of a new entity based on
  a pre-existing entity.@en
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
rank: 1000
slot_uri: prov:wasDerivedFrom
alias: was_derived_from
domain_of:
- Information
range: string

```
</details>