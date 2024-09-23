

# Class: Gene



URI: [genesummary:Gene](http://w3id.org/ontogpt/genesummary/Gene)



```mermaid
erDiagram
Gene {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Gene**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |









## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HGNC

* PR

* UniProtKB






### Annotations

| property | value |
| --- | --- |
| annotators | gilda:, bioportal:hgnc-nr |



### Schema Source


* from schema: http://w3id.org/ontogpt/gocam





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | genesummary:Gene |
| native | genesummary:Gene |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Gene
id_prefixes:
- HGNC
- PR
- UniProtKB
annotations:
  annotators:
    tag: annotators
    value: gilda:, bioportal:hgnc-nr
from_schema: http://w3id.org/ontogpt/gocam
is_a: NamedEntity
slots:
- id

```
</details>

### Induced

<details>
```yaml
name: Gene
id_prefixes:
- HGNC
- PR
- UniProtKB
annotations:
  annotators:
    tag: annotators
    value: gilda:, bioportal:hgnc-nr
from_schema: http://w3id.org/ontogpt/gocam
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
    from_schema: http://w3id.org/ontogpt/gocam
    identifier: true
    alias: id
    owner: Gene
    domain_of:
    - Gene
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
    from_schema: http://w3id.org/ontogpt/gocam
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Gene
    domain_of:
    - NamedEntity
    range: string

```
</details>