

# Class: DiseaseTermSet



URI: [all_disease_grounding:DiseaseTermSet](all_disease_grounding:DiseaseTermSet)



```mermaid
erDiagram
DiseaseTermSet {
    string id  
    string label  
}
DiseaseTerm {
    string id  
    string label  
}

DiseaseTermSet ||--}o DiseaseTerm : "terms"

```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **DiseaseTermSet**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [terms](terms.md) | * <br/> [DiseaseTerm](DiseaseTerm.md) | A semicolon-separated list of any disease names | direct |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/all_disease_grounding




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | all_disease_grounding:DiseaseTermSet |
| native | all_disease_grounding:DiseaseTermSet |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DiseaseTermSet
from_schema: http://w3id.org/ontogpt/all_disease_grounding
is_a: NamedEntity
attributes:
  terms:
    name: terms
    description: A semicolon-separated list of any disease names.
    from_schema: http://w3id.org/ontogpt/all_disease_grounding
    rank: 1000
    domain_of:
    - DiseaseTermSet
    range: DiseaseTerm
    multivalued: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: DiseaseTermSet
from_schema: http://w3id.org/ontogpt/all_disease_grounding
is_a: NamedEntity
attributes:
  terms:
    name: terms
    description: A semicolon-separated list of any disease names.
    from_schema: http://w3id.org/ontogpt/all_disease_grounding
    rank: 1000
    alias: terms
    owner: DiseaseTermSet
    domain_of:
    - DiseaseTermSet
    range: DiseaseTerm
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
    from_schema: http://w3id.org/ontogpt/all_disease_grounding
    rank: 1000
    identifier: true
    alias: id
    owner: DiseaseTermSet
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
    from_schema: http://w3id.org/ontogpt/all_disease_grounding
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: DiseaseTermSet
    domain_of:
    - NamedEntity
    range: string
tree_root: true

```
</details>