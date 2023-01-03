# Slot: measurements

URI: [sample:measurements](http://w3id.org/ontogpt/environmental-sample/measurements)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Study](Study.md) | 






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
multivalued: true
alias: measurements
owner: Study
domain_of:
- Study
range: Measurement

```
</details>