

# Slot: diet_supplementation


_A semicolon-separated list of the patient's diet supplementation therapies. Split on specific ingredients and their amounts. All acronyms should be expanded, omitting the original acronym. Relevant acronyms: PO: per os/by mouth, TPN: total parenteral nutrition, PN: parenteral nutrition, EN: enteral nutrition, D#%: dextrose percentage (e.g. D5%) for PN infusion, AA # g/kg/d: amino acid provisions (may also be in percentages) for PN infusion, SMOF # g/kg/d: soy MCT olive fish oil emulsion for PN infusion, GIR: glucose infusion rate, SBS: short bowel syndrome, LIS: low intermittent suction, BW: birth weight, EHM: exclusively human milk, RTBW: return to birth weight, Mg: magnesium, Phos: phosphorus, GI: gastrointestinal, PICC: peripherally inserted central catheter, DOL: day of life, TG: triglycerides, KUB: Kidney ureter bladder CT_



URI: [dietitian_notes:diet_supplementation](dietitian_notes:diet_supplementation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalObservations](ClinicalObservations.md) | A set of clinical observations about a single patient at a single time |  no  |







## Properties

* Range: [DietSupplementation](DietSupplementation.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:diet_supplementation |
| native | dietitian_notes:diet_supplementation |




## LinkML Source

<details>
```yaml
name: diet_supplementation
description: 'A semicolon-separated list of the patient''s diet supplementation therapies.
  Split on specific ingredients and their amounts. All acronyms should be expanded,
  omitting the original acronym. Relevant acronyms: PO: per os/by mouth, TPN: total
  parenteral nutrition, PN: parenteral nutrition, EN: enteral nutrition, D#%: dextrose
  percentage (e.g. D5%) for PN infusion, AA # g/kg/d: amino acid provisions (may also
  be in percentages) for PN infusion, SMOF # g/kg/d: soy MCT olive fish oil emulsion
  for PN infusion, GIR: glucose infusion rate, SBS: short bowel syndrome, LIS: low
  intermittent suction, BW: birth weight, EHM: exclusively human milk, RTBW: return
  to birth weight, Mg: magnesium, Phos: phosphorus, GI: gastrointestinal, PICC: peripherally
  inserted central catheter, DOL: day of life, TG: triglycerides, KUB: Kidney ureter
  bladder CT'
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: diet_supplementation
owner: ClinicalObservations
domain_of:
- ClinicalObservations
range: DietSupplementation
multivalued: true

```
</details>