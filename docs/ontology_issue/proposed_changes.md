# Slot: proposed_changes
_What part of the ontology does this pertain to._


URI: [oc:proposed_changes](http://w3id.org/ontogpt/ontology-class-templateproposed_changes)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[OntologyIssue](OntologyIssue.md) | 






## Properties

* Range: [OntologyChange](OntologyChange.md)
* Multivalued: True








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of grouping terms in the ontology. Example terms will be high level terms in the relevant ontology, e.g. "skeletal system" for an anatomy ontology. |



### Schema Source


* from schema: https://w3id.org/ontogpt/ontology_issue




## LinkML Source

<details>
```yaml
name: proposed_changes
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of grouping terms in the ontology. Example terms
      will be high level terms in the relevant ontology, e.g. "skeletal system" for
      an anatomy ontology.
description: What part of the ontology does this pertain to.
from_schema: https://w3id.org/ontogpt/ontology_issue
rank: 1000
multivalued: true
alias: proposed_changes
owner: OntologyIssue
domain_of:
- OntologyIssue
range: OntologyChange

```
</details>