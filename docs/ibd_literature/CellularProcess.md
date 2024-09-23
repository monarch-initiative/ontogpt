

# Class: CellularProcess



URI: [ibdlit:CellularProcess](http://w3id.org/ontogpt/ibd_literature/CellularProcess)



```mermaid
erDiagram
CellularProcess {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **CellularProcess**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IBDAnnotations](IBDAnnotations.md) | [cellular_process](cellular_process.md) | range | [CellularProcess](CellularProcess.md) |
| [DiseaseCellularProcessRelationship](DiseaseCellularProcessRelationship.md) | [object](object.md) | range | [CellularProcess](CellularProcess.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* GO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go || prompt | the name of the cellular process |



### Schema Source


* from schema: http://w3id.org/ontogpt/ibd_literature





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ibdlit:CellularProcess |
| native | ibdlit:CellularProcess |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellularProcess
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
  prompt:
    tag: prompt
    value: the name of the cellular process
from_schema: http://w3id.org/ontogpt/ibd_literature
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: CellularProcess
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
  prompt:
    tag: prompt
    value: the name of the cellular process
from_schema: http://w3id.org/ontogpt/ibd_literature
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
    from_schema: http://w3id.org/ontogpt/ibd_literature
    rank: 1000
    identifier: true
    alias: id
    owner: CellularProcess
    domain_of:
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
    from_schema: http://w3id.org/ontogpt/ibd_literature
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: CellularProcess
    domain_of:
    - NamedEntity
    range: string

```
</details>