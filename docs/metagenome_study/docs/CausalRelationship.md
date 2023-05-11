
# Class: CausalRelationship




URI: [eg:CausalRelationship](http://w3id.org/ontogpt/environmental-metagenome/CausalRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Variable],[CompoundExpression],[Variable]<effect%200..1-%20[CausalRelationship],[Variable]<cause%200..1-%20[CausalRelationship],[Study]++-%20causal_relationships%200..*>[CausalRelationship],[CompoundExpression]^-[CausalRelationship],[Study])](https://yuml.me/diagram/nofunky;dir:TB/class/[Variable],[CompoundExpression],[Variable]<effect%200..1-%20[CausalRelationship],[Variable]<cause%200..1-%20[CausalRelationship],[Study]++-%20causal_relationships%200..*>[CausalRelationship],[CompoundExpression]^-[CausalRelationship],[Study])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞causal_relationships](study__causal_relationships.md)*  <sub>0..\*</sub>  **[CausalRelationship](CausalRelationship.md)**

## Attributes


### Own

 * [➞cause](causalRelationship__cause.md)  <sub>0..1</sub>
     * Description: the variable that is the cause of the effect
     * Range: [Variable](Variable.md)
 * [➞effect](causalRelationship__effect.md)  <sub>0..1</sub>
     * Description: the things that is affected
     * Range: [Variable](Variable.md)
