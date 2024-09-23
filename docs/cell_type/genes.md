

# Slot: genes

URI: [RO:0002292](http://purl.obolibrary.org/obo/RO_0002292)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImmuneCell](ImmuneCell.md) |  |  no  |
| [CellType](CellType.md) | Represents a cell type |  no  |
| [Neuron](Neuron.md) |  |  no  |
| [Interneuron](Interneuron.md) |  |  no  |







## Properties

* Range: [Gene](Gene.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of genes expressed in cells of this type || owl | SubClassOf, ObjectSomeValuesFrom |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: genes
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of genes expressed in cells of this type
  owl:
    tag: owl
    value: SubClassOf, ObjectSomeValuesFrom
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
slot_uri: RO:0002292
multivalued: true
alias: genes
owner: CellType
domain_of:
- CellType
range: Gene

```
</details>