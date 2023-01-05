# Class: EnvironmentalMaterial



URI: [sample:EnvironmentalMaterial](http://w3id.org/ontogpt/environmental-sample/EnvironmentalMaterial)


```mermaid
erDiagram
EnvironmentalMaterial {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **EnvironmentalMaterial**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [environmental_material](environmental_material.md) | range | [EnvironmentalMaterial](EnvironmentalMaterial.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* ENVO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:envo |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sample:EnvironmentalMaterial |
| native | sample:EnvironmentalMaterial |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EnvironmentalMaterial
id_prefixes:
- ENVO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:envo
from_schema: http://w3id.org/ontogpt/environmental-sample
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: EnvironmentalMaterial
id_prefixes:
- ENVO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:envo
from_schema: http://w3id.org/ontogpt/environmental-sample
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
    owner: EnvironmentalMaterial
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
    owner: EnvironmentalMaterial
    domain_of:
    - NamedEntity
    range: string

```
</details>