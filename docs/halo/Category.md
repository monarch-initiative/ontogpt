
# Class: Category




URI: [oc:Category](http://w3id.org/ontogpt/ontology-class-templateCategory)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement],[OntologyElement]-%20categories%200..*>[Category&#124;name(i):string;context(i):string%20%3F;description(i):string%20%3F;synonyms(i):string%20*;equivalent_to(i):string%20%3F],[OntologyElement]^-[Category])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyElement],[OntologyElement]-%20categories%200..*>[Category&#124;name(i):string;context(i):string%20%3F;description(i):string%20%3F;synonyms(i):string%20*;equivalent_to(i):string%20%3F],[OntologyElement]^-[Category])

## Parents

 *  is_a: [OntologyElement](OntologyElement.md)

## Referenced by Class

 *  **None** *[➞categories](ontologyElement__categories.md)*  <sub>0..\*</sub>  **[Category](Category.md)**

## Attributes


### Inherited from OntologyElement:

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
