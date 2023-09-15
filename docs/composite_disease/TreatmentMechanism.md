
# Class: TreatmentMechanism




URI: [composite_disease:TreatmentMechanism](http://w3id.org/ontogpt/composite_disease/TreatmentMechanism)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Mechanism]<mechanism%200..1-%20[TreatmentMechanism],[Treatment]<treatment%200..1-%20[TreatmentMechanism],[CompositeDisease]++-%20treatment_mechanisms%200..*>[TreatmentMechanism],[CompoundExpression]^-[TreatmentMechanism],[Treatment],[Mechanism],[CompoundExpression],[CompositeDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Mechanism]<mechanism%200..1-%20[TreatmentMechanism],[Treatment]<treatment%200..1-%20[TreatmentMechanism],[CompositeDisease]++-%20treatment_mechanisms%200..*>[TreatmentMechanism],[CompoundExpression]^-[TreatmentMechanism],[Treatment],[Mechanism],[CompoundExpression],[CompositeDisease])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞treatment_mechanisms](compositeDisease__treatment_mechanisms.md)*  <sub>0..\*</sub>  **[TreatmentMechanism](TreatmentMechanism.md)**

## Attributes


### Own

 * [➞treatment](treatmentMechanism__treatment.md)  <sub>0..1</sub>
     * Range: [Treatment](Treatment.md)
 * [➞mechanism](treatmentMechanism__mechanism.md)  <sub>0..1</sub>
     * Range: [Mechanism](Mechanism.md)
