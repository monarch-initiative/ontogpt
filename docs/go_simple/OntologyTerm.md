

# Class: OntologyTerm



URI: [go_simple:OntologyTerm](http://w3id.org/ontogpt/go_simpleOntologyTerm)



```mermaid
erDiagram
OntologyTerm {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **OntologyTerm**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [OntologyTermSet](OntologyTermSet.md) | [terms](terms.md) | range | [OntologyTerm](OntologyTerm.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* GO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go || prompt | The name of a Gene Ontology term. Examples include: regulation of dehydroepiandrosterone secretion, lignan metabolic process, ITP catabolic process, determination of imaginal disc primordium, kinetoplast |



### Schema Source


* from schema: http://w3id.org/ontogpt/go_simple





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | go_simple:OntologyTerm |
| native | go_simple:OntologyTerm |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OntologyTerm
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
  prompt:
    tag: prompt
    value: 'The name of a Gene Ontology term. Examples include: regulation of dehydroepiandrosterone
      secretion, lignan metabolic process, ITP catabolic process, determination of
      imaginal disc primordium, kinetoplast'
from_schema: http://w3id.org/ontogpt/go_simple
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: OntologyTerm
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
  prompt:
    tag: prompt
    value: 'The name of a Gene Ontology term. Examples include: regulation of dehydroepiandrosterone
      secretion, lignan metabolic process, ITP catabolic process, determination of
      imaginal disc primordium, kinetoplast'
from_schema: http://w3id.org/ontogpt/go_simple
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
    from_schema: http://w3id.org/ontogpt/go_simple
    rank: 1000
    identifier: true
    alias: id
    owner: OntologyTerm
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
    from_schema: http://w3id.org/ontogpt/go_simple
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: OntologyTerm
    domain_of:
    - NamedEntity
    range: string

```
</details>