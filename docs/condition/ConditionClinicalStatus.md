# Enum: ConditionClinicalStatus



URI: [ConditionClinicalStatus](ConditionClinicalStatus.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| active | None | The subject is currently experiencing the condition or situation, there is ev... |
| recurrence | None | The subject is experiencing a reoccurence or repeating of a previously resolv... |
| relapse | None | The subject is experiencing a return of a condition or situation after a peri... |
| inactive | None | The subject is no longer experiencing the condition or situation and there is... |
| remission | None | The subject is not presently experiencing the condition or situation, but the... |
| resolved | None | The subject is not presently experiencing the condition or situation and ther... |
| unknown | None | The authoring/source system does not know which of the status values currentl... |




## Slots

| Name | Description |
| ---  | --- |
| [clinical_status](clinical_status.md) | The clinical status of the condition |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/condition






## LinkML Source

<details>
```yaml
name: ConditionClinicalStatus
from_schema: http://w3id.org/ontogpt/condition
rank: 1000
permissible_values:
  active:
    text: active
    description: The subject is currently experiencing the condition or situation,
      there is evidence of the condition or situation, or considered to be a significant
      risk.
  recurrence:
    text: recurrence
    description: The subject is experiencing a reoccurence or repeating of a previously
      resolved condition or situation, e.g. urinary tract infection, food insecurity.
  relapse:
    text: relapse
    description: The subject is experiencing a return of a condition or situation
      after a period of improvement or remission, e.g. relapse of cancer, alcoholism.
  inactive:
    text: inactive
    description: The subject is no longer experiencing the condition or situation
      and there is no longer evidence or appreciable risk of the condition or situation.
  remission:
    text: remission
    description: The subject is not presently experiencing the condition or situation,
      but there is a risk of the condition or situation returning.
  resolved:
    text: resolved
    description: The subject is not presently experiencing the condition or situation
      and there is a negligible perceived risk of the condition or situation returning.
  unknown:
    text: unknown
    description: The authoring/source system does not know which of the status values
      currently applies for this condition.

```
</details>
