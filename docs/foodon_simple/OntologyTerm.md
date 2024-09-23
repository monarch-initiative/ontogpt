

# Class: OntologyTerm



URI: [foodon_simple:OntologyTerm](http://w3id.org/ontogpt/foodon_simpleOntologyTerm)



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

* FOODON

* CHEBI






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:foodon || prompt | The name of a Food Ontology term. Examples include: vitamin A, apple juice, okra pod, chocolate substitute, breakfast cereal, tuna (flaked, canned), beef chuck roast |



### Schema Source


* from schema: http://w3id.org/ontogpt/foodon_simple




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foodon_simple:OntologyTerm |
| native | foodon_simple:OntologyTerm |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OntologyTerm
id_prefixes:
- FOODON
- CHEBI
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:foodon
  prompt:
    tag: prompt
    value: 'The name of a Food Ontology term. Examples include: vitamin A, apple juice,
      okra pod, chocolate substitute, breakfast cereal, tuna (flaked, canned), beef
      chuck roast'
from_schema: http://w3id.org/ontogpt/foodon_simple
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: OntologyTerm
id_prefixes:
- FOODON
- CHEBI
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:foodon
  prompt:
    tag: prompt
    value: 'The name of a Food Ontology term. Examples include: vitamin A, apple juice,
      okra pod, chocolate substitute, breakfast cereal, tuna (flaked, canned), beef
      chuck roast'
from_schema: http://w3id.org/ontogpt/foodon_simple
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
    from_schema: http://w3id.org/ontogpt/foodon_simple
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
    from_schema: http://w3id.org/ontogpt/foodon_simple
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