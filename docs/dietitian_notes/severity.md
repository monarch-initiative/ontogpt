

# Slot: severity


_The severity of the patient's malnutrition, if present. This may be Mild, Moderate, or Severe. In general, a patient receiving less than 50% of their estimated energy requirement for greater than 5 days is considered to have severe malnutrition. N/A if not provided._



URI: [dietitian_notes:severity](dietitian_notes:severity)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MalnutritionObservations](MalnutritionObservations.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:severity |
| native | dietitian_notes:severity |




## LinkML Source

<details>
```yaml
name: severity
description: The severity of the patient's malnutrition, if present. This may be Mild,
  Moderate, or Severe. In general, a patient receiving less than 50% of their estimated
  energy requirement for greater than 5 days is considered to have severe malnutrition.
  N/A if not provided.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: severity
owner: MalnutritionObservations
domain_of:
- MalnutritionObservations
range: string

```
</details>