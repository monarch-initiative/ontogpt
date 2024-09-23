

# Slot: media_type


_The media type of the data. This is not the same as the format. Rather, this is the media type of the data in a more general sense, e.g., text/csv, application/json, etc., though as it is defined here the media type can be any string._



URI: [dcat:mediaType](http://www.w3.org/ns/dcat#mediaType)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataSubset](DataSubset.md) | A subset of a dataset, likely containing multiple files of multiple potential... |  no  |
| [Dataset](Dataset.md) | A single component of related observations and/or information that can be rea... |  no  |







## Properties

* Range: [String](String.md)






## Examples

| Value |
| --- |
| text/csv |
| application/json |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: media_type
description: The media type of the data. This is not the same as the format. Rather,
  this is the media type of the data in a more general sense, e.g., text/csv, application/json,
  etc., though as it is defined here the media type can be any string.
examples:
- value: text/csv
- value: application/json
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
exact_mappings:
- frictionless:mediatype
- schema:encodingFormat
rank: 1000
slot_uri: dcat:mediaType
alias: media_type
domain_of:
- Dataset
range: string

```
</details>