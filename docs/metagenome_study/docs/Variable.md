
# Class: Variable




URI: [eg:Variable](http://w3id.org/ontogpt/environmental-metagenome/Variable)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CausalRelationship]-%20cause%200..1>[Variable&#124;id(i):string;label(i):string%20%3F],[CausalRelationship]-%20effect%200..1>[Variable],[Study]-%20variables%200..*>[Variable],[NamedEntity]^-[Variable],[Study],[NamedEntity],[CausalRelationship])](https://yuml.me/diagram/nofunky;dir:TB/class/[CausalRelationship]-%20cause%200..1>[Variable&#124;id(i):string;label(i):string%20%3F],[CausalRelationship]-%20effect%200..1>[Variable],[Study]-%20variables%200..*>[Variable],[NamedEntity]^-[Variable],[Study],[NamedEntity],[CausalRelationship])

## Identifier prefixes

 * ENVO
 * MIXS
 * PATO

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞cause](causalRelationship__cause.md)*  <sub>0..1</sub>  **[Variable](Variable.md)**
 *  **None** *[➞effect](causalRelationship__effect.md)*  <sub>0..1</sub>  **[Variable](Variable.md)**
 *  **None** *[➞variables](study__variables.md)*  <sub>0..\*</sub>  **[Variable](Variable.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
