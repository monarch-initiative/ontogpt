# Slot: environments

URI: [eg:environments](http://w3id.org/ontogpt/environmental-metagenome/environments)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Study](Study.md) | 






## Properties

* Range: [Environment](Environment.md)
* Multivalued: True








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of environmental systems or biomes in which the study was conducted |



### Schema Source


* from schema: http://w3id.org/ontogpt/metagenome




## LinkML Source

<details>
```yaml
name: environments
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of environmental systems or biomes in which the
      study was conducted
from_schema: http://w3id.org/ontogpt/metagenome
rank: 1000
multivalued: true
alias: environments
owner: Study
domain_of:
- Study
range: Environment

```
</details>