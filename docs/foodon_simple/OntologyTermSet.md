

# Class: OntologyTermSet



URI: [foodon_simple:OntologyTermSet](http://w3id.org/ontogpt/foodon_simpleOntologyTermSet)



```mermaid
erDiagram
OntologyTermSet {
    string id  
    string label  
}
OntologyTerm {
    string id  
    string label  
}

OntologyTermSet ||--}o OntologyTerm : "terms"

```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **OntologyTermSet**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [terms](terms.md) | * <br/> [OntologyTerm](OntologyTerm.md) | A semicolon-separated list of any Food Ontology terms | direct |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/foodon_simple




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foodon_simple:OntologyTermSet |
| native | foodon_simple:OntologyTermSet |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OntologyTermSet
from_schema: http://w3id.org/ontogpt/foodon_simple
is_a: NamedEntity
attributes:
  terms:
    name: terms
    description: A semicolon-separated list of any Food Ontology terms.
    from_schema: http://w3id.org/ontogpt/foodon_simple
    rank: 1000
    domain_of:
    - OntologyTermSet
    range: OntologyTerm
    multivalued: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: OntologyTermSet
from_schema: http://w3id.org/ontogpt/foodon_simple
is_a: NamedEntity
attributes:
  terms:
    name: terms
    description: A semicolon-separated list of any Food Ontology terms.
    from_schema: http://w3id.org/ontogpt/foodon_simple
    rank: 1000
    alias: terms
    owner: OntologyTermSet
    domain_of:
    - OntologyTermSet
    range: OntologyTerm
    multivalued: true
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
    owner: OntologyTermSet
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
    owner: OntologyTermSet
    domain_of:
    - NamedEntity
    range: string
tree_root: true

```
</details>