
# Class: ChemicalToDiseasePredicate


A predicate for chemical to disease relationships

URI: [drug:ChemicalToDiseasePredicate](http://w3id.org/ontogpt/drug/ChemicalToDiseasePredicate)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipType],[ChemicalToDiseaseRelationship],[ChemicalToDiseaseRelationship]-%20predicate%200..1>[ChemicalToDiseasePredicate&#124;id(i):string;label(i):string%20%3F],[RelationshipType]^-[ChemicalToDiseasePredicate])](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipType],[ChemicalToDiseaseRelationship],[ChemicalToDiseaseRelationship]-%20predicate%200..1>[ChemicalToDiseasePredicate&#124;id(i):string;label(i):string%20%3F],[RelationshipType]^-[ChemicalToDiseasePredicate])

## Parents

 *  is_a: [RelationshipType](RelationshipType.md)

## Referenced by Class

 *  **[ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md)** *[ChemicalToDiseaseRelationship➞predicate](ChemicalToDiseaseRelationship_predicate.md)*  <sub>0..1</sub>  **[ChemicalToDiseasePredicate](ChemicalToDiseasePredicate.md)**

## Attributes


### Inherited from RelationshipType:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | for the purposes of evaluation against BC5CDR, any predicate other than INDUCES is ignored. |

