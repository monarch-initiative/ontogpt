# Class: Treatment



URI: [eg:Treatment](http://w3id.org/ontogpt/environmental-metagenome/Treatment)


```mermaid
 classDiagram
    class Treatment
      NamedEntity <|-- Treatment
      
      Treatment : id
      Treatment : label
      
```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Treatment**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [treatments](treatments.md) | range | [Treatment](Treatment.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* PECO

* OBI






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:peco, sqlite:obo:obi, bioportal:bero |



### Schema Source


* from schema: http://w3id.org/ontogpt/metagenome





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | eg:Treatment |
| native | eg:Treatment |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Treatment
id_prefixes:
- PECO
- OBI
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:peco, sqlite:obo:obi, bioportal:bero
from_schema: http://w3id.org/ontogpt/metagenome
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Treatment
id_prefixes:
- PECO
- OBI
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:peco, sqlite:obo:obi, bioportal:bero
from_schema: http://w3id.org/ontogpt/metagenome
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
    owner: Treatment
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
    owner: Treatment
    domain_of:
    - NamedEntity
    range: string

```
</details>