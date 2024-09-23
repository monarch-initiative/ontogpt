

# Slot: conforms_to


_The standard to which the data conforms. This is not the same as the media type. Rather, this is the standard to which the data conforms in a more specific sense, e.g., frictionless, schema.org, etc._



URI: [dcterms:conformsTo](dcterms:conformsTo)




## Inheritance

* **conforms_to**
    * [conforms_to_schema](conforms_to_schema.md)
    * [conforms_to_class](conforms_to_class.md)






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
name: conforms_to
description: The standard to which the data conforms. This is not the same as the
  media type. Rather, this is the standard to which the data conforms in a more specific
  sense, e.g., frictionless, schema.org, etc.
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
rank: 1000
slot_uri: dcterms:conformsTo
alias: conforms_to
domain_of:
- Information
range: uriorcurie

```
</details>