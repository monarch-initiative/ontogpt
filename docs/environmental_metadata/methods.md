

# Slot: methods

URI: [envmd:methods](http://w3id.org/ontogpt/environmental-metadatamethods)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) |  |  no  |







## Properties

* Range: [Method](Method.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of methods used in measuring sample variables |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-metadata




## LinkML Source

<details>
```yaml
name: methods
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of methods used in measuring sample variables
from_schema: http://w3id.org/ontogpt/environmental-metadata
rank: 1000
multivalued: true
alias: methods
owner: Dataset
domain_of:
- Dataset
range: Method

```
</details>