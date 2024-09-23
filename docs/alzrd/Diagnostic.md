

# Class: Diagnostic



URI: [alzrd:Diagnostic](http://w3id.org/ontogpt/alzrdDiagnostic)



```mermaid
erDiagram
Diagnostic {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Diagnostic**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Document](Document.md) | [diagnostics](diagnostics.md) | range | [Diagnostic](Diagnostic.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* MAXO

* MESH






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:maxo, sqlite:obo:mesh, sqlite:obo:ncit || prompt | The name of a diagnostic procedure or test. Examples are MRI, PET scan, lumbar puncture, blood test, biopsy. |



### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:Diagnostic |
| native | alzrd:Diagnostic |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Diagnostic
id_prefixes:
- MAXO
- MESH
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:maxo, sqlite:obo:mesh, sqlite:obo:ncit
  prompt:
    tag: prompt
    value: The name of a diagnostic procedure or test. Examples are MRI, PET scan,
      lumbar puncture, blood test, biopsy.
from_schema: http://w3id.org/ontogpt/alzrd
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Diagnostic
id_prefixes:
- MAXO
- MESH
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:maxo, sqlite:obo:mesh, sqlite:obo:ncit
  prompt:
    tag: prompt
    value: The name of a diagnostic procedure or test. Examples are MRI, PET scan,
      lumbar puncture, blood test, biopsy.
from_schema: http://w3id.org/ontogpt/alzrd
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
    from_schema: http://w3id.org/ontogpt/alzrd
    rank: 1000
    identifier: true
    alias: id
    owner: Diagnostic
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
    from_schema: http://w3id.org/ontogpt/alzrd
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Diagnostic
    domain_of:
    - NamedEntity
    range: string

```
</details>