
# Class: AdverseEffect




URI: [composite_disease:AdverseEffect](http://w3id.org/ontogpt/composite_disease/AdverseEffect)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[TreatmentAdverseEffect]-%20adverse_effects%200..*>[AdverseEffect&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[AdverseEffect],[TreatmentAdverseEffect])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[TreatmentAdverseEffect]-%20adverse_effects%200..*>[AdverseEffect&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[AdverseEffect],[TreatmentAdverseEffect])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞adverse_effects](treatmentAdverseEffect__adverse_effects.md)*  <sub>0..\*</sub>  **[AdverseEffect](AdverseEffect.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
