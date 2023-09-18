
# Class: OntologyClass




URI: [oc:OntologyClass](http://w3id.org/ontogpt/ontology-class-templateOntologyClass)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyChange]-%20about%200..*>[OntologyClass&#124;id(i):string;label(i):string%20%3F],[OntologyIssue]-%20domains%200..*>[OntologyClass],[OntologyProblem]-%20about%200..*>[OntologyClass],[NamedEntity]^-[OntologyClass],[OntologyProblem],[OntologyIssue],[OntologyChange],[NamedEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyChange]-%20about%200..*>[OntologyClass&#124;id(i):string;label(i):string%20%3F],[OntologyIssue]-%20domains%200..*>[OntologyClass],[OntologyProblem]-%20about%200..*>[OntologyClass],[NamedEntity]^-[OntologyClass],[OntologyProblem],[OntologyIssue],[OntologyChange],[NamedEntity])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞about](ontologyChange__about.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **None** *[➞domains](ontologyIssue__domains.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **None** *[➞about](ontologyProblem__about.md)*  <sub>0..\*</sub>  **[OntologyClass](OntologyClass.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
