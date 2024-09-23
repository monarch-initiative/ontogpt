

# Slot: genes

URI: [mendelian_disease:genes](http://w3id.org/ontogpt/mendelian_disease/genes)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MendelianDisease](MendelianDisease.md) |  |  no  |







## Properties

* Range: [Gene](Gene.md)

* Multivalued: True






## Examples

| Value |
| --- |
| PEX1 |
| PEX2 |
| PEX3 |

## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon separated list of gene symbols; for example: PEX1; PEX2; PEX3 |



### Schema Source


* from schema: http://w3id.org/ontogpt/mendelian_disease




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mendelian_disease:genes |
| native | mendelian_disease:genes |




## LinkML Source

<details>
```yaml
name: genes
annotations:
  prompt:
    tag: prompt
    value: 'semicolon separated list of gene symbols; for example: PEX1; PEX2; PEX3'
examples:
- value: PEX1
- value: PEX2
- value: PEX3
from_schema: http://w3id.org/ontogpt/mendelian_disease
rank: 1000
alias: genes
owner: MendelianDisease
domain_of:
- MendelianDisease
range: Gene
multivalued: true

```
</details>