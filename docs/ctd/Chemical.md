# Class: Chemical



URI: [drug:Chemical](http://w3id.org/ontogpt/drug/Chemical)


```mermaid
erDiagram
Chemical {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Chemical**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md) | [subject](subject.md) | range | [Chemical](Chemical.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* MESH






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:mesh, sqlite:obo:chebi, sqlite:obo:ncit, bioportal:mdm, sqlite:obo:drugbank, gilda: || prompt.examples | Lidocaine, Hydroxychloroquine, Methyldopa, Imatinib |



### Schema Source


* from schema: http://w3id.org/ontogpt/ctd





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | drug:Chemical |
| native | drug:Chemical |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Chemical
id_prefixes:
- MESH
annotations:
  annotators:
    tag: annotators
    value: 'sqlite:obo:mesh, sqlite:obo:chebi, sqlite:obo:ncit, bioportal:mdm, sqlite:obo:drugbank,
      gilda:'
  prompt.examples:
    tag: prompt.examples
    value: Lidocaine, Hydroxychloroquine, Methyldopa, Imatinib
from_schema: http://w3id.org/ontogpt/ctd
rank: 1000
is_a: NamedEntity
slot_usage:
  id:
    name: id
    values_from:
    - MeshChemicalIdentifier
    domain_of:
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    pattern: ^MESH:[CD][0-9]{6}$

```
</details>

### Induced

<details>
```yaml
name: Chemical
id_prefixes:
- MESH
annotations:
  annotators:
    tag: annotators
    value: 'sqlite:obo:mesh, sqlite:obo:chebi, sqlite:obo:ncit, bioportal:mdm, sqlite:obo:drugbank,
      gilda:'
  prompt.examples:
    tag: prompt.examples
    value: Lidocaine, Hydroxychloroquine, Methyldopa, Imatinib
from_schema: http://w3id.org/ontogpt/ctd
rank: 1000
is_a: NamedEntity
slot_usage:
  id:
    name: id
    values_from:
    - MeshChemicalIdentifier
    domain_of:
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    pattern: ^MESH:[CD][0-9]{6}$
attributes:
  id:
    name: id
    description: A unique identifier for the named entity
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    values_from:
    - MeshChemicalIdentifier
    identifier: true
    alias: id
    owner: Chemical
    domain_of:
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    - NamedEntity
    - Publication
    range: string
    pattern: ^MESH:[CD][0-9]{6}$
  label:
    name: label
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/core
    aliases:
    - name
    rank: 1000
    alias: label
    owner: Chemical
    domain_of:
    - NamedEntity
    range: string

```
</details>