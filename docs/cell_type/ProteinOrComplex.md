

# Class: ProteinOrComplex



URI: [cell_type:ProteinOrComplex](http://w3id.org/ontogpt/cell_type/ProteinOrComplex)



```mermaid
erDiagram
ProteinOrComplex {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **ProteinOrComplex**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ImmuneCell](ImmuneCell.md) | [has_surface_markers](has_surface_markers.md) | range | [ProteinOrComplex](ProteinOrComplex.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HGNC

* MGI

* PR

* UniProtKB

* GO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:hgnc, bioportal:hgnc-nr, sqlite:obo:go, sqlite:obo:pr |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cell_type:ProteinOrComplex |
| native | cell_type:ProteinOrComplex |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProteinOrComplex
id_prefixes:
- HGNC
- MGI
- PR
- UniProtKB
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hgnc, bioportal:hgnc-nr, sqlite:obo:go, sqlite:obo:pr
from_schema: http://w3id.org/ontogpt/cell_type
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: ProteinOrComplex
id_prefixes:
- HGNC
- MGI
- PR
- UniProtKB
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hgnc, bioportal:hgnc-nr, sqlite:obo:go, sqlite:obo:pr
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
    owner: ProteinOrComplex
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
    owner: ProteinOrComplex
    domain_of:
    - CellType
    - NamedEntity
    range: string

```
</details>