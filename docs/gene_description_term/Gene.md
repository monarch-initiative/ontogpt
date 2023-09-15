
# Class: Gene




URI: [bp:Gene](http://w3id.org/ontogpt/biological-process-templateGene)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneDescription]-%20about%200..1>[Gene&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Gene],[GeneDescription])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneDescription]-%20about%200..1>[Gene&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Gene],[GeneDescription])

## Identifier prefixes

 * HGNC

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞about](geneDescription__about.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
