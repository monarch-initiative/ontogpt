

# Class: ExperimentalMetricToChemicalRelationship


_A triple where the subject is an experimental metric, the object is a chemical, drug, or other substance, and the predicate describes the relationship between the metric and the chemical, usually MEASURED_IN_RESPONSE_TO._





URI: [alzrd:ExperimentalMetricToChemicalRelationship](http://w3id.org/ontogpt/alzrdExperimentalMetricToChemicalRelationship)



```mermaid
erDiagram
ExperimentalMetricToChemicalRelationship {
    string direct_or_indirect  
    string association  
}
NamedEntity {
    string id  
    string label  
}
Chemical {
    string id  
    string label  
}
MetricOrIndicator {
    string id  
    string label  
}

ExperimentalMetricToChemicalRelationship ||--|o MetricOrIndicator : "metric"
ExperimentalMetricToChemicalRelationship ||--|o Chemical : "chemical"
ExperimentalMetricToChemicalRelationship ||--|o NamedEntity : "predicate"
ExperimentalMetricToChemicalRelationship ||--|o NamedEntity : "metric_qualifier"
ExperimentalMetricToChemicalRelationship ||--|o NamedEntity : "chemical_qualifier"

```




## Inheritance
* [CompoundExpression](CompoundExpression.md)
    * **ExperimentalMetricToChemicalRelationship**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [metric](metric.md) | 0..1 <br/> [MetricOrIndicator](MetricOrIndicator.md) | The name of an experimental metric, sign, symptom, or outcome used to measure... | direct |
| [chemical](chemical.md) | 0..1 <br/> [Chemical](Chemical.md) | The name of a chemical, drug, or other substance | direct |
| [predicate](predicate.md) | 0..1 <br/> [NamedEntity](NamedEntity.md) | The relationship type, generally MEASURED_IN_RESPONSE_TO to indicate a metric... | direct |
| [metric_qualifier](metric_qualifier.md) | 0..1 <br/> [NamedEntity](NamedEntity.md) | An optional qualifier or modifier for the experimental metric, as described i... | direct |
| [chemical_qualifier](chemical_qualifier.md) | 0..1 <br/> [NamedEntity](NamedEntity.md) | An optional qualifier or modifier for the chemical, drug, or other substance,... | direct |
| [direct_or_indirect](direct_or_indirect.md) | 0..1 <br/> [String](String.md) | Whether the relationship between the metric and the chemical is direct or ind... | direct |
| [association](association.md) | 0..1 <br/> [String](String.md) | The type of any observed association between the value of the metric and the ... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Document](Document.md) | [experimental_metric_to_chemical_relationships](experimental_metric_to_chemical_relationships.md) | range | [ExperimentalMetricToChemicalRelationship](ExperimentalMetricToChemicalRelationship.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:ExperimentalMetricToChemicalRelationship |
| native | alzrd:ExperimentalMetricToChemicalRelationship |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ExperimentalMetricToChemicalRelationship
description: A triple where the subject is an experimental metric, the object is a
  chemical, drug, or other substance, and the predicate describes the relationship
  between the metric and the chemical, usually MEASURED_IN_RESPONSE_TO.
from_schema: http://w3id.org/ontogpt/alzrd
is_a: CompoundExpression
attributes:
  metric:
    name: metric
    description: The name of an experimental metric, sign, symptom, or outcome used
      to measure the effects of treatments on symptoms or diagnostics, or of the progression
      of Alzheimer's disease and related dementias. In experimental animal models
      these are analogues of cognitive impairment or indicators of disease progression
      modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris
      water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive
      decline.
    from_schema: http://w3id.org/ontogpt/alzrd
    domain_of:
    - ExperimentalMetricToTaxonRelationship
    - ExperimentalMetricToDiseaseRelationship
    - ExperimentalMetricToEnvironmentRelationship
    - ExperimentalMetricToChemicalRelationship
    range: MetricOrIndicator
  chemical:
    name: chemical
    description: The name of a chemical, drug, or other substance. Examples are "donepezil",
      "Aβ42", "Aβ40", "tau", "insulin", "caffeine", "nicotine", "alcohol".
    from_schema: http://w3id.org/ontogpt/alzrd
    domain_of:
    - Document
    - ExperimentalMetricToChemicalRelationship
    range: Chemical
  predicate:
    name: predicate
    description: The relationship type, generally MEASURED_IN_RESPONSE_TO to indicate
      a metric is measured in response to a chemical.
    from_schema: http://w3id.org/ontogpt/alzrd
    domain_of:
    - ExperimentalMetricToTaxonRelationship
    - ExperimentalMetricToDiseaseRelationship
    - ExperimentalMetricToEnvironmentRelationship
    - ExperimentalMetricToChemicalRelationship
    - Triple
    range: NamedEntity
  metric_qualifier:
    name: metric_qualifier
    description: An optional qualifier or modifier for the experimental metric, as
      described in the input text. This may include the method of measurement or the
      specific assay used.
    from_schema: http://w3id.org/ontogpt/alzrd
    domain_of:
    - ExperimentalMetricToTaxonRelationship
    - ExperimentalMetricToDiseaseRelationship
    - ExperimentalMetricToEnvironmentRelationship
    - ExperimentalMetricToChemicalRelationship
    range: NamedEntity
  chemical_qualifier:
    name: chemical_qualifier
    description: An optional qualifier or modifier for the chemical, drug, or other
      substance, as described in the input text. This may include the dose or route
      of administration.
    from_schema: http://w3id.org/ontogpt/alzrd
    rank: 1000
    domain_of:
    - ExperimentalMetricToChemicalRelationship
    range: NamedEntity
  direct_or_indirect:
    name: direct_or_indirect
    description: Whether the relationship between the metric and the chemical is direct
      or indirect. UNKNOWN if this is not specified in the text or is unclear.
    from_schema: http://w3id.org/ontogpt/alzrd
    domain_of:
    - ExperimentalMetricToTaxonRelationship
    - ExperimentalMetricToDiseaseRelationship
    - ExperimentalMetricToEnvironmentRelationship
    - ExperimentalMetricToChemicalRelationship
    range: string
  association:
    name: association
    description: The type of any observed association between the value of the metric
      and the chemical. May be "positive", "negative", "inconclusive", or UNKNOWN
      if this is not specified in the text or is unclear.
    from_schema: http://w3id.org/ontogpt/alzrd
    domain_of:
    - ExperimentalMetricToDiseaseRelationship
    - ExperimentalMetricToEnvironmentRelationship
    - ExperimentalMetricToChemicalRelationship
    range: string

```
</details>

### Induced

<details>
```yaml
name: ExperimentalMetricToChemicalRelationship
description: A triple where the subject is an experimental metric, the object is a
  chemical, drug, or other substance, and the predicate describes the relationship
  between the metric and the chemical, usually MEASURED_IN_RESPONSE_TO.
from_schema: http://w3id.org/ontogpt/alzrd
is_a: CompoundExpression
attributes:
  metric:
    name: metric
    description: The name of an experimental metric, sign, symptom, or outcome used
      to measure the effects of treatments on symptoms or diagnostics, or of the progression
      of Alzheimer's disease and related dementias. In experimental animal models
      these are analogues of cognitive impairment or indicators of disease progression
      modeling those observed in humans. Examples are Amyloid beta (Aβ) levels, Morris
      water maze test, tau phosphorylation, neurofibrillary tangles, and cognitive
      decline.
    from_schema: http://w3id.org/ontogpt/alzrd
    alias: metric
    owner: ExperimentalMetricToChemicalRelationship
    domain_of:
    - ExperimentalMetricToTaxonRelationship
    - ExperimentalMetricToDiseaseRelationship
    - ExperimentalMetricToEnvironmentRelationship
    - ExperimentalMetricToChemicalRelationship
    range: MetricOrIndicator
  chemical:
    name: chemical
    description: The name of a chemical, drug, or other substance. Examples are "donepezil",
      "Aβ42", "Aβ40", "tau", "insulin", "caffeine", "nicotine", "alcohol".
    from_schema: http://w3id.org/ontogpt/alzrd
    alias: chemical
    owner: ExperimentalMetricToChemicalRelationship
    domain_of:
    - Document
    - ExperimentalMetricToChemicalRelationship
    range: Chemical
  predicate:
    name: predicate
    description: The relationship type, generally MEASURED_IN_RESPONSE_TO to indicate
      a metric is measured in response to a chemical.
    from_schema: http://w3id.org/ontogpt/alzrd
    alias: predicate
    owner: ExperimentalMetricToChemicalRelationship
    domain_of:
    - ExperimentalMetricToTaxonRelationship
    - ExperimentalMetricToDiseaseRelationship
    - ExperimentalMetricToEnvironmentRelationship
    - ExperimentalMetricToChemicalRelationship
    - Triple
    range: NamedEntity
  metric_qualifier:
    name: metric_qualifier
    description: An optional qualifier or modifier for the experimental metric, as
      described in the input text. This may include the method of measurement or the
      specific assay used.
    from_schema: http://w3id.org/ontogpt/alzrd
    alias: metric_qualifier
    owner: ExperimentalMetricToChemicalRelationship
    domain_of:
    - ExperimentalMetricToTaxonRelationship
    - ExperimentalMetricToDiseaseRelationship
    - ExperimentalMetricToEnvironmentRelationship
    - ExperimentalMetricToChemicalRelationship
    range: NamedEntity
  chemical_qualifier:
    name: chemical_qualifier
    description: An optional qualifier or modifier for the chemical, drug, or other
      substance, as described in the input text. This may include the dose or route
      of administration.
    from_schema: http://w3id.org/ontogpt/alzrd
    rank: 1000
    alias: chemical_qualifier
    owner: ExperimentalMetricToChemicalRelationship
    domain_of:
    - ExperimentalMetricToChemicalRelationship
    range: NamedEntity
  direct_or_indirect:
    name: direct_or_indirect
    description: Whether the relationship between the metric and the chemical is direct
      or indirect. UNKNOWN if this is not specified in the text or is unclear.
    from_schema: http://w3id.org/ontogpt/alzrd
    alias: direct_or_indirect
    owner: ExperimentalMetricToChemicalRelationship
    domain_of:
    - ExperimentalMetricToTaxonRelationship
    - ExperimentalMetricToDiseaseRelationship
    - ExperimentalMetricToEnvironmentRelationship
    - ExperimentalMetricToChemicalRelationship
    range: string
  association:
    name: association
    description: The type of any observed association between the value of the metric
      and the chemical. May be "positive", "negative", "inconclusive", or UNKNOWN
      if this is not specified in the text or is unclear.
    from_schema: http://w3id.org/ontogpt/alzrd
    alias: association
    owner: ExperimentalMetricToChemicalRelationship
    domain_of:
    - ExperimentalMetricToDiseaseRelationship
    - ExperimentalMetricToEnvironmentRelationship
    - ExperimentalMetricToChemicalRelationship
    range: string

```
</details>