

# Class: Method



URI: [envmd:Method](http://w3id.org/ontogpt/environmental-metadataMethod)



```mermaid
erDiagram
Method {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Method**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Dataset](Dataset.md) | [methods](methods.md) | range | [Method](Method.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* ENVTHES






### Annotations

| property | value |
| --- | --- |
| annotators | bioportal:ENVTHES |



### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-metadata





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | envmd:Method |
| native | envmd:Method |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Method
id_prefixes:
- ENVTHES
annotations:
  annotators:
    tag: annotators
    value: bioportal:ENVTHES
from_schema: http://w3id.org/ontogpt/environmental-metadata
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Method
id_prefixes:
- ENVTHES
annotations:
  annotators:
    tag: annotators
    value: bioportal:ENVTHES
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
    owner: Method
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
    owner: Method
    domain_of:
    - NamedEntity
    range: string

```
</details>