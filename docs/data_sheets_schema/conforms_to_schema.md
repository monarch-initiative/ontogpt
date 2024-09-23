

# Slot: conforms_to_schema


_The schema to which the data conforms. This is not the same as the media type. Rather, this is the schema to which the data conforms in a more specific sense, and even more specific than the general set of standards it conforms to._



URI: [data_sheets_schema:conforms_to_schema](https://w3id.org/bridge2ai/data-sheets-schema/conforms_to_schema)




## Inheritance

* [conforms_to](conforms_to.md)
    * **conforms_to_schema**






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DatasetCollection](DatasetCollection.md) | A collection of related datasets, likely containing multiple files of multipl... |  no  |
| [Information](Information.md) | Grouping for datasets and data files |  no  |
| [DataSubset](DataSubset.md) | A subset of a dataset, likely containing multiple files of multiple potential... |  no  |
| [Dataset](Dataset.md) | A single component of related observations and/or information that can be rea... |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: conforms_to_schema
description: The schema to which the data conforms. This is not the same as the media
  type. Rather, this is the schema to which the data conforms in a more specific sense,
  and even more specific than the general set of standards it conforms to.
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
exact_mappings:
- frictionless:schema
rank: 1000
is_a: conforms_to
alias: conforms_to_schema
domain_of:
- Information
range: uriorcurie

```
</details>