# Class: MolecularActivity



URI: [bp:MolecularActivity](http://w3id.org/ontogpt/biological-process-templateMolecularActivity)


```mermaid
 classDiagram
    class MolecularActivity
      NamedEntity <|-- MolecularActivity
      
      MolecularActivity : id
      MolecularActivity : label
      
```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **MolecularActivity**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [BiologicalProcess](BiologicalProcess.md) | [steps](steps.md) | range | [MolecularActivity](MolecularActivity.md) |
| [GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md) | [molecular_activity](molecular_activity.md) | range | [MolecularActivity](MolecularActivity.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* GO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go |



### Schema Source


* from schema: https://w3id.org/ontogpt/biological_process





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bp:MolecularActivity |
| native | bp:MolecularActivity |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MolecularActivity
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
from_schema: https://w3id.org/ontogpt/biological_process
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: MolecularActivity
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
from_schema: https://w3id.org/ontogpt/biological_process
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
    owner: MolecularActivity
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
    alias: label
    owner: MolecularActivity
    domain_of:
    - BiologicalProcess
    - NamedEntity
    range: string

```
</details>