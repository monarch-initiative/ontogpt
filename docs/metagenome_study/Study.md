
# Class: Study




URI: [eg:Study](http://w3id.org/ontogpt/environmental-metagenome/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Variable],[Treatment],[Organism]<organisms%200..*-%20[Study],[SequencingTechnology]<sequencing_technologies%200..1-%20[Study],[EnvironmentalMaterial]<environmental_material%200..*-%20[Study],[Location]<location%200..*-%20[Study],[Measurement]<measurements%200..*-++[Study],[Treatment]<treatments%200..*-%20[Study],[Variable]<variables%200..*-%20[Study],[CausalRelationship]<causal_relationships%200..*-++[Study],[Environment]<environments%200..*-%20[Study],[SequencingTechnology],[Organism],[Measurement],[Location],[EnvironmentalMaterial],[Environment],[CausalRelationship])](https://yuml.me/diagram/nofunky;dir:TB/class/[Variable],[Treatment],[Organism]<organisms%200..*-%20[Study],[SequencingTechnology]<sequencing_technologies%200..1-%20[Study],[EnvironmentalMaterial]<environmental_material%200..*-%20[Study],[Location]<location%200..*-%20[Study],[Measurement]<measurements%200..*-++[Study],[Treatment]<treatments%200..*-%20[Study],[Variable]<variables%200..*-%20[Study],[CausalRelationship]<causal_relationships%200..*-++[Study],[Environment]<environments%200..*-%20[Study],[SequencingTechnology],[Organism],[Measurement],[Location],[EnvironmentalMaterial],[Environment],[CausalRelationship])

## Attributes


### Own

 * [➞environments](study__environments.md)  <sub>0..\*</sub>
     * Range: [Environment](Environment.md)
 * [➞causal_relationships](study__causal_relationships.md)  <sub>0..\*</sub>
     * Range: [CausalRelationship](CausalRelationship.md)
 * [➞variables](study__variables.md)  <sub>0..\*</sub>
     * Range: [Variable](Variable.md)
 * [➞treatments](study__treatments.md)  <sub>0..\*</sub>
     * Range: [Treatment](Treatment.md)
 * [➞measurements](study__measurements.md)  <sub>0..\*</sub>
     * Range: [Measurement](Measurement.md)
 * [➞location](study__location.md)  <sub>0..\*</sub>
     * Description: the sites at which the study was conducted
     * Range: [Location](Location.md)
 * [➞environmental_material](study__environmental_material.md)  <sub>0..\*</sub>
     * Description: the environmental material that was sampled
     * Range: [EnvironmentalMaterial](EnvironmentalMaterial.md)
 * [➞sequencing_technologies](study__sequencing_technologies.md)  <sub>0..1</sub>
     * Range: [SequencingTechnology](SequencingTechnology.md)
 * [➞organisms](study__organisms.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of all studied organism taxons
     * Range: [Organism](Organism.md)
