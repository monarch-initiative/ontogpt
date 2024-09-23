

# Class: ClinicalAttribute



URI: [diag:ClinicalAttribute](http://w3id.org/ontogpt/diagnostic_procedure/ClinicalAttribute)



```mermaid
erDiagram
ClinicalAttribute {
    string id  
    string label  
}
Unit {
    string id  
    string label  
}

ClinicalAttribute ||--|o Unit : "unit"

```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **ClinicalAttribute**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [unit](unit.md) | 0..1 <br/> [Unit](Unit.md) | the unit used to measure the attribute | direct |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiagnosticProceduretoAttributeAssociation](DiagnosticProceduretoAttributeAssociation.md) | [object](object.md) | range | [ClinicalAttribute](ClinicalAttribute.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* OBA






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:oba, sqlite:obo:ncit |



### Schema Source


* from schema: http://w3id.org/ontogpt/diagnostic_procedure




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | diag:ClinicalAttribute |
| native | diag:ClinicalAttribute |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ClinicalAttribute
id_prefixes:
- OBA
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:oba, sqlite:obo:ncit
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
is_a: NamedEntity
attributes:
  unit:
    name: unit
    description: the unit used to measure the attribute
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    domain_of:
    - ClinicalAttribute
    range: Unit

```
</details>

### Induced

<details>
```yaml
name: ClinicalAttribute
id_prefixes:
- OBA
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:oba, sqlite:obo:ncit
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
is_a: NamedEntity
attributes:
  unit:
    name: unit
    description: the unit used to measure the attribute
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: unit
    owner: ClinicalAttribute
    domain_of:
    - ClinicalAttribute
    range: Unit
  id:
    name: id
    annotations:
      prompt.skip:
        tag: prompt.skip
        value: 'true'
    description: A unique identifier for the named entity
    comments:
    - this is populated during the grounding and normalization step
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    identifier: true
    alias: id
    owner: ClinicalAttribute
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
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: ClinicalAttribute
    domain_of:
    - NamedEntity
    range: string

```
</details>