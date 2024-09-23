

# Class: Disease



URI: [alzrd:Disease](http://w3id.org/ontogpt/alzrdDisease)



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
| [Document](Document.md) | [diseases](diseases.md) | range | [Disease](Disease.md) |
| [ExperimentalMetricToDiseaseRelationship](ExperimentalMetricToDiseaseRelationship.md) | [disease](disease.md) | range | [Disease](Disease.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* MONDO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:mondo || prompt | The name of a disease or condition. Examples are Alzheimer's disease, Parkinson's disease, Huntington's disease. |



### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:Disease |
| native | alzrd:Disease |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Disease
id_prefixes:
- MONDO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:mondo
  prompt:
    tag: prompt
    value: The name of a disease or condition. Examples are Alzheimer's disease, Parkinson's
      disease, Huntington's disease.
from_schema: http://w3id.org/ontogpt/alzrd
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Disease
id_prefixes:
- MONDO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:mondo
  prompt:
    tag: prompt
    value: The name of a disease or condition. Examples are Alzheimer's disease, Parkinson's
      disease, Huntington's disease.
from_schema: http://w3id.org/ontogpt/alzrd
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
    from_schema: http://w3id.org/ontogpt/alzrd
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
    from_schema: http://w3id.org/ontogpt/alzrd
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