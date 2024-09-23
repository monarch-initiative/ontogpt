

# Slot: diseases


_A semicolon-separated list of diseases or conditions mentioned in the input text. If no diseases are mentioned, return NOT FOUND._



URI: [alzrd:diseases](http://w3id.org/ontogpt/alzrddiseases)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) |  |  no  |







## Properties

* Range: [Disease](Disease.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




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
  input text. If no diseases are mentioned, return NOT FOUND.
from_schema: http://w3id.org/ontogpt/alzrd
rank: 1000
alias: diseases
owner: Document
domain_of:
- Document
range: Disease
multivalued: true

```
</details>