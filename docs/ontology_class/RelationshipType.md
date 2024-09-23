

# Class: RelationshipType



URI: [oc:RelationshipType](http://w3id.org/ontogpt/ontology-class-templateRelationshipType)



```mermaid
erDiagram
RelationshipType {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **RelationshipType**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Triple](Triple.md) | [predicate](predicate.md) | range | [RelationshipType](RelationshipType.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* RO

* biolink








### Schema Source


* from schema: https://w3id.org/ontogpt/ontology_class





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oc:RelationshipType |
| native | oc:RelationshipType |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RelationshipType
id_prefixes:
- RO
- biolink
from_schema: https://w3id.org/ontogpt/ontology_class
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: RelationshipType
id_prefixes:
- RO
- biolink
from_schema: https://w3id.org/ontogpt/ontology_class
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
    from_schema: https://w3id.org/ontogpt/ontology_class
    rank: 1000
    identifier: true
    alias: id
    owner: RelationshipType
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
    from_schema: https://w3id.org/ontogpt/ontology_class
    aliases:
    - name
    slot_uri: rdfs:label
    alias: label
    owner: RelationshipType
    domain_of:
    - OntologyClass
    - NamedEntity
    range: string

```
</details>