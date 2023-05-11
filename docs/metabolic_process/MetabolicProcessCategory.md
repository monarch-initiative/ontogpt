# Class: MetabolicProcessCategory



URI: [bp:MetabolicProcessCategory](http://w3id.org/ontogpt/metabolic-process-templateMetabolicProcessCategory)


```mermaid
erDiagram
MetabolicProcessCategory {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **MetabolicProcessCategory**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MetabolicProcess](MetabolicProcess.md) | [subclass_of](subclass_of.md) | range | [MetabolicProcessCategory](MetabolicProcessCategory.md) |
| [MetabolicProcess](MetabolicProcess.md) | [category](category.md) | range | [MetabolicProcessCategory](MetabolicProcessCategory.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* GO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go |



### Schema Source


* from schema: https://w3id.org/ontogpt/metabolic_process





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bp:MetabolicProcessCategory |
| native | bp:MetabolicProcessCategory |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MetabolicProcessCategory
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
from_schema: https://w3id.org/ontogpt/metabolic_process
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: MetabolicProcessCategory
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
from_schema: https://w3id.org/ontogpt/metabolic_process
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
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    identifier: true
    alias: id
    owner: MetabolicProcessCategory
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
    from_schema: https://w3id.org/ontogpt/metabolic_process
    aliases:
    - name
    slot_uri: rdfs:label
    alias: label
    owner: MetabolicProcessCategory
    domain_of:
    - MetabolicProcess
    - NamedEntity
    range: string

```
</details>