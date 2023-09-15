
# Class: IBDAnnotations




URI: [ibdlit:IBDAnnotations](http://w3id.org/ontogpt/ibd_literature/IBDAnnotations)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseCellularProcessRelationship]<disease_cellular_process_relationships%200..*-++[IBDAnnotations],[CellularProcess]<cellular_process%200..*-%20[IBDAnnotations],[Disease]<diseases%200..*-%20[IBDAnnotations],[GeneExposureRelationship]<gene_exposures_relationships%200..*-++[IBDAnnotations],[ChemicalExposure]<exposures%200..*-%20[IBDAnnotations],[Gene]<genes%200..*-%20[IBDAnnotations],[GeneExposureRelationship],[Gene],[DiseaseCellularProcessRelationship],[Disease],[ChemicalExposure],[CellularProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseCellularProcessRelationship]<disease_cellular_process_relationships%200..*-++[IBDAnnotations],[CellularProcess]<cellular_process%200..*-%20[IBDAnnotations],[Disease]<diseases%200..*-%20[IBDAnnotations],[GeneExposureRelationship]<gene_exposures_relationships%200..*-++[IBDAnnotations],[ChemicalExposure]<exposures%200..*-%20[IBDAnnotations],[Gene]<genes%200..*-%20[IBDAnnotations],[GeneExposureRelationship],[Gene],[DiseaseCellularProcessRelationship],[Disease],[ChemicalExposure],[CellularProcess])

## Attributes


### Own

 * [➞genes](iBDAnnotations__genes.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of genes
     * Range: [Gene](Gene.md)
 * [➞exposures](iBDAnnotations__exposures.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of exposures
     * Range: [ChemicalExposure](ChemicalExposure.md)
 * [➞gene_exposures_relationships](iBDAnnotations__gene_exposures_relationships.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of gene to molecular activity relationships
     * Range: [GeneExposureRelationship](GeneExposureRelationship.md)
 * [➞diseases](iBDAnnotations__diseases.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of diseases
     * Range: [Disease](Disease.md)
 * [➞cellular_process](iBDAnnotations__cellular_process.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of cellular processes
     * Range: [CellularProcess](CellularProcess.md)
 * [➞disease_cellular_process_relationships](iBDAnnotations__disease_cellular_process_relationships.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of disease to cellular process relationships
     * Range: [DiseaseCellularProcessRelationship](DiseaseCellularProcessRelationship.md)
