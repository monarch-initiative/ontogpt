

# Class: EnvironmentalExposure



URI: [alzrd:EnvironmentalExposure](http://w3id.org/ontogpt/alzrd_sectionEnvironmentalExposure)



```mermaid
erDiagram
EnvironmentalExposure {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **EnvironmentalExposure**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DocumentSection](DocumentSection.md) | [environmental_exposures](environmental_exposures.md) | range | [EnvironmentalExposure](EnvironmentalExposure.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* ENVO

* MESH






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:envo, sqlite:obo:mesh || prompt | The name of an environmental exposure or condition. Examples are "pesticides", "chronic stress", "air pollution", "heavy metals", "radiation", "heat stress". |



### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd_section




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:EnvironmentalExposure |
| native | alzrd:EnvironmentalExposure |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EnvironmentalExposure
id_prefixes:
- ENVO
- MESH
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:envo, sqlite:obo:mesh
  prompt:
    tag: prompt
    value: The name of an environmental exposure or condition. Examples are "pesticides",
      "chronic stress", "air pollution", "heavy metals", "radiation", "heat stress".
from_schema: http://w3id.org/ontogpt/alzrd_section
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: EnvironmentalExposure
id_prefixes:
- ENVO
- MESH
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:envo, sqlite:obo:mesh
  prompt:
    tag: prompt
    value: The name of an environmental exposure or condition. Examples are "pesticides",
      "chronic stress", "air pollution", "heavy metals", "radiation", "heat stress".
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
    owner: EnvironmentalExposure
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
    owner: EnvironmentalExposure
    domain_of:
    - NamedEntity
    range: string

```
</details>