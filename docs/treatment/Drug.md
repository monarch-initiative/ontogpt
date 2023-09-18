
# Class: Drug




URI: [treatment:Drug](http://w3id.org/ontogpt/treatments/Drug)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[DiseaseTreatmentSummary]-%20drugs%200..*>[Drug&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Drug],[DiseaseTreatmentSummary])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[DiseaseTreatmentSummary]-%20drugs%200..*>[Drug&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Drug],[DiseaseTreatmentSummary])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞drugs](diseaseTreatmentSummary__drugs.md)*  <sub>0..\*</sub>  **[Drug](Drug.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
