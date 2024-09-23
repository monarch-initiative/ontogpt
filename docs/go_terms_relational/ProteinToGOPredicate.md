

# Class: ProteinToGOPredicate


_A predicate for protein to GO term relationships._





URI: [go_terms_relational:ProteinToGOPredicate](http://w3id.org/ontogpt/go_terms_relationalProteinToGOPredicate)



```mermaid
erDiagram
ProteinToGOPredicate {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * [RelationshipType](RelationshipType.md)
        * **ProteinToGOPredicate**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ProteinToGORelationship](ProteinToGORelationship.md) | [predicate](predicate.md) | range | [ProteinToGOPredicate](ProteinToGOPredicate.md) |






## Comments

* This may be changed to a more specific type, like RO
* Any changes should be reflected for the triples slot in Document

## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/go_terms_relational





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | go_terms_relational:ProteinToGOPredicate |
| native | go_terms_relational:ProteinToGOPredicate |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProteinToGOPredicate
description: A predicate for protein to GO term relationships.
comments:
- This may be changed to a more specific type, like RO
- Any changes should be reflected for the triples slot in Document
from_schema: http://w3id.org/ontogpt/go_terms_relational
is_a: RelationshipType

```
</details>

### Induced

<details>
```yaml
name: ProteinToGOPredicate
description: A predicate for protein to GO term relationships.
comments:
- This may be changed to a more specific type, like RO
- Any changes should be reflected for the triples slot in Document
from_schema: http://w3id.org/ontogpt/go_terms_relational
is_a: RelationshipType
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
    from_schema: http://w3id.org/ontogpt/go_terms_relational
    rank: 1000
    identifier: true
    alias: id
    owner: ProteinToGOPredicate
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
    from_schema: http://w3id.org/ontogpt/go_terms_relational
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: ProteinToGOPredicate
    domain_of:
    - NamedEntity
    range: string

```
</details>