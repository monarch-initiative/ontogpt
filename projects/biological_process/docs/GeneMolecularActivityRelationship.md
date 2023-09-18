
# Class: GeneMolecularActivityRelationship




URI: [bp:GeneMolecularActivityRelationship](http://w3id.org/ontogpt/biological-process-templateGeneMolecularActivityRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MolecularActivity],[MolecularActivity]<molecular_activity%200..1-%20[GeneMolecularActivityRelationship],[Gene]<gene%200..1-%20[GeneMolecularActivityRelationship],[BiologicalProcess]++-%20gene_activities%200..*>[GeneMolecularActivityRelationship],[Gene],[BiologicalProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[MolecularActivity],[MolecularActivity]<molecular_activity%200..1-%20[GeneMolecularActivityRelationship],[Gene]<gene%200..1-%20[GeneMolecularActivityRelationship],[BiologicalProcess]++-%20gene_activities%200..*>[GeneMolecularActivityRelationship],[Gene],[BiologicalProcess])

## Referenced by Class

 *  **None** *[➞gene_activities](biologicalProcess__gene_activities.md)*  <sub>0..\*</sub>  **[GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md)**

## Attributes


### Own

 * [➞gene](geneMolecularActivityRelationship__gene.md)  <sub>0..1</sub>
     * Range: [Gene](Gene.md)
 * [➞molecular_activity](geneMolecularActivityRelationship__molecular_activity.md)  <sub>0..1</sub>
     * Range: [MolecularActivity](MolecularActivity.md)
