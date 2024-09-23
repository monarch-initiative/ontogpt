

# Class: AdverseEffect



URI: [treatment:AdverseEffect](http://w3id.org/ontogpt/treatments/AdverseEffect)



```mermaid
erDiagram
AdverseEffect {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **AdverseEffect**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TreatmentAdverseEffect](TreatmentAdverseEffect.md) | [adverse_effects](adverse_effects.md) | range | [AdverseEffect](AdverseEffect.md) |






## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:hp, sqlite:obo:ncit |



### Schema Source


* from schema: http://w3id.org/ontogpt/treatment





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | treatment:AdverseEffect |
| native | treatment:AdverseEffect |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AdverseEffect
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hp, sqlite:obo:ncit
from_schema: http://w3id.org/ontogpt/treatment
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: AdverseEffect
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hp, sqlite:obo:ncit
from_schema: http://w3id.org/ontogpt/treatment
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
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    identifier: true
    alias: id
    owner: AdverseEffect
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
    from_schema: http://w3id.org/ontogpt/treatment
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: AdverseEffect
    domain_of:
    - NamedEntity
    range: string

```
</details>