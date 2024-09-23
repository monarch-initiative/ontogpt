

# Slot: diagnosis


_The patient's malnutrition diagnosis, if present. This should not include modifiers like 'severe'. N/A if not provided._



URI: [dietitian_notes:diagnosis](dietitian_notes:diagnosis)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MalnutritionObservations](MalnutritionObservations.md) |  |  no  |







## Properties

* Range: [Disease](Disease.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:diagnosis |
| native | dietitian_notes:diagnosis |




## LinkML Source

<details>
```yaml
name: diagnosis
description: The patient's malnutrition diagnosis, if present. This should not include
  modifiers like 'severe'. N/A if not provided.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: diagnosis
owner: MalnutritionObservations
domain_of:
- MalnutritionObservations
range: Disease

```
</details>