

# Class: BrainRegion



URI: [cell_type:BrainRegion](http://w3id.org/ontogpt/cell_type/BrainRegion)



```mermaid
erDiagram
BrainRegion {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * [AnatomicalStructure](AnatomicalStructure.md)
        * **BrainRegion**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Interneuron](Interneuron.md) | [projects_to_or_from](projects_to_or_from.md) | range | [BrainRegion](BrainRegion.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* UBERON

* FBbt

* WBbt






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:uberon, sqlite:obo:fbbt, sqlite:obo:wbbt |



### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cell_type:BrainRegion |
| native | cell_type:BrainRegion |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BrainRegion
id_prefixes:
- UBERON
- FBbt
- WBbt
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:uberon, sqlite:obo:fbbt, sqlite:obo:wbbt
from_schema: http://w3id.org/ontogpt/cell_type
is_a: AnatomicalStructure
slot_usage:
  id:
    name: id
    values_from:
    - BrainRegionIdentifier
    identifier: true
    domain_of:
    - CellType
    - NamedEntity
    - Publication

```
</details>

### Induced

<details>
```yaml
name: BrainRegion
id_prefixes:
- UBERON
- FBbt
- WBbt
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:uberon, sqlite:obo:fbbt, sqlite:obo:wbbt
from_schema: http://w3id.org/ontogpt/cell_type
is_a: AnatomicalStructure
slot_usage:
  id:
    name: id
    values_from:
    - BrainRegionIdentifier
    identifier: true
    domain_of:
    - CellType
    - NamedEntity
    - Publication
attributes:
  id:
    name: id
    description: A unique identifier for the named entity
    from_schema: http://w3id.org/ontogpt/cell_type
    values_from:
    - BrainRegionIdentifier
    identifier: true
    alias: id
    owner: BrainRegion
    domain_of:
    - CellType
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
    from_schema: http://w3id.org/ontogpt/cell_type
    aliases:
    - name
    slot_uri: rdfs:label
    alias: label
    owner: BrainRegion
    domain_of:
    - CellType
    - NamedEntity
    range: string

```
</details>