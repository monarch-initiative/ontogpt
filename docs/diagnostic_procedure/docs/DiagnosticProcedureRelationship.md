
# Class: DiagnosticProcedureRelationship


A triple representing a relationship between a diagnostic procedure and an associated phenotype, e.g., "blood pressure measurement" is associated with "high blood pressure".

URI: [diag:DiagnosticProcedureRelationship](http://w3id.org/ontogpt/diagnostic_procedure/DiagnosticProcedureRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[ProcedureToPhenotypePredicate],[Procedure],[Phenotype],[NamedEntity],[NamedEntity]<object_qualifier%200..1-%20[DiagnosticProcedureRelationship&#124;qualifier(i):string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[DiagnosticProcedureRelationship],[ProcedureToPhenotypePredicate]<predicate%200..1-%20[DiagnosticProcedureRelationship],[Phenotype]<object%200..1-%20[DiagnosticProcedureRelationship],[Procedure]<subject%200..1-%20[DiagnosticProcedureRelationship],[Triple]^-[DiagnosticProcedureRelationship])](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[ProcedureToPhenotypePredicate],[Procedure],[Phenotype],[NamedEntity],[NamedEntity]<object_qualifier%200..1-%20[DiagnosticProcedureRelationship&#124;qualifier(i):string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[DiagnosticProcedureRelationship],[ProcedureToPhenotypePredicate]<predicate%200..1-%20[DiagnosticProcedureRelationship],[Phenotype]<object%200..1-%20[DiagnosticProcedureRelationship],[Procedure]<subject%200..1-%20[DiagnosticProcedureRelationship],[Triple]^-[DiagnosticProcedureRelationship])

## Parents

 *  is_a: [Triple](Triple.md) - Abstract parent for Relation Extraction tasks

## Referenced by Class


## Attributes


### Own

 * [DiagnosticProcedureRelationship➞subject](DiagnosticProcedureRelationship_subject.md)  <sub>0..1</sub>
     * Description: A diagnostic procedure yielding a result, which in turn may be interpreted as a phenotype. Procedures include "heart rate measurement", "blood pressure measurement", "oxygen saturation measurement", etc. In practice, procedures may be named based on what they measure, with the "measurement" part left implicit.
     * Range: [Procedure](Procedure.md)
 * [DiagnosticProcedureRelationship➞object](DiagnosticProcedureRelationship_object.md)  <sub>0..1</sub>
     * Description: The observable physical or biochemical characteristics of a patient. Not equivalent to a disease state, but may contribute to a diagnosis.
     * Range: [Phenotype](Phenotype.md)
 * [DiagnosticProcedureRelationship➞predicate](DiagnosticProcedureRelationship_predicate.md)  <sub>0..1</sub>
     * Description: The relationship type, e.g. RELATED_TO
     * Range: [ProcedureToPhenotypePredicate](ProcedureToPhenotypePredicate.md)
 * [DiagnosticProcedureRelationship➞subject_qualifier](DiagnosticProcedureRelationship_subject_qualifier.md)  <sub>0..1</sub>
     * Description: An optional qualifier or modifier for the procedure.
     * Range: [NamedEntity](NamedEntity.md)
 * [DiagnosticProcedureRelationship➞object_qualifier](DiagnosticProcedureRelationship_object_qualifier.md)  <sub>0..1</sub>
     * Description: An optional qualifier or modifier for the phenotype.
     * Range: [NamedEntity](NamedEntity.md)

### Inherited from Triple:

 * [➞qualifier](triple__qualifier.md)  <sub>0..1</sub>
     * Description: A qualifier for the statements, e.g. "NOT" for negation
     * Range: [String](types/String.md)
