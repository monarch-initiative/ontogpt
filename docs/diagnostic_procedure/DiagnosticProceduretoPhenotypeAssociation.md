

# Class: DiagnosticProceduretoPhenotypeAssociation


_A triple representing a relationship between a diagnostic procedure and an associated phenotype, e.g., "blood pressure measurement" is associated with "high blood pressure"._





URI: [diag:DiagnosticProceduretoPhenotypeAssociation](http://w3id.org/ontogpt/diagnostic_procedure/DiagnosticProceduretoPhenotypeAssociation)



```mermaid
erDiagram
DiagnosticProceduretoPhenotypeAssociation {
    string qualifier  
}
NamedEntity {
    string id  
    string label  
}
Phenotype {
    string id  
    string label  
}
ProcedureToPhenotypePredicate {
    string id  
    string label  
}
DiagnosticProcedure {
    string id  
    string label  
}

DiagnosticProceduretoPhenotypeAssociation ||--|o DiagnosticProcedure : "subject"
DiagnosticProceduretoPhenotypeAssociation ||--|o ProcedureToPhenotypePredicate : "predicate"
DiagnosticProceduretoPhenotypeAssociation ||--}o Phenotype : "object"
DiagnosticProceduretoPhenotypeAssociation ||--|o NamedEntity : "subject_qualifier"
DiagnosticProceduretoPhenotypeAssociation ||--|o NamedEntity : "object_qualifier"

```




## Inheritance
* [CompoundExpression](CompoundExpression.md)
    * [Triple](Triple.md)
        * **DiagnosticProceduretoPhenotypeAssociation**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject](subject.md) | 0..1 <br/> [DiagnosticProcedure](DiagnosticProcedure.md) | A diagnostic procedure yielding a result, which in turn may be interpreted as... | [Triple](Triple.md) |
| [predicate](predicate.md) | 0..1 <br/> [ProcedureToPhenotypePredicate](ProcedureToPhenotypePredicate.md) | The relationship type, e | [Triple](Triple.md) |
| [object](object.md) | * <br/> [Phenotype](Phenotype.md) | The observable physical or biochemical characteristics of a patient | [Triple](Triple.md) |
| [qualifier](qualifier.md) | 0..1 <br/> [String](String.md) | A qualifier for the statements, e | [Triple](Triple.md) |
| [subject_qualifier](subject_qualifier.md) | 0..1 <br/> [NamedEntity](NamedEntity.md) | An optional qualifier or modifier for the procedure | [Triple](Triple.md) |
| [object_qualifier](object_qualifier.md) | 0..1 <br/> [NamedEntity](NamedEntity.md) | An optional qualifier or modifier for the phenotype | [Triple](Triple.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/diagnostic_procedure




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | diag:DiagnosticProceduretoPhenotypeAssociation |
| native | diag:DiagnosticProceduretoPhenotypeAssociation |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DiagnosticProceduretoPhenotypeAssociation
description: A triple representing a relationship between a diagnostic procedure and
  an associated phenotype, e.g., "blood pressure measurement" is associated with "high
  blood pressure".
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
is_a: Triple
slot_usage:
  subject:
    name: subject
    description: A diagnostic procedure yielding a result, which in turn may be interpreted
      as a phenotype. Procedures include "heart rate measurement", "blood pressure
      measurement", "oxygen saturation measurement", etc. In practice, procedures
      may be named based on what they measure, with the "measurement" part left implicit.
    domain_of:
    - Triple
    range: DiagnosticProcedure
  object:
    name: object
    description: The observable physical or biochemical characteristics of a patient.
      Not equivalent to a disease state, but may contribute to a diagnosis.
    domain_of:
    - Triple
    range: Phenotype
    multivalued: true
  predicate:
    name: predicate
    description: The relationship type, e.g. RELATED_TO
    domain_of:
    - Triple
    range: ProcedureToPhenotypePredicate
  subject_qualifier:
    name: subject_qualifier
    description: An optional qualifier or modifier for the procedure.
    domain_of:
    - Triple
    range: NamedEntity
  object_qualifier:
    name: object_qualifier
    description: An optional qualifier or modifier for the phenotype.
    domain_of:
    - Triple
    range: NamedEntity
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: DiagnosticProceduretoPhenotypeAssociation
description: A triple representing a relationship between a diagnostic procedure and
  an associated phenotype, e.g., "blood pressure measurement" is associated with "high
  blood pressure".
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
is_a: Triple
slot_usage:
  subject:
    name: subject
    description: A diagnostic procedure yielding a result, which in turn may be interpreted
      as a phenotype. Procedures include "heart rate measurement", "blood pressure
      measurement", "oxygen saturation measurement", etc. In practice, procedures
      may be named based on what they measure, with the "measurement" part left implicit.
    domain_of:
    - Triple
    range: DiagnosticProcedure
  object:
    name: object
    description: The observable physical or biochemical characteristics of a patient.
      Not equivalent to a disease state, but may contribute to a diagnosis.
    domain_of:
    - Triple
    range: Phenotype
    multivalued: true
  predicate:
    name: predicate
    description: The relationship type, e.g. RELATED_TO
    domain_of:
    - Triple
    range: ProcedureToPhenotypePredicate
  subject_qualifier:
    name: subject_qualifier
    description: An optional qualifier or modifier for the procedure.
    domain_of:
    - Triple
    range: NamedEntity
  object_qualifier:
    name: object_qualifier
    description: An optional qualifier or modifier for the phenotype.
    domain_of:
    - Triple
    range: NamedEntity
attributes:
  subject:
    name: subject
    description: A diagnostic procedure yielding a result, which in turn may be interpreted
      as a phenotype. Procedures include "heart rate measurement", "blood pressure
      measurement", "oxygen saturation measurement", etc. In practice, procedures
      may be named based on what they measure, with the "measurement" part left implicit.
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: subject
    owner: DiagnosticProceduretoPhenotypeAssociation
    domain_of:
    - Triple
    range: DiagnosticProcedure
  predicate:
    name: predicate
    description: The relationship type, e.g. RELATED_TO
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: predicate
    owner: DiagnosticProceduretoPhenotypeAssociation
    domain_of:
    - Triple
    range: ProcedureToPhenotypePredicate
  object:
    name: object
    description: The observable physical or biochemical characteristics of a patient.
      Not equivalent to a disease state, but may contribute to a diagnosis.
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: object
    owner: DiagnosticProceduretoPhenotypeAssociation
    domain_of:
    - Triple
    range: Phenotype
    multivalued: true
  qualifier:
    name: qualifier
    description: A qualifier for the statements, e.g. "NOT" for negation
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: qualifier
    owner: DiagnosticProceduretoPhenotypeAssociation
    domain_of:
    - Triple
    range: string
  subject_qualifier:
    name: subject_qualifier
    description: An optional qualifier or modifier for the procedure.
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: subject_qualifier
    owner: DiagnosticProceduretoPhenotypeAssociation
    domain_of:
    - Triple
    range: NamedEntity
  object_qualifier:
    name: object_qualifier
    description: An optional qualifier or modifier for the phenotype.
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: object_qualifier
    owner: DiagnosticProceduretoPhenotypeAssociation
    domain_of:
    - Triple
    range: NamedEntity
tree_root: true

```
</details>