
# Class: CompositeDisease




URI: [composite_disease:CompositeDisease](http://w3id.org/ontogpt/composite_disease/CompositeDisease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TreatmentMechanism],[TreatmentEfficacy],[TreatmentAdverseEffect],[Treatment],[Drug],[Disease],[TreatmentAdverseEffect]<treatment_adverse_effects%200..*-++[CompositeDisease],[TreatmentEfficacy]<treatment_efficacies%200..*-++[CompositeDisease],[TreatmentMechanism]<treatment_mechanisms%200..*-++[CompositeDisease],[Treatment]<contraindications%200..*-%20[CompositeDisease],[Treatment]<treatments%200..*-%20[CompositeDisease],[Drug]<drugs%200..*-%20[CompositeDisease],[Disease]<main_disease%200..1-%20[CompositeDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[TreatmentMechanism],[TreatmentEfficacy],[TreatmentAdverseEffect],[Treatment],[Drug],[Disease],[TreatmentAdverseEffect]<treatment_adverse_effects%200..*-++[CompositeDisease],[TreatmentEfficacy]<treatment_efficacies%200..*-++[CompositeDisease],[TreatmentMechanism]<treatment_mechanisms%200..*-++[CompositeDisease],[Treatment]<contraindications%200..*-%20[CompositeDisease],[Treatment]<treatments%200..*-%20[CompositeDisease],[Drug]<drugs%200..*-%20[CompositeDisease],[Disease]<main_disease%200..1-%20[CompositeDisease])

## Attributes


### Own

 * [➞main_disease](compositeDisease__main_disease.md)  <sub>0..1</sub>
     * Description: the name of the disease that is treated.
     * Range: [Disease](Disease.md)
 * [➞drugs](compositeDisease__drugs.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of named small molecule drugs
     * Range: [Drug](Drug.md)
 * [➞treatments](compositeDisease__treatments.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of therapies and treatments are indicated for treating the disease.
     * Range: [Treatment](Treatment.md)
 * [➞contraindications](compositeDisease__contraindications.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of therapies and treatments that are contra-indicated for the disease, and should not be used, due to risk of adverse effects.
     * Range: [Treatment](Treatment.md)
 * [➞treatment_mechanisms](compositeDisease__treatment_mechanisms.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of treatment to asterisk-separated mechanism associations
     * Range: [TreatmentMechanism](TreatmentMechanism.md)
 * [➞treatment_efficacies](compositeDisease__treatment_efficacies.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of treatment to efficacy associations, e.g. Imatinib*effective
     * Range: [TreatmentEfficacy](TreatmentEfficacy.md)
 * [➞treatment_adverse_effects](compositeDisease__treatment_adverse_effects.md)  <sub>0..\*</sub>
     * Description: semicolon-separated list of treatment to adverse effect associations, e.g. Imatinib*nausea
     * Range: [TreatmentAdverseEffect](TreatmentAdverseEffect.md)
