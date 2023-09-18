
# Class: Triple


Abstract parent for Relation Extraction tasks

URI: [diag:Triple](http://w3id.org/ontogpt/diagnostic_procedure/Triple)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity]<object_qualifier%200..1-%20[Triple&#124;qualifier:string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[Triple],[NamedEntity]<object%200..1-%20[Triple],[RelationshipType]<predicate%200..1-%20[Triple],[NamedEntity]<subject%200..1-%20[Triple],[TextWithTriples]++-%20triples%200..*>[Triple],[Triple]^-[DiagnosticProceduretoPhenotypeAssociation],[Triple]^-[DiagnosticProceduretoAttributeAssociation],[CompoundExpression]^-[Triple],[TextWithTriples],[RelationshipType],[NamedEntity],[DiagnosticProceduretoPhenotypeAssociation],[DiagnosticProceduretoAttributeAssociation],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity]<object_qualifier%200..1-%20[Triple&#124;qualifier:string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[Triple],[NamedEntity]<object%200..1-%20[Triple],[RelationshipType]<predicate%200..1-%20[Triple],[NamedEntity]<subject%200..1-%20[Triple],[TextWithTriples]++-%20triples%200..*>[Triple],[Triple]^-[DiagnosticProceduretoPhenotypeAssociation],[Triple]^-[DiagnosticProceduretoAttributeAssociation],[CompoundExpression]^-[Triple],[TextWithTriples],[RelationshipType],[NamedEntity],[DiagnosticProceduretoPhenotypeAssociation],[DiagnosticProceduretoAttributeAssociation],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Children

 * [DiagnosticProceduretoAttributeAssociation](DiagnosticProceduretoAttributeAssociation.md) - A triple representing a relationship between a diagnostic procedure and a measured attribute, e.g., "blood pressure measurement" is associated with "blood pressure" (or in OBA, something like OBA:VT0000183, "blood pressure trait").
 * [DiagnosticProceduretoPhenotypeAssociation](DiagnosticProceduretoPhenotypeAssociation.md) - A triple representing a relationship between a diagnostic procedure and an associated phenotype, e.g., "blood pressure measurement" is associated with "high blood pressure".

## Referenced by Class

 *  **None** *[➞triples](textWithTriples__triples.md)*  <sub>0..\*</sub>  **[Triple](Triple.md)**

## Attributes


### Own

 * [➞subject](triple__subject.md)  <sub>0..1</sub>
     * Range: [NamedEntity](NamedEntity.md)
 * [➞predicate](triple__predicate.md)  <sub>0..1</sub>
     * Range: [RelationshipType](RelationshipType.md)
 * [➞object](triple__object.md)  <sub>0..1</sub>
     * Range: [NamedEntity](NamedEntity.md)
 * [➞qualifier](triple__qualifier.md)  <sub>0..1</sub>
     * Description: A qualifier for the statements, e.g. "NOT" for negation
     * Range: [String](types/String.md)
 * [➞subject_qualifier](triple__subject_qualifier.md)  <sub>0..1</sub>
     * Description: An optional qualifier or modifier for the subject of the statement, e.g. "high dose" or "intravenously administered"
     * Range: [NamedEntity](NamedEntity.md)
 * [➞object_qualifier](triple__object_qualifier.md)  <sub>0..1</sub>
     * Description: An optional qualifier or modifier for the object of the statement, e.g. "severe" or "with additional complications"
     * Range: [NamedEntity](NamedEntity.md)
