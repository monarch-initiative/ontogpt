
# Class: DiseaseTreatmentSummary




URI: [treatment:DiseaseTreatmentSummary](http://w3id.org/ontogpt/treatments/DiseaseTreatmentSummary)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TreatmentMechanism],[TreatmentEfficacy],[TreatmentAdverseEffect],[Treatment],[Drug],[TreatmentAdverseEffect]<treatment_adverse_effects%200..*-++[DiseaseTreatmentSummary],[TreatmentEfficacy]<treatment_efficacies%200..*-++[DiseaseTreatmentSummary],[TreatmentMechanism]<treatment_mechanisms%200..*-++[DiseaseTreatmentSummary],[Treatment]<contraindications%200..*-%20[DiseaseTreatmentSummary],[Treatment]<treatments%200..*-%20[DiseaseTreatmentSummary],[Drug]<drugs%200..*-%20[DiseaseTreatmentSummary],[Disease]<disease%200..1-%20[DiseaseTreatmentSummary],[Disease])](https://yuml.me/diagram/nofunky;dir:TB/class/[TreatmentMechanism],[TreatmentEfficacy],[TreatmentAdverseEffect],[Treatment],[Drug],[TreatmentAdverseEffect]<treatment_adverse_effects%200..*-++[DiseaseTreatmentSummary],[TreatmentEfficacy]<treatment_efficacies%200..*-++[DiseaseTreatmentSummary],[TreatmentMechanism]<treatment_mechanisms%200..*-++[DiseaseTreatmentSummary],[Treatment]<contraindications%200..*-%20[DiseaseTreatmentSummary],[Treatment]<treatments%200..*-%20[DiseaseTreatmentSummary],[Drug]<drugs%200..*-%20[DiseaseTreatmentSummary],[Disease]<disease%200..1-%20[DiseaseTreatmentSummary],[Disease])

## Attributes


### Own

 * [➞disease](diseaseTreatmentSummary__disease.md)  <sub>0..1</sub>
     * Description: the name of the disease that is treated.
     * Range: [Disease](Disease.md)
 * [➞drugs](diseaseTreatmentSummary__drugs.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of named small molecule drugs
     * Range: [Drug](Drug.md)
 * [➞treatments](diseaseTreatmentSummary__treatments.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of therapies and treatments are indicated for treating the disease.
     * Range: [Treatment](Treatment.md)
 * [➞contraindications](diseaseTreatmentSummary__contraindications.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of therapies and treatments that are contra-indicated for the disease, and should not be used, due to risk of adverse effects.
     * Range: [Treatment](Treatment.md)
 * [➞treatment_mechanisms](diseaseTreatmentSummary__treatment_mechanisms.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of treatment to asterisk-separated mechanism associations
     * Range: [TreatmentMechanism](TreatmentMechanism.md)
 * [➞treatment_efficacies](diseaseTreatmentSummary__treatment_efficacies.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of treatment to efficacy associations, e.g. Imatinib*effective
     * Range: [TreatmentEfficacy](TreatmentEfficacy.md)
 * [➞treatment_adverse_effects](diseaseTreatmentSummary__treatment_adverse_effects.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of treatment to adverse effect associations, e.g. Imatinib*nausea
     * Range: [TreatmentAdverseEffect](TreatmentAdverseEffect.md)
