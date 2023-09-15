
# Class: Organism




URI: [gocam:Organism](http://w3id.org/ontogpt/gocam/Organism)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneOrganismRelationship]-%20organism%200..1>[Organism&#124;id(i):string;label(i):string%20%3F],[IBDAnnotations]-%20organisms%200..*>[Organism],[NamedEntity]^-[Organism],[NamedEntity],[IBDAnnotations],[GeneOrganismRelationship])](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneOrganismRelationship]-%20organism%200..1>[Organism&#124;id(i):string;label(i):string%20%3F],[IBDAnnotations]-%20organisms%200..*>[Organism],[NamedEntity]^-[Organism],[NamedEntity],[IBDAnnotations],[GeneOrganismRelationship])

## Identifier prefixes

 * NCBITaxon
 * EFO

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞organism](geneOrganismRelationship__organism.md)*  <sub>0..1</sub>  **[Organism](Organism.md)**
 *  **None** *[➞organisms](iBDAnnotations__organisms.md)*  <sub>0..\*</sub>  **[Organism](Organism.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
