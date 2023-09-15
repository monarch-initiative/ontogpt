
# Class: TreatmentAdverseEffect




URI: [treatment:TreatmentAdverseEffect](http://w3id.org/ontogpt/treatments/TreatmentAdverseEffect)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[AdverseEffect]<adverse_effects%200..*-%20[TreatmentAdverseEffect],[Treatment]<treatment%200..1-%20[TreatmentAdverseEffect],[DiseaseTreatmentSummary]++-%20treatment_adverse_effects%200..*>[TreatmentAdverseEffect],[CompoundExpression]^-[TreatmentAdverseEffect],[Treatment],[DiseaseTreatmentSummary],[CompoundExpression],[AdverseEffect])](https://yuml.me/diagram/nofunky;dir:TB/class/[AdverseEffect]<adverse_effects%200..*-%20[TreatmentAdverseEffect],[Treatment]<treatment%200..1-%20[TreatmentAdverseEffect],[DiseaseTreatmentSummary]++-%20treatment_adverse_effects%200..*>[TreatmentAdverseEffect],[CompoundExpression]^-[TreatmentAdverseEffect],[Treatment],[DiseaseTreatmentSummary],[CompoundExpression],[AdverseEffect])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞treatment_adverse_effects](diseaseTreatmentSummary__treatment_adverse_effects.md)*  <sub>0..\*</sub>  **[TreatmentAdverseEffect](TreatmentAdverseEffect.md)**

## Attributes


### Own

 * [➞treatment](treatmentAdverseEffect__treatment.md)  <sub>0..1</sub>
     * Range: [Treatment](Treatment.md)
 * [➞adverse_effects](treatmentAdverseEffect__adverse_effects.md)  <sub>0..\*</sub>
     * Range: [AdverseEffect](AdverseEffect.md)
