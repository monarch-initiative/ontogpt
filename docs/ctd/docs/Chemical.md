
# Class: Chemical




URI: [drug:Chemical](http://w3id.org/ontogpt/drug/Chemical)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[ChemicalToDiseaseRelationship],[ChemicalToDiseaseRelationship]-%20subject%200..1>[Chemical&#124;id:string;label(i):string%20%3F],[NamedEntity]^-[Chemical])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[ChemicalToDiseaseRelationship],[ChemicalToDiseaseRelationship]-%20subject%200..1>[Chemical&#124;id:string;label(i):string%20%3F],[NamedEntity]^-[Chemical])

## Identifier prefixes

 * MESH

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **[ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md)** *[ChemicalToDiseaseRelationship➞subject](ChemicalToDiseaseRelationship_subject.md)*  <sub>0..1</sub>  **[Chemical](Chemical.md)**

## Attributes


### Own

 * [Chemical➞id](Chemical_id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)

### Inherited from NamedEntity:

 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
