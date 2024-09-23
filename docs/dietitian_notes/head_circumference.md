

# Slot: head_circumference

URI: [dietitian_notes:head_circumference](dietitian_notes:head_circumference)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalObservations](ClinicalObservations.md) | A set of clinical observations about a single patient at a single time |  no  |







## Properties

* Range: [QuantitativeValueWithMetric](QuantitativeValueWithMetric.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | The value and units of the patient's head circumference. This may be abbreviated as "HC". 'Not provided' if not provided. |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:head_circumference |
| native | dietitian_notes:head_circumference |




## LinkML Source

<details>
```yaml
name: head_circumference
annotations:
  prompt:
    tag: prompt
    value: The value and units of the patient's head circumference. This may be abbreviated
      as "HC". 'Not provided' if not provided.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: head_circumference
owner: ClinicalObservations
domain_of:
- ClinicalObservations
range: QuantitativeValueWithMetric

```
</details>