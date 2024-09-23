

# Slot: hash


_The hash representation of the data, e.g., sha256, md5, etc. Subtypes have their own slots._



URI: [data_sheets_schema:hash](https://w3id.org/bridge2ai/data-sheets-schema/hash)




## Inheritance

* **hash**
    * [sha256](sha256.md)
    * [md5](md5.md)






## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
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
name: hash
description: The hash representation of the data, e.g., sha256, md5, etc. Subtypes
  have their own slots.
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
rank: 1000
alias: hash
domain_of:
- Dataset
range: string

```
</details>