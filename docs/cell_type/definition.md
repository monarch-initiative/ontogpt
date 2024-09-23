

# Slot: definition

URI: [IAO:0000115](http://purl.obolibrary.org/obo/IAO_0000115)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImmuneCell](ImmuneCell.md) |  |  no  |
| [CellType](CellType.md) | Represents a cell type |  no  |
| [Neuron](Neuron.md) |  |  no  |
| [Interneuron](Interneuron.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | A concise textual definition in genus-differentia form, i.e  'A <genus> that <differentiating characteristics>' || owl | AnnotationProperty, AnnotationAssertion |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: definition
annotations:
  prompt:
    tag: prompt
    value: A concise textual definition in genus-differentia form, i.e  'A <genus>
      that <differentiating characteristics>'
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
slot_uri: IAO:0000115
alias: definition
owner: CellType
domain_of:
- CellType
range: string

```
</details>