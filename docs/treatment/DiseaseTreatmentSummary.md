# Class: DiseaseTreatmentSummary



URI: [treatment:DiseaseTreatmentSummary](http://w3id.org/ontogpt/treatments/DiseaseTreatmentSummary)


```mermaid
 classDiagram
    class DiseaseTreatmentSummary
      DiseaseTreatmentSummary : disease
      DiseaseTreatmentSummary : drugs
      DiseaseTreatmentSummary : treatment_efficacies
      DiseaseTreatmentSummary : treatment_mechanisms
      DiseaseTreatmentSummary : treatments
      
```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [disease](disease.md) | 0..1 <br/> [Disease](Disease.md) | the name of the disease that is treated | direct |
| [drugs](drugs.md) | 0..* <br/> [Drug](Drug.md) | semicolon-separated list of named small molecule drugs | direct |
| [treatments](treatments.md) | 0..* <br/> [Treatment](Treatment.md) | semicolon-separated list of therapies and treatments | direct |
| [treatment_mechanisms](treatment_mechanisms.md) | 0..* <br/> [TreatmentMechanism](TreatmentMechanism.md) | semicolon-separated list of treatment to asterisk-separated mechanism associa... | direct |
| [treatment_efficacies](treatment_efficacies.md) | 0..* <br/> [TreatmentEfficacy](TreatmentEfficacy.md) | semicolon-separated list of treatment to efficacy associations, e | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/treatment





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | treatment:DiseaseTreatmentSummary |
| native | treatment:DiseaseTreatmentSummary |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DiseaseTreatmentSummary
from_schema: http://w3id.org/ontogpt/treatment
rank: 1000
attributes:
  disease:
    name: disease
    description: the name of the disease that is treated
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    range: Disease
  drugs:
    name: drugs
    description: semicolon-separated list of named small molecule drugs
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    multivalued: true
    range: Drug
  treatments:
    name: treatments
    description: semicolon-separated list of therapies and treatments
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    multivalued: true
    range: Treatment
  treatment_mechanisms:
    name: treatment_mechanisms
    annotations:
      prompt.separator:
        tag: prompt.separator
        value: '*'
    description: semicolon-separated list of treatment to asterisk-separated mechanism
      associations
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    multivalued: true
    range: TreatmentMechanism
  treatment_efficacies:
    name: treatment_efficacies
    annotations:
      prompt.separator:
        tag: prompt.separator
        value: '*'
    description: semicolon-separated list of treatment to efficacy associations, e.g.
      Imatinib*effective
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    multivalued: true
    range: TreatmentEfficacy

```
</details>

### Induced

<details>
```yaml
name: DiseaseTreatmentSummary
from_schema: http://w3id.org/ontogpt/treatment
rank: 1000
attributes:
  disease:
    name: disease
    description: the name of the disease that is treated
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    alias: disease
    owner: DiseaseTreatmentSummary
    domain_of:
    - DiseaseTreatmentSummary
    range: Disease
  drugs:
    name: drugs
    description: semicolon-separated list of named small molecule drugs
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    multivalued: true
    alias: drugs
    owner: DiseaseTreatmentSummary
    domain_of:
    - DiseaseTreatmentSummary
    range: Drug
  treatments:
    name: treatments
    description: semicolon-separated list of therapies and treatments
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    multivalued: true
    alias: treatments
    owner: DiseaseTreatmentSummary
    domain_of:
    - DiseaseTreatmentSummary
    range: Treatment
  treatment_mechanisms:
    name: treatment_mechanisms
    annotations:
      prompt.separator:
        tag: prompt.separator
        value: '*'
    description: semicolon-separated list of treatment to asterisk-separated mechanism
      associations
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    multivalued: true
    alias: treatment_mechanisms
    owner: DiseaseTreatmentSummary
    domain_of:
    - DiseaseTreatmentSummary
    range: TreatmentMechanism
  treatment_efficacies:
    name: treatment_efficacies
    annotations:
      prompt.separator:
        tag: prompt.separator
        value: '*'
    description: semicolon-separated list of treatment to efficacy associations, e.g.
      Imatinib*effective
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    multivalued: true
    alias: treatment_efficacies
    owner: DiseaseTreatmentSummary
    domain_of:
    - DiseaseTreatmentSummary
    range: TreatmentEfficacy

```
</details>