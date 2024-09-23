

# Class: Gene



URI: [cell_type:Gene](http://w3id.org/ontogpt/cell_type/Gene)



```mermaid
erDiagram
Gene {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Gene**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CellType](CellType.md) | [genes](genes.md) | range | [Gene](Gene.md) |
| [ImmuneCell](ImmuneCell.md) | [genes](genes.md) | range | [Gene](Gene.md) |
| [Neuron](Neuron.md) | [genes](genes.md) | range | [Gene](Gene.md) |
| [Interneuron](Interneuron.md) | [genes](genes.md) | range | [Gene](Gene.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HGNC

* MGI

* PR

* UniProtKB






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:hgnc, bioportal:hgnc-nr |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cell_type:Gene |
| native | cell_type:Gene |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gene
id_prefixes:
- HGNC
- MGI
- PR
- UniProtKB
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hgnc, bioportal:hgnc-nr
from_schema: http://w3id.org/ontogpt/cell_type
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Gene
id_prefixes:
- HGNC
- MGI
- PR
- UniProtKB
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hgnc, bioportal:hgnc-nr
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
    owner: Gene
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
    owner: Gene
    domain_of:
    - CellType
    - NamedEntity
    range: string

```
</details>