

# Slot: causal_relationships

URI: [sample:causal_relationships](http://w3id.org/ontogpt/environmental-sample-ungrounded/causal_relationships)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) |  |  no  |







## Properties

* Range: [CausalRelationship](CausalRelationship.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of cause-effect pairs, for example, effect of temperature on growth |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample-ungrounded




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sample:causal_relationships |
| native | sample:causal_relationships |




## LinkML Source

<details>
```yaml
name: causal_relationships
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of cause-effect pairs, for example, effect of
      temperature on growth
from_schema: http://w3id.org/ontogpt/environmental-sample-ungrounded
rank: 1000
alias: causal_relationships
owner: Study
domain_of:
- Study
range: CausalRelationship
multivalued: true

```
</details>