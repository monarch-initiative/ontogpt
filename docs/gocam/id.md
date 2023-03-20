# Slot: id
_A unique identifier for the named entity_


URI: [core:id](http://w3id.org/ontogpt/core/id)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Gene](Gene.md) | 
[Pathway](Pathway.md) | 
[CellularProcess](CellularProcess.md) | 
[MolecularActivity](MolecularActivity.md) | 
[GeneLocation](GeneLocation.md) | 
[Organism](Organism.md) | 
[Molecule](Molecule.md) | 
[NamedEntity](NamedEntity.md) | 
[RelationshipType](RelationshipType.md) | 
[Publication](Publication.md) | 






## Properties

* Range: [xsd:string](xsd:string)







## Comments

* this is populated during the grounding and normalization step

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt.skip | true |



### Schema Source


* from schema: http://w3id.org/ontogpt/core




## LinkML Source

<details>
```yaml
name: id
annotations:
  prompt.skip:
    tag: prompt.skip
    value: 'true'
description: A unique identifier for the named entity
comments:
- this is populated during the grounding and normalization step
from_schema: http://w3id.org/ontogpt/core
rank: 1000
identifier: true
alias: id
domain_of:
- NamedEntity
- Publication
range: string

```
</details>