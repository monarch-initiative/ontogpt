

# Slot: topic


_the general scientific area of study concerning the sample(s)_



URI: [envmd:topic](http://w3id.org/ontogpt/environmental-metadatatopic)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) |  |  no  |







## Properties

* Range: [Topic](Topic.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of scientific areas of study concerning the sample(s) |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-metadata




## LinkML Source

<details>
```yaml
name: topic
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of scientific areas of study concerning the sample(s)
description: the general scientific area of study concerning the sample(s)
from_schema: http://w3id.org/ontogpt/environmental-metadata
rank: 1000
multivalued: true
alias: topic
owner: Dataset
domain_of:
- Dataset
range: Topic

```
</details>