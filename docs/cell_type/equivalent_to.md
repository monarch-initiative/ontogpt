

# Slot: equivalent_to


_the the cell type described_



URI: [skos:exactMatch](http://www.w3.org/2004/02/skos/core#exactMatch)



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





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | the cell type described in the text || owl | AnnotationAssertion |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: equivalent_to
annotations:
  prompt:
    tag: prompt
    value: the cell type described in the text
  owl:
    tag: owl
    value: AnnotationAssertion
description: the the cell type described
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
slot_uri: skos:exactMatch
alias: equivalent_to
owner: CellType
domain_of:
- CellType
range: CellOntologyTerm

```
</details>