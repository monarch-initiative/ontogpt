

# Class: CellType



URI: [kidney:CellType](http://w3id.org/ontogpt/kidney-templateCellType)



```mermaid
erDiagram
CellType {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **CellType**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [KidneyAnnotations](KidneyAnnotations.md) | [cell_type](cell_type.md) | range | [CellType](CellType.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* CL

* UBERON






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:cl, sqlite:obo:uberon || prompt.examples | tubule epithelial cell, macula densa cell, glomerular endothelial cell,
podocyte, mesangial cell, parietal epithelial cell
 |



### Schema Source


* from schema: https://w3id.org/ontogpt/biological_process





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | kidney:CellType |
| native | kidney:CellType |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellType
id_prefixes:
- CL
- UBERON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:cl, sqlite:obo:uberon
  prompt.examples:
    tag: prompt.examples
    value: 'tubule epithelial cell, macula densa cell, glomerular endothelial cell,

      podocyte, mesangial cell, parietal epithelial cell

      '
from_schema: https://w3id.org/ontogpt/biological_process
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: CellType
id_prefixes:
- CL
- UBERON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:cl, sqlite:obo:uberon
  prompt.examples:
    tag: prompt.examples
    value: 'tubule epithelial cell, macula densa cell, glomerular endothelial cell,

      podocyte, mesangial cell, parietal epithelial cell

      '
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
    owner: CellType
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
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: CellType
    domain_of:
    - NamedEntity
    range: string

```
</details>