

# Slot: malnutrition_status

URI: [dietitian_notes:malnutrition_status](dietitian_notes:malnutrition_status)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalObservations](ClinicalObservations.md) | A set of clinical observations about a single patient at a single time |  no  |







## Properties

* Range: [MalnutritionObservations](MalnutritionObservations.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | Observations of the patient's malnutrition status. This should include any details of malnutrition presence, risk, severity, duration, diagnosis, and etiology. Should also include any risk for refeeding syndrome. 'Not provided' if not provided. |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:malnutrition_status |
| native | dietitian_notes:malnutrition_status |




## LinkML Source

<details>
```yaml
name: malnutrition_status
annotations:
  prompt:
    tag: prompt
    value: Observations of the patient's malnutrition status. This should include
      any details of malnutrition presence, risk, severity, duration, diagnosis, and
      etiology. Should also include any risk for refeeding syndrome. 'Not provided'
      if not provided.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: malnutrition_status
owner: ClinicalObservations
domain_of:
- ClinicalObservations
range: MalnutritionObservations

```
</details>