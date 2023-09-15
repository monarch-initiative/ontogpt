
# Class: ChemicalEntity




URI: [phenotype:ChemicalEntity](http://w3id.org/ontogpt/phenotype/ChemicalEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[Trait]-%20chemical_entity%200..1>[ChemicalEntity&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[ChemicalEntity],[Trait])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[Trait]-%20chemical_entity%200..1>[ChemicalEntity&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[ChemicalEntity],[Trait])

## Identifier prefixes

 * CHEBI
 * PR

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞chemical_entity](trait__chemical_entity.md)*  <sub>0..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
