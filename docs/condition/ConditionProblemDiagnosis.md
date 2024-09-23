

# Class: ConditionProblemDiagnosis



URI: [UNKNOWN:ConditionProblemDiagnosis](UNKNOWN:ConditionProblemDiagnosis)



```mermaid
erDiagram
ConditionProblemDiagnosis {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **ConditionProblemDiagnosis**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Condition](Condition.md) | [code](code.md) | range | [ConditionProblemDiagnosis](ConditionProblemDiagnosis.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* SNOMEDCT






### Annotations

| property | value |
| --- | --- |
| annotators | bioportal:SNOMEDCT |



### Schema Source


* from schema: http://w3id.org/ontogpt/condition




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | UNKNOWN:ConditionProblemDiagnosis |
| native | UNKNOWN:ConditionProblemDiagnosis |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ConditionProblemDiagnosis
id_prefixes:
- SNOMEDCT
annotations:
  annotators:
    tag: annotators
    value: bioportal:SNOMEDCT
from_schema: http://w3id.org/ontogpt/condition
is_a: NamedEntity
slot_usage:
  id:
    name: id
    values_from:
    - ConditionProblemDiagnosisIdentifier
    domain_of:
    - NamedEntity
    - Publication

```
</details>

### Induced

<details>
```yaml
name: ConditionProblemDiagnosis
id_prefixes:
- SNOMEDCT
annotations:
  annotators:
    tag: annotators
    value: bioportal:SNOMEDCT
from_schema: http://w3id.org/ontogpt/condition
is_a: NamedEntity
slot_usage:
  id:
    name: id
    values_from:
    - ConditionProblemDiagnosisIdentifier
    domain_of:
    - NamedEntity
    - Publication
attributes:
  id:
    name: id
    description: A unique identifier for the named entity
    from_schema: http://w3id.org/ontogpt/condition
    rank: 1000
    values_from:
    - ConditionProblemDiagnosisIdentifier
    identifier: true
    alias: id
    owner: ConditionProblemDiagnosis
    domain_of:
    - NamedEntity
    - Publication
    range: string
    required: true
  label:
    name: label
    annotations:
      owl:
        tag: owl
        value: AnnotationProperty, AnnotationAssertion
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/condition
    aliases:
    - name
    slot_uri: rdfs:label
    alias: label
    owner: ConditionProblemDiagnosis
    domain_of:
    - Condition
    - NamedEntity
    range: string

```
</details>