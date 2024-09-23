# Class: Action


_A clinically prescribed procedure, therapy, intervention, or recommendation._





URI: [maxo_extract:Action](http://w3id.org/ontogpt/maxoAction)



```mermaid
erDiagram
Action {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Action**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MaxoAnnotations](MaxoAnnotations.md) | [action](action.md) | range | [Action](Action.md) |
| [ActionToDiseaseRelationship](ActionToDiseaseRelationship.md) | [subject](subject.md) | range | [Action](Action.md) |
| [ActionToSymptomRelationship](ActionToSymptomRelationship.md) | [subject](subject.md) | range | [Action](Action.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* MAXO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:maxo, sqlite:obo:ogms, sqlite:obo:ncit |



### Schema Source


* from schema: http://w3id.org/ontogpt/maxo





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | maxo_extract:Action |
| native | maxo_extract:Action |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Action
id_prefixes:
- MAXO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:maxo, sqlite:obo:ogms, sqlite:obo:ncit
description: A clinically prescribed procedure, therapy, intervention, or recommendation.
from_schema: http://w3id.org/ontogpt/maxo
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Action
id_prefixes:
- MAXO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:maxo, sqlite:obo:ogms, sqlite:obo:ncit
description: A clinically prescribed procedure, therapy, intervention, or recommendation.
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
    owner: Action
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
    owner: Action
    domain_of:
    - NamedEntity
    range: string

```
</details>