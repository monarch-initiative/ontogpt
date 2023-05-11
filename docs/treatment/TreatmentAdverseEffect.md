# Class: TreatmentAdverseEffect



URI: [treatment:TreatmentAdverseEffect](http://w3id.org/ontogpt/treatments/TreatmentAdverseEffect)


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
| [treatment](treatment.md) | 0..1 <br/> [String](String.md) |  | direct |
| [adverse_effects](adverse_effects.md) | 0..* <br/> [AdverseEffect](AdverseEffect.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiseaseTreatmentSummary](DiseaseTreatmentSummary.md) | [treatment_adverse_effects](treatment_adverse_effects.md) | range | [TreatmentAdverseEffect](TreatmentAdverseEffect.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/treatment





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | treatment:TreatmentAdverseEffect |
| native | treatment:TreatmentAdverseEffect |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TreatmentAdverseEffect
from_schema: http://w3id.org/ontogpt/treatment
rank: 1000
is_a: CompoundExpression
attributes:
  treatment:
    name: treatment
    from_schema: http://w3id.org/ontogpt/treatment
    range: Treatment
  adverse_effects:
    name: adverse_effects
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    multivalued: true
    range: AdverseEffect

```
</details>

### Induced

<details>
```yaml
name: TreatmentAdverseEffect
from_schema: http://w3id.org/ontogpt/treatment
rank: 1000
is_a: CompoundExpression
attributes:
  treatment:
    name: treatment
    from_schema: http://w3id.org/ontogpt/treatment
    alias: treatment
    owner: TreatmentAdverseEffect
    domain_of:
    - TreatmentMechanism
    - TreatmentAdverseEffect
    - TreatmentEfficacy
    range: Treatment
  adverse_effects:
    name: adverse_effects
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    multivalued: true
    alias: adverse_effects
    owner: TreatmentAdverseEffect
    domain_of:
    - TreatmentAdverseEffect
    range: AdverseEffect

```
</details>