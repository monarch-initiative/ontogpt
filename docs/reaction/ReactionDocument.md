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
| [genes](genes.md) | 0..* <br/> [Gene](Gene.md) | semicolon separated list of genes that catalyzes the mentioned reactions | direct |
| [reactions](reactions.md) | 0..1 <br/> [String](String.md) |  | direct |
| [gene_reaction_pairings](gene_reaction_pairings.md) | 0..* <br/> [GeneReactionPairing](GeneReactionPairing.md) | semicolon separated list of gene to reaction pairings | direct |
| [organism](organism.md) | 0..1 <br/> [String](String.md) |  | direct |
| [has_evidence](has_evidence.md) | 0..* <br/> [Evidence](Evidence.md) | evidence for the reaction | direct |









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
rank: 1000
attributes:
  genes:
    name: genes
    description: semicolon separated list of genes that catalyzes the mentioned reactions
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    multivalued: true
    range: Gene
  reactions:
    name: reactions
    description: semicolon separated list of reaction equations (e.g. A+B = C+D) catalyzed
      by the gene
    from_schema: https://w3id.org/ontogpt/reaction
    multivalued: true
    range: Reaction
    inlined: true
  gene_reaction_pairings:
    name: gene_reaction_pairings
    description: semicolon separated list of gene to reaction pairings
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    multivalued: true
    range: GeneReactionPairing
    inlined: true
  organism:
    name: organism
    from_schema: https://w3id.org/ontogpt/reaction
    range: Organism
  has_evidence:
    name: has_evidence
    description: evidence for the reaction
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    multivalued: true
    range: Evidence

```
</details>

### Induced

<details>
```yaml
name: ReactionDocument
from_schema: https://w3id.org/ontogpt/reaction
rank: 1000
attributes:
  genes:
    name: genes
    description: semicolon separated list of genes that catalyzes the mentioned reactions
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    multivalued: true
    alias: genes
    owner: ReactionDocument
    domain_of:
    - ReactionDocument
    range: Gene
  reactions:
    name: reactions
    description: semicolon separated list of reaction equations (e.g. A+B = C+D) catalyzed
      by the gene
    from_schema: https://w3id.org/ontogpt/reaction
    multivalued: true
    alias: reactions
    owner: ReactionDocument
    domain_of:
    - GeneToReaction
    - ReactionDocument
    range: Reaction
    inlined: true
  gene_reaction_pairings:
    name: gene_reaction_pairings
    description: semicolon separated list of gene to reaction pairings
    from_schema: https://w3id.org/ontogpt/reaction
    rank: 1000
    multivalued: true
    alias: gene_reaction_pairings
    owner: ReactionDocument
    domain_of:
    - ReactionDocument
    range: GeneReactionPairing
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
    multivalued: true
    alias: has_evidence
    owner: ReactionDocument
    domain_of:
    - ReactionDocument
    range: Evidence

```
</details>