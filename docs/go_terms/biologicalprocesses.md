

# Slot: biologicalprocesses


_One or more biological processes, as defined by the Gene Ontology._



URI: [go_terms:biologicalprocesses](http://w3id.org/ontogpt/go_termsbiologicalprocesses)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) | A document that contains biological or biomedical concepts |  no  |







## Properties

* Range: [BiologicalProcess](BiologicalProcess.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | A semi-colon separated list of biological processes, for example: nuclear axial expansion; intracellular transport; medial surface of mandible; ribosomal subunit export from nucleus; pole cell development |



### Schema Source


* from schema: http://w3id.org/ontogpt/go_terms




## LinkML Source

<details>
```yaml
name: biologicalprocesses
annotations:
  prompt:
    tag: prompt
    value: 'A semi-colon separated list of biological processes, for example: nuclear
      axial expansion; intracellular transport; medial surface of mandible; ribosomal
      subunit export from nucleus; pole cell development'
description: One or more biological processes, as defined by the Gene Ontology.
from_schema: http://w3id.org/ontogpt/go_terms
rank: 1000
multivalued: true
alias: biologicalprocesses
owner: Document
domain_of:
- Document
range: BiologicalProcess

```
</details>