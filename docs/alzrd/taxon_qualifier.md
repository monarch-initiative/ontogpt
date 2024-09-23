

# Slot: taxon_qualifier


_An optional qualifier or modifier for the taxon, as described_

_ in the input text._

_ This may include a strain or genetic background of the model organism._



URI: [alzrd:taxon_qualifier](http://w3id.org/ontogpt/alzrdtaxon_qualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentalMetricToTaxonRelationship](ExperimentalMetricToTaxonRelationship.md) | A triple where the subject is an experimental metric, the object is an taxon,... |  no  |







## Properties

* Range: [NamedEntity](NamedEntity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:taxon_qualifier |
| native | alzrd:taxon_qualifier |




## LinkML Source

<details>
```yaml
name: taxon_qualifier
description: "An optional qualifier or modifier for the taxon, as described\n in the\
  \ input text.\n This may include a strain or genetic background of the model organism."
from_schema: http://w3id.org/ontogpt/alzrd
rank: 1000
alias: taxon_qualifier
owner: ExperimentalMetricToTaxonRelationship
domain_of:
- ExperimentalMetricToTaxonRelationship
range: NamedEntity

```
</details>