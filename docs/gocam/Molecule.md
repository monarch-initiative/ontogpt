# Class: Molecule



URI: [gocam:Molecule](http://w3id.org/ontogpt/gocam/Molecule)


```mermaid
erDiagram
Molecule {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Molecule**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneMolecularActivityRelationship2](GeneMolecularActivityRelationship2.md) | [target](target.md) | range | [Molecule](Molecule.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CHEBI

* PR






### Annotations

| property | value |
| --- | --- |
| annotators | gilda:, sqlite:obo:chebi |



### Schema Source


* from schema: http://w3id.org/ontogpt/gocam





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gocam:Molecule |
| native | gocam:Molecule |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Molecule
id_prefixes:
- CHEBI
- PR
annotations:
  annotators:
    tag: annotators
    value: gilda:, sqlite:obo:chebi
from_schema: http://w3id.org/ontogpt/gocam
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Molecule
id_prefixes:
- CHEBI
- PR
annotations:
  annotators:
    tag: annotators
    value: gilda:, sqlite:obo:chebi
from_schema: http://w3id.org/ontogpt/gocam
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
    owner: Molecule
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
    owner: Molecule
    domain_of:
    - NamedEntity
    range: string

```
</details>