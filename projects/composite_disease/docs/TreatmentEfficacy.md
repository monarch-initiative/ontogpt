
# Class: TreatmentEfficacy




URI: [composite_disease:TreatmentEfficacy](http://w3id.org/ontogpt/composite_disease/TreatmentEfficacy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Treatment]<treatment%200..1-%20[TreatmentEfficacy&#124;efficacy:string%20%3F],[CompositeDisease]++-%20treatment_efficacies%200..*>[TreatmentEfficacy],[CompoundExpression]^-[TreatmentEfficacy],[Treatment],[CompoundExpression],[CompositeDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Treatment]<treatment%200..1-%20[TreatmentEfficacy&#124;efficacy:string%20%3F],[CompositeDisease]++-%20treatment_efficacies%200..*>[TreatmentEfficacy],[CompoundExpression]^-[TreatmentEfficacy],[Treatment],[CompoundExpression],[CompositeDisease])

## Parents

 *  is_a: [CompoundExpression](CompoundExpression.md)

## Referenced by Class

 *  **None** *[➞treatment_efficacies](compositeDisease__treatment_efficacies.md)*  <sub>0..\*</sub>  **[TreatmentEfficacy](TreatmentEfficacy.md)**

## Attributes


### Own

 * [➞treatment](treatmentEfficacy__treatment.md)  <sub>0..1</sub>
     * Range: [Treatment](Treatment.md)
 * [➞efficacy](treatmentEfficacy__efficacy.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
