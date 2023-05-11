
# Class: GeneSubcellularLocalizationRelationship




URI: [gocam:GeneSubcellularLocalizationRelationship](http://w3id.org/ontogpt/gocam/GeneSubcellularLocalizationRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneLocation]<location%200..1-%20[GeneSubcellularLocalizationRelationship],[Gene]<gene%200..1-%20[GeneSubcellularLocalizationRelationship],[GoCamAnnotations]++-%20gene_localizations%200..*>[GeneSubcellularLocalizationRelationship],[CompoundExpression]^-[GeneSubcellularLocalizationRelationship],[GoCamAnnotations],[GeneLocation],[Gene],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[GeneLocation]<location%200..1-%20[GeneSubcellularLocalizationRelationship],[Gene]<gene%200..1-%20[GeneSubcellularLocalizationRelationship],[GoCamAnnotations]++-%20gene_localizations%200..*>[GeneSubcellularLocalizationRelationship],[CompoundExpression]^-[GeneSubcellularLocalizationRelationship],[GoCamAnnotations],[GeneLocation],[Gene],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞gene_localizations](goCamAnnotations__gene_localizations.md)*  <sub>0..\*</sub>  **[GeneSubcellularLocalizationRelationship](GeneSubcellularLocalizationRelationship.md)**

## Attributes


### Own

 * [➞gene](geneSubcellularLocalizationRelationship__gene.md)  <sub>0..1</sub>
     * Range: [Gene](Gene.md)
 * [➞location](geneSubcellularLocalizationRelationship__location.md)  <sub>0..1</sub>
     * Range: [GeneLocation](GeneLocation.md)
