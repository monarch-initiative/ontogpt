

# Class: Action



URI: [recipe:Action](http://w3id.org/ontogpt/recipe/Action)



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
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Step](Step.md) | [action](action.md) | range | [Action](Action.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* dbpediaont

* FOODON






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:dbpediaont, sqlite:obo:foodon |



### Schema Source


* from schema: https://w3id.org/ontogpt/recipe





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | recipe:Action |
| native | recipe:Action |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Action
id_prefixes:
- dbpediaont
- FOODON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:dbpediaont, sqlite:obo:foodon
from_schema: https://w3id.org/ontogpt/recipe
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Action
id_prefixes:
- dbpediaont
- FOODON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:dbpediaont, sqlite:obo:foodon
from_schema: https://w3id.org/ontogpt/recipe
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
    from_schema: https://w3id.org/ontogpt/recipe
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
    from_schema: https://w3id.org/ontogpt/recipe
    aliases:
    - name
    slot_uri: rdfs:label
    alias: label
    owner: Action
    domain_of:
    - Recipe
    - NamedEntity
    range: string

```
</details>