# Class: Symptom



URI: [mendelian_disease:Symptom](http://w3id.org/ontogpt/mendelian_disease/Symptom)


```mermaid
 classDiagram
    class Symptom
      NamedEntity <|-- Symptom
      
      Symptom : affects
      Symptom : characteristic
      Symptom : id
      Symptom : label
      Symptom : onset_of_symptom
      Symptom : severity
      
```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Symptom**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [characteristic](characteristic.md) | 0..1 <br/> NONE |  | direct |
| [affects](affects.md) | 0..1 <br/> NONE |  | direct |
| [severity](severity.md) | 0..1 <br/> NONE |  | direct |
| [onset_of_symptom](onset_of_symptom.md) | 0..1 <br/> [Onset](Onset.md) |  | direct |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MendelianDisease](MendelianDisease.md) | [symptoms](symptoms.md) | range | [Symptom](Symptom.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HP






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:hp, sqlite:obo:mondo |



### Schema Source


* from schema: http://w3id.org/ontogpt/mendelian_disease





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mendelian_disease:Symptom |
| native | mendelian_disease:Symptom |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Symptom
id_prefixes:
- HP
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hp, sqlite:obo:mondo
from_schema: http://w3id.org/ontogpt/mendelian_disease
rank: 1000
is_a: NamedEntity
attributes:
  characteristic:
    name: characteristic
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
  affects:
    name: affects
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
  severity:
    name: severity
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
  onset_of_symptom:
    name: onset_of_symptom
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
    range: Onset

```
</details>

### Induced

<details>
```yaml
name: Symptom
id_prefixes:
- HP
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hp, sqlite:obo:mondo
from_schema: http://w3id.org/ontogpt/mendelian_disease
rank: 1000
is_a: NamedEntity
attributes:
  characteristic:
    name: characteristic
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
    alias: characteristic
    owner: Symptom
    domain_of:
    - Symptom
    range: string
  affects:
    name: affects
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
    alias: affects
    owner: Symptom
    domain_of:
    - Symptom
    range: string
  severity:
    name: severity
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
    alias: severity
    owner: Symptom
    domain_of:
    - Symptom
    range: string
  onset_of_symptom:
    name: onset_of_symptom
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
    alias: onset_of_symptom
    owner: Symptom
    domain_of:
    - Symptom
    range: Onset
  id:
    name: id
    annotations:
      prompt.skip:
        tag: prompt.skip
        value: 'true'
    description: A unique identifier for the named entity
    comments:
    - this is populated during the grounding and normalization step
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    identifier: true
    alias: id
    owner: Symptom
    domain_of:
    - NamedEntity
    - Publication
    range: string
  label:
    name: label
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/core
    aliases:
    - name
    rank: 1000
    alias: label
    owner: Symptom
    domain_of:
    - NamedEntity
    range: string

```
</details>