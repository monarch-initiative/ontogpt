# Slot: subject_qualifier
_An optional qualifier or modifier for the subject of the statement, e.g. "high dose" or "intravenously administered"_


URI: [core:subject_qualifier](http://w3id.org/ontogpt/core/subject_qualifier)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md) | A triple where the subject is a chemical and the object is a disease
[Triple](Triple.md) | Abstract parent for Relation Extraction tasks






## Properties

* Range: [NamedEntity](NamedEntity.md)







## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/core




## LinkML Source

<details>
```yaml
name: subject_qualifier
description: An optional qualifier or modifier for the subject of the statement, e.g.
  "high dose" or "intravenously administered"
from_schema: http://w3id.org/ontogpt/core
rank: 1000
alias: subject_qualifier
owner: Triple
domain_of:
- Triple
range: NamedEntity

```
</details>