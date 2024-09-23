

# Slot: taxa


_A semicolon-separated list of taxa or species of organisms mentioned in the input text. Where possible, translate to the binomial species name (e.g., change "mouse" to "Mus musculus"), unless a different species name is provided in the text. If no taxon is mentioned, return NOT FOUND._



URI: [alzrd:taxa](http://w3id.org/ontogpt/alzrdtaxa)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) |  |  no  |







## Properties

* Range: [Taxon](Taxon.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:taxa |
| native | alzrd:taxa |




## LinkML Source

<details>
```yaml
name: taxa
description: A semicolon-separated list of taxa or species of organisms mentioned
  in the input text. Where possible, translate to the binomial species name (e.g.,
  change "mouse" to "Mus musculus"), unless a different species name is provided in
  the text. If no taxon is mentioned, return NOT FOUND.
from_schema: http://w3id.org/ontogpt/alzrd
rank: 1000
alias: taxa
owner: Document
domain_of:
- Document
range: Taxon
multivalued: true

```
</details>