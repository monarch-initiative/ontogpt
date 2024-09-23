

# Slot: taxon


_A semicolon-separated list of taxa or species of organisms mentioned in the section. Where possible, translate to the binomial species name (e.g., change "mouse" to "Mus musculus"), unless a different species name is provided in the text. If no taxon is mentioned, return NOT FOUND._



URI: [alzrd:taxon](http://w3id.org/ontogpt/alzrd_sectiontaxon)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DocumentSection](DocumentSection.md) |  |  no  |







## Properties

* Range: [Taxon](Taxon.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd_section




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:taxon |
| native | alzrd:taxon |




## LinkML Source

<details>
```yaml
name: taxon
description: A semicolon-separated list of taxa or species of organisms mentioned
  in the section. Where possible, translate to the binomial species name (e.g., change
  "mouse" to "Mus musculus"), unless a different species name is provided in the text.
  If no taxon is mentioned, return NOT FOUND.
from_schema: http://w3id.org/ontogpt/alzrd_section
rank: 1000
alias: taxon
owner: DocumentSection
domain_of:
- DocumentSection
range: Taxon
multivalued: true

```
</details>