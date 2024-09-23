

# Slot: roles

URI: [RO:0002215](http://purl.obolibrary.org/obo/RO_0002215)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImmuneCell](ImmuneCell.md) |  |  no  |
| [CellType](CellType.md) | Represents a cell type |  no  |
| [Neuron](Neuron.md) |  |  no  |
| [Interneuron](Interneuron.md) |  |  no  |







## Properties

* Range: [BiologicalProcess](BiologicalProcess.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of roles (e.g. biological processes) that this cell type plays. These should be short descriptive terms corresponding to ontology terms in the GO biological process hierarchy. || owl | SubClassOf, ObjectSomeValuesFrom |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: roles
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of roles (e.g. biological processes) that this
      cell type plays. These should be short descriptive terms corresponding to ontology
      terms in the GO biological process hierarchy.
  owl:
    tag: owl
    value: SubClassOf, ObjectSomeValuesFrom
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
slot_uri: RO:0002215
multivalued: true
alias: roles
owner: CellType
domain_of:
- CellType
range: BiologicalProcess

```
</details>