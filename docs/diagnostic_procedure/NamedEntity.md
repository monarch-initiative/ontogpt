
# Class: NamedEntity




URI: [diag:NamedEntity](http://w3id.org/ontogpt/diagnostic_procedure/NamedEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Unit],[RelationshipType],[Quality],[Phenotype],[DiagnosticProceduretoAttributeAssociation]-%20subject_qualifier%200..1>[NamedEntity&#124;id:string;label:string%20%3F],[DiagnosticProceduretoPhenotypeAssociation]-%20object_qualifier%200..1>[NamedEntity],[DiagnosticProceduretoPhenotypeAssociation]-%20subject_qualifier%200..1>[NamedEntity],[Triple]-%20object%200..1>[NamedEntity],[Triple]-%20object_qualifier%200..1>[NamedEntity],[Triple]-%20subject%200..1>[NamedEntity],[Triple]-%20subject_qualifier%200..1>[NamedEntity],[NamedEntity]^-[Unit],[NamedEntity]^-[RelationshipType],[NamedEntity]^-[Quality],[NamedEntity]^-[Phenotype],[NamedEntity]^-[DiagnosticProcedure],[NamedEntity]^-[ClinicalAttribute],[Triple],[DiagnosticProceduretoPhenotypeAssociation],[DiagnosticProceduretoAttributeAssociation],[DiagnosticProcedure],[ClinicalAttribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Unit],[RelationshipType],[Quality],[Phenotype],[DiagnosticProceduretoAttributeAssociation]-%20subject_qualifier%200..1>[NamedEntity&#124;id:string;label:string%20%3F],[DiagnosticProceduretoPhenotypeAssociation]-%20object_qualifier%200..1>[NamedEntity],[DiagnosticProceduretoPhenotypeAssociation]-%20subject_qualifier%200..1>[NamedEntity],[Triple]-%20object%200..1>[NamedEntity],[Triple]-%20object_qualifier%200..1>[NamedEntity],[Triple]-%20subject%200..1>[NamedEntity],[Triple]-%20subject_qualifier%200..1>[NamedEntity],[NamedEntity]^-[Unit],[NamedEntity]^-[RelationshipType],[NamedEntity]^-[Quality],[NamedEntity]^-[Phenotype],[NamedEntity]^-[DiagnosticProcedure],[NamedEntity]^-[ClinicalAttribute],[Triple],[DiagnosticProceduretoPhenotypeAssociation],[DiagnosticProceduretoAttributeAssociation],[DiagnosticProcedure],[ClinicalAttribute])

## Children

 * [ClinicalAttribute](ClinicalAttribute.md)
 * [DiagnosticProcedure](DiagnosticProcedure.md)
 * [Phenotype](Phenotype.md)
 * [Quality](Quality.md)
 * [RelationshipType](RelationshipType.md)
 * [Unit](Unit.md)

## Referenced by Class

 *  **[DiagnosticProceduretoAttributeAssociation](DiagnosticProceduretoAttributeAssociation.md)** *[DiagnosticProceduretoAttributeAssociation➞subject_qualifier](DiagnosticProceduretoAttributeAssociation_subject_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **[DiagnosticProceduretoPhenotypeAssociation](DiagnosticProceduretoPhenotypeAssociation.md)** *[DiagnosticProceduretoPhenotypeAssociation➞object_qualifier](DiagnosticProceduretoPhenotypeAssociation_object_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **[DiagnosticProceduretoPhenotypeAssociation](DiagnosticProceduretoPhenotypeAssociation.md)** *[DiagnosticProceduretoPhenotypeAssociation➞subject_qualifier](DiagnosticProceduretoPhenotypeAssociation_subject_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **None** *[➞object](triple__object.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **None** *[➞object_qualifier](triple__object_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **None** *[➞subject](triple__subject.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **None** *[➞subject_qualifier](triple__subject_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**

## Attributes


### Own

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
