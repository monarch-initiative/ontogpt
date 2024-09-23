

# Slot: diagnostics


_A semicolon-separated list of diagnostic procedures mentioned in the input text. If no diagnostic procedures are mentioned, return NOT FOUND._



URI: [alzrd:diagnostics](http://w3id.org/ontogpt/alzrddiagnostics)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) |  |  no  |







## Properties

* Range: [Diagnostic](Diagnostic.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:diagnostics |
| native | alzrd:diagnostics |




## LinkML Source

<details>
```yaml
name: diagnostics
description: A semicolon-separated list of diagnostic procedures mentioned in the
  input text. If no diagnostic procedures are mentioned, return NOT FOUND.
from_schema: http://w3id.org/ontogpt/alzrd
rank: 1000
alias: diagnostics
owner: Document
domain_of:
- Document
range: Diagnostic
multivalued: true

```
</details>