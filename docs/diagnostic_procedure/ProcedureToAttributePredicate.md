
# Class: ProcedureToAttributePredicate


A predicate for procedure to attribute relationships, defining "this procedure is a measurement of this attribute".

URI: [diag:ProcedureToAttributePredicate](http://w3id.org/ontogpt/diagnostic_procedure/ProcedureToAttributePredicate)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipType],[DiagnosticProceduretoAttributeAssociation]-%20predicate%200..1>[ProcedureToAttributePredicate&#124;id(i):string;label(i):string%20%3F],[RelationshipType]^-[ProcedureToAttributePredicate],[DiagnosticProceduretoAttributeAssociation])](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipType],[DiagnosticProceduretoAttributeAssociation]-%20predicate%200..1>[ProcedureToAttributePredicate&#124;id(i):string;label(i):string%20%3F],[RelationshipType]^-[ProcedureToAttributePredicate],[DiagnosticProceduretoAttributeAssociation])

## Parents

 *  is_a: [RelationshipType](RelationshipType.md)

## Referenced by Class

 *  **[DiagnosticProceduretoAttributeAssociation](DiagnosticProceduretoAttributeAssociation.md)** *[DiagnosticProceduretoAttributeAssociation➞predicate](DiagnosticProceduretoAttributeAssociation_predicate.md)*  <sub>0..1</sub>  **[ProcedureToAttributePredicate](ProcedureToAttributePredicate.md)**

## Attributes


### Inherited from RelationshipType:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
