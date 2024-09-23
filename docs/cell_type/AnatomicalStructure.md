

# Class: AnatomicalStructure



URI: [cell_type:AnatomicalStructure](http://w3id.org/ontogpt/cell_type/AnatomicalStructure)



```mermaid
erDiagram
AnatomicalStructure {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **AnatomicalStructure**
        * [BrainRegion](BrainRegion.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CellType](CellType.md) | [localizations](localizations.md) | range | [AnatomicalStructure](AnatomicalStructure.md) |
| [ImmuneCell](ImmuneCell.md) | [localizations](localizations.md) | range | [AnatomicalStructure](AnatomicalStructure.md) |
| [Neuron](Neuron.md) | [localizations](localizations.md) | range | [AnatomicalStructure](AnatomicalStructure.md) |
| [Interneuron](Interneuron.md) | [localizations](localizations.md) | range | [AnatomicalStructure](AnatomicalStructure.md) |






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
| self | cell_type:AnatomicalStructure |
| native | cell_type:AnatomicalStructure |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnatomicalStructure
id_prefixes:
- UBERON
- FBbt
- WBbt
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:uberon, sqlite:obo:fbbt, sqlite:obo:wbbt
from_schema: http://w3id.org/ontogpt/cell_type
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: AnatomicalStructure
id_prefixes:
- UBERON
- FBbt
- WBbt
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:uberon, sqlite:obo:fbbt, sqlite:obo:wbbt
from_schema: http://w3id.org/ontogpt/cell_type
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
    from_schema: http://w3id.org/ontogpt/cell_type
    identifier: true
    alias: id
    owner: AnatomicalStructure
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
    owner: AnatomicalStructure
    domain_of:
    - CellType
    - NamedEntity
    range: string

```
</details>