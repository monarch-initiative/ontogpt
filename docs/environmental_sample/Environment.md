# Class: Environment



URI: [sample:Environment](http://w3id.org/ontogpt/environmental-sample/Environment)


```mermaid
 classDiagram
    class Environment
      NamedEntity <|-- Environment
      
      Environment : id
      Environment : label
      
```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Environment**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [environments](environments.md) | range | [Environment](Environment.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* ENVO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:envo |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sample:Environment |
| native | sample:Environment |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Environment
id_prefixes:
- ENVO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:envo
from_schema: http://w3id.org/ontogpt/environmental-sample
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Environment
id_prefixes:
- ENVO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:envo
from_schema: http://w3id.org/ontogpt/environmental-sample
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
    owner: Environment
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
    owner: Environment
    domain_of:
    - NamedEntity
    range: string

```
</details>