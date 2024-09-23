

# Class: MolecularActivity



URI: [bp:MolecularActivity](http://w3id.org/ontogpt/biological-process-templateMolecularActivity)



```mermaid
erDiagram
MolecularActivity {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **MolecularActivity**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [BiologicalProcess](BiologicalProcess.md) | [steps](steps.md) | range | [MolecularActivity](MolecularActivity.md) |
| [GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md) | [molecular_activity](molecular_activity.md) | range | [MolecularActivity](MolecularActivity.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* GO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go |



### Schema Source


* from schema: https://w3id.org/ontogpt/biological_process





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bp:MolecularActivity |
| native | bp:MolecularActivity |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MolecularActivity
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
from_schema: https://w3id.org/ontogpt/biological_process
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: MolecularActivity
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
from_schema: https://w3id.org/ontogpt/biological_process
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
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    identifier: true
    alias: id
    owner: MolecularActivity
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
    from_schema: https://w3id.org/ontogpt/biological_process
    aliases:
    - name
    slot_uri: rdfs:label
    alias: label
    owner: MolecularActivity
    domain_of:
    - BiologicalProcess
    - NamedEntity
    range: string

```
</details>