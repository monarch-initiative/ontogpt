

# Class: Gene



URI: [gocam:Gene](http://w3id.org/ontogpt/gocam/Gene)



```mermaid
erDiagram
Gene {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Gene**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IBDAnnotations](IBDAnnotations.md) | [genes](genes.md) | range | [Gene](Gene.md) |
| [GeneOrganismRelationship](GeneOrganismRelationship.md) | [gene](gene.md) | range | [Gene](Gene.md) |
| [GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md) | [gene](gene.md) | range | [Gene](Gene.md) |
| [GeneMolecularActivityRelationship2](GeneMolecularActivityRelationship2.md) | [gene](gene.md) | range | [Gene](Gene.md) |
| [GeneSubcellularLocalizationRelationship](GeneSubcellularLocalizationRelationship.md) | [gene](gene.md) | range | [Gene](Gene.md) |
| [GeneGeneInteraction](GeneGeneInteraction.md) | [gene1](gene1.md) | range | [Gene](Gene.md) |
| [GeneGeneInteraction](GeneGeneInteraction.md) | [gene2](gene2.md) | range | [Gene](Gene.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HGNC

* PR

* UniProtKB






### Annotations

| property | value |
| --- | --- |
| annotators | gilda:, bioportal:hgnc-nr |



### Schema Source


* from schema: http://w3id.org/ontogpt/gocam





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gocam:Gene |
| native | gocam:Gene |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gene
id_prefixes:
- HGNC
- PR
- UniProtKB
annotations:
  annotators:
    tag: annotators
    value: gilda:, bioportal:hgnc-nr
from_schema: http://w3id.org/ontogpt/gocam
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Gene
id_prefixes:
- HGNC
- PR
- UniProtKB
annotations:
  annotators:
    tag: annotators
    value: gilda:, bioportal:hgnc-nr
from_schema: http://w3id.org/ontogpt/gocam
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
    from_schema: http://w3id.org/ontogpt/gocam
    rank: 1000
    identifier: true
    alias: id
    owner: Gene
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
    from_schema: http://w3id.org/ontogpt/gocam
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Gene
    domain_of:
    - NamedEntity
    range: string

```
</details>