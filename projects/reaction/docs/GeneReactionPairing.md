
# Class: GeneReactionPairing




URI: [reaction:GeneReactionPairing](http://w3id.org/ontogpt/reaction/GeneReactionPairing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Reaction],[Reaction]<reaction%200..1-%20[GeneReactionPairing],[Gene]<gene%200..1-%20[GeneReactionPairing],[ReactionDocument]++-%20gene_reaction_pairings%200..*>[GeneReactionPairing],[CompoundExpression]^-[GeneReactionPairing],[ReactionDocument],[Gene],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Reaction],[Reaction]<reaction%200..1-%20[GeneReactionPairing],[Gene]<gene%200..1-%20[GeneReactionPairing],[ReactionDocument]++-%20gene_reaction_pairings%200..*>[GeneReactionPairing],[CompoundExpression]^-[GeneReactionPairing],[ReactionDocument],[Gene],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞gene_reaction_pairings](reactionDocument__gene_reaction_pairings.md)*  <sub>0..\*</sub>  **[GeneReactionPairing](GeneReactionPairing.md)**

## Attributes


### Own

 * [➞gene](geneReactionPairing__gene.md)  <sub>0..1</sub>
     * Description: name of the gene that catalyzes the reaction
     * Range: [Gene](Gene.md)
 * [➞reaction](geneReactionPairing__reaction.md)  <sub>0..1</sub>
     * Description: equation describing the reaction (e.g. A+B = C+D) catalyzed by the gene
     * Range: [Reaction](Reaction.md)
