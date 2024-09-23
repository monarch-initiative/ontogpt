

# Slot: ecological_traits


_The ecological traits for the taxon._



URI: [traits:ecological_traits](http://w3id.org/ontogpt/traits/ecological_traits)



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
| prompt | a semicolon separated list of every specific organism ecological trait |



### Schema Source


* from schema: http://w3id.org/ontogpt/traits




## LinkML Source

<details>
```yaml
name: ecological_traits
annotations:
  prompt:
    tag: prompt
    value: a semicolon separated list of every specific organism ecological trait
description: The ecological traits for the taxon.
from_schema: http://w3id.org/ontogpt/traits
rank: 1000
multivalued: true
alias: ecological_traits
owner: Taxon
domain_of:
- Taxon
range: Trait

```
</details>