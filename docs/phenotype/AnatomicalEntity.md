

# Class: AnatomicalEntity



URI: [phenotype:AnatomicalEntity](http://w3id.org/ontogpt/phenotype/AnatomicalEntity)



```mermaid
erDiagram
AnatomicalEntity {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **AnatomicalEntity**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Trait](Trait.md) | [anatomical_entity](anatomical_entity.md) | range | [AnatomicalEntity](AnatomicalEntity.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* UBERON






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:uberon |



### Schema Source


* from schema: http://w3id.org/ontogpt/eq





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phenotype:AnatomicalEntity |
| native | phenotype:AnatomicalEntity |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnatomicalEntity
id_prefixes:
- UBERON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:uberon
from_schema: http://w3id.org/ontogpt/eq
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: AnatomicalEntity
id_prefixes:
- UBERON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:uberon
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
    owner: AnatomicalEntity
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
    owner: AnatomicalEntity
    domain_of:
    - NamedEntity
    range: string

```
</details>