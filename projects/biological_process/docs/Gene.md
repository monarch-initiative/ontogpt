
# Class: Gene




URI: [bp:Gene](http://w3id.org/ontogpt/biological-process-templateGene)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[BiologicalProcess]-%20genes%200..*>[Gene&#124;id(i):string;label(i):string%20%3F],[GeneMolecularActivityRelationship]-%20gene%200..1>[Gene],[NamedEntity]^-[Gene],[GeneMolecularActivityRelationship],[BiologicalProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[BiologicalProcess]-%20genes%200..*>[Gene&#124;id(i):string;label(i):string%20%3F],[GeneMolecularActivityRelationship]-%20gene%200..1>[Gene],[NamedEntity]^-[Gene],[GeneMolecularActivityRelationship],[BiologicalProcess])

## Identifier prefixes

 * HGNC

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞genes](biologicalProcess__genes.md)*  <sub>0..\*</sub>  **[Gene](Gene.md)**
 *  **None** *[➞gene](geneMolecularActivityRelationship__gene.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
