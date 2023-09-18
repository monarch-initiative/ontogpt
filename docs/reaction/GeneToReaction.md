
# Class: GeneToReaction




URI: [reaction:GeneToReaction](http://w3id.org/ontogpt/reaction/GeneToReaction)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Reaction],[Organism],[Organism]<organism%200..1-%20[GeneToReaction],[Reaction]<reactions%200..*-++[GeneToReaction],[Gene]<gene%200..1-%20[GeneToReaction],[Gene])](https://yuml.me/diagram/nofunky;dir:TB/class/[Reaction],[Organism],[Organism]<organism%200..1-%20[GeneToReaction],[Reaction]<reactions%200..*-++[GeneToReaction],[Gene]<gene%200..1-%20[GeneToReaction],[Gene])

## Attributes


### Own

 * [➞gene](geneToReaction__gene.md)  <sub>0..1</sub>
     * Description: name of the gene that catalyzes the reaction
     * Range: [Gene](Gene.md)
 * [➞reactions](geneToReaction__reactions.md)  <sub>0..\*</sub>
     * Description: semicolon separated list of reaction equations (e.g. A+B = C+D) catalyzed by the gene
     * Range: [Reaction](Reaction.md)
 * [➞organism](geneToReaction__organism.md)  <sub>0..1</sub>
     * Range: [Organism](Organism.md)
