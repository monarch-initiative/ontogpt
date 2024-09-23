

# Slot: triples

URI: [drug:triples](http://w3id.org/ontogpt/drug/triples)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [TextWithTriples](TextWithTriples.md) | A text containing one or more relations of the Triple type |  no  |
| [ChemicalToDiseaseDocument](ChemicalToDiseaseDocument.md) | A document that contains chemical to disease relations |  yes  |







## Properties

* Range: [Triple](Triple.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/ctd




## LinkML Source

<details>
```yaml
name: triples
from_schema: http://w3id.org/ontogpt/ctd
rank: 1000
multivalued: true
alias: triples
owner: TextWithTriples
domain_of:
- TextWithTriples
range: Triple
inlined: true
inlined_as_list: true

```
</details>