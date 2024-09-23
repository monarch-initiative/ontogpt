

# Slot: wikidata_id


_Unique Wikidata identifier._



URI: [data_sheets_schema:wikidata_id](https://w3id.org/bridge2ai/data-sheets-schema/wikidata_id)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Organization](Organization.md) | A collection of people acting in common interests |  no  |
| [Grantor](Grantor.md) | What is the name and/or identifier of the organization providing monetary sup... |  no  |







## Properties

* Range: [WikidataIdentifier](WikidataIdentifier.md)






## Examples

| Value |
| --- |
| WIKIDATA:Q282186 |

## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema




## LinkML Source

<details>
```yaml
name: wikidata_id
description: Unique Wikidata identifier.
examples:
- value: WIKIDATA:Q282186
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
rank: 1000
values_from:
- WIKIDATA
alias: wikidata_id
owner: Organization
domain_of:
- Organization
range: wikidata_identifier

```
</details>