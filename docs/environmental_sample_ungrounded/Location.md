

# Class: Location



URI: [sample:Location](http://w3id.org/ontogpt/environmental-sample-ungrounded/Location)



```mermaid
erDiagram
Location {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Location**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Study](Study.md) | [location](location.md) | range | [Location](Location.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample-ungrounded




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sample:Location |
| native | sample:Location |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Location
from_schema: http://w3id.org/ontogpt/environmental-sample-ungrounded
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Location
from_schema: http://w3id.org/ontogpt/environmental-sample-ungrounded
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
    from_schema: http://w3id.org/ontogpt/environmental-sample-ungrounded
    rank: 1000
    identifier: true
    alias: id
    owner: Location
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
    from_schema: http://w3id.org/ontogpt/environmental-sample-ungrounded
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Location
    domain_of:
    - NamedEntity
    range: string

```
</details>