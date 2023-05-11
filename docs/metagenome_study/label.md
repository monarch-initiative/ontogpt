# Slot: label
_The label (name) of the named thing_


URI: [rdfs:label](rdfs:label)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Location](Location.md) | 
[EnvironmentalMaterial](EnvironmentalMaterial.md) | 
[Environment](Environment.md) | 
[Variable](Variable.md) | 
[Unit](Unit.md) | 
[SequencingTechnology](SequencingTechnology.md) | 
[Treatment](Treatment.md) | 
[Organism](Organism.md) | 
[NamedEntity](NamedEntity.md) | 
[RelationshipType](RelationshipType.md) | 






## Properties

* Range: [String](String.md)





## Aliases


* name



## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| owl | AnnotationProperty, AnnotationAssertion |



### Schema Source


* from schema: http://w3id.org/ontogpt/metagenome




## LinkML Source

<details>
```yaml
name: label
annotations:
  owl:
    tag: owl
    value: AnnotationProperty, AnnotationAssertion
description: The label (name) of the named thing
from_schema: http://w3id.org/ontogpt/metagenome
aliases:
- name
rank: 1000
slot_uri: rdfs:label
alias: label
owner: NamedEntity
domain_of:
- NamedEntity
range: string

```
</details>