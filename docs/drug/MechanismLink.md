
# Class: MechanismLink




URI: [drug:MechanismLink](http://w3id.org/ontogpt/drug/MechanismLink)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Predicate],[MechanismElement]<object%200..1-%20[MechanismLink],[Predicate]<predicate%200..1-%20[MechanismLink],[MechanismElement]<subject%200..1-%20[MechanismLink],[DrugMechanism]++-%20mechanism_links%200..*>[MechanismLink],[CompoundExpression]^-[MechanismLink],[MechanismElement],[DrugMechanism],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Predicate],[MechanismElement]<object%200..1-%20[MechanismLink],[Predicate]<predicate%200..1-%20[MechanismLink],[MechanismElement]<subject%200..1-%20[MechanismLink],[DrugMechanism]++-%20mechanism_links%200..*>[MechanismLink],[CompoundExpression]^-[MechanismLink],[MechanismElement],[DrugMechanism],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞mechanism_links](drugMechanism__mechanism_links.md)*  <sub>0..\*</sub>  **[MechanismLink](MechanismLink.md)**

## Attributes


### Own

 * [➞subject](mechanismLink__subject.md)  <sub>0..1</sub>
     * Range: [MechanismElement](MechanismElement.md)
 * [➞predicate](mechanismLink__predicate.md)  <sub>0..1</sub>
     * Range: [Predicate](Predicate.md)
 * [➞object](mechanismLink__object.md)  <sub>0..1</sub>
     * Range: [MechanismElement](MechanismElement.md)
