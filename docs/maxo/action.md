# Slot: action


_Semicolon-separated list of medical actions._



URI: [maxo_extract:action](http://w3id.org/ontogpt/maxoaction)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
[MaxoAnnotations](MaxoAnnotations.md) |  |  no  |







## Properties

* Range: [Action](Action.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | Semicolon-separated list of medical actions, where each is a clinically prescribed procedure, therapy, intervention, or recommendation. |



### Schema Source


* from schema: http://w3id.org/ontogpt/maxo




## LinkML Source

<details>
```yaml
name: action
annotations:
  prompt:
    tag: prompt
    value: Semicolon-separated list of medical actions, where each is a clinically
      prescribed procedure, therapy, intervention, or recommendation.
description: Semicolon-separated list of medical actions.
from_schema: http://w3id.org/ontogpt/maxo
rank: 1000
multivalued: true
alias: action
owner: MaxoAnnotations
domain_of:
- MaxoAnnotations
range: Action

```
</details>