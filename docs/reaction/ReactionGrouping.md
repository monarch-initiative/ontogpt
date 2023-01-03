# Class: ReactionGrouping



URI: [reaction:ReactionGrouping](http://w3id.org/ontogpt/reaction/ReactionGrouping)


```mermaid
 classDiagram
    class ReactionGrouping
      NamedEntity <|-- ReactionGrouping
      
      ReactionGrouping : id
      ReactionGrouping : label
      
```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **ReactionGrouping**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Reaction](Reaction.md) | [subclass_of](subclass_of.md) | range | [ReactionGrouping](ReactionGrouping.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* GO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go |



### Schema Source


* from schema: https://w3id.org/ontogpt/reaction





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | reaction:ReactionGrouping |
| native | reaction:ReactionGrouping |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReactionGrouping
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
from_schema: https://w3id.org/ontogpt/reaction
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: ReactionGrouping
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
from_schema: https://w3id.org/ontogpt/reaction
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
    owner: ReactionGrouping
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
    alias: label
    owner: ReactionGrouping
    domain_of:
    - Reaction
    - NamedEntity
    range: string

```
</details>