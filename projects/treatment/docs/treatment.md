
# Class: Treatment




URI: [treatment:Treatment](http://w3id.org/ontogpt/treatments/Treatment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseTreatmentSummary]-%20contraindications%200..*>[Treatment&#124;id(i):string;label(i):string%20%3F],[DiseaseTreatmentSummary]-%20treatments%200..*>[Treatment],[TreatmentAdverseEffect]-%20treatment%200..1>[Treatment],[TreatmentEfficacy]-%20treatment%200..1>[Treatment],[TreatmentMechanism]-%20treatment%200..1>[Treatment],[NamedEntity]^-[Treatment],[TreatmentMechanism],[TreatmentEfficacy],[TreatmentAdverseEffect],[NamedEntity],[DiseaseTreatmentSummary])](https://yuml.me/diagram/nofunky;dir:TB/class/[DiseaseTreatmentSummary]-%20contraindications%200..*>[Treatment&#124;id(i):string;label(i):string%20%3F],[DiseaseTreatmentSummary]-%20treatments%200..*>[Treatment],[TreatmentAdverseEffect]-%20treatment%200..1>[Treatment],[TreatmentEfficacy]-%20treatment%200..1>[Treatment],[TreatmentMechanism]-%20treatment%200..1>[Treatment],[NamedEntity]^-[Treatment],[TreatmentMechanism],[TreatmentEfficacy],[TreatmentAdverseEffect],[NamedEntity],[DiseaseTreatmentSummary])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞contraindications](diseaseTreatmentSummary__contraindications.md)*  <sub>0..\*</sub>  **[Treatment](Treatment.md)**
 *  **None** *[➞treatments](diseaseTreatmentSummary__treatments.md)*  <sub>0..\*</sub>  **[Treatment](Treatment.md)**
 *  **None** *[➞treatment](treatmentAdverseEffect__treatment.md)*  <sub>0..1</sub>  **[Treatment](Treatment.md)**
 *  **None** *[➞treatment](treatmentEfficacy__treatment.md)*  <sub>0..1</sub>  **[Treatment](Treatment.md)**
 *  **None** *[➞treatment](treatmentMechanism__treatment.md)*  <sub>0..1</sub>  **[Treatment](Treatment.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
