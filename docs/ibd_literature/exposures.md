

# Slot: exposures


_semicolon-separated list of exposures_



URI: [ibdlit:exposures](http://w3id.org/ontogpt/ibd_literature/exposures)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IBDAnnotations](IBDAnnotations.md) |  |  no  |







## Properties

* Range: [ChemicalExposure](ChemicalExposure.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | a chemical or molecule whose direct or indirect effects cause one or more entities to experience biological change |



### Schema Source


* from schema: http://w3id.org/ontogpt/ibd_literature




## LinkML Source

<details>
```yaml
name: exposures
annotations:
  prompt:
    tag: prompt
    value: a chemical or molecule whose direct or indirect effects cause one or more
      entities to experience biological change
description: semicolon-separated list of exposures
from_schema: http://w3id.org/ontogpt/ibd_literature
rank: 1000
multivalued: true
alias: exposures
owner: IBDAnnotations
domain_of:
- IBDAnnotations
range: ChemicalExposure

```
</details>