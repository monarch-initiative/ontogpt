# Class: OntologyClass



URI: [oc:OntologyClass](http://w3id.org/ontogpt/ontology-class-templateOntologyClass)


```mermaid
erDiagram
OntologyClass {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **OntologyClass**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [OntologyIssue](OntologyIssue.md) | [domains](domains.md) | range | [OntologyClass](OntologyClass.md) |
| [OntologyProblem](OntologyProblem.md) | [about](about.md) | range | [OntologyClass](OntologyClass.md) |
| [OntologyChange](OntologyChange.md) | [about](about.md) | range | [OntologyClass](OntologyClass.md) |






## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go |



### Schema Source


* from schema: https://w3id.org/ontogpt/ontology_issue





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oc:OntologyClass |
| native | oc:OntologyClass |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OntologyClass
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
from_schema: https://w3id.org/ontogpt/ontology_issue
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: OntologyClass
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
from_schema: https://w3id.org/ontogpt/ontology_issue
rank: 1000
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
    from_schema: https://w3id.org/ontogpt/ontology_issue
    rank: 1000
    identifier: true
    alias: id
    owner: OntologyClass
    domain_of:
    - NamedEntity
    - Publication
    range: string
  label:
    name: label
    annotations:
      owl:
        tag: owl
        value: AnnotationProperty, AnnotationAssertion
    description: The label (name) of the named thing
    from_schema: https://w3id.org/ontogpt/ontology_issue
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: OntologyClass
    domain_of:
    - NamedEntity
    range: string

```
</details>