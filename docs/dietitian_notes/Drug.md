

# Class: Drug



URI: [dietitian_notes:Drug](dietitian_notes:Drug)



```mermaid
erDiagram
Drug {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Drug**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DrugTherapy](DrugTherapy.md) | [drug](drug.md) | range | [Drug](Drug.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* DRUGBANK

* CHEBI

* MESH






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:drugbank, sqlite:obo:chebi, sqlite:obo:mesh || prompt.examples | acetaminophen, ibuprofen, furosemide, insulin, heparin, warfarin |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:Drug |
| native | dietitian_notes:Drug |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Drug
id_prefixes:
- DRUGBANK
- CHEBI
- MESH
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:drugbank, sqlite:obo:chebi, sqlite:obo:mesh
  prompt.examples:
    tag: prompt.examples
    value: acetaminophen, ibuprofen, furosemide, insulin, heparin, warfarin
from_schema: http://w3id.org/ontogpt/dietician_notes
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Drug
id_prefixes:
- DRUGBANK
- CHEBI
- MESH
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:drugbank, sqlite:obo:chebi, sqlite:obo:mesh
  prompt.examples:
    tag: prompt.examples
    value: acetaminophen, ibuprofen, furosemide, insulin, heparin, warfarin
from_schema: http://w3id.org/ontogpt/dietician_notes
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
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    identifier: true
    alias: id
    owner: Drug
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
    from_schema: http://w3id.org/ontogpt/dietician_notes
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Drug
    domain_of:
    - NamedEntity
    range: string

```
</details>