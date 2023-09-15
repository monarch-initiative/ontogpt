
# Class: Study




URI: [sample:Study](http://w3id.org/ontogpt/environmental-sample/Study)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Variable],[Measurement]<measurements%200..*-++[Study],[Variable]<variables%200..*-%20[Study],[CausalRelationship]<causal_relationships%200..*-++[Study],[Environment]<environments%200..*-%20[Study],[EnvironmentalMaterial]<environmental_material%200..*-%20[Study],[Location]<location%200..*-%20[Study],[Measurement],[Location],[EnvironmentalMaterial],[Environment],[CausalRelationship])](https://yuml.me/diagram/nofunky;dir:TB/class/[Variable],[Measurement]<measurements%200..*-++[Study],[Variable]<variables%200..*-%20[Study],[CausalRelationship]<causal_relationships%200..*-++[Study],[Environment]<environments%200..*-%20[Study],[EnvironmentalMaterial]<environmental_material%200..*-%20[Study],[Location]<location%200..*-%20[Study],[Measurement],[Location],[EnvironmentalMaterial],[Environment],[CausalRelationship])

## Attributes


### Own

 * [➞location](study__location.md)  <sub>0..\*</sub>
     * Description: the sites at which the study was conducted
     * Range: [Location](Location.md)
 * [➞environmental_material](study__environmental_material.md)  <sub>0..\*</sub>
     * Description: the environmental material that was sampled
     * Range: [EnvironmentalMaterial](EnvironmentalMaterial.md)
 * [➞environments](study__environments.md)  <sub>0..\*</sub>
     * Range: [Environment](Environment.md)
 * [➞causal_relationships](study__causal_relationships.md)  <sub>0..\*</sub>
     * Range: [CausalRelationship](CausalRelationship.md)
 * [➞variables](study__variables.md)  <sub>0..\*</sub>
     * Range: [Variable](Variable.md)
 * [➞measurements](study__measurements.md)  <sub>0..\*</sub>
     * Range: [Measurement](Measurement.md)
