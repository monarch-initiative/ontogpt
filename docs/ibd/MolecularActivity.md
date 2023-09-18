
# Class: MolecularActivity




URI: [gocam:MolecularActivity](http://w3id.org/ontogpt/gocam/MolecularActivity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneMolecularActivityRelationship2]-%20molecular_activity%200..1>[MolecularActivity&#124;id(i):string;label(i):string%20%3F],[GeneMolecularActivityRelationship]-%20molecular_activity%200..1>[MolecularActivity],[IBDAnnotations]-%20activities%200..*>[MolecularActivity],[NamedEntity]^-[MolecularActivity],[IBDAnnotations],[GeneMolecularActivityRelationship2],[GeneMolecularActivityRelationship])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneMolecularActivityRelationship2]-%20molecular_activity%200..1>[MolecularActivity&#124;id(i):string;label(i):string%20%3F],[GeneMolecularActivityRelationship]-%20molecular_activity%200..1>[MolecularActivity],[IBDAnnotations]-%20activities%200..*>[MolecularActivity],[NamedEntity]^-[MolecularActivity],[IBDAnnotations],[GeneMolecularActivityRelationship2],[GeneMolecularActivityRelationship])

## Identifier prefixes

 * GO

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞molecular_activity](geneMolecularActivityRelationship2__molecular_activity.md)*  <sub>0..1</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **None** *[➞molecular_activity](geneMolecularActivityRelationship__molecular_activity.md)*  <sub>0..1</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **None** *[➞activities](iBDAnnotations__activities.md)*  <sub>0..\*</sub>  **[MolecularActivity](MolecularActivity.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
