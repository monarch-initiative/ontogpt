

# Class: Quality



URI: [phenotype:Quality](http://w3id.org/ontogpt/phenotype/Quality)



```mermaid
erDiagram
Quality {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Quality**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Trait](Trait.md) | [quality](quality.md) | range | [Quality](Quality.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* PATO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:pato |



### Schema Source


* from schema: http://w3id.org/ontogpt/eq





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phenotype:Quality |
| native | phenotype:Quality |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Quality
id_prefixes:
- PATO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:pato
from_schema: http://w3id.org/ontogpt/eq
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Quality
id_prefixes:
- PATO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:pato
from_schema: http://w3id.org/ontogpt/eq
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
    from_schema: http://w3id.org/ontogpt/eq
    rank: 1000
    identifier: true
    alias: id
    owner: Quality
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
    from_schema: http://w3id.org/ontogpt/eq
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Quality
    domain_of:
    - NamedEntity
    range: string

```
</details>