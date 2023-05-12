# Class: Unit



URI: [diag:Unit](http://w3id.org/ontogpt/diagnostic_procedure/Unit)


```mermaid
erDiagram
Unit {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Unit**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ClinicalAttribute](ClinicalAttribute.md) | [unit](unit.md) | range | [Unit](Unit.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* UO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:uo |



### Schema Source


* from schema: http://w3id.org/ontogpt/diagnostic_procedure





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | diag:Unit |
| native | diag:Unit |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Unit
id_prefixes:
- UO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:uo
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Unit
id_prefixes:
- UO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:uo
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
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
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    identifier: true
    alias: id
    owner: Unit
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
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Unit
    domain_of:
    - NamedEntity
    range: string

```
</details>