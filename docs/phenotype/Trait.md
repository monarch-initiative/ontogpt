
# Class: Trait




URI: [phenotype:Trait](http://w3id.org/ontogpt/phenotype/Trait)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ChemicalEntity]<chemical_entity%200..1-%20[Trait],[AnatomicalEntity]<anatomical_entity%200..1-%20[Trait],[Quality]<quality%200..1-%20[Trait],[Quality],[ChemicalEntity],[AnatomicalEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[ChemicalEntity]<chemical_entity%200..1-%20[Trait],[AnatomicalEntity]<anatomical_entity%200..1-%20[Trait],[Quality]<quality%200..1-%20[Trait],[Quality],[ChemicalEntity],[AnatomicalEntity])

## Attributes


### Own

 * [➞quality](trait__quality.md)  <sub>0..1</sub>
     * Description: The property being measured, or changes in this property, for example, amount, level, increased amount, decreased concentration
     * Range: [Quality](Quality.md)
 * [➞anatomical_entity](trait__anatomical_entity.md)  <sub>0..1</sub>
     * Description: The anatomical location that the chemical entity is measured in
     * Range: [AnatomicalEntity](AnatomicalEntity.md)
 * [➞chemical_entity](trait__chemical_entity.md)  <sub>0..1</sub>
     * Description: The chemical entity that is being measured
     * Range: [ChemicalEntity](ChemicalEntity.md)
