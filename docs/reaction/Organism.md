

# Class: Organism



URI: [reaction:Organism](http://w3id.org/ontogpt/reaction/Organism)



```mermaid
erDiagram
Organism {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Organism**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GeneToReaction](GeneToReaction.md) | [organism](organism.md) | range | [Organism](Organism.md) |
| [ReactionDocument](ReactionDocument.md) | [organism](organism.md) | range | [Organism](Organism.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* NCBITaxon






### Annotations

| property | value |
| --- | --- |
| annotators | gilda:, sqlite:obo:ncbitaxon |



### Schema Source


* from schema: https://w3id.org/ontogpt/reaction




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | reaction:Organism |
| native | reaction:Organism |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Organism
id_prefixes:
- NCBITaxon
annotations:
  annotators:
    tag: annotators
    value: gilda:, sqlite:obo:ncbitaxon
from_schema: https://w3id.org/ontogpt/reaction
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Organism
id_prefixes:
- NCBITaxon
annotations:
  annotators:
    tag: annotators
    value: gilda:, sqlite:obo:ncbitaxon
from_schema: https://w3id.org/ontogpt/reaction
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
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    identifier: true
    alias: id
    owner: Organism
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
    from_schema: https://w3id.org/ontogpt/reaction
    aliases:
    - name
    slot_uri: rdfs:label
    alias: label
    owner: Organism
    domain_of:
    - Reaction
    - NamedEntity
    range: string

```
</details>