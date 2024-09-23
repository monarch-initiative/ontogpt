

# Class: Taxon



URI: [bp:Taxon](http://w3id.org/ontogpt/biotic-interaction-templateTaxon)



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
| [BioticInteraction](BioticInteraction.md) | [source_taxon](source_taxon.md) | range | [Taxon](Taxon.md) |
| [BioticInteraction](BioticInteraction.md) | [target_taxon](target_taxon.md) | range | [Taxon](Taxon.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* NCBITaxon

* SNOMEDCT






### Annotations

| property | value |
| --- | --- |
| annotators | pronto:taxslim.obo, bioportal:SNOMEDCT |



### Schema Source


* from schema: https://w3id.org/ontogpt/biotic_interaction




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bp:Taxon |
| native | bp:Taxon |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Taxon
id_prefixes:
- NCBITaxon
- SNOMEDCT
annotations:
  annotators:
    tag: annotators
    value: pronto:taxslim.obo, bioportal:SNOMEDCT
from_schema: https://w3id.org/ontogpt/biotic_interaction
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Taxon
id_prefixes:
- NCBITaxon
- SNOMEDCT
annotations:
  annotators:
    tag: annotators
    value: pronto:taxslim.obo, bioportal:SNOMEDCT
from_schema: https://w3id.org/ontogpt/biotic_interaction
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
    from_schema: https://w3id.org/ontogpt/biotic_interaction
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
    from_schema: https://w3id.org/ontogpt/biotic_interaction
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