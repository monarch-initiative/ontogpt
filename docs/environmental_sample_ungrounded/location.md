

# Slot: location


_the sites at which the study was conducted_



URI: [sample:location](http://w3id.org/ontogpt/environmental-sample-ungrounded/location)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) |  |  no  |







## Properties

* Range: [Location](Location.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of sites at which the study was conducted. Give specific place names. if you cannot find a specific place name leave the field as empty. |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample-ungrounded




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sample:location |
| native | sample:location |




## LinkML Source

<details>
```yaml
name: location
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of sites at which the study was conducted. Give
      specific place names. if you cannot find a specific place name leave the field
      as empty.
description: the sites at which the study was conducted
from_schema: http://w3id.org/ontogpt/environmental-sample-ungrounded
rank: 1000
alias: location
owner: Study
domain_of:
- Study
range: Location
multivalued: true

```
</details>