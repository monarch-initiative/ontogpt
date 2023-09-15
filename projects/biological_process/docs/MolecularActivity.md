
# Class: MolecularActivity




URI: [bp:MolecularActivity](http://w3id.org/ontogpt/biological-process-templateMolecularActivity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[BiologicalProcess]-%20steps%200..*>[MolecularActivity&#124;id(i):string;label(i):string%20%3F],[GeneMolecularActivityRelationship]-%20molecular_activity%200..1>[MolecularActivity],[NamedEntity]^-[MolecularActivity],[GeneMolecularActivityRelationship],[BiologicalProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[BiologicalProcess]-%20steps%200..*>[MolecularActivity&#124;id(i):string;label(i):string%20%3F],[GeneMolecularActivityRelationship]-%20molecular_activity%200..1>[MolecularActivity],[NamedEntity]^-[MolecularActivity],[GeneMolecularActivityRelationship],[BiologicalProcess])

## Identifier prefixes

 * GO

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞steps](biologicalProcess__steps.md)*  <sub>0..\*</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **None** *[➞molecular_activity](geneMolecularActivityRelationship__molecular_activity.md)*  <sub>0..1</sub>  **[MolecularActivity](MolecularActivity.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
