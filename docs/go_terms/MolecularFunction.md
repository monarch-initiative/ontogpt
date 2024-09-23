

# Class: MolecularFunction



URI: [go_terms:MolecularFunction](http://w3id.org/ontogpt/go_termsMolecularFunction)



```mermaid
erDiagram
MolecularFunction {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **MolecularFunction**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Document](Document.md) | [molecularfunctions](molecularfunctions.md) | range | [MolecularFunction](MolecularFunction.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* GO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:go || prompt.examples | catalytic activity, amine binding, peptide receptor activity, oxygen carrier activity, structural constituent of cytoskeleton |



### Schema Source


* from schema: http://w3id.org/ontogpt/go_terms





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | go_terms:MolecularFunction |
| native | go_terms:MolecularFunction |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MolecularFunction
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
  prompt.examples:
    tag: prompt.examples
    value: catalytic activity, amine binding, peptide receptor activity, oxygen carrier
      activity, structural constituent of cytoskeleton
from_schema: http://w3id.org/ontogpt/go_terms
is_a: NamedEntity
slot_usage:
  id:
    name: id
    values_from:
    - GOMolecularFunctionType
    domain_of:
    - NamedEntity
    - Publication

```
</details>

### Induced

<details>
```yaml
name: MolecularFunction
id_prefixes:
- GO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:go
  prompt.examples:
    tag: prompt.examples
    value: catalytic activity, amine binding, peptide receptor activity, oxygen carrier
      activity, structural constituent of cytoskeleton
from_schema: http://w3id.org/ontogpt/go_terms
is_a: NamedEntity
slot_usage:
  id:
    name: id
    values_from:
    - GOMolecularFunctionType
    domain_of:
    - NamedEntity
    - Publication
attributes:
  id:
    name: id
    description: A unique identifier for the named entity
    from_schema: http://w3id.org/ontogpt/go_terms
    rank: 1000
    values_from:
    - GOMolecularFunctionType
    identifier: true
    alias: id
    owner: MolecularFunction
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
    from_schema: http://w3id.org/ontogpt/go_terms
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: MolecularFunction
    domain_of:
    - NamedEntity
    range: string

```
</details>