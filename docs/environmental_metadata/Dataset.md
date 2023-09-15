
# Class: Dataset




URI: [envmd:Dataset](http://w3id.org/ontogpt/environmental-metadataDataset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Topic],[Method],[Location],[EnvironmentalMaterial],[Environment],[Method]<methods%200..*-%20[Dataset&#124;packageid:string%20%3F],[Environment]<environments%200..*-%20[Dataset],[EnvironmentalMaterial]<environmental_material%200..*-%20[Dataset],[Location]<location%200..*-%20[Dataset],[Topic]<topic%200..*-%20[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Topic],[Method],[Location],[EnvironmentalMaterial],[Environment],[Method]<methods%200..*-%20[Dataset&#124;packageid:string%20%3F],[Environment]<environments%200..*-%20[Dataset],[EnvironmentalMaterial]<environmental_material%200..*-%20[Dataset],[Location]<location%200..*-%20[Dataset],[Topic]<topic%200..*-%20[Dataset])

## Attributes


### Own

 * [➞packageid](dataset__packageid.md)  <sub>0..1</sub>
     * Description: The internal identifier for the dataset
     * Range: [String](types/String.md)
 * [➞topic](dataset__topic.md)  <sub>0..\*</sub>
     * Description: the general scientific area of study concerning the sample(s)
     * Range: [Topic](Topic.md)
 * [➞location](dataset__location.md)  <sub>0..\*</sub>
     * Description: the geographic location where the sample was isolated
     * Range: [Location](Location.md)
 * [➞environmental_material](dataset__environmental_material.md)  <sub>0..\*</sub>
     * Description: the environmental material that was sampled
     * Range: [EnvironmentalMaterial](EnvironmentalMaterial.md)
 * [➞environments](dataset__environments.md)  <sub>0..\*</sub>
     * Description: the environmental context in which the study was conducted
     * Range: [Environment](Environment.md)
 * [➞methods](dataset__methods.md)  <sub>0..\*</sub>
     * Range: [Method](Method.md)
