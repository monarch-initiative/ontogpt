
# Class: LogicalDefinition




URI: [oc:LogicalDefinition](http://w3id.org/ontogpt/ontology-class-templateLogicalDefinition)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Relation],[OntologyClass],[OntologyClass]<differentiating_characteristic_parents%200..*-%20[LogicalDefinition],[Relation]<differentiating_characteristic_relationship%200..1-%20[LogicalDefinition],[OntologyClass]<genus%200..*-%20[LogicalDefinition],[OntologyClass]++-%20logical_definition%200..1>[LogicalDefinition])](https://yuml.me/diagram/nofunky;dir:TB/class/[Relation],[OntologyClass],[OntologyClass]<differentiating_characteristic_parents%200..*-%20[LogicalDefinition],[Relation]<differentiating_characteristic_relationship%200..1-%20[LogicalDefinition],[OntologyClass]<genus%200..*-%20[LogicalDefinition],[OntologyClass]++-%20logical_definition%200..1>[LogicalDefinition])

## Referenced by Class

 *  **None** *[➞logical_definition](ontologyClass__logical_definition.md)*  <sub>0..1</sub>  **[LogicalDefinition](LogicalDefinition.md)**

## Attributes


### Own

 * [➞genus](logicalDefinition__genus.md)  <sub>0..\*</sub>
     * Range: [OntologyClass](OntologyClass.md)
 * [➞differentiating_characteristic_relationship](logicalDefinition__differentiating_characteristic_relationship.md)  <sub>0..1</sub>
     * Range: [Relation](Relation.md)
 * [➞differentiating_characteristic_parents](logicalDefinition__differentiating_characteristic_parents.md)  <sub>0..\*</sub>
     * Range: [OntologyClass](OntologyClass.md)
