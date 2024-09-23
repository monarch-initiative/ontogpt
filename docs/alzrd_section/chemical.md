

# Slot: chemical


_A semicolon-separated list of chemicals, drugs, or other substances mentioned in the section. If no chemicals are mentioned, return NOT FOUND._



URI: [alzrd:chemical](http://w3id.org/ontogpt/alzrd_sectionchemical)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DocumentSection](DocumentSection.md) |  |  no  |







## Properties

* Range: [Chemical](Chemical.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd_section




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:chemical |
| native | alzrd:chemical |




## LinkML Source

<details>
```yaml
name: chemical
description: A semicolon-separated list of chemicals, drugs, or other substances mentioned
  in the section. If no chemicals are mentioned, return NOT FOUND.
from_schema: http://w3id.org/ontogpt/alzrd_section
rank: 1000
alias: chemical
owner: DocumentSection
domain_of:
- DocumentSection
range: Chemical
multivalued: true

```
</details>