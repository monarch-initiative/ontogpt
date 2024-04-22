
# Class: GeneExposureRelationship




URI: [ibdlit:GeneExposureRelationship](http://w3id.org/ontogpt/ibd_literature/GeneExposureRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[NamedEntity],[NamedEntity]<object_qualifier%200..1-%20[GeneExposureRelationship&#124;qualifier(i):string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[GeneExposureRelationship],[Gene]<object%200..1-%20[GeneExposureRelationship],[ChemicalExposureToGenePredicate]<predicate%200..1-%20[GeneExposureRelationship],[ChemicalExposure]<subject%200..1-%20[GeneExposureRelationship],[IBDAnnotations]++-%20gene_exposures_relationships%200..*>[GeneExposureRelationship],[Triple]^-[GeneExposureRelationship],[IBDAnnotations],[Gene],[ChemicalExposureToGenePredicate],[ChemicalExposure])](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[NamedEntity],[NamedEntity]<object_qualifier%200..1-%20[GeneExposureRelationship&#124;qualifier(i):string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[GeneExposureRelationship],[Gene]<object%200..1-%20[GeneExposureRelationship],[ChemicalExposureToGenePredicate]<predicate%200..1-%20[GeneExposureRelationship],[ChemicalExposure]<subject%200..1-%20[GeneExposureRelationship],[IBDAnnotations]++-%20gene_exposures_relationships%200..*>[GeneExposureRelationship],[Triple]^-[GeneExposureRelationship],[IBDAnnotations],[Gene],[ChemicalExposureToGenePredicate],[ChemicalExposure])

## Parents

 *  is_a: [Triple](Triple.md) - Abstract parent for Relation Extraction tasks

## Referenced by Class

 *  **None** *[➞gene_exposures_relationships](iBDAnnotations__gene_exposures_relationships.md)*  <sub>0..\*</sub>  **[GeneExposureRelationship](GeneExposureRelationship.md)**

## Attributes


### Own

 * [GeneExposureRelationship➞subject](GeneExposureRelationship_subject.md)  <sub>0..1</sub>
     * Description: The name of the exposure, such as a exposure to a chemical toxin.
     * Range: [ChemicalExposure](ChemicalExposure.md)
 * [GeneExposureRelationship➞predicate](GeneExposureRelationship_predicate.md)  <sub>0..1</sub>
     * Description: The name of the type of relationship between a chemical exposure and a gene.
     * Range: [ChemicalExposureToGenePredicate](ChemicalExposureToGenePredicate.md)
 * [GeneExposureRelationship➞object](GeneExposureRelationship_object.md)  <sub>0..1</sub>
     * Description: The name of the gene in the pair. This comes second in the pair.
     * Range: [Gene](Gene.md)
 * [GeneExposureRelationship➞subject_qualifier](GeneExposureRelationship_subject_qualifier.md)  <sub>0..1</sub>
     * Description: An optional qualifier or modifier for the chemical exposure.
     * Range: [NamedEntity](NamedEntity.md)
 * [GeneExposureRelationship➞object_qualifier](GeneExposureRelationship_object_qualifier.md)  <sub>0..1</sub>
     * Description: An optional qualifier or modifier for the gene.
     * Range: [NamedEntity](NamedEntity.md)

### Inherited from Triple:

 * [➞qualifier](triple__qualifier.md)  <sub>0..1</sub>
     * Description: A qualifier for the statements, e.g. "NOT" for negation
     * Range: [String](types/String.md)
