

# Class: Disease



URI: [cell_type:Disease](http://w3id.org/ontogpt/cell_type/Disease)



```mermaid
erDiagram
Disease {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Disease**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CellType](CellType.md) | [diseases](diseases.md) | range | [Disease](Disease.md) |
| [ImmuneCell](ImmuneCell.md) | [diseases](diseases.md) | range | [Disease](Disease.md) |
| [Neuron](Neuron.md) | [diseases](diseases.md) | range | [Disease](Disease.md) |
| [Interneuron](Interneuron.md) | [diseases](diseases.md) | range | [Disease](Disease.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* MONDO

* HP






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:mondo, sqlite:obo:hp |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cell_type:Disease |
| native | cell_type:Disease |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Disease
id_prefixes:
- MONDO
- HP
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:mondo, sqlite:obo:hp
from_schema: http://w3id.org/ontogpt/cell_type
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Disease
id_prefixes:
- MONDO
- HP
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:mondo, sqlite:obo:hp
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
    owner: Disease
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
    owner: Disease
    domain_of:
    - CellType
    - NamedEntity
    range: string

```
</details>