
# Class: OntologyIssue




URI: [oc:OntologyIssue](http://w3id.org/ontogpt/ontology-class-templateOntologyIssue)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyProblem],[OntologyChange]<proposed_changes%200..*-++[OntologyIssue&#124;title:string%20%3F;summary:string%20%3F;status:string%20%3F],[OntologyProblem]<problem_list%200..*-++[OntologyIssue],[OntologyClass]<domains%200..*-%20[OntologyIssue],[OntologyClass],[OntologyChange])](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyProblem],[OntologyChange]<proposed_changes%200..*-++[OntologyIssue&#124;title:string%20%3F;summary:string%20%3F;status:string%20%3F],[OntologyProblem]<problem_list%200..*-++[OntologyIssue],[OntologyClass]<domains%200..*-%20[OntologyIssue],[OntologyClass],[OntologyChange])

## Attributes


### Own

 * [➞title](ontologyIssue__title.md)  <sub>0..1</sub>
     * Description: the title of the issue
     * Range: [String](types/String.md)
 * [➞summary](ontologyIssue__summary.md)  <sub>0..1</sub>
     * Description: a high level summary
     * Range: [String](types/String.md)
 * [➞status](ontologyIssue__status.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞domains](ontologyIssue__domains.md)  <sub>0..\*</sub>
     * Description: What part of the ontology does this pertain to.
     * Range: [OntologyClass](OntologyClass.md)
 * [➞problem_list](ontologyIssue__problem_list.md)  <sub>0..\*</sub>
     * Description: A list of problems stated at a high level
     * Range: [OntologyProblem](OntologyProblem.md)
 * [➞proposed_changes](ontologyIssue__proposed_changes.md)  <sub>0..\*</sub>
     * Description: What part of the ontology does this pertain to.
     * Range: [OntologyChange](OntologyChange.md)
