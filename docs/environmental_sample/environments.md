

# Slot: environments

URI: [sample:environments](http://w3id.org/ontogpt/environmental-sample/environments)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Study](Study.md) |  |  no  |







## Properties

* Range: [Environment](Environment.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of environment terms for the location in which the study was conducted |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sample:environments |
| native | sample:environments |




## LinkML Source

<details>
```yaml
name: environments
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of environment terms for the location in which
      the study was conducted
from_schema: http://w3id.org/ontogpt/environmental-sample
rank: 1000
alias: environments
owner: Study
domain_of:
- Study
range: Environment
multivalued: true

```
</details>