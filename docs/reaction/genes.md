

# Slot: genes


_semicolon separated list of genes that catalyzes the mentioned reactions_



URI: [reaction:genes](http://w3id.org/ontogpt/reaction/genes)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ReactionDocument](ReactionDocument.md) |  |  no  |







## Properties

* Range: [Gene](Gene.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/ontogpt/reaction




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | reaction:genes |
| native | reaction:genes |




## LinkML Source

<details>
```yaml
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

```
</details>