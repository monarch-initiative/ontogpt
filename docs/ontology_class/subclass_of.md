# Slot: subclass_of

URI: [oc:subclass_of](http://w3id.org/ontogpt/ontology-class-templatesubclass_of)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[OntologyClass](OntologyClass.md) | 






## Properties

* Range: [OntologyClass](OntologyClass.md)
* Multivalued: True








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | semicolon-separated list of parent classes |



### Schema Source


* from schema: https://w3id.org/ontogpt/ontology_class




## LinkML Source

<details>
```yaml
name: subclass_of
annotations:
  prompt:
    tag: prompt
    value: semicolon-separated list of parent classes
from_schema: https://w3id.org/ontogpt/ontology_class
rank: 1000
multivalued: true
alias: subclass_of
owner: OntologyClass
domain_of:
- OntologyClass
range: OntologyClass

```
</details>