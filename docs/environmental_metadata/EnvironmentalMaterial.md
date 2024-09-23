

# Class: EnvironmentalMaterial



URI: [envmd:EnvironmentalMaterial](http://w3id.org/ontogpt/environmental-metadataEnvironmentalMaterial)



```mermaid
erDiagram
EnvironmentalMaterial {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **EnvironmentalMaterial**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Dataset](Dataset.md) | [environmental_material](environmental_material.md) | range | [EnvironmentalMaterial](EnvironmentalMaterial.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* ENVO

* ENVTHES






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:envo, bioportal:ENVTHES |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-metadata





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | envmd:EnvironmentalMaterial |
| native | envmd:EnvironmentalMaterial |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EnvironmentalMaterial
id_prefixes:
- ENVO
- ENVTHES
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:envo, bioportal:ENVTHES
from_schema: http://w3id.org/ontogpt/environmental-metadata
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: EnvironmentalMaterial
id_prefixes:
- ENVO
- ENVTHES
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:envo, bioportal:ENVTHES
from_schema: http://w3id.org/ontogpt/environmental-metadata
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
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    identifier: true
    alias: id
    owner: EnvironmentalMaterial
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
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: EnvironmentalMaterial
    domain_of:
    - NamedEntity
    range: string

```
</details>