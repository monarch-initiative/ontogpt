

# Class: Trait



URI: [desiccation:Trait](http://w3id.org/ontogpt/desiccationTrait)



```mermaid
erDiagram
Trait {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Trait**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EntityContainingDocument](EntityContainingDocument.md) | [traits](traits.md) | range | [Trait](Trait.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* TO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:to || prompt | the description of a plant trait.
 Examples of trait categories are germination ratio, fruit hollowness, arid region exposure. |



### Schema Source


* from schema: http://w3id.org/ontogpt/desiccation





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | desiccation:Trait |
| native | desiccation:Trait |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Trait
id_prefixes:
- TO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:to
  prompt:
    tag: prompt
    value: "the description of a plant trait.\n Examples of trait categories are germination\
      \ ratio, fruit hollowness, arid region exposure."
from_schema: http://w3id.org/ontogpt/desiccation
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Trait
id_prefixes:
- TO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:to
  prompt:
    tag: prompt
    value: "the description of a plant trait.\n Examples of trait categories are germination\
      \ ratio, fruit hollowness, arid region exposure."
from_schema: http://w3id.org/ontogpt/desiccation
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
    from_schema: http://w3id.org/ontogpt/desiccation
    rank: 1000
    identifier: true
    alias: id
    owner: Trait
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
    from_schema: http://w3id.org/ontogpt/desiccation
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Trait
    domain_of:
    - NamedEntity
    range: string

```
</details>