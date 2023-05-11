
# Class: DiagnosticProcedure




URI: [diag:DiagnosticProcedure](http://w3id.org/ontogpt/diagnostic_procedure/DiagnosticProcedure)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[DiagnosticProceduretoPhenotypeAssociation],[DiagnosticProceduretoAttributeAssociation],[DiagnosticProceduretoAttributeAssociation]-%20subject%200..1>[DiagnosticProcedure&#124;id(i):string;label(i):string%20%3F],[DiagnosticProceduretoPhenotypeAssociation]-%20subject%200..1>[DiagnosticProcedure],[NamedEntity]^-[DiagnosticProcedure])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[DiagnosticProceduretoPhenotypeAssociation],[DiagnosticProceduretoAttributeAssociation],[DiagnosticProceduretoAttributeAssociation]-%20subject%200..1>[DiagnosticProcedure&#124;id(i):string;label(i):string%20%3F],[DiagnosticProceduretoPhenotypeAssociation]-%20subject%200..1>[DiagnosticProcedure],[NamedEntity]^-[DiagnosticProcedure])

## Identifier prefixes

 * LOINC

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **[DiagnosticProceduretoAttributeAssociation](DiagnosticProceduretoAttributeAssociation.md)** *[DiagnosticProceduretoAttributeAssociation➞subject](DiagnosticProceduretoAttributeAssociation_subject.md)*  <sub>0..1</sub>  **[DiagnosticProcedure](DiagnosticProcedure.md)**
 *  **[DiagnosticProceduretoPhenotypeAssociation](DiagnosticProceduretoPhenotypeAssociation.md)** *[DiagnosticProceduretoPhenotypeAssociation➞subject](DiagnosticProceduretoPhenotypeAssociation_subject.md)*  <sub>0..1</sub>  **[DiagnosticProcedure](DiagnosticProcedure.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
