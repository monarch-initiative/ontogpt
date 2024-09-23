

# Slot: diseases


_A semicolon-separated list of diseases or conditions mentioned in the section. If no diseases are mentioned, return NOT FOUND._



URI: [alzrd:diseases](http://w3id.org/ontogpt/alzrd_sectiondiseases)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DocumentSection](DocumentSection.md) |  |  no  |







## Properties

* Range: [Disease](Disease.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd_section




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:diseases |
| native | alzrd:diseases |




## LinkML Source

<details>
```yaml
name: diseases
description: A semicolon-separated list of diseases or conditions mentioned in the
  section. If no diseases are mentioned, return NOT FOUND.
from_schema: http://w3id.org/ontogpt/alzrd_section
rank: 1000
alias: diseases
owner: DocumentSection
domain_of:
- DocumentSection
range: Disease
multivalued: true

```
</details>