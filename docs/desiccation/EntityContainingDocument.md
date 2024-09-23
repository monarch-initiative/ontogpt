

# Class: EntityContainingDocument



URI: [desiccation:EntityContainingDocument](http://w3id.org/ontogpt/desiccationEntityContainingDocument)



```mermaid
erDiagram
EntityContainingDocument {
    string id  
    string label  
}
Trait {
    string id  
    string label  
}
Taxon {
    string id  
    string label  
}
EnvironmentalCondition {
    string id  
    string label  
}

EntityContainingDocument ||--}o EnvironmentalCondition : "environmental_conditions"
EntityContainingDocument ||--}o Taxon : "taxa"
EntityContainingDocument ||--}o Trait : "traits"

```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **EntityContainingDocument**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [environmental_conditions](environmental_conditions.md) | * <br/> [EnvironmentalCondition](EnvironmentalCondition.md) | A semicolon-separated list of environmental terms | direct |
| [taxa](taxa.md) | * <br/> [Taxon](Taxon.md) | A semicolon-separated list of taxonomic terms of living things | direct |
| [traits](traits.md) | * <br/> [Trait](Trait.md) | A semicolon-separated list of plant traits | direct |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/desiccation





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | desiccation:EntityContainingDocument |
| native | desiccation:EntityContainingDocument |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EntityContainingDocument
from_schema: http://w3id.org/ontogpt/desiccation
is_a: NamedEntity
attributes:
  environmental_conditions:
    name: environmental_conditions
    description: A semicolon-separated list of environmental terms.
    from_schema: http://w3id.org/ontogpt/desiccation
    rank: 1000
    multivalued: true
    domain_of:
    - EntityContainingDocument
    range: EnvironmentalCondition
  taxa:
    name: taxa
    description: A semicolon-separated list of taxonomic terms of living things.
    from_schema: http://w3id.org/ontogpt/desiccation
    rank: 1000
    multivalued: true
    domain_of:
    - EntityContainingDocument
    range: Taxon
  traits:
    name: traits
    description: A semicolon-separated list of plant traits.
    from_schema: http://w3id.org/ontogpt/desiccation
    rank: 1000
    multivalued: true
    domain_of:
    - EntityContainingDocument
    range: Trait
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: EntityContainingDocument
from_schema: http://w3id.org/ontogpt/desiccation
is_a: NamedEntity
attributes:
  environmental_conditions:
    name: environmental_conditions
    description: A semicolon-separated list of environmental terms.
    from_schema: http://w3id.org/ontogpt/desiccation
    rank: 1000
    multivalued: true
    alias: environmental_conditions
    owner: EntityContainingDocument
    domain_of:
    - EntityContainingDocument
    range: EnvironmentalCondition
  taxa:
    name: taxa
    description: A semicolon-separated list of taxonomic terms of living things.
    from_schema: http://w3id.org/ontogpt/desiccation
    rank: 1000
    multivalued: true
    alias: taxa
    owner: EntityContainingDocument
    domain_of:
    - EntityContainingDocument
    range: Taxon
  traits:
    name: traits
    description: A semicolon-separated list of plant traits.
    from_schema: http://w3id.org/ontogpt/desiccation
    rank: 1000
    multivalued: true
    alias: traits
    owner: EntityContainingDocument
    domain_of:
    - EntityContainingDocument
    range: Trait
  id:
    name: id
    annotations:
      prompt.skip:
        tag: prompt.skip
        value: 'true'
    description: A unique identifier for the named entity
    comments:
    - this is populated during the grounding and normalization step
    from_schema: http://w3id.org/ontogpt/desiccation
    rank: 1000
    identifier: true
    alias: id
    owner: EntityContainingDocument
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
    from_schema: http://w3id.org/ontogpt/desiccation
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: EntityContainingDocument
    domain_of:
    - NamedEntity
    range: string
tree_root: true

```
</details>