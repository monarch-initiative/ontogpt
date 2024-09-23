

# Slot: measurements

URI: [sample:measurements](http://w3id.org/ontogpt/environmental-sample/measurements)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) |  |  no  |







## Properties

* Range: [Measurement](Measurement.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of value-measurement pairs |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sample:measurements |
| native | sample:measurements |




## LinkML Source

<details>
```yaml
name: measurements
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of value-measurement pairs
from_schema: http://w3id.org/ontogpt/environmental-sample
rank: 1000
alias: measurements
owner: Study
domain_of:
- Study
range: Measurement
multivalued: true

```
</details>