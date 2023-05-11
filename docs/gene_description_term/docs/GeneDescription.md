
# Class: GeneDescription


A summarization of an individual gene

URI: [bp:GeneDescription](http://w3id.org/ontogpt/biological-process-templateGeneDescription)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneDescriptionTerm],[GeneDescriptionTerm]<terms%200..*-%20[GeneDescription&#124;narrative_summary:string%20%3F],[Gene]<about%200..1-%20[GeneDescription],[Gene])](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneDescriptionTerm],[GeneDescriptionTerm]<terms%200..*-%20[GeneDescription&#124;narrative_summary:string%20%3F],[Gene]<about%200..1-%20[GeneDescription],[Gene])

## Attributes


### Own

 * [➞about](geneDescription__about.md)  <sub>0..1</sub>
     * Description: The official symbol of the gene that is described. For example "TP53". Do not include the word "gene" in the answer.
     * Range: [Gene](Gene.md)
 * [➞narrative_summary](geneDescription__narrative_summary.md)  <sub>0..1</sub>
     * Description: A free text summary describing the function of the gene
     * Range: [String](types/String.md)
 * [➞terms](geneDescription__terms.md)  <sub>0..\*</sub>
     * Description: A semicolon separated list of controlled terms drawn from the Gene Ontology that describe the function of the gene
     * Range: [GeneDescriptionTerm](GeneDescriptionTerm.md)
