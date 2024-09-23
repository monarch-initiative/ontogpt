

# Slot: clinical_status


_The clinical status of the condition._



URI: [UNKNOWN:clinical_status](UNKNOWN:clinical_status)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Condition](Condition.md) |  |  no  |







## Properties

* Range: [ConditionClinicalStatus](ConditionClinicalStatus.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/condition




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | UNKNOWN:clinical_status |
| native | UNKNOWN:clinical_status |




## LinkML Source

<details>
```yaml
name: clinical_status
description: The clinical status of the condition.
from_schema: http://w3id.org/ontogpt/condition
rank: 1000
ifabsent: string("unknown")
alias: clinical_status
owner: Condition
domain_of:
- Condition
range: ConditionClinicalStatus
required: true

```
</details>