

# Class: ChemicalExposure



URI: [ibdlit:ChemicalExposure](http://w3id.org/ontogpt/ibd_literature/ChemicalExposure)



```mermaid
erDiagram
ChemicalExposure {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **ChemicalExposure**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IBDAnnotations](IBDAnnotations.md) | [exposures](exposures.md) | range | [ChemicalExposure](ChemicalExposure.md) |
| [GeneExposureRelationship](GeneExposureRelationship.md) | [subject](subject.md) | range | [ChemicalExposure](ChemicalExposure.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CHEBI

* ECTO

* ExO

* NCIT






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:ecto, sqlite:obo:chebi || prompt | the name of the exposure, such as a exposure to a chemical toxin. For example, CHEBI:17968 butyrate. |



### Schema Source


* from schema: http://w3id.org/ontogpt/ibd_literature





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ibdlit:ChemicalExposure |
| native | ibdlit:ChemicalExposure |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChemicalExposure
id_prefixes:
- CHEBI
- ECTO
- ExO
- NCIT
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:ecto, sqlite:obo:chebi
  prompt:
    tag: prompt
    value: the name of the exposure, such as a exposure to a chemical toxin. For example,
      CHEBI:17968 butyrate.
from_schema: http://w3id.org/ontogpt/ibd_literature
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: ChemicalExposure
id_prefixes:
- CHEBI
- ECTO
- ExO
- NCIT
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:ecto, sqlite:obo:chebi
  prompt:
    tag: prompt
    value: the name of the exposure, such as a exposure to a chemical toxin. For example,
      CHEBI:17968 butyrate.
from_schema: http://w3id.org/ontogpt/ibd_literature
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
    from_schema: http://w3id.org/ontogpt/ibd_literature
    rank: 1000
    identifier: true
    alias: id
    owner: ChemicalExposure
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
    from_schema: http://w3id.org/ontogpt/ibd_literature
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: ChemicalExposure
    domain_of:
    - NamedEntity
    range: string

```
</details>