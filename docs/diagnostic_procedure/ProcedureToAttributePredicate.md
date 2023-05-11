# Class: ProcedureToAttributePredicate
_A predicate for procedure to attribute relationships, defining "this procedure is a measurement of this attribute"._




URI: [diag:ProcedureToAttributePredicate](http://w3id.org/ontogpt/diagnostic_procedure/ProcedureToAttributePredicate)


```mermaid
erDiagram
ProcedureToAttributePredicate {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * [RelationshipType](RelationshipType.md)
        * **ProcedureToAttributePredicate**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiagnosticProceduretoAttributeAssociation](DiagnosticProceduretoAttributeAssociation.md) | [predicate](predicate.md) | range | [ProcedureToAttributePredicate](ProcedureToAttributePredicate.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/diagnostic_procedure





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | diag:ProcedureToAttributePredicate |
| native | diag:ProcedureToAttributePredicate |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProcedureToAttributePredicate
description: A predicate for procedure to attribute relationships, defining "this
  procedure is a measurement of this attribute".
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
rank: 1000
is_a: RelationshipType

```
</details>

### Induced

<details>
```yaml
name: ProcedureToAttributePredicate
description: A predicate for procedure to attribute relationships, defining "this
  procedure is a measurement of this attribute".
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
rank: 1000
is_a: RelationshipType
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
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    identifier: true
    alias: id
    owner: ProcedureToAttributePredicate
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
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: ProcedureToAttributePredicate
    domain_of:
    - NamedEntity
    range: string

```
</details>