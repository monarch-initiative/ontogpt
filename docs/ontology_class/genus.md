

# Slot: genus

URI: [oc:genus](http://w3id.org/ontogpt/ontology-class-templategenus)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [LogicalDefinition](LogicalDefinition.md) |  |  no  |







## Properties

* Range: [OntologyClass](OntologyClass.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | in a logical definition expression, this is the parent (genus) class, e.g. bone |



### Schema Source


* from schema: https://w3id.org/ontogpt/ontology_class




## LinkML Source

<details>
```yaml
name: genus
annotations:
  prompt:
    tag: prompt
    value: in a logical definition expression, this is the parent (genus) class, e.g.
      bone
from_schema: https://w3id.org/ontogpt/ontology_class
rank: 1000
multivalued: true
alias: genus
owner: LogicalDefinition
domain_of:
- LogicalDefinition
range: OntologyClass

```
</details>