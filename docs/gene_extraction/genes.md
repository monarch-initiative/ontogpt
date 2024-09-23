

# Slot: genes

URI: [geneextraction:genes](http://w3id.org/ontogpt/gene_extractiongenes)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AcronymList](AcronymList.md) |  |  no  |







## Properties

* Range: [Gene](Gene.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | A semicolon-delimited list of potential gene symbols within the text. Include all acronyms that could be gene symbols, i.e., any string of capital letters, particularly if it is followed by a number. Examples of gene symbols include: BRCA1, TP53, EGR2, ITGB6, PRKCD. Gene symbols may resemble acronyms referring to diseases or phenotypes, and may be surrounded by punctuation or other text. |



### Schema Source


* from schema: http://w3id.org/ontogpt/gene_extraction




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | geneextraction:genes |
| native | geneextraction:genes |




## LinkML Source

<details>
```yaml
name: genes
annotations:
  prompt:
    tag: prompt
    value: 'A semicolon-delimited list of potential gene symbols within the text.
      Include all acronyms that could be gene symbols, i.e., any string of capital
      letters, particularly if it is followed by a number. Examples of gene symbols
      include: BRCA1, TP53, EGR2, ITGB6, PRKCD. Gene symbols may resemble acronyms
      referring to diseases or phenotypes, and may be surrounded by punctuation or
      other text.'
from_schema: http://w3id.org/ontogpt/gene_extraction
rank: 1000
alias: genes
owner: AcronymList
domain_of:
- AcronymList
range: Gene
multivalued: true

```
</details>