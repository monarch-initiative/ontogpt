

# Class: Variable



URI: [eg:Variable](http://w3id.org/ontogpt/environmental-metagenome/Variable)



```mermaid
erDiagram
Variable {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Variable**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [variables](variables.md) | range | [Variable](Variable.md) |
| [CausalRelationship](CausalRelationship.md) | [cause](cause.md) | range | [Variable](Variable.md) |
| [CausalRelationship](CausalRelationship.md) | [effect](effect.md) | range | [Variable](Variable.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* ENVO

* MIXS

* PATO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:envo, bioportal:bero |



### Schema Source


* from schema: http://w3id.org/ontogpt/metagenome





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | eg:Variable |
| native | eg:Variable |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Variable
id_prefixes:
- ENVO
- MIXS
- PATO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:envo, bioportal:bero
from_schema: http://w3id.org/ontogpt/metagenome
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Variable
id_prefixes:
- ENVO
- MIXS
- PATO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:envo, bioportal:bero
from_schema: http://w3id.org/ontogpt/metagenome
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
    from_schema: http://w3id.org/ontogpt/metagenome
    rank: 1000
    identifier: true
    alias: id
    owner: Variable
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
    from_schema: http://w3id.org/ontogpt/metagenome
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Variable
    domain_of:
    - NamedEntity
    range: string

```
</details>