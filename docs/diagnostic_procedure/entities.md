

# Slot: entities

URI: [diag:entities](http://w3id.org/ontogpt/diagnostic_procedure/entities)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextWithEntity](TextWithEntity.md) | A text containing one or more instances of a single type of entity |  no  |







## Properties

* Range: [NamedEntity](NamedEntity.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/diagnostic_procedure




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | diag:entities |
| native | diag:entities |




## LinkML Source

<details>
```yaml
name: entities
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
rank: 1000
alias: entities
owner: TextWithEntity
domain_of:
- TextWithEntity
range: NamedEntity
multivalued: true

```
</details>