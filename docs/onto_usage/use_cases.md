

# Slot: use_cases

URI: [onto_usage:use_cases](http://w3id.org/ontogpt/onto_usageuse_cases)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) |  |  no  |







## Properties

* Range: [UseCase](UseCase.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | A semicolon-delimited list of all use cases mentioned in the text. A use case is a specific application or context in which an ontology is used. For example, "Gene Ontology USED FOR gene function prediction", "MONDO Disease Ontology USED FOR disease diagnosis" |



### Schema Source


* from schema: http://w3id.org/ontogpt/onto_usage




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | onto_usage:use_cases |
| native | onto_usage:use_cases |




## LinkML Source

<details>
```yaml
name: use_cases
annotations:
  prompt:
    tag: prompt
    value: A semicolon-delimited list of all use cases mentioned in the text. A use
      case is a specific application or context in which an ontology is used. For
      example, "Gene Ontology USED FOR gene function prediction", "MONDO Disease Ontology
      USED FOR disease diagnosis"
from_schema: http://w3id.org/ontogpt/onto_usage
rank: 1000
alias: use_cases
owner: Document
domain_of:
- Document
range: UseCase
multivalued: true

```
</details>