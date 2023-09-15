
# Class: OntologyChange




URI: [oc:OntologyChange](http://w3id.org/ontogpt/ontology-class-templateOntologyChange)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass],[OntologyClass]<about%200..*-%20[OntologyChange&#124;description:string%20%3F;category:ChangeType%20%3F],[OntologyIssue]++-%20proposed_changes%200..*>[OntologyChange],[CompoundExpression]^-[OntologyChange],[OntologyIssue],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass],[OntologyClass]<about%200..*-%20[OntologyChange&#124;description:string%20%3F;category:ChangeType%20%3F],[OntologyIssue]++-%20proposed_changes%200..*>[OntologyChange],[CompoundExpression]^-[OntologyChange],[OntologyIssue],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞proposed_changes](ontologyIssue__proposed_changes.md)*  <sub>0..\*</sub>  **[OntologyChange](OntologyChange.md)**

## Attributes


### Own

 * [➞description](ontologyChange__description.md)  <sub>0..1</sub>
     * Description: A succinct description of the proposed change
     * Range: [String](types/String.md)
 * [➞category](ontologyChange__category.md)  <sub>0..1</sub>
     * Description: What kind of change?
     * Range: [ChangeType](ChangeType.md)
 * [➞about](ontologyChange__about.md)  <sub>0..\*</sub>
     * Description: What terms in the ontology will this change affect?
     * Range: [OntologyClass](OntologyClass.md)
