# Class: MetabolicProcess



URI: [bp:MetabolicProcess](http://w3id.org/ontogpt/metabolic-process-templateMetabolicProcess)


```mermaid
erDiagram
MetabolicProcess {
    string label  
    string description  
    stringList synonyms  
    string id  
}
ChemicalEntity {
    string id  
    string label  
}
MetabolicProcessCategory {
    string id  
    string label  
}

MetabolicProcess ||--}o MetabolicProcessCategory : "subclass_of"
MetabolicProcess ||--|o MetabolicProcessCategory : "category"
MetabolicProcess ||--}o ChemicalEntity : "inputs"
MetabolicProcess ||--}o ChemicalEntity : "outputs"

```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **MetabolicProcess**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.md) | 0..1 <br/> NONE |  | direct |
| [description](description.md) | 0..1 <br/> NONE | a textual description of the metabolic process | direct |
| [synonyms](synonyms.md) | 0..* <br/> NONE | alternative names of the metabolic process | direct |
| [subclass_of](subclass_of.md) | 0..* <br/> [MetabolicProcessCategory](MetabolicProcessCategory.md) | a semicolon separated list of broader metabolic processes which this is a sub... | direct |
| [category](category.md) | 0..1 <br/> [MetabolicProcessCategory](MetabolicProcessCategory.md) | the category of metabolic process, e | direct |
| [inputs](inputs.md) | 0..* <br/> [ChemicalEntity](ChemicalEntity.md) | the inputs of the metabolic process | direct |
| [outputs](outputs.md) | 0..* <br/> [ChemicalEntity](ChemicalEntity.md) | the outputs of the metabolic process | direct |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/ontogpt/metabolic_process





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bp:MetabolicProcess |
| native | bp:MetabolicProcess |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MetabolicProcess
from_schema: https://w3id.org/ontogpt/metabolic_process
rank: 1000
is_a: NamedEntity
attributes:
  label:
    name: label
    description: the name of the metabolic process
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
  description:
    name: description
    description: a textual description of the metabolic process
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
  synonyms:
    name: synonyms
    description: alternative names of the metabolic process
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    multivalued: true
  subclass_of:
    name: subclass_of
    description: a semicolon separated list of broader metabolic processes which this
      is a subclass of
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    multivalued: true
    range: MetabolicProcessCategory
  category:
    name: category
    description: the category of metabolic process, e.g metabolic process, catabolic
      process, biosynthetic process, small molecule sensor activity
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    range: MetabolicProcessCategory
  inputs:
    name: inputs
    description: the inputs of the metabolic process
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    multivalued: true
    range: ChemicalEntity
  outputs:
    name: outputs
    description: the outputs of the metabolic process
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    multivalued: true
    range: ChemicalEntity

```
</details>

### Induced

<details>
```yaml
name: MetabolicProcess
from_schema: https://w3id.org/ontogpt/metabolic_process
rank: 1000
is_a: NamedEntity
attributes:
  label:
    name: label
    description: the name of the metabolic process
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    alias: label
    owner: MetabolicProcess
    domain_of:
    - MetabolicProcess
    - NamedEntity
    range: string
  description:
    name: description
    description: a textual description of the metabolic process
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    alias: description
    owner: MetabolicProcess
    domain_of:
    - MetabolicProcess
    range: string
  synonyms:
    name: synonyms
    description: alternative names of the metabolic process
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    multivalued: true
    alias: synonyms
    owner: MetabolicProcess
    domain_of:
    - MetabolicProcess
    range: string
  subclass_of:
    name: subclass_of
    description: a semicolon separated list of broader metabolic processes which this
      is a subclass of
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    multivalued: true
    alias: subclass_of
    owner: MetabolicProcess
    domain_of:
    - MetabolicProcess
    range: MetabolicProcessCategory
  category:
    name: category
    description: the category of metabolic process, e.g metabolic process, catabolic
      process, biosynthetic process, small molecule sensor activity
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    alias: category
    owner: MetabolicProcess
    domain_of:
    - MetabolicProcess
    range: MetabolicProcessCategory
  inputs:
    name: inputs
    description: the inputs of the metabolic process
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    multivalued: true
    alias: inputs
    owner: MetabolicProcess
    domain_of:
    - MetabolicProcess
    range: ChemicalEntity
  outputs:
    name: outputs
    description: the outputs of the metabolic process
    from_schema: https://w3id.org/ontogpt/metabolic_process
    rank: 1000
    multivalued: true
    alias: outputs
    owner: MetabolicProcess
    domain_of:
    - MetabolicProcess
    range: ChemicalEntity
  id:
    name: id
    annotations:
      prompt.skip:
        tag: prompt.skip
        value: 'true'
    description: A unique identifier for the named entity
    comments:
    - this is populated during the grounding and normalization step
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    identifier: true
    alias: id
    owner: MetabolicProcess
    domain_of:
    - NamedEntity
    - Publication
    range: string

```
</details>