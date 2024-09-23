

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
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





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
is_a: NamedEntity
slot_usage:
  id:
    name: id
    values_from:
    - MeshChemicalIdentifier
    domain_of:
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
is_a: NamedEntity
slot_usage:
  id:
    name: id
    values_from:
    - MeshChemicalIdentifier
    domain_of:
    - NamedEntity
    - Publication
    pattern: ^MESH:[CD][0-9]{6}$
attributes:
  id:
    name: id
    description: A unique identifier for the named entity
    from_schema: http://w3id.org/ontogpt/ctd
    rank: 1000
    values_from:
    - MeshChemicalIdentifier
    identifier: true
    alias: id
    owner: Chemical
    domain_of:
    - NamedEntity
    - Publication
    range: string
    required: true
    pattern: ^MESH:[CD][0-9]{6}$
  label:
    name: label
    annotations:
      owl:
        tag: owl
        value: AnnotationProperty, AnnotationAssertion
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/ctd
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Chemical
    domain_of:
    - NamedEntity
    range: string

```
</details>