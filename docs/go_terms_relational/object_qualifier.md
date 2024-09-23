

# Slot: object_qualifier


_An optional qualifier or modifier for the object of the statement, e.g. "severe" or "with additional complications"_



URI: [go_terms_relational:object_qualifier](http://w3id.org/ontogpt/go_terms_relationalobject_qualifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |  no  |
| [ProteinToGORelationship](ProteinToGORelationship.md) | A triple where the subject is a protein and the object is a GO term |  yes  |







## Properties

* Range: [NamedEntity](NamedEntity.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/go_terms_relational




## LinkML Source

<details>
```yaml
name: object_qualifier
description: An optional qualifier or modifier for the object of the statement, e.g.
  "severe" or "with additional complications"
from_schema: http://w3id.org/ontogpt/go_terms_relational
rank: 1000
alias: object_qualifier
owner: Triple
domain_of:
- Triple
range: NamedEntity

```
</details>