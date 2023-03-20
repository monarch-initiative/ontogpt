# Class: NamedEntity


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [core:NamedEntity](http://w3id.org/ontogpt/core/NamedEntity)


```mermaid
erDiagram
NamedEntity {
    string id  
    string label  
}



```




## Inheritance
* **NamedEntity**
    * [RelationshipType](RelationshipType.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [xsd:string](xsd:string) | A unique identifier for the named entity | direct |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Triple](Triple.md) | [subject](subject.md) | range | [NamedEntity](NamedEntity.md) |
| [Triple](Triple.md) | [object](object.md) | range | [NamedEntity](NamedEntity.md) |
| [Triple](Triple.md) | [subject_qualifier](subject_qualifier.md) | range | [NamedEntity](NamedEntity.md) |
| [Triple](Triple.md) | [object_qualifier](object_qualifier.md) | range | [NamedEntity](NamedEntity.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/core





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | core:NamedEntity |
| native | core:NamedEntity |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NamedEntity
from_schema: http://w3id.org/ontogpt/core
rank: 1000
abstract: true
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
  label:
    name: label
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/core
    aliases:
    - name
    rank: 1000
    range: string

```
</details>

### Induced

<details>
```yaml
name: NamedEntity
from_schema: http://w3id.org/ontogpt/core
rank: 1000
abstract: true
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
    owner: NamedEntity
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
    owner: NamedEntity
    domain_of:
    - NamedEntity
    range: string

```
</details>