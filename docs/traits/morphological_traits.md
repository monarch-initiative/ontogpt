

# Slot: morphological_traits


_The morphological traits for the taxon._



URI: [traits:morphological_traits](http://w3id.org/ontogpt/traits/morphological_traits)



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
| prompt | a semicolon separated list of every specific organism morphological trait |



### Schema Source


* from schema: http://w3id.org/ontogpt/traits




## LinkML Source

<details>
```yaml
name: morphological_traits
annotations:
  prompt:
    tag: prompt
    value: a semicolon separated list of every specific organism morphological trait
description: The morphological traits for the taxon.
from_schema: http://w3id.org/ontogpt/traits
rank: 1000
multivalued: true
alias: morphological_traits
owner: Taxon
domain_of:
- Taxon
range: Trait

```
</details>