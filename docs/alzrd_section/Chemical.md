

# Class: Chemical



URI: [alzrd:Chemical](http://w3id.org/ontogpt/alzrd_sectionChemical)



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
| [DocumentSection](DocumentSection.md) | [chemical](chemical.md) | range | [Chemical](Chemical.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CHEBI

* MESH






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:chebi, sqlite:obo:mesh || prompt | The name of a chemical, drug, or other substance. Examples are "donepezil", "Aβ42", "Aβ40", "tau", "insulin", "caffeine", "nicotine", "alcohol". |



### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd_section




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:Chemical |
| native | alzrd:Chemical |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Chemical
id_prefixes:
- CHEBI
- MESH
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:chebi, sqlite:obo:mesh
  prompt:
    tag: prompt
    value: The name of a chemical, drug, or other substance. Examples are "donepezil",
      "Aβ42", "Aβ40", "tau", "insulin", "caffeine", "nicotine", "alcohol".
from_schema: http://w3id.org/ontogpt/alzrd_section
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Chemical
id_prefixes:
- CHEBI
- MESH
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:chebi, sqlite:obo:mesh
  prompt:
    tag: prompt
    value: The name of a chemical, drug, or other substance. Examples are "donepezil",
      "Aβ42", "Aβ40", "tau", "insulin", "caffeine", "nicotine", "alcohol".
from_schema: http://w3id.org/ontogpt/alzrd_section
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
    from_schema: http://w3id.org/ontogpt/alzrd_section
    rank: 1000
    identifier: true
    alias: id
    owner: Chemical
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
    from_schema: http://w3id.org/ontogpt/alzrd_section
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