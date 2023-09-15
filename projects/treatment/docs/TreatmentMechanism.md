
# Class: TreatmentMechanism




URI: [treatment:TreatmentMechanism](http://w3id.org/ontogpt/treatments/TreatmentMechanism)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Mechanism]<mechanism%200..1-%20[TreatmentMechanism],[Treatment]<treatment%200..1-%20[TreatmentMechanism],[DiseaseTreatmentSummary]++-%20treatment_mechanisms%200..*>[TreatmentMechanism],[CompoundExpression]^-[TreatmentMechanism],[Treatment],[Mechanism],[DiseaseTreatmentSummary],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Mechanism]<mechanism%200..1-%20[TreatmentMechanism],[Treatment]<treatment%200..1-%20[TreatmentMechanism],[DiseaseTreatmentSummary]++-%20treatment_mechanisms%200..*>[TreatmentMechanism],[CompoundExpression]^-[TreatmentMechanism],[Treatment],[Mechanism],[DiseaseTreatmentSummary],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞treatment_mechanisms](diseaseTreatmentSummary__treatment_mechanisms.md)*  <sub>0..\*</sub>  **[TreatmentMechanism](TreatmentMechanism.md)**

## Attributes


### Own

 * [➞treatment](treatmentMechanism__treatment.md)  <sub>0..1</sub>
     * Range: [Treatment](Treatment.md)
 * [➞mechanism](treatmentMechanism__mechanism.md)  <sub>0..1</sub>
     * Range: [Mechanism](Mechanism.md)
