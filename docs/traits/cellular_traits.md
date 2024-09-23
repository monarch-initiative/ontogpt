

# Slot: cellular_traits


_The cellular traits for the taxon._



URI: [traits:cellular_traits](http://w3id.org/ontogpt/traits/cellular_traits)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Taxon](Taxon.md) |  |  no  |







## Properties

* Range: [Trait](Trait.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | a semicolon separated list of every specific organism cellular trait |



### Schema Source


* from schema: http://w3id.org/ontogpt/traits




## LinkML Source

<details>
```yaml
name: cellular_traits
annotations:
  prompt:
    tag: prompt
    value: a semicolon separated list of every specific organism cellular trait
description: The cellular traits for the taxon.
from_schema: http://w3id.org/ontogpt/traits
rank: 1000
multivalued: true
alias: cellular_traits
owner: Taxon
domain_of:
- Taxon
range: Trait

```
</details>