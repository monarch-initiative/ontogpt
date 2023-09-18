
# Class: TreatmentEfficacy




URI: [treatment:TreatmentEfficacy](http://w3id.org/ontogpt/treatments/TreatmentEfficacy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Treatment]<treatment%200..1-%20[TreatmentEfficacy&#124;efficacy:string%20%3F],[DiseaseTreatmentSummary]++-%20treatment_efficacies%200..*>[TreatmentEfficacy],[CompoundExpression]^-[TreatmentEfficacy],[Treatment],[DiseaseTreatmentSummary],[CompoundExpression])](https://yuml.me/diagram/nofunky;dir:TB/class/[Treatment]<treatment%200..1-%20[TreatmentEfficacy&#124;efficacy:string%20%3F],[DiseaseTreatmentSummary]++-%20treatment_efficacies%200..*>[TreatmentEfficacy],[CompoundExpression]^-[TreatmentEfficacy],[Treatment],[DiseaseTreatmentSummary],[CompoundExpression])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞treatment_efficacies](diseaseTreatmentSummary__treatment_efficacies.md)*  <sub>0..\*</sub>  **[TreatmentEfficacy](TreatmentEfficacy.md)**

## Attributes


### Own

 * [➞treatment](treatmentEfficacy__treatment.md)  <sub>0..1</sub>
     * Range: [Treatment](Treatment.md)
 * [➞efficacy](treatmentEfficacy__efficacy.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
