

# Class: Ontology


_a single ontology name or abbreviation._





URI: [onto_usage:Ontology](http://w3id.org/ontogpt/onto_usageOntology)



```mermaid
erDiagram
Ontology {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Ontology**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Document](Document.md) | [ontologies](ontologies.md) | range | [Ontology](Ontology.md) |
| [UseCase](UseCase.md) | [ontology](ontology.md) | range | [Ontology](Ontology.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/onto_usage




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | onto_usage:Ontology |
| native | onto_usage:Ontology |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Ontology
description: a single ontology name or abbreviation.
from_schema: http://w3id.org/ontogpt/onto_usage
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Ontology
description: a single ontology name or abbreviation.
from_schema: http://w3id.org/ontogpt/onto_usage
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
    from_schema: http://w3id.org/ontogpt/onto_usage
    rank: 1000
    identifier: true
    alias: id
    owner: Ontology
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
    from_schema: http://w3id.org/ontogpt/onto_usage
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Ontology
    domain_of:
    - NamedEntity
    range: string

```
</details>