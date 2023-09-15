
# Class: ReactionDocument




URI: [reaction:ReactionDocument](http://w3id.org/ontogpt/reaction/ReactionDocument)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Evidence]<has_evidence%200..*-%20[ReactionDocument],[Organism]<organism%200..1-%20[ReactionDocument],[GeneReactionPairing]<gene_reaction_pairings%200..*-++[ReactionDocument],[Reaction]<reactions%200..*-++[ReactionDocument],[Gene]<genes%200..*-%20[ReactionDocument],[Reaction],[Organism],[GeneReactionPairing],[Gene],[Evidence])](https://yuml.me/diagram/nofunky;dir:TB/class/[Evidence]<has_evidence%200..*-%20[ReactionDocument],[Organism]<organism%200..1-%20[ReactionDocument],[GeneReactionPairing]<gene_reaction_pairings%200..*-++[ReactionDocument],[Reaction]<reactions%200..*-++[ReactionDocument],[Gene]<genes%200..*-%20[ReactionDocument],[Reaction],[Organism],[GeneReactionPairing],[Gene],[Evidence])

## Attributes


### Own

 * [➞genes](reactionDocument__genes.md)  <sub>0..\*</sub>
     * Description: semicolon separated list of genes that catalyzes the mentioned reactions
     * Range: [Gene](Gene.md)
 * [➞reactions](reactionDocument__reactions.md)  <sub>0..\*</sub>
     * Description: semicolon separated list of reaction equations (e.g. A+B = C+D) catalyzed by the gene
     * Range: [Reaction](Reaction.md)
 * [➞gene_reaction_pairings](reactionDocument__gene_reaction_pairings.md)  <sub>0..\*</sub>
     * Description: semicolon separated list of gene to reaction pairings
     * Range: [GeneReactionPairing](GeneReactionPairing.md)
 * [➞organism](reactionDocument__organism.md)  <sub>0..1</sub>
     * Range: [Organism](Organism.md)
 * [➞has_evidence](reactionDocument__has_evidence.md)  <sub>0..\*</sub>
     * Description: evidence for the reaction
     * Range: [Evidence](Evidence.md)
