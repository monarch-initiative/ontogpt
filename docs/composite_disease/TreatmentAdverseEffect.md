
# Class: TreatmentAdverseEffect




URI: [composite_disease:TreatmentAdverseEffect](http://w3id.org/ontogpt/composite_disease/TreatmentAdverseEffect)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AdverseEffect]<adverse_effects%200..*-%20[TreatmentAdverseEffect],[Treatment]<treatment%200..1-%20[TreatmentAdverseEffect],[CompositeDisease]++-%20treatment_adverse_effects%200..*>[TreatmentAdverseEffect],[CompoundExpression]^-[TreatmentAdverseEffect],[Treatment],[CompoundExpression],[CompositeDisease],[AdverseEffect])](https://yuml.me/diagram/nofunky;dir:TB/class/[AdverseEffect]<adverse_effects%200..*-%20[TreatmentAdverseEffect],[Treatment]<treatment%200..1-%20[TreatmentAdverseEffect],[CompositeDisease]++-%20treatment_adverse_effects%200..*>[TreatmentAdverseEffect],[CompoundExpression]^-[TreatmentAdverseEffect],[Treatment],[CompoundExpression],[CompositeDisease],[AdverseEffect])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞treatment_adverse_effects](compositeDisease__treatment_adverse_effects.md)*  <sub>0..\*</sub>  **[TreatmentAdverseEffect](TreatmentAdverseEffect.md)**

## Attributes


### Own

 * [➞treatment](treatmentAdverseEffect__treatment.md)  <sub>0..1</sub>
     * Range: [Treatment](Treatment.md)
 * [➞adverse_effects](treatmentAdverseEffect__adverse_effects.md)  <sub>0..\*</sub>
     * Range: [AdverseEffect](AdverseEffect.md)
