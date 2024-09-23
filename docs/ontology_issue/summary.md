

# Slot: summary


_a high level summary_



URI: [oc:summary](http://w3id.org/ontogpt/ontology-class-templatesummary)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OntologyIssue](OntologyIssue.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | a high level one or two line summary of the issue, e.g. "the definition of the class 'bone' is too vague" |



### Schema Source


* from schema: https://w3id.org/ontogpt/ontology_issue




## LinkML Source

<details>
```yaml
name: summary
annotations:
  prompt:
    tag: prompt
    value: a high level one or two line summary of the issue, e.g. "the definition
      of the class 'bone' is too vague"
description: a high level summary
from_schema: https://w3id.org/ontogpt/ontology_issue
rank: 1000
alias: summary
owner: OntologyIssue
domain_of:
- OntologyIssue
range: string

```
</details>