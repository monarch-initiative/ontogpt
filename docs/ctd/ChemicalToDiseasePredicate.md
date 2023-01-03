# Class: ChemicalToDiseasePredicate
_A predicate for chemical to disease relationships_




URI: [drug:ChemicalToDiseasePredicate](http://w3id.org/ontogpt/drug/ChemicalToDiseasePredicate)


```mermaid
 classDiagram
    class ChemicalToDiseasePredicate
      RelationshipType <|-- ChemicalToDiseasePredicate
      
      ChemicalToDiseasePredicate : id
      ChemicalToDiseasePredicate : label
      
```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * [RelationshipType](RelationshipType.md)
        * **ChemicalToDiseasePredicate**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [xsd:string](xsd:string) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md) | [predicate](predicate.md) | range | [ChemicalToDiseasePredicate](ChemicalToDiseasePredicate.md) |






## Comments

* for the purposes of evaluation against BC5CDR, any predicate other than INDUCES is ignored.

## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/ctd





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | drug:ChemicalToDiseasePredicate |
| native | drug:ChemicalToDiseasePredicate |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChemicalToDiseasePredicate
description: A predicate for chemical to disease relationships
comments:
- for the purposes of evaluation against BC5CDR, any predicate other than INDUCES
  is ignored.
from_schema: http://w3id.org/ontogpt/ctd
rank: 1000
is_a: RelationshipType

```
</details>

### Induced

<details>
```yaml
name: ChemicalToDiseasePredicate
description: A predicate for chemical to disease relationships
comments:
- for the purposes of evaluation against BC5CDR, any predicate other than INDUCES
  is ignored.
from_schema: http://w3id.org/ontogpt/ctd
rank: 1000
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
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    identifier: true
    alias: id
    owner: ChemicalToDiseasePredicate
    domain_of:
    - NamedEntity
    - Publication
    range: string
  label:
    name: label
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/core
    aliases:
    - name
    rank: 1000
    alias: label
    owner: ChemicalToDiseasePredicate
    domain_of:
    - NamedEntity
    range: string

```
</details>