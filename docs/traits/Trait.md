

# Class: Trait



URI: [traits:Trait](http://w3id.org/ontogpt/traits/Trait)



```mermaid
erDiagram
Trait {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Trait**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Taxon](Taxon.md) | [metabolic_traits](metabolic_traits.md) | range | [Trait](Trait.md) |
| [Taxon](Taxon.md) | [morphological_traits](morphological_traits.md) | range | [Trait](Trait.md) |
| [Taxon](Taxon.md) | [genetic_traits](genetic_traits.md) | range | [Trait](Trait.md) |
| [Taxon](Taxon.md) | [cellular_traits](cellular_traits.md) | range | [Trait](Trait.md) |
| [Taxon](Taxon.md) | [ecological_traits](ecological_traits.md) | range | [Trait](Trait.md) |
| [Taxon](Taxon.md) | [reproductive_traits](reproductive_traits.md) | range | [Trait](Trait.md) |
| [Taxon](Taxon.md) | [survival_traits](survival_traits.md) | range | [Trait](Trait.md) |
| [Taxon](Taxon.md) | [phenotypic_plasticiticy_traits](phenotypic_plasticiticy_traits.md) | range | [Trait](Trait.md) |
| [Taxon](Taxon.md) | [preferred_environments](preferred_environments.md) | range | [Trait](Trait.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* ECOCORE

* PATO

* GO

* OBA

* BIODIVTHES






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:ecocore, sqlite:obo:pato, sqlite:obo:go, sqlite:obo:oba, bioportal:biodivthes |



### Schema Source


* from schema: http://w3id.org/ontogpt/traits





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | traits:Trait |
| native | traits:Trait |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Trait
id_prefixes:
- ECOCORE
- PATO
- GO
- OBA
- BIODIVTHES
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:ecocore, sqlite:obo:pato, sqlite:obo:go, sqlite:obo:oba, bioportal:biodivthes
from_schema: http://w3id.org/ontogpt/traits
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Trait
id_prefixes:
- ECOCORE
- PATO
- GO
- OBA
- BIODIVTHES
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:ecocore, sqlite:obo:pato, sqlite:obo:go, sqlite:obo:oba, bioportal:biodivthes
from_schema: http://w3id.org/ontogpt/traits
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
    from_schema: http://w3id.org/ontogpt/traits
    rank: 1000
    identifier: true
    alias: id
    owner: Trait
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
    from_schema: http://w3id.org/ontogpt/traits
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Trait
    domain_of:
    - NamedEntity
    range: string

```
</details>