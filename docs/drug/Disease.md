

# Class: Disease



URI: [drug:Disease](http://w3id.org/ontogpt/drug/Disease)



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
| [DrugMechanism](DrugMechanism.md) | [disease](disease.md) | range | [Disease](Disease.md) |






## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:mesh, sqlite:obo:mondo |



### Schema Source


* from schema: http://w3id.org/ontogpt/drug





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | drug:Disease |
| native | drug:Disease |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Disease
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:mesh, sqlite:obo:mondo
from_schema: http://w3id.org/ontogpt/drug
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Disease
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:mesh, sqlite:obo:mondo
from_schema: http://w3id.org/ontogpt/drug
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
    from_schema: http://w3id.org/ontogpt/drug
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
    from_schema: http://w3id.org/ontogpt/drug
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