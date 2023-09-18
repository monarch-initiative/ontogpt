
# Class: GeneMolecularActivityRelationship




URI: [gocam:GeneMolecularActivityRelationship](http://w3id.org/ontogpt/gocam/GeneMolecularActivityRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MolecularActivity],[MolecularActivity]<molecular_activity%200..1-%20[GeneMolecularActivityRelationship],[Gene]<gene%200..1-%20[GeneMolecularActivityRelationship],[IBDAnnotations]++-%20gene_functions%200..*>[GeneMolecularActivityRelationship],[CompoundExpression]^-[GeneMolecularActivityRelationship],[IBDAnnotations],[Gene],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[MolecularActivity],[MolecularActivity]<molecular_activity%200..1-%20[GeneMolecularActivityRelationship],[Gene]<gene%200..1-%20[GeneMolecularActivityRelationship],[IBDAnnotations]++-%20gene_functions%200..*>[GeneMolecularActivityRelationship],[CompoundExpression]^-[GeneMolecularActivityRelationship],[IBDAnnotations],[Gene],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞gene_functions](iBDAnnotations__gene_functions.md)*  <sub>0..\*</sub>  **[GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md)**

## Attributes


### Own

 * [➞gene](geneMolecularActivityRelationship__gene.md)  <sub>0..1</sub>
     * Range: [Gene](Gene.md)
 * [➞molecular_activity](geneMolecularActivityRelationship__molecular_activity.md)  <sub>0..1</sub>
     * Range: [MolecularActivity](MolecularActivity.md)
