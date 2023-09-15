
# Class: IBDAnnotations




URI: [ibdlit:IBDAnnotations](http://w3id.org/ontogpt/ibd_literature/IBDAnnotations)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Disease]<diseases%200..*-%20[IBDAnnotations],[GeneExposureRelationship]<gene_exposures_relationships%200..*-++[IBDAnnotations],[ChemicalExposure]<exposures%200..*-%20[IBDAnnotations],[Gene]<genes%200..*-%20[IBDAnnotations],[GeneExposureRelationship],[Gene],[Disease],[ChemicalExposure])](https://yuml.me/diagram/nofunky;dir:TB/class/[Disease]<diseases%200..*-%20[IBDAnnotations],[GeneExposureRelationship]<gene_exposures_relationships%200..*-++[IBDAnnotations],[ChemicalExposure]<exposures%200..*-%20[IBDAnnotations],[Gene]<genes%200..*-%20[IBDAnnotations],[GeneExposureRelationship],[Gene],[Disease],[ChemicalExposure])

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
