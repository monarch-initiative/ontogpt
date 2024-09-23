

# Class: EnvironmentalCondition



URI: [desiccation:EnvironmentalCondition](http://w3id.org/ontogpt/desiccationEnvironmentalCondition)



```mermaid
erDiagram
EnvironmentalCondition {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **EnvironmentalCondition**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [EntityContainingDocument](EntityContainingDocument.md) | [environmental_conditions](environmental_conditions.md) | range | [EnvironmentalCondition](EnvironmentalCondition.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* PECO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:peco || prompt | the name of an environmental treatment.
 Examples are drought, salt stress, cold tolerance. |



### Schema Source


* from schema: http://w3id.org/ontogpt/desiccation





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | desiccation:EnvironmentalCondition |
| native | desiccation:EnvironmentalCondition |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EnvironmentalCondition
id_prefixes:
- PECO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:peco
  prompt:
    tag: prompt
    value: "the name of an environmental treatment.\n Examples are drought, salt stress,\
      \ cold tolerance."
from_schema: http://w3id.org/ontogpt/desiccation
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: EnvironmentalCondition
id_prefixes:
- PECO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:peco
  prompt:
    tag: prompt
    value: "the name of an environmental treatment.\n Examples are drought, salt stress,\
      \ cold tolerance."
from_schema: http://w3id.org/ontogpt/desiccation
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
    from_schema: http://w3id.org/ontogpt/desiccation
    rank: 1000
    identifier: true
    alias: id
    owner: EnvironmentalCondition
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
    from_schema: http://w3id.org/ontogpt/desiccation
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: EnvironmentalCondition
    domain_of:
    - NamedEntity
    range: string

```
</details>