
# Class: OntologyElement




URI: [oc:OntologyElement](http://w3id.org/ontogpt/ontology-class-templateOntologyElement)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement]<parts%200..*-%20[OntologyElement&#124;name:string;context:string%20%3F;description:string%20%3F;synonyms:string%20*;equivalent_to:string%20%3F],[OntologyElement]<subtypes%200..*-%20[OntologyElement],[OntologyElement]<part_of%200..*-%20[OntologyElement],[OntologyElement]<subclass_of%200..*-%20[OntologyElement],[Category]<categories%200..*-%20[OntologyElement],[Ontology]++-%20elements%200..*>[OntologyElement],[OntologyElement]^-[Category],[Ontology],[Category])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement]<parts%200..*-%20[OntologyElement&#124;name:string;context:string%20%3F;description:string%20%3F;synonyms:string%20*;equivalent_to:string%20%3F],[OntologyElement]<subtypes%200..*-%20[OntologyElement],[OntologyElement]<part_of%200..*-%20[OntologyElement],[OntologyElement]<subclass_of%200..*-%20[OntologyElement],[Category]<categories%200..*-%20[OntologyElement],[Ontology]++-%20elements%200..*>[OntologyElement],[OntologyElement]^-[Category],[Ontology],[Category])

## Children

 * [Category](Category.md)

## Referenced by Class

 *  **None** *[➞part_of](ontologyElement__part_of.md)*  <sub>0..\*</sub>  **[OntologyElement](OntologyElement.md)**
 *  **None** *[➞parts](ontologyElement__parts.md)*  <sub>0..\*</sub>  **[OntologyElement](OntologyElement.md)**
 *  **None** *[➞subclass_of](ontologyElement__subclass_of.md)*  <sub>0..\*</sub>  **[OntologyElement](OntologyElement.md)**
 *  **None** *[➞subtypes](ontologyElement__subtypes.md)*  <sub>0..\*</sub>  **[OntologyElement](OntologyElement.md)**
 *  **None** *[➞elements](ontology__elements.md)*  <sub>0..\*</sub>  **[OntologyElement](OntologyElement.md)**
 *  **[OntologyElement](OntologyElement.md)** *[part_of](part_of.md)*  <sub>0..\*</sub>  **[OntologyElement](OntologyElement.md)**
 *  **[OntologyElement](OntologyElement.md)** *[subclass_of](subclass_of.md)*  <sub>0..\*</sub>  **[OntologyElement](OntologyElement.md)**

## Attributes


### Own

 * [➞name](ontologyElement__name.md)  <sub>1..1</sub>
     * Description: the name of the entity
     * Range: [String](types/String.md)
 * [➞context](ontologyElement__context.md)  <sub>0..1</sub>
     * Description: the ontology to which this belongs (single-valued)
     * Range: [String](types/String.md)
 * [➞description](ontologyElement__description.md)  <sub>0..1</sub>
     * Description: a textual description of the entity (single-valued)
     * Range: [String](types/String.md)
 * [➞synonyms](ontologyElement__synonyms.md)  <sub>0..\*</sub>
     * Description: a list of alternative names of the entity
     * Range: [String](types/String.md)
 * [➞categories](ontologyElement__categories.md)  <sub>0..\*</sub>
     * Description: a list of the categories to which this entity belongs
     * Range: [Category](Category.md)
 * [➞subclass_of](ontologyElement__subclass_of.md)  <sub>0..\*</sub>
     * Description: a list of parent class (superclasses) of this entity
     * Range: [OntologyElement](OntologyElement.md)
 * [➞part_of](ontologyElement__part_of.md)  <sub>0..\*</sub>
     * Description: a list of things this element is part of
     * Range: [OntologyElement](OntologyElement.md)
 * [➞subtypes](ontologyElement__subtypes.md)  <sub>0..\*</sub>
     * Description: a list of child classes (subclasses) of this entity
     * Range: [OntologyElement](OntologyElement.md)
 * [➞parts](ontologyElement__parts.md)  <sub>0..\*</sub>
     * Description: a list of names of things this element has as parts (components)
     * Range: [OntologyElement](OntologyElement.md)
 * [➞equivalent_to](ontologyElement__equivalent_to.md)  <sub>0..1</sub>
     * Description: an OWL class expression with the necessary and sufficient conditions for this entity to be an instance of this class
     * Range: [String](types/String.md)
