

# Class: NamedEntity


* __NOTE__: this is an abstract class and should not be instantiated directly


URI: [phenotype:NamedEntity](http://w3id.org/ontogpt/phenotype/NamedEntity)



```mermaid
erDiagram
NamedEntity {
    string id  
    string label  
}



```




## Inheritance
* **NamedEntity**
    * [Quality](Quality.md)
    * [ChemicalEntity](ChemicalEntity.md)
    * [AnatomicalEntity](AnatomicalEntity.md)
    * [RelationshipType](RelationshipType.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Triple](Triple.md) | [subject](subject.md) | range | [NamedEntity](NamedEntity.md) |
| [Triple](Triple.md) | [object](object.md) | range | [NamedEntity](NamedEntity.md) |
| [Triple](Triple.md) | [subject_qualifier](subject_qualifier.md) | range | [NamedEntity](NamedEntity.md) |
| [Triple](Triple.md) | [object_qualifier](object_qualifier.md) | range | [NamedEntity](NamedEntity.md) |
| [TextWithEntity](TextWithEntity.md) | [entities](entities.md) | range | [NamedEntity](NamedEntity.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/eq





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | phenotype:NamedEntity |
| native | phenotype:NamedEntity |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NamedEntity
from_schema: http://w3id.org/ontogpt/eq
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
    from_schema: http://w3id.org/ontogpt/eq
    rank: 1000
    identifier: true
    domain_of:
    - NamedEntity
    - Publication
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
    domain_of:
    - NamedEntity
    range: string

```
</details>

### Induced

<details>
```yaml
name: NamedEntity
from_schema: http://w3id.org/ontogpt/eq
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
    from_schema: http://w3id.org/ontogpt/eq
    rank: 1000
    identifier: true
    alias: id
    owner: NamedEntity
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
    owner: NamedEntity
    domain_of:
    - NamedEntity
    range: string

```
</details>