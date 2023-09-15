
# Class: Treatment




URI: [composite_disease:Treatment](http://w3id.org/ontogpt/composite_disease/Treatment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CompositeDisease]-%20contraindications%200..*>[Treatment&#124;id(i):string;label(i):string%20%3F],[CompositeDisease]-%20treatments%200..*>[Treatment],[TreatmentAdverseEffect]-%20treatment%200..1>[Treatment],[TreatmentEfficacy]-%20treatment%200..1>[Treatment],[TreatmentMechanism]-%20treatment%200..1>[Treatment],[NamedEntity]^-[Treatment],[TreatmentMechanism],[TreatmentEfficacy],[TreatmentAdverseEffect],[NamedEntity],[CompositeDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[CompositeDisease]-%20contraindications%200..*>[Treatment&#124;id(i):string;label(i):string%20%3F],[CompositeDisease]-%20treatments%200..*>[Treatment],[TreatmentAdverseEffect]-%20treatment%200..1>[Treatment],[TreatmentEfficacy]-%20treatment%200..1>[Treatment],[TreatmentMechanism]-%20treatment%200..1>[Treatment],[NamedEntity]^-[Treatment],[TreatmentMechanism],[TreatmentEfficacy],[TreatmentAdverseEffect],[NamedEntity],[CompositeDisease])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞contraindications](compositeDisease__contraindications.md)*  <sub>0..\*</sub>  **[Treatment](Treatment.md)**
 *  **None** *[➞treatments](compositeDisease__treatments.md)*  <sub>0..\*</sub>  **[Treatment](Treatment.md)**
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
