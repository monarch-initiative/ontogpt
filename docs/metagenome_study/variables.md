# Slot: variables

URI: [eg:variables](http://w3id.org/ontogpt/environmental-metagenome/variables)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Study](Study.md) | 






## Properties

* Range: [Variable](Variable.md)
* Multivalued: True








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of environmental variables which are studies. E.g. temperature, pH, salinity |



### Schema Source


* from schema: http://w3id.org/ontogpt/metagenome




## LinkML Source

<details>
```yaml
name: variables
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of environmental variables which are studies.
      E.g. temperature, pH, salinity
from_schema: http://w3id.org/ontogpt/metagenome
rank: 1000
multivalued: true
alias: variables
owner: Study
domain_of:
- Study
range: Variable

```
</details>