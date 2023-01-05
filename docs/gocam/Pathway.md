# Class: Pathway



URI: [gocam:Pathway](http://w3id.org/ontogpt/gocam/Pathway)


```mermaid
erDiagram
Pathway {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Pathway**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GoCamAnnotations](GoCamAnnotations.md) | [pathways](pathways.md) | range | [Pathway](Pathway.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* GO

* PW






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go, sqlite:obo:pw |



### Schema Source


* from schema: http://w3id.org/ontogpt/gocam





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gocam:Pathway |
| native | gocam:Pathway |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Pathway
id_prefixes:
- GO
- PW
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go, sqlite:obo:pw
from_schema: http://w3id.org/ontogpt/gocam
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Pathway
id_prefixes:
- GO
- PW
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go, sqlite:obo:pw
from_schema: http://w3id.org/ontogpt/gocam
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
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    identifier: true
    alias: id
    owner: Pathway
    domain_of:
    - NamedEntity
    - Publication
    range: string
  label:
    name: label
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/core
    aliases:
    - name
    rank: 1000
    alias: label
    owner: Pathway
    domain_of:
    - NamedEntity
    range: string

```
</details>