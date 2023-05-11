
# Class: Procedure




URI: [diag:Procedure](http://w3id.org/ontogpt/diagnostic_procedure/Procedure)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DiagnosticProcedure]-%20procedure_name%200..1>[Procedure&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Procedure],[NamedEntity],[DiagnosticProcedure])](https://yuml.me/diagram/nofunky;dir:TB/class/[DiagnosticProcedure]-%20procedure_name%200..1>[Procedure&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Procedure],[NamedEntity],[DiagnosticProcedure])

## Identifier prefixes

 * LOINC

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞procedure_name](diagnosticProcedure__procedure_name.md)*  <sub>0..1</sub>  **[Procedure](Procedure.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
