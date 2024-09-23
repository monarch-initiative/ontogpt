# Class: ActionToSymptomRelationship


_A triple representing a relationship between a medical action (A clinically prescribed procedure, therapy, intervention, or recommendation) and a symptom, for example, a chest X-ray IS USED TO DIAGNOSE pleural effusion._





URI: [maxo_extract:ActionToSymptomRelationship](http://w3id.org/ontogpt/maxoActionToSymptomRelationship)



```mermaid
erDiagram
ActionToSymptomRelationship {
    string qualifier  
}
NamedEntity {
    string id  
    string label  
}
Symptom {
    string id  
    string label  
}
Action {
    string id  
    string label  
}

ActionToSymptomRelationship ||--|o Action : "subject"
ActionToSymptomRelationship ||--|o NamedEntity : "predicate"
ActionToSymptomRelationship ||--}o Symptom : "object"
ActionToSymptomRelationship ||--|o NamedEntity : "subject_qualifier"
ActionToSymptomRelationship ||--|o NamedEntity : "object_qualifier"

```




## Inheritance
* [CompoundExpression](CompoundExpression.md)
    * [Triple](Triple.md)
        * **ActionToSymptomRelationship**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject](subject.md) | 0..1 <br/> [Action](Action.md) |  | [Triple](Triple.md) |
| [predicate](predicate.md) | 0..1 <br/> [NamedEntity](NamedEntity.md) | The relationship type, usually IS USED TO DIAGNOSE | [Triple](Triple.md) |
| [object](object.md) | 0..* <br/> [Symptom](Symptom.md) |  | [Triple](Triple.md) |
| [qualifier](qualifier.md) | 0..1 <br/> [String](String.md) | A qualifier for the statements, e | [Triple](Triple.md) |
| [subject_qualifier](subject_qualifier.md) | 0..1 <br/> [NamedEntity](NamedEntity.md) | An optional qualifier or modifier for the medical action | [Triple](Triple.md) |
| [object_qualifier](object_qualifier.md) | 0..1 <br/> [NamedEntity](NamedEntity.md) | An optional qualifier or modifier for the symptom | [Triple](Triple.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MaxoAnnotations](MaxoAnnotations.md) | [action_to_symptom](action_to_symptom.md) | range | [ActionToSymptomRelationship](ActionToSymptomRelationship.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/maxo





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | maxo_extract:ActionToSymptomRelationship |
| native | maxo_extract:ActionToSymptomRelationship |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ActionToSymptomRelationship
description: A triple representing a relationship between a medical action (A clinically
  prescribed procedure, therapy, intervention, or recommendation) and a symptom, for
  example, a chest X-ray IS USED TO DIAGNOSE pleural effusion.
from_schema: http://w3id.org/ontogpt/maxo
is_a: Triple
slot_usage:
  subject:
    name: subject
    domain_of:
    - Triple
    range: Action
  object:
    name: object
    multivalued: true
    domain_of:
    - Triple
    range: Symptom
  predicate:
    name: predicate
    description: The relationship type, usually IS USED TO DIAGNOSE
    domain_of:
    - Triple
    range: NamedEntity
  subject_qualifier:
    name: subject_qualifier
    description: An optional qualifier or modifier for the medical action.
    domain_of:
    - Triple
    range: NamedEntity
  object_qualifier:
    name: object_qualifier
    description: An optional qualifier or modifier for the symptom.
    domain_of:
    - Triple
    range: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: ActionToSymptomRelationship
description: A triple representing a relationship between a medical action (A clinically
  prescribed procedure, therapy, intervention, or recommendation) and a symptom, for
  example, a chest X-ray IS USED TO DIAGNOSE pleural effusion.
from_schema: http://w3id.org/ontogpt/maxo
is_a: Triple
slot_usage:
  subject:
    name: subject
    domain_of:
    - Triple
    range: Action
  object:
    name: object
    multivalued: true
    domain_of:
    - Triple
    range: Symptom
  predicate:
    name: predicate
    description: The relationship type, usually IS USED TO DIAGNOSE
    domain_of:
    - Triple
    range: NamedEntity
  subject_qualifier:
    name: subject_qualifier
    description: An optional qualifier or modifier for the medical action.
    domain_of:
    - Triple
    range: NamedEntity
  object_qualifier:
    name: object_qualifier
    description: An optional qualifier or modifier for the symptom.
    domain_of:
    - Triple
    range: NamedEntity
attributes:
  subject:
    name: subject
    from_schema: http://w3id.org/ontogpt/maxo
    rank: 1000
    alias: subject
    owner: ActionToSymptomRelationship
    domain_of:
    - Triple
    range: Action
  predicate:
    name: predicate
    description: The relationship type, usually IS USED TO DIAGNOSE
    from_schema: http://w3id.org/ontogpt/maxo
    rank: 1000
    alias: predicate
    owner: ActionToSymptomRelationship
    domain_of:
    - Triple
    range: NamedEntity
  object:
    name: object
    from_schema: http://w3id.org/ontogpt/maxo
    rank: 1000
    multivalued: true
    alias: object
    owner: ActionToSymptomRelationship
    domain_of:
    - Triple
    range: Symptom
  qualifier:
    name: qualifier
    description: A qualifier for the statements, e.g. "NOT" for negation
    from_schema: http://w3id.org/ontogpt/maxo
    rank: 1000
    alias: qualifier
    owner: ActionToSymptomRelationship
    domain_of:
    - Triple
    range: string
  subject_qualifier:
    name: subject_qualifier
    description: An optional qualifier or modifier for the medical action.
    from_schema: http://w3id.org/ontogpt/maxo
    rank: 1000
    alias: subject_qualifier
    owner: ActionToSymptomRelationship
    domain_of:
    - Triple
    range: NamedEntity
  object_qualifier:
    name: object_qualifier
    description: An optional qualifier or modifier for the symptom.
    from_schema: http://w3id.org/ontogpt/maxo
    rank: 1000
    alias: object_qualifier
    owner: ActionToSymptomRelationship
    domain_of:
    - Triple
    range: NamedEntity

```
</details>