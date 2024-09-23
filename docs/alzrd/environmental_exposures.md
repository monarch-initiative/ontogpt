

# Slot: environmental_exposures


_A semicolon-separated list of environmental exposures mentioned in the input text. These may include exposure to general classes of materials, e.g., "exposure to pesticides", or other phenomena, e.g., "chronic stress". If no environmental exposures are mentioned, return NOT FOUND._



URI: [alzrd:environmental_exposures](http://w3id.org/ontogpt/alzrdenvironmental_exposures)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) |  |  no  |







## Properties

* Range: [EnvironmentalExposure](EnvironmentalExposure.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:environmental_exposures |
| native | alzrd:environmental_exposures |




## LinkML Source

<details>
```yaml
name: environmental_exposures
description: A semicolon-separated list of environmental exposures mentioned in the
  input text. These may include exposure to general classes of materials, e.g., "exposure
  to pesticides", or other phenomena, e.g., "chronic stress". If no environmental
  exposures are mentioned, return NOT FOUND.
from_schema: http://w3id.org/ontogpt/alzrd
rank: 1000
alias: environmental_exposures
owner: Document
domain_of:
- Document
range: EnvironmentalExposure
multivalued: true

```
</details>