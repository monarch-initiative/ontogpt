

# Slot: nutrition_support


_A semicolon-separated list of the patient's nutrition support therapies, usually enteral or parenteral nutrition. All acronyms should be expanded, omitting the original acronym. Relevant acronyms: PO: per os/by mouth, TPN: total parenteral nutrition, PN: parenteral nutrition, EN: enteral nutrition, D#%: dextrose percentage (e.g. D5%) for PN infusion, AA # g/kg/d: amino acid provisions (may also be in percentages) for PN infusion, SMOF # g/kg/d: soy MCT olive fish oil emulsion for PN infusion, GIR: glucose infusion rate, SBS: short bowel syndrome, LIS: low intermittent suction, BW: birth weight, EHM: exclusively human milk, RTBW: return to birth weight, Mg: magnesium, Phos: phosphorus, GI: gastrointestinal, PICC: peripherally inserted central catheter, DOL: day of life, TG: triglycerides, KUB: Kidney ureter bladder CT_



URI: [dietitian_notes:nutrition_support](dietitian_notes:nutrition_support)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ClinicalObservations](ClinicalObservations.md) | A set of clinical observations about a single patient at a single time |  no  |







## Properties

* Range: [NutritionSupport](NutritionSupport.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:nutrition_support |
| native | dietitian_notes:nutrition_support |




## LinkML Source

<details>
```yaml
name: nutrition_support
description: 'A semicolon-separated list of the patient''s nutrition support therapies,
  usually enteral or parenteral nutrition. All acronyms should be expanded, omitting
  the original acronym. Relevant acronyms: PO: per os/by mouth, TPN: total parenteral
  nutrition, PN: parenteral nutrition, EN: enteral nutrition, D#%: dextrose percentage
  (e.g. D5%) for PN infusion, AA # g/kg/d: amino acid provisions (may also be in percentages)
  for PN infusion, SMOF # g/kg/d: soy MCT olive fish oil emulsion for PN infusion,
  GIR: glucose infusion rate, SBS: short bowel syndrome, LIS: low intermittent suction,
  BW: birth weight, EHM: exclusively human milk, RTBW: return to birth weight, Mg:
  magnesium, Phos: phosphorus, GI: gastrointestinal, PICC: peripherally inserted central
  catheter, DOL: day of life, TG: triglycerides, KUB: Kidney ureter bladder CT'
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: nutrition_support
owner: ClinicalObservations
domain_of:
- ClinicalObservations
range: NutritionSupport
multivalued: true

```
</details>