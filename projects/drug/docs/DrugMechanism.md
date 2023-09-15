
# Class: DrugMechanism




URI: [drug:DrugMechanism](http://w3id.org/ontogpt/drug/DrugMechanism)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MechanismLink],[MechanismLink]<mechanism_links%200..*-++[DrugMechanism&#124;references:string%20*;source_text:string%20%3F],[Drug]<drug%200..1-%20[DrugMechanism],[Disease]<disease%200..1-%20[DrugMechanism],[Drug],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[MechanismLink],[MechanismLink]<mechanism_links%200..*-++[DrugMechanism&#124;references:string%20*;source_text:string%20%3F],[Drug]<drug%200..1-%20[DrugMechanism],[Disease]<disease%200..1-%20[DrugMechanism],[Drug],[Disease])

## Attributes


### Own

 * [➞disease](drugMechanism__disease.md)  <sub>0..1</sub>
     * Description: the name of the disease that is treated
     * Range: [Disease](Disease.md)
 * [➞drug](drugMechanism__drug.md)  <sub>0..1</sub>
     * Description: the name of the drug that treats the disease
     * Range: [Drug](Drug.md)
 * [➞mechanism_links](drugMechanism__mechanism_links.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of links, where each link is a triple connecting two entities via a relationship type
     * Range: [MechanismLink](MechanismLink.md)
 * [➞references](drugMechanism__references.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [➞source_text](drugMechanism__source_text.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
