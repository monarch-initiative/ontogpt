

# Slot: subject_extension


_An optional term describing some specific aspect of the subject, e.g. "analgesic agent therapy" has the aspect "analgesic"_



URI: [maxo_extract:subject_extension](http://w3id.org/ontogpt/maxosubject_extension)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ActionAnnotationRelationship](ActionAnnotationRelationship.md) | An association representing a relationships between a disease, the mentioned ... |  yes  |
| [ExtendedTriple](ExtendedTriple.md) | Abstract parent for Relation Extraction tasks, with additional support for an... |  no  |







## Properties

* Range: [NamedEntity](NamedEntity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/maxo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | maxo_extract:subject_extension |
| native | maxo_extract:subject_extension |




## LinkML Source

<details>
```yaml
name: subject_extension
description: An optional term describing some specific aspect of the subject, e.g.
  "analgesic agent therapy" has the aspect "analgesic"
from_schema: http://w3id.org/ontogpt/maxo
rank: 1000
alias: subject_extension
owner: ExtendedTriple
domain_of:
- ExtendedTriple
range: NamedEntity

```
</details>