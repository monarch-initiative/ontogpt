# Class: AnnotatorResult



URI: [core:AnnotatorResult](http://w3id.org/ontogpt/core/AnnotatorResult)


```mermaid
 classDiagram
    class AnnotatorResult
      AnnotatorResult : object_id
      AnnotatorResult : object_text
      AnnotatorResult : subject_text
      
```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [subject_text](subject_text.md) | 0..1 <br/> NONE |  | direct |
| [object_id](object_id.md) | 0..1 <br/> NONE |  | direct |
| [object_text](object_text.md) | 0..1 <br/> NONE |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/core





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | core:AnnotatorResult |
| native | core:AnnotatorResult |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnnotatorResult
from_schema: http://w3id.org/ontogpt/core
rank: 1000
attributes:
  subject_text:
    name: subject_text
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
  object_id:
    name: object_id
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
  object_text:
    name: object_text
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000

```
</details>

### Induced

<details>
```yaml
name: AnnotatorResult
from_schema: http://w3id.org/ontogpt/core
rank: 1000
attributes:
  subject_text:
    name: subject_text
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    alias: subject_text
    owner: AnnotatorResult
    domain_of:
    - AnnotatorResult
    range: string
  object_id:
    name: object_id
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    alias: object_id
    owner: AnnotatorResult
    domain_of:
    - AnnotatorResult
    range: string
  object_text:
    name: object_text
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    alias: object_text
    owner: AnnotatorResult
    domain_of:
    - AnnotatorResult
    range: string

```
</details>