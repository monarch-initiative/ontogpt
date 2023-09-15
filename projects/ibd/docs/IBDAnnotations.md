
# Class: IBDAnnotations




URI: [gocam:IBDAnnotations](http://w3id.org/ontogpt/gocam/IBDAnnotations)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Pathway],[Organism],[MolecularActivity],[GeneSubcellularLocalizationRelationship]<gene_localizations%200..*-++[IBDAnnotations],[GeneGeneInteraction]<gene_gene_interactions%200..*-++[IBDAnnotations],[Pathway]<pathways%200..*-%20[IBDAnnotations],[CellularProcess]<cellular_processes%200..*-%20[IBDAnnotations],[GeneMolecularActivityRelationship]<gene_functions%200..*-++[IBDAnnotations],[MolecularActivity]<activities%200..*-%20[IBDAnnotations],[GeneOrganismRelationship]<gene_organisms%200..*-++[IBDAnnotations],[Organism]<organisms%200..*-%20[IBDAnnotations],[Gene]<genes%200..*-%20[IBDAnnotations],[GeneSubcellularLocalizationRelationship],[GeneOrganismRelationship],[GeneMolecularActivityRelationship],[GeneGeneInteraction],[Gene],[CellularProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[Pathway],[Organism],[MolecularActivity],[GeneSubcellularLocalizationRelationship]<gene_localizations%200..*-++[IBDAnnotations],[GeneGeneInteraction]<gene_gene_interactions%200..*-++[IBDAnnotations],[Pathway]<pathways%200..*-%20[IBDAnnotations],[CellularProcess]<cellular_processes%200..*-%20[IBDAnnotations],[GeneMolecularActivityRelationship]<gene_functions%200..*-++[IBDAnnotations],[MolecularActivity]<activities%200..*-%20[IBDAnnotations],[GeneOrganismRelationship]<gene_organisms%200..*-++[IBDAnnotations],[Organism]<organisms%200..*-%20[IBDAnnotations],[Gene]<genes%200..*-%20[IBDAnnotations],[GeneSubcellularLocalizationRelationship],[GeneOrganismRelationship],[GeneMolecularActivityRelationship],[GeneGeneInteraction],[Gene],[CellularProcess])

## Attributes


### Own

 * [➞genes](iBDAnnotations__genes.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of genes
     * Range: [Gene](Gene.md)
 * [➞organisms](iBDAnnotations__organisms.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of organism taxons
     * Range: [Organism](Organism.md)
 * [➞gene_organisms](iBDAnnotations__gene_organisms.md)  <sub>0..\*</sub>
     * Range: [GeneOrganismRelationship](GeneOrganismRelationship.md)
 * [➞activities](iBDAnnotations__activities.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of molecular activities
     * Range: [MolecularActivity](MolecularActivity.md)
 * [➞gene_functions](iBDAnnotations__gene_functions.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of gene to molecular activity relationships
     * Range: [GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md)
 * [➞cellular_processes](iBDAnnotations__cellular_processes.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of cellular processes
     * Range: [CellularProcess](CellularProcess.md)
 * [➞pathways](iBDAnnotations__pathways.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of pathways
     * Range: [Pathway](Pathway.md)
 * [➞gene_gene_interactions](iBDAnnotations__gene_gene_interactions.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of gene to gene interactions
     * Range: [GeneGeneInteraction](GeneGeneInteraction.md)
 * [➞gene_localizations](iBDAnnotations__gene_localizations.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of genes plus their location in the cell; for example, "gene1 / cytoplasm; gene2 / mitochondrion"
     * Range: [GeneSubcellularLocalizationRelationship](GeneSubcellularLocalizationRelationship.md)
