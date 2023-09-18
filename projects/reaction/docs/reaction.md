
# Class: Reaction




URI: [reaction:Reaction](http://w3id.org/ontogpt/reaction/Reaction)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ReactionGrouping],[ChemicalEntity]<right_side%200..*-%20[Reaction&#124;label:string%20%3F;description:string%20%3F;synonyms:string%20*;id(i):string],[ChemicalEntity]<left_side%200..*-%20[Reaction],[ReactionGrouping]<subclass_of%200..1-%20[Reaction],[GeneReactionPairing]-%20reaction%200..1>[Reaction],[GeneToReaction]++-%20reactions%200..*>[Reaction],[ReactionDocument]++-%20reactions%200..*>[Reaction],[NamedEntity]^-[Reaction],[ReactionDocument],[NamedEntity],[GeneToReaction],[GeneReactionPairing],[ChemicalEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[ReactionGrouping],[ChemicalEntity]<right_side%200..*-%20[Reaction&#124;label:string%20%3F;description:string%20%3F;synonyms:string%20*;id(i):string],[ChemicalEntity]<left_side%200..*-%20[Reaction],[ReactionGrouping]<subclass_of%200..1-%20[Reaction],[GeneReactionPairing]-%20reaction%200..1>[Reaction],[GeneToReaction]++-%20reactions%200..*>[Reaction],[ReactionDocument]++-%20reactions%200..*>[Reaction],[NamedEntity]^-[Reaction],[ReactionDocument],[NamedEntity],[GeneToReaction],[GeneReactionPairing],[ChemicalEntity])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞reaction](geneReactionPairing__reaction.md)*  <sub>0..1</sub>  **[Reaction](Reaction.md)**
 *  **None** *[➞reactions](geneToReaction__reactions.md)*  <sub>0..\*</sub>  **[Reaction](Reaction.md)**
 *  **None** *[➞reactions](reactionDocument__reactions.md)*  <sub>0..\*</sub>  **[Reaction](Reaction.md)**

## Attributes


### Own

 * [➞label](reaction__label.md)  <sub>0..1</sub>
     * Description: the name of the reaction
     * Range: [String](types/String.md)
 * [➞description](reaction__description.md)  <sub>0..1</sub>
     * Description: a textual description of the reaction
     * Range: [String](types/String.md)
 * [➞synonyms](reaction__synonyms.md)  <sub>0..\*</sub>
     * Description: alternative names of the reaction
     * Range: [String](types/String.md)
 * [➞subclass_of](reaction__subclass_of.md)  <sub>0..1</sub>
     * Description: the category to which this biological process belongs
     * Range: [ReactionGrouping](ReactionGrouping.md)
 * [➞left_side](reaction__left_side.md)  <sub>0..\*</sub>
     * Description: semicolon separated list of chemical entities on the left side
     * Range: [ChemicalEntity](ChemicalEntity.md)
 * [➞right_side](reaction__right_side.md)  <sub>0..\*</sub>
     * Description: semicolon separated list of chemical entities on the right side
     * Range: [ChemicalEntity](ChemicalEntity.md)

### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
