# Class: SequencingTechnology



URI: [eg:SequencingTechnology](http://w3id.org/ontogpt/environmental-metagenome/SequencingTechnology)


```mermaid
 classDiagram
    class SequencingTechnology
      NamedEntity <|-- SequencingTechnology
      
      SequencingTechnology : id
      SequencingTechnology : label
      
```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **SequencingTechnology**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [sequencing_technologies](sequencing_technologies.md) | range | [SequencingTechnology](SequencingTechnology.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* IDO

* EFO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:obi, sqlite:obo:efo, bioportal:bero |



### Schema Source


* from schema: http://w3id.org/ontogpt/metagenome





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | eg:SequencingTechnology |
| native | eg:SequencingTechnology |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SequencingTechnology
id_prefixes:
- IDO
- EFO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:obi, sqlite:obo:efo, bioportal:bero
from_schema: http://w3id.org/ontogpt/metagenome
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: SequencingTechnology
id_prefixes:
- IDO
- EFO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:obi, sqlite:obo:efo, bioportal:bero
from_schema: http://w3id.org/ontogpt/metagenome
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
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    identifier: true
    alias: id
    owner: SequencingTechnology
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
    owner: SequencingTechnology
    domain_of:
    - NamedEntity
    range: string

```
</details>