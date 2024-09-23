

# Slot: gene_localizations


_semicolon-separated list of genes plus their location in the cell; for example, "gene1 / cytoplasm; gene2 / mitochondrion"_



URI: [gocam:gene_localizations](http://w3id.org/ontogpt/gocam/gene_localizations)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IBDAnnotations](IBDAnnotations.md) |  |  no  |







## Properties

* Range: [GeneSubcellularLocalizationRelationship](GeneSubcellularLocalizationRelationship.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/gocam




## LinkML Source

<details>
```yaml
name: gene_localizations
description: semicolon-separated list of genes plus their location in the cell; for
  example, "gene1 / cytoplasm; gene2 / mitochondrion"
from_schema: http://w3id.org/ontogpt/gocam
rank: 1000
multivalued: true
alias: gene_localizations
owner: IBDAnnotations
domain_of:
- IBDAnnotations
range: GeneSubcellularLocalizationRelationship

```
</details>