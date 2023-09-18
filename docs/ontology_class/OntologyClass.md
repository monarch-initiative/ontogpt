
# Class: OntologyClass




URI: [oc:OntologyClass](http://w3id.org/ontogpt/ontology-class-templateOntologyClass)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[LogicalDefinition]<logical_definition%200..1-++[OntologyClass&#124;label:string%20%3F;description:string%20%3F;synonyms:string%20*;id(i):string],[OntologyClass]<subclass_of%200..*-%20[OntologyClass],[OntologyClass]<categories%200..*-%20[OntologyClass],[LogicalDefinition]-%20differentiating_characteristic_parents%200..*>[OntologyClass],[LogicalDefinition]-%20genus%200..*>[OntologyClass],[NamedEntity]^-[OntologyClass],[NamedEntity],[LogicalDefinition])](https://yuml.me/diagram/nofunky;dir:TB/class/[LogicalDefinition]<logical_definition%200..1-++[OntologyClass&#124;label:string%20%3F;description:string%20%3F;synonyms:string%20*;id(i):string],[OntologyClass]<subclass_of%200..*-%20[OntologyClass],[OntologyClass]<categories%200..*-%20[OntologyClass],[LogicalDefinition]-%20differentiating_characteristic_parents%200..*>[OntologyClass],[LogicalDefinition]-%20genus%200..*>[OntologyClass],[NamedEntity]^-[OntologyClass],[NamedEntity],[LogicalDefinition])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞differentiating_characteristic_parents](logicalDefinition__differentiating_characteristic_parents.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **None** *[➞genus](logicalDefinition__genus.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **None** *[➞categories](ontologyClass__categories.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **None** *[➞subclass_of](ontologyClass__subclass_of.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**

## Attributes


### Own

 * [➞label](ontologyClass__label.md)  <sub>0..1</sub>
     * Description: the name of the main entity being defined
     * Range: [String](types/String.md)
 * [➞description](ontologyClass__description.md)  <sub>0..1</sub>
     * Description: a textual description of the entity
     * Range: [String](types/String.md)
 * [➞synonyms](ontologyClass__synonyms.md)  <sub>0..\*</sub>
     * Description: alternative names of the entity
     * Range: [String](types/String.md)
 * [➞categories](ontologyClass__categories.md)  <sub>0..\*</sub>
     * Description: the categories to which this entity belongs.
     * Range: [OntologyClass](OntologyClass.md)
 * [➞subclass_of](ontologyClass__subclass_of.md)  <sub>0..\*</sub>
     * Range: [OntologyClass](OntologyClass.md)
 * [➞logical_definition](ontologyClass__logical_definition.md)  <sub>0..1</sub>
     * Description: the necessary and sufficient conditions for this entity to be an instance of this class
     * Range: [LogicalDefinition](LogicalDefinition.md)

### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
