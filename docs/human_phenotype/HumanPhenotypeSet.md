

# Class: HumanPhenotypeSet



URI: [human_phenotype:HumanPhenotypeSet](http://w3id.org/ontogpt/human_phenotypeHumanPhenotypeSet)



```mermaid
erDiagram
HumanPhenotypeSet {
    string id  
    string label  
}
HumanPhenotype {
    string id  
    string label  
}

HumanPhenotypeSet ||--}o HumanPhenotype : "phenotypes"

```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **HumanPhenotypeSet**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [phenotypes](phenotypes.md) | * <br/> [HumanPhenotype](HumanPhenotype.md) | A semicolon-separated list of human phenotypes, including symptoms of disease | direct |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/human_phenotype





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | human_phenotype:HumanPhenotypeSet |
| native | human_phenotype:HumanPhenotypeSet |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HumanPhenotypeSet
from_schema: http://w3id.org/ontogpt/human_phenotype
is_a: NamedEntity
attributes:
  phenotypes:
    name: phenotypes
    description: A semicolon-separated list of human phenotypes, including symptoms
      of disease. It must be semicolon-separated. Labels containing the word 'with'
      should be split into multiple phenotypes.
    from_schema: http://w3id.org/ontogpt/human_phenotype
    rank: 1000
    multivalued: true
    domain_of:
    - HumanPhenotypeSet
    range: HumanPhenotype
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: HumanPhenotypeSet
from_schema: http://w3id.org/ontogpt/human_phenotype
is_a: NamedEntity
attributes:
  phenotypes:
    name: phenotypes
    description: A semicolon-separated list of human phenotypes, including symptoms
      of disease. It must be semicolon-separated. Labels containing the word 'with'
      should be split into multiple phenotypes.
    from_schema: http://w3id.org/ontogpt/human_phenotype
    rank: 1000
    multivalued: true
    alias: phenotypes
    owner: HumanPhenotypeSet
    domain_of:
    - HumanPhenotypeSet
    range: HumanPhenotype
  id:
    name: id
    annotations:
      prompt.skip:
        tag: prompt.skip
        value: 'true'
    description: A unique identifier for the named entity
    comments:
    - this is populated during the grounding and normalization step
    from_schema: http://w3id.org/ontogpt/human_phenotype
    rank: 1000
    identifier: true
    alias: id
    owner: HumanPhenotypeSet
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
    from_schema: http://w3id.org/ontogpt/human_phenotype
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: HumanPhenotypeSet
    domain_of:
    - NamedEntity
    range: string
tree_root: true

```
</details>