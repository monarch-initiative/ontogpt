# Class: Gene



URI: [mendelian_disease:Gene](http://w3id.org/ontogpt/mendelian_disease/Gene)


```mermaid
erDiagram
Gene {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Gene**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MendelianDisease](MendelianDisease.md) | [genes](genes.md) | range | [Gene](Gene.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HGNC






### Annotations

| property | value |
| --- | --- |
| annotators | gilda:, bioportal:hgnc-nr, sqlite:obo:pr |



### Schema Source


* from schema: http://w3id.org/ontogpt/mendelian_disease





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mendelian_disease:Gene |
| native | mendelian_disease:Gene |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gene
id_prefixes:
- HGNC
annotations:
  annotators:
    tag: annotators
    value: gilda:, bioportal:hgnc-nr, sqlite:obo:pr
from_schema: http://w3id.org/ontogpt/mendelian_disease
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Gene
id_prefixes:
- HGNC
annotations:
  annotators:
    tag: annotators
    value: gilda:, bioportal:hgnc-nr, sqlite:obo:pr
from_schema: http://w3id.org/ontogpt/mendelian_disease
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
    owner: Gene
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
    owner: Gene
    domain_of:
    - NamedEntity
    range: string

```
</details>