

# Class: DietSupplementation



URI: [dietitian_notes:DietSupplementation](dietitian_notes:DietSupplementation)



```mermaid
erDiagram
DietSupplementation {
    string route_of_administration  
}
QuantitativeValue {
    string value  
}
Unit {
    string id  
    string label  
}
QuantitativeValueWithFrequency {
    string frequency  
    string value  
}
TherapeuticMaterial {
    string id  
    string label  
}

DietSupplementation ||--|o TherapeuticMaterial : "supplement"
DietSupplementation ||--|o QuantitativeValueWithFrequency : "amount"
DietSupplementation ||--|o Unit : "dosage_by_unit"
DietSupplementation ||--|o QuantitativeValue : "duration"
QuantitativeValue ||--|o Unit : "unit"
QuantitativeValueWithFrequency ||--|o Unit : "unit"

```




## Inheritance
* [CompoundExpression](CompoundExpression.md)
    * **DietSupplementation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [supplement](supplement.md) | 0..1 <br/> [TherapeuticMaterial](TherapeuticMaterial.md) | The name of a specific material added to a patient's diet | direct |
| [amount](amount.md) | 0..1 <br/> [QuantitativeValueWithFrequency](QuantitativeValueWithFrequency.md) | The quantity or dosage of the therapy, if provided | direct |
| [dosage_by_unit](dosage_by_unit.md) | 0..1 <br/> [Unit](Unit.md) | The unit of a patient's properties used to determine supplement dosage | direct |
| [duration](duration.md) | 0..1 <br/> [QuantitativeValue](QuantitativeValue.md) | The duration of the supplementation, if provided | direct |
| [route_of_administration](route_of_administration.md) | 0..1 <br/> [String](String.md) | The route of administration for the supplementation, if provided | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ClinicalObservations](ClinicalObservations.md) | [diet_supplementation](diet_supplementation.md) | range | [DietSupplementation](DietSupplementation.md) |






## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| owl | IntersectionOf |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:DietSupplementation |
| native | dietitian_notes:DietSupplementation |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DietSupplementation
annotations:
  owl:
    tag: owl
    value: IntersectionOf
from_schema: http://w3id.org/ontogpt/dietician_notes
is_a: CompoundExpression
attributes:
  supplement:
    name: supplement
    description: The name of a specific material added to a patient's diet.
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    domain_of:
    - DietSupplementation
    range: TherapeuticMaterial
  amount:
    name: amount
    description: The quantity or dosage of the therapy, if provided. May include a
      frequency. N/A if not provided.
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    domain_of:
    - DietSupplementation
    - NutritionSupportComponent
    - DrugTherapy
    range: QuantitativeValueWithFrequency
  dosage_by_unit:
    name: dosage_by_unit
    description: The unit of a patient's properties used to determine supplement dosage.
      Often "kilogram". N/A if not provided.
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    domain_of:
    - DietSupplementation
    - NutritionSupportComponent
    - DrugTherapy
    range: Unit
  duration:
    name: duration
    description: The duration of the supplementation, if provided. N/A if not provided.
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    domain_of:
    - DietSupplementation
    - NutritionSupportComponent
    - DrugTherapy
    range: QuantitativeValue
  route_of_administration:
    name: route_of_administration
    description: The route of administration for the supplementation, if provided.
      N/A if not provided.
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    domain_of:
    - DietSupplementation
    - DrugTherapy
    range: string

```
</details>

### Induced

<details>
```yaml
name: DietSupplementation
annotations:
  owl:
    tag: owl
    value: IntersectionOf
from_schema: http://w3id.org/ontogpt/dietician_notes
is_a: CompoundExpression
attributes:
  supplement:
    name: supplement
    description: The name of a specific material added to a patient's diet.
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    alias: supplement
    owner: DietSupplementation
    domain_of:
    - DietSupplementation
    range: TherapeuticMaterial
  amount:
    name: amount
    description: The quantity or dosage of the therapy, if provided. May include a
      frequency. N/A if not provided.
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    alias: amount
    owner: DietSupplementation
    domain_of:
    - DietSupplementation
    - NutritionSupportComponent
    - DrugTherapy
    range: QuantitativeValueWithFrequency
  dosage_by_unit:
    name: dosage_by_unit
    description: The unit of a patient's properties used to determine supplement dosage.
      Often "kilogram". N/A if not provided.
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    alias: dosage_by_unit
    owner: DietSupplementation
    domain_of:
    - DietSupplementation
    - NutritionSupportComponent
    - DrugTherapy
    range: Unit
  duration:
    name: duration
    description: The duration of the supplementation, if provided. N/A if not provided.
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    alias: duration
    owner: DietSupplementation
    domain_of:
    - DietSupplementation
    - NutritionSupportComponent
    - DrugTherapy
    range: QuantitativeValue
  route_of_administration:
    name: route_of_administration
    description: The route of administration for the supplementation, if provided.
      N/A if not provided.
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    alias: route_of_administration
    owner: DietSupplementation
    domain_of:
    - DietSupplementation
    - DrugTherapy
    range: string

```
</details>