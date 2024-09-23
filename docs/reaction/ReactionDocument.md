

# Class: ReactionDocument



URI: [reaction:ReactionDocument](http://w3id.org/ontogpt/reaction/ReactionDocument)



```mermaid
erDiagram
ReactionDocument {

}
Evidence {
    string id  
    string label  
}
Organism {
    string id  
    string label  
}
GeneReactionPairing {

}
Reaction {
    string label  
    string description  
    stringList synonyms  
    string id  
}
Gene {
    string id  
    string label  
}

ReactionDocument ||--}o Gene : "genes"
ReactionDocument ||--}o Reaction : "reactions"
ReactionDocument ||--}o GeneReactionPairing : "gene_reaction_pairings"
ReactionDocument ||--|o Organism : "organism"
ReactionDocument ||--}o Evidence : "has_evidence"
GeneReactionPairing ||--|o Gene : "gene"
GeneReactionPairing ||--|o Reaction : "reaction"
Reaction ||--|o ReactionGrouping : "subclass_of"
Reaction ||--}o ChemicalEntity : "left_side"
Reaction ||--}o ChemicalEntity : "right_side"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [genes](genes.md) | * <br/> [Gene](Gene.md) | semicolon separated list of genes that catalyzes the mentioned reactions | direct |
| [reactions](reactions.md) | * <br/> [Reaction](Reaction.md) | semicolon separated list of reaction equations (e | direct |
| [gene_reaction_pairings](gene_reaction_pairings.md) | * <br/> [GeneReactionPairing](GeneReactionPairing.md) | semicolon separated list of gene to reaction pairings | direct |
| [organism](organism.md) | 0..1 <br/> [Organism](Organism.md) |  | direct |
| [has_evidence](has_evidence.md) | * <br/> [Evidence](Evidence.md) | evidence for the reaction | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/ontogpt/reaction




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | reaction:ReactionDocument |
| native | reaction:ReactionDocument |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ReactionDocument
from_schema: https://w3id.org/ontogpt/reaction
attributes:
  genes:
    name: genes
    description: semicolon separated list of genes that catalyzes the mentioned reactions
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    domain_of:
    - ReactionDocument
    range: Gene
    multivalued: true
  reactions:
    name: reactions
    description: semicolon separated list of reaction equations (e.g. A+B = C+D) catalyzed
      by the gene
    from_schema: https://w3id.org/ontogpt/reaction
    domain_of:
    - GeneToReaction
    - ReactionDocument
    range: Reaction
    multivalued: true
    inlined: true
  gene_reaction_pairings:
    name: gene_reaction_pairings
    description: semicolon separated list of gene to reaction pairings
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    domain_of:
    - ReactionDocument
    range: GeneReactionPairing
    multivalued: true
    inlined: true
  organism:
    name: organism
    from_schema: https://w3id.org/ontogpt/reaction
    domain_of:
    - GeneToReaction
    - ReactionDocument
    range: Organism
  has_evidence:
    name: has_evidence
    description: evidence for the reaction
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    domain_of:
    - ReactionDocument
    range: Evidence
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: ReactionDocument
from_schema: https://w3id.org/ontogpt/reaction
attributes:
  genes:
    name: genes
    description: semicolon separated list of genes that catalyzes the mentioned reactions
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    alias: genes
    owner: ReactionDocument
    domain_of:
    - ReactionDocument
    range: Gene
    multivalued: true
  reactions:
    name: reactions
    description: semicolon separated list of reaction equations (e.g. A+B = C+D) catalyzed
      by the gene
    from_schema: https://w3id.org/ontogpt/reaction
    alias: reactions
    owner: ReactionDocument
    domain_of:
    - GeneToReaction
    - ReactionDocument
    range: Reaction
    multivalued: true
    inlined: true
  gene_reaction_pairings:
    name: gene_reaction_pairings
    description: semicolon separated list of gene to reaction pairings
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    alias: gene_reaction_pairings
    owner: ReactionDocument
    domain_of:
    - ReactionDocument
    range: GeneReactionPairing
    multivalued: true
    inlined: true
  organism:
    name: organism
    from_schema: https://w3id.org/ontogpt/reaction
    alias: organism
    owner: ReactionDocument
    domain_of:
    - GeneToReaction
    - ReactionDocument
    range: Organism
  has_evidence:
    name: has_evidence
    description: evidence for the reaction
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    alias: has_evidence
    owner: ReactionDocument
    domain_of:
    - ReactionDocument
    range: Evidence
    multivalued: true

```
</details>