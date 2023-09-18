
# Class: BioticInteraction




URI: [bp:BioticInteraction](http://w3id.org/ontogpt/biotic-interaction-templateBioticInteraction)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Taxon],[InteractionType],[InteractionType]<interaction_type%200..1-%20[BioticInteraction],[Taxon]<target_taxon%200..1-%20[BioticInteraction],[Taxon]<source_taxon%200..1-%20[BioticInteraction],[Container]++-%20interactions%200..*>[BioticInteraction],[Container])](https://yuml.me/diagram/nofunky;dir:TB/class/[Taxon],[InteractionType],[InteractionType]<interaction_type%200..1-%20[BioticInteraction],[Taxon]<target_taxon%200..1-%20[BioticInteraction],[Taxon]<source_taxon%200..1-%20[BioticInteraction],[Container]++-%20interactions%200..*>[BioticInteraction],[Container])

## Referenced by Class

 *  **None** *[➞interactions](container__interactions.md)*  <sub>0..\*</sub>  **[BioticInteraction](BioticInteraction.md)**

## Attributes


### Own

 * [➞source_taxon](bioticInteraction__source_taxon.md)  <sub>0..1</sub>
     * Description: the taxon that is the subject of the interaction
     * Range: [Taxon](Taxon.md)
 * [➞target_taxon](bioticInteraction__target_taxon.md)  <sub>0..1</sub>
     * Description: the taxon that is the object of the ineteraction
     * Range: [Taxon](Taxon.md)
 * [➞interaction_type](bioticInteraction__interaction_type.md)  <sub>0..1</sub>
     * Description: the type of interaction
     * Range: [InteractionType](InteractionType.md)
