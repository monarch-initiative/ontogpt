

# Class: CellOntologyTerm



URI: [cell_type:CellOntologyTerm](http://w3id.org/ontogpt/cell_type/CellOntologyTerm)



```mermaid
erDiagram
CellOntologyTerm {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **CellOntologyTerm**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CellType](CellType.md) | [equivalent_to](equivalent_to.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [CellType](CellType.md) | [parents](parents.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [CellType](CellType.md) | [subtypes](subtypes.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [ImmuneCell](ImmuneCell.md) | [equivalent_to](equivalent_to.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [ImmuneCell](ImmuneCell.md) | [parents](parents.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [ImmuneCell](ImmuneCell.md) | [subtypes](subtypes.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [Neuron](Neuron.md) | [equivalent_to](equivalent_to.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [Neuron](Neuron.md) | [parents](parents.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [Neuron](Neuron.md) | [subtypes](subtypes.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [Interneuron](Interneuron.md) | [equivalent_to](equivalent_to.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [Interneuron](Interneuron.md) | [parents](parents.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |
| [Interneuron](Interneuron.md) | [subtypes](subtypes.md) | range | [CellOntologyTerm](CellOntologyTerm.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CL

* FBbt

* WBbt






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:cl, sqlite:obo:fbbt, sqlite:obo:wbbt |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cell_type:CellOntologyTerm |
| native | cell_type:CellOntologyTerm |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellOntologyTerm
id_prefixes:
- CL
- FBbt
- WBbt
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:cl, sqlite:obo:fbbt, sqlite:obo:wbbt
from_schema: http://w3id.org/ontogpt/cell_type
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: CellOntologyTerm
id_prefixes:
- CL
- FBbt
- WBbt
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:cl, sqlite:obo:fbbt, sqlite:obo:wbbt
from_schema: http://w3id.org/ontogpt/cell_type
is_a: NamedEntity
attributes:
  id:
    name: id
    annotations:
      prompt.skip:
        tag: prompt.skip
        value: 'true'
    description: A unique identifier for the named entity
    comments:
    - this is populated during the grounding and normalization step
    from_schema: http://w3id.org/ontogpt/cell_type
    identifier: true
    alias: id
    owner: CellOntologyTerm
    domain_of:
    - CellType
    - NamedEntity
    - Publication
    range: string
    required: true
  label:
    name: label
    annotations:
      owl:
        tag: owl
        value: AnnotationProperty, AnnotationAssertion
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/cell_type
    aliases:
    - name
    slot_uri: rdfs:label
    alias: label
    owner: CellOntologyTerm
    domain_of:
    - CellType
    - NamedEntity
    range: string

```
</details>