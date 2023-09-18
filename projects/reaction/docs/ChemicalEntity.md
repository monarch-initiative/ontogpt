
# Class: ChemicalEntity




URI: [reaction:ChemicalEntity](http://w3id.org/ontogpt/reaction/ChemicalEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[Reaction]-%20left_side%200..*>[ChemicalEntity&#124;id(i):string;label(i):string%20%3F],[Reaction]-%20right_side%200..*>[ChemicalEntity],[NamedEntity]^-[ChemicalEntity],[Reaction])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[Reaction]-%20left_side%200..*>[ChemicalEntity&#124;id(i):string;label(i):string%20%3F],[Reaction]-%20right_side%200..*>[ChemicalEntity],[NamedEntity]^-[ChemicalEntity],[Reaction])

## Identifier prefixes

 * CHEBI

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞left_side](reaction__left_side.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **None** *[➞right_side](reaction__right_side.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
