

# Slot: localizations

URI: [BFO:0000050](http://purl.obolibrary.org/obo/BFO_0000050)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImmuneCell](ImmuneCell.md) |  |  no  |
| [CellType](CellType.md) | Represents a cell type |  no  |
| [Neuron](Neuron.md) |  |  no  |
| [Interneuron](Interneuron.md) |  |  no  |







## Properties

* Range: [AnatomicalStructure](AnatomicalStructure.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of anatomical structures in which this cell type is localized || owl | SubClassOf, ObjectSomeValuesFrom |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: localizations
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of anatomical structures in which this cell type
      is localized
  owl:
    tag: owl
    value: SubClassOf, ObjectSomeValuesFrom
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
slot_uri: BFO:0000050
multivalued: true
alias: localizations
owner: CellType
domain_of:
- CellType
range: AnatomicalStructure

```
</details>