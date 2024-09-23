

# Slot: variables

URI: [sample:variables](http://w3id.org/ontogpt/environmental-sample/variables)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) |  |  no  |







## Properties

* Range: [Variable](Variable.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of study variables |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sample:variables |
| native | sample:variables |




## LinkML Source

<details>
```yaml
name: variables
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of study variables
from_schema: http://w3id.org/ontogpt/environmental-sample
rank: 1000
alias: variables
owner: Study
domain_of:
- Study
range: Variable
multivalued: true

```
</details>