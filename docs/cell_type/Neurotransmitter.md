

# Class: Neurotransmitter



URI: [cell_type:Neurotransmitter](http://w3id.org/ontogpt/cell_type/Neurotransmitter)



```mermaid
erDiagram
Neurotransmitter {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * [ChemicalEntity](ChemicalEntity.md)
        * **Neurotransmitter**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Neuron](Neuron.md) | [releases_neurotransitter](releases_neurotransitter.md) | range | [Neurotransmitter](Neurotransmitter.md) |
| [Interneuron](Interneuron.md) | [releases_neurotransitter](releases_neurotransitter.md) | range | [Neurotransmitter](Neurotransmitter.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CHEBI






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:chebi |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cell_type:Neurotransmitter |
| native | cell_type:Neurotransmitter |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Neurotransmitter
id_prefixes:
- CHEBI
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:chebi
from_schema: http://w3id.org/ontogpt/cell_type
is_a: ChemicalEntity
slot_usage:
  id:
    name: id
    values_from:
    - NeurotransmitterIdentifier
    identifier: true
    domain_of:
    - CellType
    - NamedEntity
    - Publication

```
</details>

### Induced

<details>
```yaml
name: Neurotransmitter
id_prefixes:
- CHEBI
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:chebi
from_schema: http://w3id.org/ontogpt/cell_type
is_a: ChemicalEntity
slot_usage:
  id:
    name: id
    values_from:
    - NeurotransmitterIdentifier
    identifier: true
    domain_of:
    - CellType
    - NamedEntity
    - Publication
attributes:
  id:
    name: id
    description: A unique identifier for the named entity
    from_schema: http://w3id.org/ontogpt/cell_type
    values_from:
    - NeurotransmitterIdentifier
    identifier: true
    alias: id
    owner: Neurotransmitter
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
    owner: Neurotransmitter
    domain_of:
    - CellType
    - NamedEntity
    range: string

```
</details>