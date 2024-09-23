

# Slot: terms


_A semicolon separated list of controlled terms drawn from the Gene Ontology that describe the function of the gene_



URI: [bp:terms](http://w3id.org/ontogpt/biological-process-templateterms)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [GeneDescription](GeneDescription.md) | A summarization of an individual gene |  no  |







## Properties

* Range: [GeneDescriptionTerm](GeneDescriptionTerm.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/ontogpt/go_term




## LinkML Source

<details>
```yaml
name: terms
description: A semicolon separated list of controlled terms drawn from the Gene Ontology
  that describe the function of the gene
from_schema: https://w3id.org/ontogpt/go_term
rank: 1000
multivalued: true
alias: terms
owner: GeneDescription
domain_of:
- GeneDescription
range: GeneDescriptionTerm

```
</details>