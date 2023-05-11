# Class: Phenotype



URI: [diag:Phenotype](http://w3id.org/ontogpt/diagnostic_procedure/Phenotype)


```mermaid
erDiagram
Phenotype {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Phenotype**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiagnosticProceduretoPhenotypeAssociation](DiagnosticProceduretoPhenotypeAssociation.md) | [object](object.md) | range | [Phenotype](Phenotype.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HP






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:hp |



### Schema Source


* from schema: http://w3id.org/ontogpt/diagnostic_procedure





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | diag:Phenotype |
| native | diag:Phenotype |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Phenotype
id_prefixes:
- HP
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hp
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Phenotype
id_prefixes:
- HP
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hp
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
rank: 1000
is_a: NamedEntity
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
    owner: Phenotype
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
    owner: Phenotype
    domain_of:
    - NamedEntity
    range: string

```
</details>