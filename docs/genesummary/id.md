

# Slot: id


_A unique identifier for the named entity_



URI: [genesummary:id](http://w3id.org/ontogpt/genesummary/id)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Publication](Publication.md) |  |  no  |
| [RelationshipType](RelationshipType.md) |  |  no  |
| [NamedEntity](NamedEntity.md) |  |  no  |
| [Gene](Gene.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Comments

* this is populated during the grounding and normalization step

## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/gocam




## LinkML Source

<details>
```yaml
name: id
description: A unique identifier for the named entity
comments:
- this is populated during the grounding and normalization step
from_schema: http://w3id.org/ontogpt/gocam
rank: 1000
identifier: true
alias: id
domain_of:
- Gene
- NamedEntity
- Publication
range: string

```
</details>