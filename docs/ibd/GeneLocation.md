

# Class: GeneLocation



URI: [gocam:GeneLocation](http://w3id.org/ontogpt/gocam/GeneLocation)



```mermaid
erDiagram
GeneLocation {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **GeneLocation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneSubcellularLocalizationRelationship](GeneSubcellularLocalizationRelationship.md) | [location](location.md) | range | [GeneLocation](GeneLocation.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* GO

* CL

* UBERON






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go, sqlite:obo:cl |



### Schema Source


* from schema: http://w3id.org/ontogpt/gocam





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gocam:GeneLocation |
| native | gocam:GeneLocation |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneLocation
id_prefixes:
- GO
- CL
- UBERON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go, sqlite:obo:cl
from_schema: http://w3id.org/ontogpt/gocam
is_a: NamedEntity
slot_usage:
  id:
    name: id
    values_from:
    - GOCellComponentType
    - CellType
    domain_of:
    - NamedEntity
    - Publication

```
</details>

### Induced

<details>
```yaml
name: GeneLocation
id_prefixes:
- GO
- CL
- UBERON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go, sqlite:obo:cl
from_schema: http://w3id.org/ontogpt/gocam
is_a: NamedEntity
slot_usage:
  id:
    name: id
    values_from:
    - GOCellComponentType
    - CellType
    domain_of:
    - NamedEntity
    - Publication
attributes:
  id:
    name: id
    description: A unique identifier for the named entity
    from_schema: http://w3id.org/ontogpt/gocam
    rank: 1000
    values_from:
    - GOCellComponentType
    - CellType
    identifier: true
    alias: id
    owner: GeneLocation
    domain_of:
    - NamedEntity
    - Publication
    range: string
    required: true
  label:
    name: label
    annotations:
      owl:
        tag: owl
        value: AnnotationProperty, AnnotationAssertion
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/gocam
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: GeneLocation
    domain_of:
    - NamedEntity
    range: string

```
</details>