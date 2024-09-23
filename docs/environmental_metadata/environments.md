

# Slot: environments


_the environmental context in which the study was conducted_



URI: [envmd:environments](http://w3id.org/ontogpt/environmental-metadataenvironments)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) |  |  no  |







## Properties

* Range: [Environment](Environment.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of environmental contexts in which the study was conducted |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-metadata




## LinkML Source

<details>
```yaml
name: environments
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of environmental contexts in which the study was
      conducted
description: the environmental context in which the study was conducted
from_schema: http://w3id.org/ontogpt/environmental-metadata
rank: 1000
multivalued: true
alias: environments
owner: Dataset
domain_of:
- Dataset
range: Environment

```
</details>