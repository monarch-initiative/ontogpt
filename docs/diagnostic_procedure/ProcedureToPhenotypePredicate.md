
# Class: ProcedureToPhenotypePredicate


A predicate for procedure to phenotype relationships, defining "this procedure is intended to provide support for/against this phenotype".

URI: [diag:ProcedureToPhenotypePredicate](http://w3id.org/ontogpt/diagnostic_procedure/ProcedureToPhenotypePredicate)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipType],[DiagnosticProceduretoPhenotypeAssociation]-%20predicate%200..1>[ProcedureToPhenotypePredicate&#124;id(i):string;label(i):string%20%3F],[RelationshipType]^-[ProcedureToPhenotypePredicate],[DiagnosticProceduretoPhenotypeAssociation])](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipType],[DiagnosticProceduretoPhenotypeAssociation]-%20predicate%200..1>[ProcedureToPhenotypePredicate&#124;id(i):string;label(i):string%20%3F],[RelationshipType]^-[ProcedureToPhenotypePredicate],[DiagnosticProceduretoPhenotypeAssociation])

## Parents

 *  is_a: [RelationshipType](RelationshipType.md)

## Referenced by Class

 *  **[DiagnosticProceduretoPhenotypeAssociation](DiagnosticProceduretoPhenotypeAssociation.md)** *[DiagnosticProceduretoPhenotypeAssociation➞predicate](DiagnosticProceduretoPhenotypeAssociation_predicate.md)*  <sub>0..1</sub>  **[ProcedureToPhenotypePredicate](ProcedureToPhenotypePredicate.md)**

## Attributes


### Inherited from RelationshipType:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
