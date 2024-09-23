

# Slot: treatments

URI: [eg:treatments](http://w3id.org/ontogpt/environmental-metagenome/treatments)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) |  |  no  |







## Properties

* Range: [Treatment](Treatment.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of treatments that are applied |



### Schema Source


* from schema: http://w3id.org/ontogpt/metagenome




## LinkML Source

<details>
```yaml
name: treatments
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of treatments that are applied
from_schema: http://w3id.org/ontogpt/metagenome
rank: 1000
multivalued: true
alias: treatments
owner: Study
domain_of:
- Study
range: Treatment

```
</details>