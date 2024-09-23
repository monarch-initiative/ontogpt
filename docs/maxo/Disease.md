

# Class: Disease


_A disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism. For example: Beck-Fahrner syndrome, hereditary retinoblastoma, progeria, diabetes mellitus, infectious otitis media_





URI: [maxo_extract:Disease](http://w3id.org/ontogpt/maxoDisease)



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
| [MaxoAnnotations](MaxoAnnotations.md) | [primary_disease](primary_disease.md) | range | [Disease](Disease.md) |
| [ActionAnnotationRelationship](ActionAnnotationRelationship.md) | [qualifier](qualifier.md) | range | [Disease](Disease.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* MONDO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:mondo, sqlite:obo:hp, sqlite:obo:ncit |



### Schema Source


* from schema: http://w3id.org/ontogpt/maxo




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | maxo_extract:Disease |
| native | maxo_extract:Disease |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Disease
id_prefixes:
- MONDO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:mondo, sqlite:obo:hp, sqlite:obo:ncit
description: 'A disposition to undergo pathological processes that exists in an organism
  because of one or more disorders in that organism. For example: Beck-Fahrner syndrome,
  hereditary retinoblastoma, progeria, diabetes mellitus, infectious otitis media'
from_schema: http://w3id.org/ontogpt/maxo
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Disease
id_prefixes:
- MONDO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:mondo, sqlite:obo:hp, sqlite:obo:ncit
description: 'A disposition to undergo pathological processes that exists in an organism
  because of one or more disorders in that organism. For example: Beck-Fahrner syndrome,
  hereditary retinoblastoma, progeria, diabetes mellitus, infectious otitis media'
from_schema: http://w3id.org/ontogpt/maxo
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
    from_schema: http://w3id.org/ontogpt/maxo
    rank: 1000
    identifier: true
    alias: id
    owner: Disease
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
    from_schema: http://w3id.org/ontogpt/maxo
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Disease
    domain_of:
    - NamedEntity
    range: string

```
</details>