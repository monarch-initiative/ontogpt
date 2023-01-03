# Slot: location
_the sites at which the study was conducted_


URI: [sample:location](http://w3id.org/ontogpt/environmental-sample/location)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Study](Study.md) | 






## Properties

* Range: [Location](Location.md)
* Multivalued: True








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of sites at which the study was conducted |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample




## LinkML Source

<details>
```yaml
name: location
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of sites at which the study was conducted
description: the sites at which the study was conducted
from_schema: http://w3id.org/ontogpt/environmental-sample
rank: 1000
multivalued: true
alias: location
owner: Study
domain_of:
- Study
range: Location

```
</details>