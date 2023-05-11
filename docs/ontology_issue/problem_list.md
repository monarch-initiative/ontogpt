# Slot: problem_list
_A list of problems stated at a high level_


URI: [oc:problem_list](http://w3id.org/ontogpt/ontology-class-templateproblem_list)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[OntologyIssue](OntologyIssue.md) | 






## Properties

* Range: [OntologyProblem](OntologyProblem.md)
* Multivalued: True








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of problems each written as a simple statement. For example "T cell is classified in the wrong place" |



### Schema Source


* from schema: https://w3id.org/ontogpt/ontology_issue




## LinkML Source

<details>
```yaml
name: problem_list
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of problems each written as a simple statement.
      For example "T cell is classified in the wrong place"
description: A list of problems stated at a high level
from_schema: https://w3id.org/ontogpt/ontology_issue
rank: 1000
multivalued: true
alias: problem_list
owner: OntologyIssue
domain_of:
- OntologyIssue
range: OntologyProblem

```
</details>