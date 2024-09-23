

# Class: InteractionType



URI: [bp:InteractionType](http://w3id.org/ontogpt/biotic-interaction-templateInteractionType)



```mermaid
erDiagram
InteractionType {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **InteractionType**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [BioticInteraction](BioticInteraction.md) | [interaction_type](interaction_type.md) | range | [InteractionType](InteractionType.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* RO

* MESH

* ECOCORE

* NCIT






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go, sqlite:obo:ro, sqlite:obo:bero |



### Schema Source


* from schema: https://w3id.org/ontogpt/biotic_interaction




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bp:InteractionType |
| native | bp:InteractionType |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InteractionType
id_prefixes:
- RO
- MESH
- ECOCORE
- NCIT
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go, sqlite:obo:ro, sqlite:obo:bero
from_schema: https://w3id.org/ontogpt/biotic_interaction
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: InteractionType
id_prefixes:
- RO
- MESH
- ECOCORE
- NCIT
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go, sqlite:obo:ro, sqlite:obo:bero
from_schema: https://w3id.org/ontogpt/biotic_interaction
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
    from_schema: https://w3id.org/ontogpt/biotic_interaction
    rank: 1000
    identifier: true
    alias: id
    owner: InteractionType
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
    from_schema: https://w3id.org/ontogpt/biotic_interaction
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: InteractionType
    domain_of:
    - NamedEntity
    range: string

```
</details>