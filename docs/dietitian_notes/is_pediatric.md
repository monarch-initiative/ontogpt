

# Slot: is_pediatric

URI: [dietitian_notes:is_pediatric](dietitian_notes:is_pediatric)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalObservations](ClinicalObservations.md) | A set of clinical observations about a single patient at a single time |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | True if the patient is a child, False otherwise. |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:is_pediatric |
| native | dietitian_notes:is_pediatric |




## LinkML Source

<details>
```yaml
name: is_pediatric
annotations:
  prompt:
    tag: prompt
    value: True if the patient is a child, False otherwise.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: is_pediatric
owner: ClinicalObservations
domain_of:
- ClinicalObservations
range: string

```
</details>