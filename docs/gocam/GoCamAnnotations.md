
# Class: GoCamAnnotations




URI: [gocam:GoCamAnnotations](http://w3id.org/ontogpt/gocam/GoCamAnnotations)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Pathway],[Organism],[MolecularActivity],[GeneSubcellularLocalizationRelationship]<gene_localizations%200..*-++[GoCamAnnotations],[GeneGeneInteraction]<gene_gene_interactions%200..*-++[GoCamAnnotations],[Pathway]<pathways%200..*-%20[GoCamAnnotations],[CellularProcess]<cellular_processes%200..*-%20[GoCamAnnotations],[GeneMolecularActivityRelationship]<gene_functions%200..*-++[GoCamAnnotations],[MolecularActivity]<activities%200..*-%20[GoCamAnnotations],[GeneOrganismRelationship]<gene_organisms%200..*-++[GoCamAnnotations],[Organism]<organisms%200..*-%20[GoCamAnnotations],[Gene]<genes%200..*-%20[GoCamAnnotations],[GeneSubcellularLocalizationRelationship],[GeneOrganismRelationship],[GeneMolecularActivityRelationship],[GeneGeneInteraction],[Gene],[CellularProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[Pathway],[Organism],[MolecularActivity],[GeneSubcellularLocalizationRelationship]<gene_localizations%200..*-++[GoCamAnnotations],[GeneGeneInteraction]<gene_gene_interactions%200..*-++[GoCamAnnotations],[Pathway]<pathways%200..*-%20[GoCamAnnotations],[CellularProcess]<cellular_processes%200..*-%20[GoCamAnnotations],[GeneMolecularActivityRelationship]<gene_functions%200..*-++[GoCamAnnotations],[MolecularActivity]<activities%200..*-%20[GoCamAnnotations],[GeneOrganismRelationship]<gene_organisms%200..*-++[GoCamAnnotations],[Organism]<organisms%200..*-%20[GoCamAnnotations],[Gene]<genes%200..*-%20[GoCamAnnotations],[GeneSubcellularLocalizationRelationship],[GeneOrganismRelationship],[GeneMolecularActivityRelationship],[GeneGeneInteraction],[Gene],[CellularProcess])

## Attributes


### Own

 * [➞genes](goCamAnnotations__genes.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of genes
     * Range: [Gene](Gene.md)
 * [➞organisms](goCamAnnotations__organisms.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of organism taxons
     * Range: [Organism](Organism.md)
 * [➞gene_organisms](goCamAnnotations__gene_organisms.md)  <sub>0..\*</sub>
     * Range: [GeneOrganismRelationship](GeneOrganismRelationship.md)
 * [➞activities](goCamAnnotations__activities.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of molecular activities
     * Range: [MolecularActivity](MolecularActivity.md)
 * [➞gene_functions](goCamAnnotations__gene_functions.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of gene to molecular activity relationships
     * Range: [GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md)
 * [➞cellular_processes](goCamAnnotations__cellular_processes.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of cellular processes
     * Range: [CellularProcess](CellularProcess.md)
 * [➞pathways](goCamAnnotations__pathways.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of pathways
     * Range: [Pathway](Pathway.md)
 * [➞gene_gene_interactions](goCamAnnotations__gene_gene_interactions.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of gene to gene interactions
     * Range: [GeneGeneInteraction](GeneGeneInteraction.md)
 * [➞gene_localizations](goCamAnnotations__gene_localizations.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of genes plus their location in the cell; for example, "gene1 / cytoplasm; gene2 / mitochondrion"
     * Range: [GeneSubcellularLocalizationRelationship](GeneSubcellularLocalizationRelationship.md)
