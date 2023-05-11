
# Class: Phenotype




URI: [diag:Phenotype](http://w3id.org/ontogpt/diagnostic_procedure/Phenotype)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DiagnosticProceduretoPhenotypeAssociation]-%20object%200..*>[Phenotype&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Phenotype],[NamedEntity],[DiagnosticProceduretoPhenotypeAssociation])](https://yuml.me/diagram/nofunky;dir:TB/class/[DiagnosticProceduretoPhenotypeAssociation]-%20object%200..*>[Phenotype&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Phenotype],[NamedEntity],[DiagnosticProceduretoPhenotypeAssociation])

## Identifier prefixes

 * HP

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **[DiagnosticProceduretoPhenotypeAssociation](DiagnosticProceduretoPhenotypeAssociation.md)** *[DiagnosticProceduretoPhenotypeAssociation➞object](DiagnosticProceduretoPhenotypeAssociation_object.md)*  <sub>0..\*</sub>  **[Phenotype](Phenotype.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
