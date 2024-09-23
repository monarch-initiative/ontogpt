

# Class: CompositeDisease



URI: [composite_disease:CompositeDisease](http://w3id.org/ontogpt/composite_disease/CompositeDisease)



```mermaid
erDiagram
CompositeDisease {

}
TreatmentAdverseEffect {

}
AdverseEffect {
    string id  
    string label  
}
Treatment {
    string id  
    string label  
}
TreatmentEfficacy {
    string efficacy  
}
TreatmentMechanism {

}
Mechanism {
    string id  
    string label  
}
Drug {
    string id  
    string label  
}
Disease {
    string id  
    string label  
}

CompositeDisease ||--|o Disease : "main_disease"
CompositeDisease ||--}o Drug : "drugs"
CompositeDisease ||--}o Treatment : "treatments"
CompositeDisease ||--}o Treatment : "contraindications"
CompositeDisease ||--}o TreatmentMechanism : "treatment_mechanisms"
CompositeDisease ||--}o TreatmentEfficacy : "treatment_efficacies"
CompositeDisease ||--}o TreatmentAdverseEffect : "treatment_adverse_effects"
TreatmentAdverseEffect ||--|o Treatment : "treatment"
TreatmentAdverseEffect ||--}o AdverseEffect : "adverse_effects"
TreatmentEfficacy ||--|o Treatment : "treatment"
TreatmentMechanism ||--|o Treatment : "treatment"
TreatmentMechanism ||--|o Mechanism : "mechanism"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [main_disease](main_disease.md) | 0..1 <br/> [Disease](Disease.md) | the name of the disease that is treated | direct |
| [drugs](drugs.md) | * <br/> [Drug](Drug.md) | semicolon-separated list of named small molecule drugs | direct |
| [treatments](treatments.md) | * <br/> [Treatment](Treatment.md) | semicolon-separated list of therapies and treatments are indicated for treati... | direct |
| [contraindications](contraindications.md) | * <br/> [Treatment](Treatment.md) | semicolon-separated list of therapies and treatments that are contra-indicate... | direct |
| [treatment_mechanisms](treatment_mechanisms.md) | * <br/> [TreatmentMechanism](TreatmentMechanism.md) | semicolon-separated list of treatment to asterisk-separated mechanism associa... | direct |
| [treatment_efficacies](treatment_efficacies.md) | * <br/> [TreatmentEfficacy](TreatmentEfficacy.md) | semicolon-separated list of treatment to efficacy associations, e | direct |
| [treatment_adverse_effects](treatment_adverse_effects.md) | * <br/> [TreatmentAdverseEffect](TreatmentAdverseEffect.md) | semicolon-separated list of treatment to adverse effect associations, e | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/composite_disease





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | composite_disease:CompositeDisease |
| native | composite_disease:CompositeDisease |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CompositeDisease
from_schema: http://w3id.org/ontogpt/composite_disease
attributes:
  main_disease:
    name: main_disease
    description: the name of the disease that is treated.
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    domain_of:
    - CompositeDisease
    range: Disease
  drugs:
    name: drugs
    description: semicolon-separated list of named small molecule drugs
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    domain_of:
    - CompositeDisease
    range: Drug
  treatments:
    name: treatments
    annotations:
      prompt.examples:
        tag: prompt.examples
        value: Imatinib, exercise, surgery
    description: semicolon-separated list of therapies and treatments are indicated
      for treating the disease.
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    domain_of:
    - CompositeDisease
    range: Treatment
  contraindications:
    name: contraindications
    annotations:
      prompt.examples:
        tag: prompt.examples
        value: Beta-blockers, exercise, surgery
    description: semicolon-separated list of therapies and treatments that are contra-indicated
      for the disease, and should not be used, due to risk of adverse effects.
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    domain_of:
    - CompositeDisease
    range: Treatment
  treatment_mechanisms:
    name: treatment_mechanisms
    annotations:
      prompt.separator:
        tag: prompt.separator
        value: '*'
    description: semicolon-separated list of treatment to asterisk-separated mechanism
      associations
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    domain_of:
    - CompositeDisease
    range: TreatmentMechanism
  treatment_efficacies:
    name: treatment_efficacies
    annotations:
      prompt.separator:
        tag: prompt.separator
        value: '*'
    description: semicolon-separated list of treatment to efficacy associations, e.g.
      Imatinib*effective
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    domain_of:
    - CompositeDisease
    range: TreatmentEfficacy
  treatment_adverse_effects:
    name: treatment_adverse_effects
    annotations:
      prompt.separator:
        tag: prompt.separator
        value: '*'
    description: semicolon-separated list of treatment to adverse effect associations,
      e.g. Imatinib*nausea
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    domain_of:
    - CompositeDisease
    range: TreatmentAdverseEffect
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: CompositeDisease
from_schema: http://w3id.org/ontogpt/composite_disease
attributes:
  main_disease:
    name: main_disease
    description: the name of the disease that is treated.
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    alias: main_disease
    owner: CompositeDisease
    domain_of:
    - CompositeDisease
    range: Disease
  drugs:
    name: drugs
    description: semicolon-separated list of named small molecule drugs
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    alias: drugs
    owner: CompositeDisease
    domain_of:
    - CompositeDisease
    range: Drug
  treatments:
    name: treatments
    annotations:
      prompt.examples:
        tag: prompt.examples
        value: Imatinib, exercise, surgery
    description: semicolon-separated list of therapies and treatments are indicated
      for treating the disease.
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    alias: treatments
    owner: CompositeDisease
    domain_of:
    - CompositeDisease
    range: Treatment
  contraindications:
    name: contraindications
    annotations:
      prompt.examples:
        tag: prompt.examples
        value: Beta-blockers, exercise, surgery
    description: semicolon-separated list of therapies and treatments that are contra-indicated
      for the disease, and should not be used, due to risk of adverse effects.
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    alias: contraindications
    owner: CompositeDisease
    domain_of:
    - CompositeDisease
    range: Treatment
  treatment_mechanisms:
    name: treatment_mechanisms
    annotations:
      prompt.separator:
        tag: prompt.separator
        value: '*'
    description: semicolon-separated list of treatment to asterisk-separated mechanism
      associations
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    alias: treatment_mechanisms
    owner: CompositeDisease
    domain_of:
    - CompositeDisease
    range: TreatmentMechanism
  treatment_efficacies:
    name: treatment_efficacies
    annotations:
      prompt.separator:
        tag: prompt.separator
        value: '*'
    description: semicolon-separated list of treatment to efficacy associations, e.g.
      Imatinib*effective
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    alias: treatment_efficacies
    owner: CompositeDisease
    domain_of:
    - CompositeDisease
    range: TreatmentEfficacy
  treatment_adverse_effects:
    name: treatment_adverse_effects
    annotations:
      prompt.separator:
        tag: prompt.separator
        value: '*'
    description: semicolon-separated list of treatment to adverse effect associations,
      e.g. Imatinib*nausea
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    alias: treatment_adverse_effects
    owner: CompositeDisease
    domain_of:
    - CompositeDisease
    range: TreatmentAdverseEffect
tree_root: true

```
</details>