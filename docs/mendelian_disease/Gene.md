
# Class: Gene




URI: [mendelian_disease:Gene](http://w3id.org/ontogpt/mendelian_disease/Gene)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[MendelianDisease]-%20genes%200..*>[Gene&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Gene],[MendelianDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[MendelianDisease]-%20genes%200..*>[Gene&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Gene],[MendelianDisease])

## Identifier prefixes

 * HGNC

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞genes](mendelianDisease__genes.md)*  <sub>0..\*</sub>  **[Gene](Gene.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
