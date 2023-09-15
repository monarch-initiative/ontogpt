
# Class: GeneGeneInteraction




URI: [gocam:GeneGeneInteraction](http://w3id.org/ontogpt/gocam/GeneGeneInteraction)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Gene]<gene2%200..1-%20[GeneGeneInteraction],[Gene]<gene1%200..1-%20[GeneGeneInteraction],[IBDAnnotations]++-%20gene_gene_interactions%200..*>[GeneGeneInteraction],[CompoundExpression]^-[GeneGeneInteraction],[IBDAnnotations],[Gene],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Gene]<gene2%200..1-%20[GeneGeneInteraction],[Gene]<gene1%200..1-%20[GeneGeneInteraction],[IBDAnnotations]++-%20gene_gene_interactions%200..*>[GeneGeneInteraction],[CompoundExpression]^-[GeneGeneInteraction],[IBDAnnotations],[Gene],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞gene_gene_interactions](iBDAnnotations__gene_gene_interactions.md)*  <sub>0..\*</sub>  **[GeneGeneInteraction](GeneGeneInteraction.md)**

## Attributes


### Own

 * [➞gene1](geneGeneInteraction__gene1.md)  <sub>0..1</sub>
     * Range: [Gene](Gene.md)
 * [➞gene2](geneGeneInteraction__gene2.md)  <sub>0..1</sub>
     * Range: [Gene](Gene.md)
