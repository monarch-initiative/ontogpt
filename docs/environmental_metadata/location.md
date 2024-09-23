

# Slot: location


_the geographic location where the sample was isolated_



URI: [envmd:location](http://w3id.org/ontogpt/environmental-metadatalocation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) |  |  no  |







## Properties

* Range: [Location](Location.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of geographic locations of sample isolations |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-metadata




## LinkML Source

<details>
```yaml
name: location
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of geographic locations of sample isolations
description: the geographic location where the sample was isolated
from_schema: http://w3id.org/ontogpt/environmental-metadata
rank: 1000
multivalued: true
alias: location
owner: Dataset
domain_of:
- Dataset
range: Location

```
</details>