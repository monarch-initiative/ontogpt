

# Slot: medications


_A semicolon-separated list of the patient's medications. This should include the medication name, dosage, frequency, and route of administration. Relevant acronyms: PO: per os/by mouth, PRN: pro re nata/as needed. 'Not provided' if not provided._



URI: [dietitian_notes:medications](dietitian_notes:medications)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalObservations](ClinicalObservations.md) | A set of clinical observations about a single patient at a single time |  no  |







## Properties

* Range: [DrugTherapy](DrugTherapy.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:medications |
| native | dietitian_notes:medications |




## LinkML Source

<details>
```yaml
name: medications
description: 'A semicolon-separated list of the patient''s medications. This should
  include the medication name, dosage, frequency, and route of administration. Relevant
  acronyms: PO: per os/by mouth, PRN: pro re nata/as needed. ''Not provided'' if not
  provided.'
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: medications
owner: ClinicalObservations
domain_of:
- ClinicalObservations
range: DrugTherapy
multivalued: true

```
</details>