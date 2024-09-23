

# Slot: projects_to_or_from


_Brain structures from which this cell type projects into or receives projections from_



URI: [RO:0002170](http://purl.obolibrary.org/obo/RO_0002170)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Interneuron](Interneuron.md) |  |  no  |







## Properties

* Range: [BrainRegion](BrainRegion.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of anatomical structures from which this cell type projects from or into |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: projects_to_or_from
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of anatomical structures from which this cell
      type projects from or into
description: Brain structures from which this cell type projects into or receives
  projections from
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
slot_uri: RO:0002170
multivalued: true
alias: projects_to_or_from
owner: Interneuron
domain_of:
- Interneuron
range: BrainRegion

```
</details>