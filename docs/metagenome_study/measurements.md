

# Slot: measurements

URI: [eg:measurements](http://w3id.org/ontogpt/environmental-metagenome/measurements)



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


* from schema: http://w3id.org/ontogpt/metagenome




## LinkML Source

<details>
```yaml
name: measurements
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of value-measurement pairs
from_schema: http://w3id.org/ontogpt/metagenome
rank: 1000
multivalued: true
alias: measurements
owner: Study
domain_of:
- Study
range: Measurement

```
</details>