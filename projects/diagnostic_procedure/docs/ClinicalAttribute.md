
# Class: ClinicalAttribute




URI: [diag:ClinicalAttribute](http://w3id.org/ontogpt/diagnostic_procedure/ClinicalAttribute)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Unit],[NamedEntity],[DiagnosticProceduretoAttributeAssociation],[Unit]<unit%200..1-%20[ClinicalAttribute&#124;id(i):string;label(i):string%20%3F],[DiagnosticProceduretoAttributeAssociation]-%20object%200..*>[ClinicalAttribute],[NamedEntity]^-[ClinicalAttribute])](https://yuml.me/diagram/nofunky;dir:TB/class/[Unit],[NamedEntity],[DiagnosticProceduretoAttributeAssociation],[Unit]<unit%200..1-%20[ClinicalAttribute&#124;id(i):string;label(i):string%20%3F],[DiagnosticProceduretoAttributeAssociation]-%20object%200..*>[ClinicalAttribute],[NamedEntity]^-[ClinicalAttribute])

## Identifier prefixes

 * OBA

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **[DiagnosticProceduretoAttributeAssociation](DiagnosticProceduretoAttributeAssociation.md)** *[DiagnosticProceduretoAttributeAssociation➞object](DiagnosticProceduretoAttributeAssociation_object.md)*  <sub>0..\*</sub>  **[ClinicalAttribute](ClinicalAttribute.md)**

## Attributes


### Own

 * [➞unit](clinicalAttribute__unit.md)  <sub>0..1</sub>
     * Description: the unit used to measure the attribute
     * Range: [Unit](Unit.md)

### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
