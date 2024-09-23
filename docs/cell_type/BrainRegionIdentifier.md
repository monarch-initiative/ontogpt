# Enum: BrainRegionIdentifier




_Brain region (or for now, any nervous system part)_



URI: [BrainRegionIdentifier](BrainRegionIdentifier.md)


_This is a dynamic enum_








## Comments

* consider adding brain atlases here

## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type




## LinkML Source

<details>
```yaml
name: BrainRegionIdentifier
description: Brain region (or for now, any nervous system part)
comments:
- consider adding brain atlases here
from_schema: http://w3id.org/ontogpt/cell_type
rank: 1000
include:
- reachable_from:
    source_ontology: obo:uberon
    source_nodes:
    - UBERON:0001016
    relationship_types:
    - rdfs:subClassOf
    - BFO:0000050
- reachable_from:
    source_ontology: obo:fbbt
    source_nodes:
    - FBbt:00005093
    relationship_types:
    - rdfs:subClassOf
    - BFO:0000050
- reachable_from:
    source_ontology: obo:wbbt
    source_nodes:
    - WBbt:0005735
    relationship_types:
    - rdfs:subClassOf
    - BFO:0000050

```
</details>
