

# Class: Taxon



URI: [alzrd:Taxon](http://w3id.org/ontogpt/alzrdTaxon)



```mermaid
erDiagram
Taxon {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Taxon**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Document](Document.md) | [taxa](taxa.md) | range | [Taxon](Taxon.md) |
| [ExperimentalMetricToTaxonRelationship](ExperimentalMetricToTaxonRelationship.md) | [taxon](taxon.md) | range | [Taxon](Taxon.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* NCBITaxon






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:ncbitaxon || prompt | The taxonomic group or species of a model organism. Examples are "human", "mouse", "rat", "Rhesus macaque", "canine", "marmoset", "fruit fly", "C. elegans", "S. cerevisiae". |



### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:Taxon |
| native | alzrd:Taxon |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Taxon
id_prefixes:
- NCBITaxon
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:ncbitaxon
  prompt:
    tag: prompt
    value: The taxonomic group or species of a model organism. Examples are "human",
      "mouse", "rat", "Rhesus macaque", "canine", "marmoset", "fruit fly", "C. elegans",
      "S. cerevisiae".
from_schema: http://w3id.org/ontogpt/alzrd
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Taxon
id_prefixes:
- NCBITaxon
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:ncbitaxon
  prompt:
    tag: prompt
    value: The taxonomic group or species of a model organism. Examples are "human",
      "mouse", "rat", "Rhesus macaque", "canine", "marmoset", "fruit fly", "C. elegans",
      "S. cerevisiae".
from_schema: http://w3id.org/ontogpt/alzrd
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
    from_schema: http://w3id.org/ontogpt/alzrd
    rank: 1000
    identifier: true
    alias: id
    owner: Taxon
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
    from_schema: http://w3id.org/ontogpt/alzrd
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Taxon
    domain_of:
    - NamedEntity
    range: string

```
</details>