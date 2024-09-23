

# Class: Gene


_a single gene symbol._





URI: [geneextraction:Gene](http://w3id.org/ontogpt/gene_extractionGene)



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
| [AcronymList](AcronymList.md) | [genes](genes.md) | range | [Gene](Gene.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HGNC






### Annotations

| property | value |
| --- | --- |
| annotators | bioportal:hgnc-nr, bioportal:gexo |



### Schema Source


* from schema: http://w3id.org/ontogpt/gene_extraction




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | geneextraction:Gene |
| native | geneextraction:Gene |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gene
id_prefixes:
- HGNC
annotations:
  annotators:
    tag: annotators
    value: bioportal:hgnc-nr, bioportal:gexo
description: a single gene symbol.
from_schema: http://w3id.org/ontogpt/gene_extraction
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Gene
id_prefixes:
- HGNC
annotations:
  annotators:
    tag: annotators
    value: bioportal:hgnc-nr, bioportal:gexo
description: a single gene symbol.
from_schema: http://w3id.org/ontogpt/gene_extraction
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
    from_schema: http://w3id.org/ontogpt/gene_extraction
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
    from_schema: http://w3id.org/ontogpt/gene_extraction
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