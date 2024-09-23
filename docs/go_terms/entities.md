

# Slot: entities

URI: [go_terms:entities](http://w3id.org/ontogpt/go_termsentities)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextWithEntity](TextWithEntity.md) | A text containing one or more instances of a single type of entity |  no  |
| [Document](Document.md) | A document that contains biological or biomedical concepts |  no  |







## Properties

* Range: [NamedEntity](NamedEntity.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/go_terms




## LinkML Source

<details>
```yaml
name: entities
from_schema: http://w3id.org/ontogpt/go_terms
rank: 1000
multivalued: true
alias: entities
owner: TextWithEntity
domain_of:
- TextWithEntity
range: NamedEntity

```
</details>