

# Slot: parents


_categorization_



URI: [cell_type:parents](http://w3id.org/ontogpt/cell_type/parents)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImmuneCell](ImmuneCell.md) |  |  no  |
| [CellType](CellType.md) | Represents a cell type |  no  |
| [Neuron](Neuron.md) |  |  no  |
| [Interneuron](Interneuron.md) |  |  no  |







## Properties

* Range: [CellOntologyTerm](CellOntologyTerm.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of parent (broader) cell types || owl | SubClassOf |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: parents
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of parent (broader) cell types
  owl:
    tag: owl
    value: SubClassOf
description: categorization
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
multivalued: true
alias: parents
owner: CellType
domain_of:
- CellType
range: CellOntologyTerm

```
</details>