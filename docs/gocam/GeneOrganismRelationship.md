
# Class: GeneOrganismRelationship




URI: [gocam:GeneOrganismRelationship](http://w3id.org/ontogpt/gocam/GeneOrganismRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Organism],[Organism]<organism%200..1-%20[GeneOrganismRelationship],[Gene]<gene%200..1-%20[GeneOrganismRelationship],[GoCamAnnotations]++-%20gene_organisms%200..*>[GeneOrganismRelationship],[CompoundExpression]^-[GeneOrganismRelationship],[GoCamAnnotations],[Gene],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Organism],[Organism]<organism%200..1-%20[GeneOrganismRelationship],[Gene]<gene%200..1-%20[GeneOrganismRelationship],[GoCamAnnotations]++-%20gene_organisms%200..*>[GeneOrganismRelationship],[CompoundExpression]^-[GeneOrganismRelationship],[GoCamAnnotations],[Gene],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞gene_organisms](goCamAnnotations__gene_organisms.md)*  <sub>0..\*</sub>  **[GeneOrganismRelationship](GeneOrganismRelationship.md)**

## Attributes


### Own

 * [➞gene](geneOrganismRelationship__gene.md)  <sub>0..1</sub>
     * Range: [Gene](Gene.md)
 * [➞organism](geneOrganismRelationship__organism.md)  <sub>0..1</sub>
     * Range: [Organism](Organism.md)
