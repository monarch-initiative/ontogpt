

# Slot: diagnostics


_A semicolon-separated list of diagnostic procedures mentioned in the section. If no diagnostic procedures are mentioned, return NOT FOUND._



URI: [alzrd:diagnostics](http://w3id.org/ontogpt/alzrd_sectiondiagnostics)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DocumentSection](DocumentSection.md) |  |  no  |







## Properties

* Range: [Diagnostic](Diagnostic.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd_section




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
  section. If no diagnostic procedures are mentioned, return NOT FOUND.
from_schema: http://w3id.org/ontogpt/alzrd_section
rank: 1000
alias: diagnostics
owner: DocumentSection
domain_of:
- DocumentSection
range: Diagnostic
multivalued: true

```
</details>