

# Slot: molecularfunctions


_One or more molecular functions, as defined by the Gene Ontology._



URI: [go_terms:molecularfunctions](http://w3id.org/ontogpt/go_termsmolecularfunctions)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) | A document that contains biological or biomedical concepts |  no  |







## Properties

* Range: [MolecularFunction](MolecularFunction.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | A semi-colon separated list of molecular functions, for example: catalytic activity; amine binding; peptide receptor activity; oxygen carrier activity; structural constituent of cytoskeleton |



### Schema Source


* from schema: http://w3id.org/ontogpt/go_terms




## LinkML Source

<details>
```yaml
name: molecularfunctions
annotations:
  prompt:
    tag: prompt
    value: 'A semi-colon separated list of molecular functions, for example: catalytic
      activity; amine binding; peptide receptor activity; oxygen carrier activity;
      structural constituent of cytoskeleton'
description: One or more molecular functions, as defined by the Gene Ontology.
from_schema: http://w3id.org/ontogpt/go_terms
rank: 1000
multivalued: true
alias: molecularfunctions
owner: Document
domain_of:
- Document
range: MolecularFunction

```
</details>