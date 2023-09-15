
# Class: OntologyProblem




URI: [oc:OntologyProblem](http://w3id.org/ontogpt/ontology-class-templateOntologyProblem)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass]<about%200..*-%20[OntologyProblem&#124;description:string%20%3F;severity:string%20%3F;category:ProblemType%20%3F],[OntologyIssue]++-%20problem_list%200..*>[OntologyProblem],[CompoundExpression]^-[OntologyProblem],[OntologyIssue],[OntologyClass],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass]<about%200..*-%20[OntologyProblem&#124;description:string%20%3F;severity:string%20%3F;category:ProblemType%20%3F],[OntologyIssue]++-%20problem_list%200..*>[OntologyProblem],[CompoundExpression]^-[OntologyProblem],[OntologyIssue],[OntologyClass],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞problem_list](ontologyIssue__problem_list.md)*  <sub>0..\*</sub>  **[OntologyProblem](OntologyProblem.md)**

## Attributes


### Own

 * [➞description](ontologyProblem__description.md)  <sub>0..1</sub>
     * Description: A succinct description of the problem
     * Range: [String](types/String.md)
 * [➞severity](ontologyProblem__severity.md)  <sub>0..1</sub>
     * Description: How severe is this problem?
     * Range: [String](types/String.md)
 * [➞category](ontologyProblem__category.md)  <sub>0..1</sub>
     * Description: What category does this problem fall into?
     * Range: [ProblemType](ProblemType.md)
 * [➞about](ontologyProblem__about.md)  <sub>0..\*</sub>
     * Description: What terms in the ontology is this problem about?
     * Range: [OntologyClass](OntologyClass.md)
