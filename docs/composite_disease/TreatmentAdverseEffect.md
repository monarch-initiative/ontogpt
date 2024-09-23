

# Class: TreatmentAdverseEffect



URI: [composite_disease:TreatmentAdverseEffect](http://w3id.org/ontogpt/composite_disease/TreatmentAdverseEffect)



```mermaid
erDiagram
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

TreatmentAdverseEffect ||--|o Treatment : "treatment"
TreatmentAdverseEffect ||--}o AdverseEffect : "adverse_effects"

```




## Inheritance
* [CompoundExpression](CompoundExpression.md)
    * **TreatmentAdverseEffect**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [treatment](treatment.md) | 0..1 <br/> [Treatment](Treatment.md) |  | direct |
| [adverse_effects](adverse_effects.md) | * <br/> [AdverseEffect](AdverseEffect.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [CompositeDisease](CompositeDisease.md) | [treatment_adverse_effects](treatment_adverse_effects.md) | range | [TreatmentAdverseEffect](TreatmentAdverseEffect.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/composite_disease





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | composite_disease:TreatmentAdverseEffect |
| native | composite_disease:TreatmentAdverseEffect |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TreatmentAdverseEffect
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
  adverse_effects:
    name: adverse_effects
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    domain_of:
    - TreatmentAdverseEffect
    range: AdverseEffect

```
</details>

### Induced

<details>
```yaml
name: TreatmentAdverseEffect
from_schema: http://w3id.org/ontogpt/composite_disease
is_a: CompoundExpression
attributes:
  treatment:
    name: treatment
    from_schema: http://w3id.org/ontogpt/composite_disease
    alias: treatment
    owner: TreatmentAdverseEffect
    domain_of:
    - TreatmentMechanism
    - TreatmentAdverseEffect
    - TreatmentEfficacy
    range: Treatment
  adverse_effects:
    name: adverse_effects
    from_schema: http://w3id.org/ontogpt/composite_disease
    rank: 1000
    multivalued: true
    alias: adverse_effects
    owner: TreatmentAdverseEffect
    domain_of:
    - TreatmentAdverseEffect
    range: AdverseEffect

```
</details>