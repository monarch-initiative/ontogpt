
# Class: BiologicalProcess




URI: [bp:BiologicalProcess](http://w3id.org/ontogpt/biological-process-templateBiologicalProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[MolecularActivity],[GeneMolecularActivityRelationship],[Gene],[ChemicalEntity],[GeneMolecularActivityRelationship]<gene_activities%200..*-++[BiologicalProcess&#124;label:string%20%3F;description:string%20%3F;synonyms:string%20*;id(i):string],[Gene]<genes%200..*-%20[BiologicalProcess],[MolecularActivity]<steps%200..*-%20[BiologicalProcess],[ChemicalEntity]<outputs%200..*-%20[BiologicalProcess],[ChemicalEntity]<inputs%200..*-%20[BiologicalProcess],[BiologicalProcess]<subclass_of%200..1-%20[BiologicalProcess],[NamedEntity]^-[BiologicalProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[MolecularActivity],[GeneMolecularActivityRelationship],[Gene],[ChemicalEntity],[GeneMolecularActivityRelationship]<gene_activities%200..*-++[BiologicalProcess&#124;label:string%20%3F;description:string%20%3F;synonyms:string%20*;id(i):string],[Gene]<genes%200..*-%20[BiologicalProcess],[MolecularActivity]<steps%200..*-%20[BiologicalProcess],[ChemicalEntity]<outputs%200..*-%20[BiologicalProcess],[ChemicalEntity]<inputs%200..*-%20[BiologicalProcess],[BiologicalProcess]<subclass_of%200..1-%20[BiologicalProcess],[NamedEntity]^-[BiologicalProcess])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞subclass_of](biologicalProcess__subclass_of.md)*  <sub>0..1</sub>  **[BiologicalProcess](BiologicalProcess.md)**

## Attributes


### Own

 * [➞label](biologicalProcess__label.md)  <sub>0..1</sub>
     * Description: the name of the biological process
     * Range: [String](types/String.md)
 * [➞description](biologicalProcess__description.md)  <sub>0..1</sub>
     * Description: a textual description of the biological process
     * Range: [String](types/String.md)
 * [➞synonyms](biologicalProcess__synonyms.md)  <sub>0..\*</sub>
     * Description: alternative names of the biological process
     * Range: [String](types/String.md)
 * [➞subclass_of](biologicalProcess__subclass_of.md)  <sub>0..1</sub>
     * Description: the category to which this biological process belongs
     * Range: [BiologicalProcess](BiologicalProcess.md)
 * [➞inputs](biologicalProcess__inputs.md)  <sub>0..\*</sub>
     * Description: the inputs of the biological process
     * Range: [ChemicalEntity](ChemicalEntity.md)
 * [➞outputs](biologicalProcess__outputs.md)  <sub>0..\*</sub>
     * Description: the outputs of the biological process
     * Range: [ChemicalEntity](ChemicalEntity.md)
 * [➞steps](biologicalProcess__steps.md)  <sub>0..\*</sub>
     * Description: the steps involved in this biological process
     * Range: [MolecularActivity](MolecularActivity.md)
 * [➞genes](biologicalProcess__genes.md)  <sub>0..\*</sub>
     * Range: [Gene](Gene.md)
 * [➞gene_activities](biologicalProcess__gene_activities.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of gene to molecular activity relationships
     * Range: [GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md)

### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
