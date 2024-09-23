

# Class: Publication



URI: [diag:Publication](http://w3id.org/ontogpt/diagnostic_procedure/Publication)



```mermaid
erDiagram
Publication {
    string id  
    string title  
    string abstract  
    string combined_text  
    string full_text  
}



```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> [String](String.md) | The publication identifier | direct |
| [title](title.md) | 0..1 <br/> [String](String.md) | The title of the publication | direct |
| [abstract](abstract.md) | 0..1 <br/> [String](String.md) | The abstract of the publication | direct |
| [combined_text](combined_text.md) | 0..1 <br/> [String](String.md) |  | direct |
| [full_text](full_text.md) | 0..1 <br/> [String](String.md) | The full text of the publication | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TextWithTriples](TextWithTriples.md) | [publication](publication.md) | range | [Publication](Publication.md) |
| [TextWithEntity](TextWithEntity.md) | [publication](publication.md) | range | [Publication](Publication.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/diagnostic_procedure




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | diag:Publication |
| native | diag:Publication |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Publication
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
attributes:
  id:
    name: id
    description: The publication identifier
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    domain_of:
    - NamedEntity
    - Publication
  title:
    name: title
    description: The title of the publication
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    domain_of:
    - Publication
  abstract:
    name: abstract
    description: The abstract of the publication
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    domain_of:
    - Publication
  combined_text:
    name: combined_text
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    domain_of:
    - Publication
  full_text:
    name: full_text
    description: The full text of the publication
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    domain_of:
    - Publication

```
</details>

### Induced

<details>
```yaml
name: Publication
from_schema: http://w3id.org/ontogpt/diagnostic_procedure
attributes:
  id:
    name: id
    description: The publication identifier
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    alias: id
    owner: Publication
    domain_of:
    - NamedEntity
    - Publication
    range: string
  title:
    name: title
    description: The title of the publication
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: title
    owner: Publication
    domain_of:
    - Publication
    range: string
  abstract:
    name: abstract
    description: The abstract of the publication
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: abstract
    owner: Publication
    domain_of:
    - Publication
    range: string
  combined_text:
    name: combined_text
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: combined_text
    owner: Publication
    domain_of:
    - Publication
    range: string
  full_text:
    name: full_text
    description: The full text of the publication
    from_schema: http://w3id.org/ontogpt/diagnostic_procedure
    rank: 1000
    alias: full_text
    owner: Publication
    domain_of:
    - Publication
    range: string

```
</details>