# Class: Treatment



URI: [treatment:Treatment](http://w3id.org/ontogpt/treatments/Treatment)


```mermaid
erDiagram
Treatment {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Treatment**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiseaseTreatmentSummary](DiseaseTreatmentSummary.md) | [treatments](treatments.md) | range | [Treatment](Treatment.md) |
| [DiseaseTreatmentSummary](DiseaseTreatmentSummary.md) | [contraindications](contraindications.md) | range | [Treatment](Treatment.md) |
| [TreatmentMechanism](TreatmentMechanism.md) | [treatment](treatment.md) | range | [Treatment](Treatment.md) |
| [TreatmentAdverseEffect](TreatmentAdverseEffect.md) | [treatment](treatment.md) | range | [Treatment](Treatment.md) |
| [TreatmentEfficacy](TreatmentEfficacy.md) | [treatment](treatment.md) | range | [Treatment](Treatment.md) |






## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:maxo, sqlite:obo:ncit, sqlite:obo:mesh, sqlite:obo:chebi |



### Schema Source


* from schema: http://w3id.org/ontogpt/treatment





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | treatment:Treatment |
| native | treatment:Treatment |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Treatment
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:maxo, sqlite:obo:ncit, sqlite:obo:mesh, sqlite:obo:chebi
from_schema: http://w3id.org/ontogpt/treatment
rank: 1000
is_a: NamedEntity
values_from:
- NCITDrugType
- NCITTreatmentType
- NCITActivityType
- MAXOTreatmentType
- MESHTherapeuticType
- CHEBIDrugType

```
</details>

### Induced

<details>
```yaml
name: Treatment
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:maxo, sqlite:obo:ncit, sqlite:obo:mesh, sqlite:obo:chebi
from_schema: http://w3id.org/ontogpt/treatment
rank: 1000
is_a: NamedEntity
values_from:
- NCITDrugType
- NCITTreatmentType
- NCITActivityType
- MAXOTreatmentType
- MESHTherapeuticType
- CHEBIDrugType
attributes:
  id:
    name: id
    annotations:
      prompt.skip:
        tag: prompt.skip
        value: 'true'
    description: A unique identifier for the named entity
    comments:
    - this is populated during the grounding and normalization step
    from_schema: http://w3id.org/ontogpt/treatment
    rank: 1000
    identifier: true
    alias: id
    owner: Treatment
    domain_of:
    - NamedEntity
    - Publication
    range: string
  label:
    name: label
    annotations:
      owl:
        tag: owl
        value: AnnotationProperty, AnnotationAssertion
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/treatment
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Treatment
    domain_of:
    - NamedEntity
    range: string

```
</details>