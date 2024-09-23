

# Slot: patient_age

URI: [dietitian_notes:patient_age](dietitian_notes:patient_age)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalObservations](ClinicalObservations.md) | A set of clinical observations about a single patient at a single time |  no  |







## Properties

* Range: [QuantitativeValue](QuantitativeValue.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | The patient's age at the time of the current assessment. Omit the word "old" from the response. 'Not provided' if not provided. |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:patient_age |
| native | dietitian_notes:patient_age |




## LinkML Source

<details>
```yaml
name: patient_age
annotations:
  prompt:
    tag: prompt
    value: The patient's age at the time of the current assessment. Omit the word
      "old" from the response. 'Not provided' if not provided.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: patient_age
owner: ClinicalObservations
domain_of:
- ClinicalObservations
range: QuantitativeValue

```
</details>