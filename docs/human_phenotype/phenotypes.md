

# Slot: phenotypes


_A semicolon-separated list of human phenotypes, including symptoms of disease. It must be semicolon-separated. Labels containing the word 'with' should be split into multiple phenotypes._



URI: [human_phenotype:phenotypes](http://w3id.org/ontogpt/human_phenotypephenotypes)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [HumanPhenotypeSet](HumanPhenotypeSet.md) |  |  no  |







## Properties

* Range: [HumanPhenotype](HumanPhenotype.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/human_phenotype




## LinkML Source

<details>
```yaml
name: phenotypes
description: A semicolon-separated list of human phenotypes, including symptoms of
  disease. It must be semicolon-separated. Labels containing the word 'with' should
  be split into multiple phenotypes.
from_schema: http://w3id.org/ontogpt/human_phenotype
rank: 1000
multivalued: true
alias: phenotypes
owner: HumanPhenotypeSet
domain_of:
- HumanPhenotypeSet
range: HumanPhenotype

```
</details>