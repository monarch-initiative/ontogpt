# Slot: molecular_activity

URI: [gocam:molecular_activity](http://w3id.org/ontogpt/gocam/molecular_activity)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md) | 
[GeneMolecularActivityRelationship2](GeneMolecularActivityRelationship2.md) | 






## Properties

* Range: [MolecularActivity](MolecularActivity.md)







## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | the name of the molecular function in the pair. This comes second. May be a GO term. |



### Schema Source


* from schema: http://w3id.org/ontogpt/gocam




## LinkML Source

<details>
```yaml
name: molecular_activity
annotations:
  prompt:
    tag: prompt
    value: the name of the molecular function in the pair. This comes second. May
      be a GO term.
from_schema: http://w3id.org/ontogpt/gocam
rank: 1000
alias: molecular_activity
domain_of:
- GeneMolecularActivityRelationship
- GeneMolecularActivityRelationship2
range: MolecularActivity

```
</details>