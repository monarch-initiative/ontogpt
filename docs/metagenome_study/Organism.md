
# Class: Organism




URI: [eg:Organism](http://w3id.org/ontogpt/environmental-metagenome/Organism)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]-%20organisms%200..*>[Organism&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Organism],[Study],[NamedEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[Study]-%20organisms%200..*>[Organism&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Organism],[Study],[NamedEntity])

## Identifier prefixes

 * NCBITaxon

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞organisms](study__organisms.md)*  <sub>0..\*</sub>  **[Organism](Organism.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
