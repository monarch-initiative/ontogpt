

# Slot: patient_height

URI: [dietitian_notes:patient_height](dietitian_notes:patient_height)



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
| prompt | The value and units of the patient's height. This should include all units, percentiles, and z-scores. 'Not provided' if not provided. |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:patient_height |
| native | dietitian_notes:patient_height |




## LinkML Source

<details>
```yaml
name: patient_height
annotations:
  prompt:
    tag: prompt
    value: The value and units of the patient's height. This should include all units,
      percentiles, and z-scores. 'Not provided' if not provided.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: patient_height
owner: ClinicalObservations
domain_of:
- ClinicalObservations
range: QuantitativeValueWithMetric

```
</details>