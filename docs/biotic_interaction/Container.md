

# Class: Container



URI: [bp:Container](http://w3id.org/ontogpt/biotic-interaction-templateContainer)



```mermaid
erDiagram
Container {

}
BioticInteraction {

}
InteractionType {
    string id  
    string label  
}
Taxon {
    string id  
    string label  
}

Container ||--}o BioticInteraction : "interactions"
BioticInteraction ||--|o Taxon : "source_taxon"
BioticInteraction ||--|o Taxon : "target_taxon"
BioticInteraction ||--|o InteractionType : "interaction_type"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [interactions](interactions.md) | * <br/> [BioticInteraction](BioticInteraction.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/ontogpt/biotic_interaction




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bp:Container |
| native | bp:Container |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Container
from_schema: https://w3id.org/ontogpt/biotic_interaction
attributes:
  interactions:
    name: interactions
    from_schema: https://w3id.org/ontogpt/biotic_interaction
    rank: 1000
    domain_of:
    - Container
    range: BioticInteraction
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Container
from_schema: https://w3id.org/ontogpt/biotic_interaction
attributes:
  interactions:
    name: interactions
    from_schema: https://w3id.org/ontogpt/biotic_interaction
    rank: 1000
    alias: interactions
    owner: Container
    domain_of:
    - Container
    range: BioticInteraction
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true

```
</details>