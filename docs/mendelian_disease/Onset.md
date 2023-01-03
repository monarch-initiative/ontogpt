# Class: Onset



URI: [mendelian_disease:Onset](http://w3id.org/ontogpt/mendelian_disease/Onset)


```mermaid
 classDiagram
    class Onset
      NamedEntity <|-- Onset
      
      Onset : decades
      Onset : id
      Onset : juvenile_or_adult
      Onset : label
      Onset : years_old
      
```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Onset**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [years_old](years_old.md) | 0..1 <br/> NONE |  | direct |
| [decades](decades.md) | 0..* <br/> NONE |  | direct |
| [juvenile_or_adult](juvenile_or_adult.md) | 0..1 <br/> NONE |  | direct |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MendelianDisease](MendelianDisease.md) | [disease_onsets](disease_onsets.md) | range | [Onset](Onset.md) |
| [Symptom](Symptom.md) | [onset_of_symptom](onset_of_symptom.md) | range | [Onset](Onset.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HP






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:hp, sqlite:obo:hsapdv |



### Schema Source


* from schema: http://w3id.org/ontogpt/mendelian_disease





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mendelian_disease:Onset |
| native | mendelian_disease:Onset |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Onset
id_prefixes:
- HP
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hp, sqlite:obo:hsapdv
from_schema: http://w3id.org/ontogpt/mendelian_disease
rank: 1000
is_a: NamedEntity
attributes:
  years_old:
    name: years_old
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
  decades:
    name: decades
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
    multivalued: true
  juvenile_or_adult:
    name: juvenile_or_adult
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000

```
</details>

### Induced

<details>
```yaml
name: Onset
id_prefixes:
- HP
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hp, sqlite:obo:hsapdv
from_schema: http://w3id.org/ontogpt/mendelian_disease
rank: 1000
is_a: NamedEntity
attributes:
  years_old:
    name: years_old
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
    alias: years_old
    owner: Onset
    domain_of:
    - Onset
    range: string
  decades:
    name: decades
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
    multivalued: true
    alias: decades
    owner: Onset
    domain_of:
    - Onset
    range: string
  juvenile_or_adult:
    name: juvenile_or_adult
    from_schema: http://w3id.org/ontogpt/mendelian_disease
    rank: 1000
    alias: juvenile_or_adult
    owner: Onset
    domain_of:
    - Onset
    range: string
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
    owner: Onset
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
    owner: Onset
    domain_of:
    - NamedEntity
    range: string

```
</details>