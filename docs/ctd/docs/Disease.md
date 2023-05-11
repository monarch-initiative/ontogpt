
# Class: Disease




URI: [drug:Disease](http://w3id.org/ontogpt/drug/Disease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[ChemicalToDiseaseRelationship]-%20object%200..1>[Disease&#124;id:string;label(i):string%20%3F],[NamedEntity]^-[Disease],[ChemicalToDiseaseRelationship])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[ChemicalToDiseaseRelationship]-%20object%200..1>[Disease&#124;id:string;label(i):string%20%3F],[NamedEntity]^-[Disease],[ChemicalToDiseaseRelationship])

## Identifier prefixes

 * MESH

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **[ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md)** *[ChemicalToDiseaseRelationship➞object](ChemicalToDiseaseRelationship_object.md)*  <sub>0..1</sub>  **[Disease](Disease.md)**

## Attributes


### Own

 * [Disease➞id](Disease_id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)

### Inherited from NamedEntity:

 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
