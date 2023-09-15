
# Class: Organism




URI: [reaction:Organism](http://w3id.org/ontogpt/reaction/Organism)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneToReaction]-%20organism%200..1>[Organism&#124;id(i):string;label(i):string%20%3F],[ReactionDocument]-%20organism%200..1>[Organism],[NamedEntity]^-[Organism],[ReactionDocument],[NamedEntity],[GeneToReaction])](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneToReaction]-%20organism%200..1>[Organism&#124;id(i):string;label(i):string%20%3F],[ReactionDocument]-%20organism%200..1>[Organism],[NamedEntity]^-[Organism],[ReactionDocument],[NamedEntity],[GeneToReaction])

## Identifier prefixes

 * NCBITaxon

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞organism](geneToReaction__organism.md)*  <sub>0..1</sub>  **[Organism](Organism.md)**
 *  **None** *[➞organism](reactionDocument__organism.md)*  <sub>0..1</sub>  **[Organism](Organism.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
