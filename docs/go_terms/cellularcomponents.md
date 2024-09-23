

# Slot: cellularcomponents


_One or more cellular components, as defined by the Gene Ontology._



URI: [go_terms:cellularcomponents](http://w3id.org/ontogpt/go_termscellularcomponents)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) | A document that contains biological or biomedical concepts |  no  |







## Properties

* Range: [CellularComponent](CellularComponent.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | A semi-colon separated list of cellular components and structures, for example: tubulin complex; proteasome complex; cytoplasm; keratohyalin granule; nucleus |



### Schema Source


* from schema: http://w3id.org/ontogpt/go_terms




## LinkML Source

<details>
```yaml
name: cellularcomponents
annotations:
  prompt:
    tag: prompt
    value: 'A semi-colon separated list of cellular components and structures, for
      example: tubulin complex; proteasome complex; cytoplasm; keratohyalin granule;
      nucleus'
description: One or more cellular components, as defined by the Gene Ontology.
from_schema: http://w3id.org/ontogpt/go_terms
rank: 1000
multivalued: true
alias: cellularcomponents
owner: Document
domain_of:
- Document
range: CellularComponent

```
</details>