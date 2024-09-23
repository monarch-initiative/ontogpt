

# Class: ClinicalObservationSet


_A set of sets of clinical observations._





URI: [dietitian_notes:ClinicalObservationSet](dietitian_notes:ClinicalObservationSet)



```mermaid
erDiagram
ClinicalObservationSet {

}
ClinicalObservations {
    string is_pediatric  
    string is_preterm  
    string nil_per_os  
    string id  
    string label  
}
DrugTherapy {
    string route_of_administration  
}
NutritionSupport {

}
DietSupplementation {
    string route_of_administration  
}
MalnutritionObservations {
    string malnutrition_presence  
    string malnutrition_risk  
    string severity  
    string acute_or_chronic  
    string risk_for_refeeding_syndrome  
}
QuantitativeValueWithMetric {
    string percentile  
    string zscore  
    string value  
}
QuantitativeValue {
    string value  
}

ClinicalObservationSet ||--}o ClinicalObservations : "observations"
ClinicalObservations ||--|o QuantitativeValue : "patient_age"
ClinicalObservations ||--|o QuantitativeValueWithMetric : "patient_height"
ClinicalObservations ||--|o QuantitativeValueWithMetric : "current_patient_weight"
ClinicalObservations ||--|o QuantitativeValueWithMetric : "usual_patient_weight"
ClinicalObservations ||--|o QuantitativeValueWithMetric : "head_circumference"
ClinicalObservations ||--|o MalnutritionObservations : "malnutrition_status"
ClinicalObservations ||--}o DietSupplementation : "diet_supplementation"
ClinicalObservations ||--}o NutritionSupport : "nutrition_support"
ClinicalObservations ||--}o DrugTherapy : "medications"
DrugTherapy ||--|o Drug : "drug"
DrugTherapy ||--|o QuantitativeValueWithFrequency : "amount"
DrugTherapy ||--|o Unit : "dosage_by_unit"
DrugTherapy ||--|o QuantitativeValue : "duration"
NutritionSupport ||--|o NutritionSupportMethod : "method"
NutritionSupport ||--}o NutritionSupportComponent : "components"
DietSupplementation ||--|o TherapeuticMaterial : "supplement"
DietSupplementation ||--|o QuantitativeValueWithFrequency : "amount"
DietSupplementation ||--|o Unit : "dosage_by_unit"
DietSupplementation ||--|o QuantitativeValue : "duration"
MalnutritionObservations ||--|o Disease : "diagnosis"
MalnutritionObservations ||--|o Disease : "etiology"
QuantitativeValueWithMetric ||--|o Unit : "unit"
QuantitativeValue ||--|o Unit : "unit"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [observations](observations.md) | * <br/> [ClinicalObservations](ClinicalObservations.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:ClinicalObservationSet |
| native | dietitian_notes:ClinicalObservationSet |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ClinicalObservationSet
description: A set of sets of clinical observations.
from_schema: http://w3id.org/ontogpt/dietician_notes
attributes:
  observations:
    name: observations
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    domain_of:
    - ClinicalObservationSet
    range: ClinicalObservations
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: ClinicalObservationSet
description: A set of sets of clinical observations.
from_schema: http://w3id.org/ontogpt/dietician_notes
attributes:
  observations:
    name: observations
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    alias: observations
    owner: ClinicalObservationSet
    domain_of:
    - ClinicalObservationSet
    range: ClinicalObservations
    multivalued: true

```
</details>