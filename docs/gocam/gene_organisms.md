

# Slot: gene_organisms

URI: [gocam:gene_organisms](http://w3id.org/ontogpt/gocam/gene_organisms)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GoCamAnnotations](GoCamAnnotations.md) |  |  no  |







## Properties

* Range: [GeneOrganismRelationship](GeneOrganismRelationship.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of asterisk separated gene to organism relationships |



### Schema Source


* from schema: http://w3id.org/ontogpt/gocam




## LinkML Source

<details>
```yaml
name: gene_organisms
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of asterisk separated gene to organism relationships
from_schema: http://w3id.org/ontogpt/gocam
rank: 1000
multivalued: true
alias: gene_organisms
owner: GoCamAnnotations
domain_of:
- GoCamAnnotations
range: GeneOrganismRelationship

```
</details>