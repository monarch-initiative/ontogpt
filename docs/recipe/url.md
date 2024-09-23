

# Slot: url

URI: [rdf:Resource](http://www.w3.org/1999/02/22-rdf-syntax-ns#Resource)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Recipe](Recipe.md) |  |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt.skip | True |



### Schema Source


* from schema: https://w3id.org/ontogpt/recipe




## LinkML Source

<details>
```yaml
name: url
annotations:
  prompt.skip:
    tag: prompt.skip
    value: true
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
slot_uri: rdf:Resource
identifier: true
alias: url
owner: Recipe
domain_of:
- Recipe
range: uriorcurie
required: true

```
</details>