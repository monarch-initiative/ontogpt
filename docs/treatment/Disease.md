
# Class: Disease




URI: [treatment:Disease](http://w3id.org/ontogpt/treatments/Disease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[DiseaseTreatmentSummary]-%20disease%200..1>[Disease&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Disease],[DiseaseTreatmentSummary])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[DiseaseTreatmentSummary]-%20disease%200..1>[Disease&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Disease],[DiseaseTreatmentSummary])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞disease](diseaseTreatmentSummary__disease.md)*  <sub>0..1</sub>  **[Disease](Disease.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
