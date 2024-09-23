

# Slot: subtypes

URI: [cell_type:subtypes](http://w3id.org/ontogpt/cell_type/subtypes)



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
| prompt | semicolon-separated list of the subtypes (subclasses) of this cell type. Use concise terms, and separate elements in a list using semicolon (;) || owl.template | {% for subtype in subtypes %}
SubClassOf( {{ tr(subtype) }} {{ id }} )
{% endfor %}
 |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: subtypes
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of the subtypes (subclasses) of this cell type.
      Use concise terms, and separate elements in a list using semicolon (;)
  owl.template:
    tag: owl.template
    value: '{% for subtype in subtypes %}

      SubClassOf( {{ tr(subtype) }} {{ id }} )

      {% endfor %}

      '
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
multivalued: true
alias: subtypes
owner: CellType
domain_of:
- CellType
range: CellOntologyTerm

```
</details>