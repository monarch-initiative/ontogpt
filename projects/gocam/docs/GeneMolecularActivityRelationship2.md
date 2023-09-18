
# Class: GeneMolecularActivityRelationship2




URI: [gocam:GeneMolecularActivityRelationship2](http://w3id.org/ontogpt/gocam/GeneMolecularActivityRelationship2)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Molecule],[MolecularActivity],[Molecule]<target%200..1-%20[GeneMolecularActivityRelationship2],[MolecularActivity]<molecular_activity%200..1-%20[GeneMolecularActivityRelationship2],[Gene]<gene%200..1-%20[GeneMolecularActivityRelationship2],[CompoundExpression]^-[GeneMolecularActivityRelationship2],[Gene],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Molecule],[MolecularActivity],[Molecule]<target%200..1-%20[GeneMolecularActivityRelationship2],[MolecularActivity]<molecular_activity%200..1-%20[GeneMolecularActivityRelationship2],[Gene]<gene%200..1-%20[GeneMolecularActivityRelationship2],[CompoundExpression]^-[GeneMolecularActivityRelationship2],[Gene],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Attributes


### Own

 * [➞gene](geneMolecularActivityRelationship2__gene.md)  <sub>0..1</sub>
     * Range: [Gene](Gene.md)
 * [➞molecular_activity](geneMolecularActivityRelationship2__molecular_activity.md)  <sub>0..1</sub>
     * Range: [MolecularActivity](MolecularActivity.md)
 * [➞target](geneMolecularActivityRelationship2__target.md)  <sub>0..1</sub>
     * Range: [Molecule](Molecule.md)
