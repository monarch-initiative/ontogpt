# Class: Relation



URI: [oc:Relation](http://w3id.org/ontogpt/ontology-class-templateRelation)


```mermaid
erDiagram
Relation {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Relation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [LogicalDefinition](LogicalDefinition.md) | [differentiating_characteristic_relationship](differentiating_characteristic_relationship.md) | range | [Relation](Relation.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* RO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:ro |



### Schema Source


* from schema: https://w3id.org/ontogpt/ontology_class





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oc:Relation |
| native | oc:Relation |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Relation
id_prefixes:
- RO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:ro
from_schema: https://w3id.org/ontogpt/ontology_class
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Relation
id_prefixes:
- RO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:ro
from_schema: https://w3id.org/ontogpt/ontology_class
rank: 1000
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
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    identifier: true
    alias: id
    owner: Relation
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
    alias: label
    owner: Relation
    domain_of:
    - OntologyClass
    - NamedEntity
    range: string

```
</details>