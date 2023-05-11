
# Class: ChemicalEntity




URI: [bp:ChemicalEntity](http://w3id.org/ontogpt/biological-process-templateChemicalEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[BiologicalProcess]-%20inputs%200..*>[ChemicalEntity&#124;id(i):string;label(i):string%20%3F],[BiologicalProcess]-%20outputs%200..*>[ChemicalEntity],[NamedEntity]^-[ChemicalEntity],[BiologicalProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[BiologicalProcess]-%20inputs%200..*>[ChemicalEntity&#124;id(i):string;label(i):string%20%3F],[BiologicalProcess]-%20outputs%200..*>[ChemicalEntity],[NamedEntity]^-[ChemicalEntity],[BiologicalProcess])

## Identifier prefixes

 * CHEBI

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞inputs](biologicalProcess__inputs.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **None** *[➞outputs](biologicalProcess__outputs.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
