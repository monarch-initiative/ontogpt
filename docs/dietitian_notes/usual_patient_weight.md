

# Slot: usual_patient_weight

URI: [dietitian_notes:usual_patient_weight](dietitian_notes:usual_patient_weight)



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
| prompt | The value and units of the patient's body weight under usual conditions and/or in the recent past. This should include all units, percentiles, and z-scores. Relevant acronyms: IBW: ideal body weight, UBW: usual body weight, ABW: actual body weight. 'Not provided' if not provided. |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:usual_patient_weight |
| native | dietitian_notes:usual_patient_weight |




## LinkML Source

<details>
```yaml
name: usual_patient_weight
annotations:
  prompt:
    tag: prompt
    value: 'The value and units of the patient''s body weight under usual conditions
      and/or in the recent past. This should include all units, percentiles, and z-scores.
      Relevant acronyms: IBW: ideal body weight, UBW: usual body weight, ABW: actual
      body weight. ''Not provided'' if not provided.'
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: usual_patient_weight
owner: ClinicalObservations
domain_of:
- ClinicalObservations
range: QuantitativeValueWithMetric

```
</details>