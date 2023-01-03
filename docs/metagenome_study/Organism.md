# Class: Organism



URI: [eg:Organism](http://w3id.org/ontogpt/environmental-metagenome/Organism)


```mermaid
 classDiagram
    class Organism
      NamedEntity <|-- Organism
      
      Organism : id
      Organism : label
      
```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Organism**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [organisms](organisms.md) | range | [Organism](Organism.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* NCBITaxon






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:ncbitaxon, gilda: |



### Schema Source


* from schema: http://w3id.org/ontogpt/metagenome





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | eg:Organism |
| native | eg:Organism |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organism
id_prefixes:
- NCBITaxon
annotations:
  annotators:
    tag: annotators
    value: 'sqlite:obo:ncbitaxon, gilda:'
from_schema: http://w3id.org/ontogpt/metagenome
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Organism
id_prefixes:
- NCBITaxon
annotations:
  annotators:
    tag: annotators
    value: 'sqlite:obo:ncbitaxon, gilda:'
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
    owner: Organism
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
    owner: Organism
    domain_of:
    - NamedEntity
    range: string

```
</details>