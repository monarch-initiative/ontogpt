

# Slot: predicate

URI: [drug:predicate](http://w3id.org/ontogpt/drug/predicate)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |  no  |
| [ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md) | A triple where the subject is a chemical and the object is a disease |  yes  |







## Properties

* Range: [RelationshipType](RelationshipType.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/ctd




## LinkML Source

<details>
```yaml
name: predicate
from_schema: http://w3id.org/ontogpt/ctd
rank: 1000
alias: predicate
owner: Triple
domain_of:
- Triple
range: RelationshipType

```
</details>