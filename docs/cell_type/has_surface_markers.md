

# Slot: has_surface_markers

URI: [cell_type:has_surface_markers](http://w3id.org/ontogpt/cell_type/has_surface_markers)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImmuneCell](ImmuneCell.md) |  |  no  |







## Properties

* Range: [ProteinOrComplex](ProteinOrComplex.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of proteins or complexes expressed on the surface of the cell || owl | SubClassOf, ObjectSomeValuesFrom |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: has_surface_markers
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of proteins or complexes expressed on the surface
      of the cell
  owl:
    tag: owl
    value: SubClassOf, ObjectSomeValuesFrom
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
multivalued: true
alias: has_surface_markers
owner: ImmuneCell
domain_of:
- ImmuneCell
range: ProteinOrComplex

```
</details>