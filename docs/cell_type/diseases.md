

# Slot: diseases

URI: [cell_type:diseases](http://w3id.org/ontogpt/cell_type/diseases)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ImmuneCell](ImmuneCell.md) |  |  no  |
| [CellType](CellType.md) | Represents a cell type |  no  |
| [Neuron](Neuron.md) |  |  no  |
| [Interneuron](Interneuron.md) |  |  no  |







## Properties

* Range: [Disease](Disease.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of diseases in which this cell type is implicated || owl.template | {% for disease in diseases %}
SubClassOf( {{ tr(disease) }} ObjectSomeValuesFrom( RO:0004026 {{ id }} ))
{% endfor %}
 |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: diseases
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of diseases in which this cell type is implicated
  owl.template:
    tag: owl.template
    value: '{% for disease in diseases %}

      SubClassOf( {{ tr(disease) }} ObjectSomeValuesFrom( RO:0004026 {{ id }} ))

      {% endfor %}

      '
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
multivalued: true
alias: diseases
owner: CellType
domain_of:
- CellType
range: Disease

```
</details>