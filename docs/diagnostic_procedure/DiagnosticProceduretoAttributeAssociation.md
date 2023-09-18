
# Class: DiagnosticProceduretoAttributeAssociation


A triple representing a relationship between a diagnostic procedure and a measured attribute, e.g., "blood pressure measurement" is associated with "blood pressure" (or in OBA, something like OBA:VT0000183, "blood pressure trait").

URI: [diag:DiagnosticProceduretoAttributeAssociation](http://w3id.org/ontogpt/diagnostic_procedure/DiagnosticProceduretoAttributeAssociation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[Quality],[ProcedureToAttributePredicate],[NamedEntity],[Quality]<object_qualifier%200..1-%20[DiagnosticProceduretoAttributeAssociation&#124;qualifier(i):string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[DiagnosticProceduretoAttributeAssociation],[ProcedureToAttributePredicate]<predicate%200..1-%20[DiagnosticProceduretoAttributeAssociation],[ClinicalAttribute]<object%200..*-%20[DiagnosticProceduretoAttributeAssociation],[DiagnosticProcedure]<subject%200..1-%20[DiagnosticProceduretoAttributeAssociation],[Triple]^-[DiagnosticProceduretoAttributeAssociation],[DiagnosticProcedure],[ClinicalAttribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[Quality],[ProcedureToAttributePredicate],[NamedEntity],[Quality]<object_qualifier%200..1-%20[DiagnosticProceduretoAttributeAssociation&#124;qualifier(i):string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[DiagnosticProceduretoAttributeAssociation],[ProcedureToAttributePredicate]<predicate%200..1-%20[DiagnosticProceduretoAttributeAssociation],[ClinicalAttribute]<object%200..*-%20[DiagnosticProceduretoAttributeAssociation],[DiagnosticProcedure]<subject%200..1-%20[DiagnosticProceduretoAttributeAssociation],[Triple]^-[DiagnosticProceduretoAttributeAssociation],[DiagnosticProcedure],[ClinicalAttribute])

## Parents

 *  is_a: [Triple](Triple.md) - Abstract parent for Relation Extraction tasks

## Referenced by Class


## Attributes


### Own

 * [DiagnosticProceduretoAttributeAssociation➞subject](DiagnosticProceduretoAttributeAssociation_subject.md)  <sub>0..1</sub>
     * Description: A diagnostic procedure yielding a result, which in turn may be interpreted as a phenotype. Procedures include "heart rate measurement", "blood pressure measurement", "oxygen saturation measurement", etc. In practice, procedures may be named based on what they measure, with the "measurement" part left implicit.
     * Range: [DiagnosticProcedure](DiagnosticProcedure.md)
 * [DiagnosticProceduretoAttributeAssociation➞object](DiagnosticProceduretoAttributeAssociation_object.md)  <sub>0..\*</sub>
     * Description: Any measurable clinical attribute.
     * Range: [ClinicalAttribute](ClinicalAttribute.md)
 * [DiagnosticProceduretoAttributeAssociation➞predicate](DiagnosticProceduretoAttributeAssociation_predicate.md)  <sub>0..1</sub>
     * Description: The relationship type, e.g. RELATED_TO
     * Range: [ProcedureToAttributePredicate](ProcedureToAttributePredicate.md)
 * [DiagnosticProceduretoAttributeAssociation➞subject_qualifier](DiagnosticProceduretoAttributeAssociation_subject_qualifier.md)  <sub>0..1</sub>
     * Description: An optional qualifier or modifier for the procedure.
     * Range: [NamedEntity](NamedEntity.md)
 * [DiagnosticProceduretoAttributeAssociation➞object_qualifier](DiagnosticProceduretoAttributeAssociation_object_qualifier.md)  <sub>0..1</sub>
     * Description: An optional qualifier or modifier for the phenotype.
     * Range: [Quality](Quality.md)

### Inherited from Triple:

 * [➞qualifier](triple__qualifier.md)  <sub>0..1</sub>
     * Description: A qualifier for the statements, e.g. "NOT" for negation
     * Range: [String](types/String.md)
