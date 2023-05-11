# Class: MechanismElement



URI: [drug:MechanismElement](http://w3id.org/ontogpt/drug/MechanismElement)


```mermaid
erDiagram
MechanismElement {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **MechanismElement**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MechanismLink](MechanismLink.md) | [subject](subject.md) | range | [MechanismElement](MechanismElement.md) |
| [MechanismLink](MechanismLink.md) | [object](object.md) | range | [MechanismElement](MechanismElement.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HGNC

* MESH






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go, sqlite:obo:mesh, sqlite:obo:uberon, sqlite:obo:pr, sqlite:obo:ncbitaxon, sqlite:obo:cl |



### Schema Source


* from schema: http://w3id.org/ontogpt/drug





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | drug:MechanismElement |
| native | drug:MechanismElement |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MechanismElement
id_prefixes:
- HGNC
- MESH
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go, sqlite:obo:mesh, sqlite:obo:uberon, sqlite:obo:pr, sqlite:obo:ncbitaxon,
      sqlite:obo:cl
from_schema: http://w3id.org/ontogpt/drug
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: MechanismElement
id_prefixes:
- HGNC
- MESH
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go, sqlite:obo:mesh, sqlite:obo:uberon, sqlite:obo:pr, sqlite:obo:ncbitaxon,
      sqlite:obo:cl
from_schema: http://w3id.org/ontogpt/drug
rank: 1000
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
    from_schema: http://w3id.org/ontogpt/drug
    rank: 1000
    identifier: true
    alias: id
    owner: MechanismElement
    domain_of:
    - NamedEntity
    - Publication
    range: string
  label:
    name: label
    annotations:
      owl:
        tag: owl
        value: AnnotationProperty, AnnotationAssertion
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/drug
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: MechanismElement
    domain_of:
    - NamedEntity
    range: string

```
</details>