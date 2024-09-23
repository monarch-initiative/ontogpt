

# Class: TreatmentEfficacy



URI: [composite_disease:TreatmentEfficacy](http://w3id.org/ontogpt/composite_disease/TreatmentEfficacy)



```mermaid
erDiagram
TreatmentEfficacy {
    string efficacy  
}
Treatment {
    string id  
    string label  
}

TreatmentEfficacy ||--|o Treatment : "treatment"

```




## Inheritance
* [CompoundExpression](CompoundExpression.md)
    * **TreatmentEfficacy**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [treatment](treatment.md) | 0..1 <br/> [Treatment](Treatment.md) |  | direct |
| [efficacy](efficacy.md) | 0..1 <br/> [String](String.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CompositeDisease](CompositeDisease.md) | [treatment_efficacies](treatment_efficacies.md) | range | [TreatmentEfficacy](TreatmentEfficacy.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/composite_disease





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | composite_disease:TreatmentEfficacy |
| native | composite_disease:TreatmentEfficacy |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TreatmentEfficacy
from_schema: http://w3id.org/ontogpt/composite_disease
is_a: CompoundExpression
attributes:
  treatment:
    name: treatment
    from_schema: http://w3id.org/ontogpt/composite_disease
    domain_of:
    - TreatmentMechanism
    - TreatmentAdverseEffect
    - TreatmentEfficacy
    range: Treatment
  efficacy:
    name: efficacy
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    domain_of:
    - TreatmentEfficacy
    range: string

```
</details>

### Induced

<details>
```yaml
name: TreatmentEfficacy
from_schema: http://w3id.org/ontogpt/composite_disease
is_a: CompoundExpression
attributes:
  treatment:
    name: treatment
    from_schema: http://w3id.org/ontogpt/composite_disease
    alias: treatment
    owner: TreatmentEfficacy
    domain_of:
    - TreatmentMechanism
    - TreatmentAdverseEffect
    - TreatmentEfficacy
    range: Treatment
  efficacy:
    name: efficacy
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    alias: efficacy
    owner: TreatmentEfficacy
    domain_of:
    - TreatmentEfficacy
    range: string

```
</details>