

# Class: HumanPhenotype



URI: [human_phenotype:HumanPhenotype](http://w3id.org/ontogpt/human_phenotypeHumanPhenotype)



```mermaid
erDiagram
HumanPhenotype {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **HumanPhenotype**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [HumanPhenotypeSet](HumanPhenotypeSet.md) | [phenotypes](phenotypes.md) | range | [HumanPhenotype](HumanPhenotype.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* HP






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:hp, sqlite:obo:mondo, sqlite:obo:mesh, sqlite:obo:ncit || prompt | the name of a human phenotype or symptom.
 Examples are ascites, fever, pain, seizure, increased intracranial
 pressure, lactic acidosis. |



### Schema Source


* from schema: http://w3id.org/ontogpt/human_phenotype





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | human_phenotype:HumanPhenotype |
| native | human_phenotype:HumanPhenotype |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HumanPhenotype
id_prefixes:
- HP
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hp, sqlite:obo:mondo, sqlite:obo:mesh, sqlite:obo:ncit
  prompt:
    tag: prompt
    value: "the name of a human phenotype or symptom.\n Examples are ascites, fever,\
      \ pain, seizure, increased intracranial\n pressure, lactic acidosis."
from_schema: http://w3id.org/ontogpt/human_phenotype
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: HumanPhenotype
id_prefixes:
- HP
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:hp, sqlite:obo:mondo, sqlite:obo:mesh, sqlite:obo:ncit
  prompt:
    tag: prompt
    value: "the name of a human phenotype or symptom.\n Examples are ascites, fever,\
      \ pain, seizure, increased intracranial\n pressure, lactic acidosis."
from_schema: http://w3id.org/ontogpt/human_phenotype
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
    from_schema: http://w3id.org/ontogpt/human_phenotype
    rank: 1000
    identifier: true
    alias: id
    owner: HumanPhenotype
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
    from_schema: http://w3id.org/ontogpt/human_phenotype
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: HumanPhenotype
    domain_of:
    - NamedEntity
    range: string

```
</details>