
# Class: Gene




URI: [reaction:Gene](http://w3id.org/ontogpt/reaction/Gene)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneReactionPairing]-%20gene%200..1>[Gene&#124;id(i):string;label(i):string%20%3F],[GeneToReaction]-%20gene%200..1>[Gene],[ReactionDocument]-%20genes%200..*>[Gene],[NamedEntity]^-[Gene],[ReactionDocument],[GeneToReaction],[GeneReactionPairing])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneReactionPairing]-%20gene%200..1>[Gene&#124;id(i):string;label(i):string%20%3F],[GeneToReaction]-%20gene%200..1>[Gene],[ReactionDocument]-%20genes%200..*>[Gene],[NamedEntity]^-[Gene],[ReactionDocument],[GeneToReaction],[GeneReactionPairing])

## Identifier prefixes

 * HGNC

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞gene](geneReactionPairing__gene.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**
 *  **None** *[➞gene](geneToReaction__gene.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**
 *  **None** *[➞genes](reactionDocument__genes.md)*  <sub>0..\*</sub>  **[Gene](Gene.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
