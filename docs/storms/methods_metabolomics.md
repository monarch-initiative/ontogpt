

# Slot: methods_metabolomics


_Specify the analytic method used (such as nuclear magnetic resonance spectroscopy or mass spectrometry). For mass spectrometry, detail which fractions were obtained (polar and/or non polar) and how these were analyzed. Provide details on metabolomics methods and platforms (e.g. derivatization, instrument type, injection type, column type and instrument settings)._



URI: [storms:methods_metabolomics](http://w3id.org/ontogpt/storms/methods_metabolomics)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [STORMSChecklist](STORMSChecklist.md) | A checklist of items that should be reported in a microbiome study |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/ontogpt/storms




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | storms:methods_metabolomics |
| native | storms:methods_metabolomics |




## LinkML Source

<details>
```yaml
name: methods_metabolomics
description: Specify the analytic method used (such as nuclear magnetic resonance
  spectroscopy or mass spectrometry). For mass spectrometry, detail which fractions
  were obtained (polar and/or non polar) and how these were analyzed. Provide details
  on metabolomics methods and platforms (e.g. derivatization, instrument type, injection
  type, column type and instrument settings).
from_schema: https://w3id.org/ontogpt/storms
rank: 1000
alias: methods_metabolomics
owner: STORMSChecklist
domain_of:
- STORMSChecklist
slot_group: methods
range: string

```
</details>