

# Class: ChemicalEntity



URI: [reaction:ChemicalEntity](http://w3id.org/ontogpt/reaction/ChemicalEntity)



```mermaid
erDiagram
ChemicalEntity {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **ChemicalEntity**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Reaction](Reaction.md) | [left_side](left_side.md) | range | [ChemicalEntity](ChemicalEntity.md) |
| [Reaction](Reaction.md) | [right_side](right_side.md) | range | [ChemicalEntity](ChemicalEntity.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CHEBI






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:chebi |



### Schema Source


* from schema: https://w3id.org/ontogpt/reaction




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | reaction:ChemicalEntity |
| native | reaction:ChemicalEntity |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChemicalEntity
id_prefixes:
- CHEBI
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:chebi
from_schema: https://w3id.org/ontogpt/reaction
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: ChemicalEntity
id_prefixes:
- CHEBI
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:chebi
from_schema: https://w3id.org/ontogpt/reaction
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
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    identifier: true
    alias: id
    owner: ChemicalEntity
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
    from_schema: https://w3id.org/ontogpt/reaction
    aliases:
    - name
    slot_uri: rdfs:label
    alias: label
    owner: ChemicalEntity
    domain_of:
    - Reaction
    - NamedEntity
    range: string

```
</details>