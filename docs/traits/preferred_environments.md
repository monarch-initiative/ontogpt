

# Slot: preferred_environments


_The preferred environments for the taxon._



URI: [traits:preferred_environments](http://w3id.org/ontogpt/traits/preferred_environments)



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
| prompt | a semicolon separated list of the environments the organism is typically found in or isolated from |



### Schema Source


* from schema: http://w3id.org/ontogpt/traits




## LinkML Source

<details>
```yaml
name: preferred_environments
annotations:
  prompt:
    tag: prompt
    value: a semicolon separated list of the environments the organism is typically
      found in or isolated from
description: The preferred environments for the taxon.
from_schema: http://w3id.org/ontogpt/traits
rank: 1000
multivalued: true
alias: preferred_environments
owner: Taxon
domain_of:
- Taxon
range: Trait

```
</details>