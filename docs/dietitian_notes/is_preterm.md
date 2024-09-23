

# Slot: is_preterm

URI: [dietitian_notes:is_preterm](dietitian_notes:is_preterm)



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
| prompt | True if the patient's birth was preterm, False otherwise. A birth before 37 weeks gestation is preterm. |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:is_preterm |
| native | dietitian_notes:is_preterm |




## LinkML Source

<details>
```yaml
name: is_preterm
annotations:
  prompt:
    tag: prompt
    value: True if the patient's birth was preterm, False otherwise. A birth before
      37 weeks gestation is preterm.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: is_preterm
owner: ClinicalObservations
domain_of:
- ClinicalObservations
range: string

```
</details>