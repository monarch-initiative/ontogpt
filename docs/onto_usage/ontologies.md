

# Slot: ontologies

URI: [onto_usage:ontologies](http://w3id.org/ontogpt/onto_usageontologies)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) |  |  no  |







## Properties

* Range: [Ontology](Ontology.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | A semicolon-delimited list of all ontologies mentioned in the text, either in name or abbreviation. For example, "Gene Ontology", "GO", "Human Phenotype Ontology", "HPO". Include all ontologies, even if they are not the focus of a specific use case. |



### Schema Source


* from schema: http://w3id.org/ontogpt/onto_usage




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | onto_usage:ontologies |
| native | onto_usage:ontologies |




## LinkML Source

<details>
```yaml
name: ontologies
annotations:
  prompt:
    tag: prompt
    value: A semicolon-delimited list of all ontologies mentioned in the text, either
      in name or abbreviation. For example, "Gene Ontology", "GO", "Human Phenotype
      Ontology", "HPO". Include all ontologies, even if they are not the focus of
      a specific use case.
from_schema: http://w3id.org/ontogpt/onto_usage
rank: 1000
alias: ontologies
owner: Document
domain_of:
- Document
range: Ontology
multivalued: true

```
</details>