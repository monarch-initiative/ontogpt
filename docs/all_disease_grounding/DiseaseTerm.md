

# Class: DiseaseTerm



URI: [all_disease_grounding:DiseaseTerm](all_disease_grounding:DiseaseTerm)



```mermaid
erDiagram
DiseaseTerm {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **DiseaseTerm**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [DiseaseTermSet](DiseaseTermSet.md) | [terms](terms.md) | range | [DiseaseTerm](DiseaseTerm.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* MONDO






### Annotations

| property | value |
| --- | --- |
| annotators | bioportal:OMIM, sqlite:obo:mondo || prompt | The name of a disease, with specific subtype if provided. Examples include: neurothekoma, retinal vasculitis, chicken monocytic leukemia, neoplasm of spinal cord, moyamoya disease 3, noninsulin-dependent diabetes mellitus with deafness, Teebi hypertelorism syndrome 1, multiple pterygium syndrome escobar variant, Otopalatodigital syndrome type II, Alzheimer disease type 3 |



### Schema Source


* from schema: http://w3id.org/ontogpt/all_disease_grounding




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | all_disease_grounding:DiseaseTerm |
| native | all_disease_grounding:DiseaseTerm |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DiseaseTerm
id_prefixes:
- MONDO
annotations:
  annotators:
    tag: annotators
    value: bioportal:OMIM, sqlite:obo:mondo
  prompt:
    tag: prompt
    value: 'The name of a disease, with specific subtype if provided. Examples include:
      neurothekoma, retinal vasculitis, chicken monocytic leukemia, neoplasm of spinal
      cord, moyamoya disease 3, noninsulin-dependent diabetes mellitus with deafness,
      Teebi hypertelorism syndrome 1, multiple pterygium syndrome escobar variant,
      Otopalatodigital syndrome type II, Alzheimer disease type 3'
from_schema: http://w3id.org/ontogpt/all_disease_grounding
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: DiseaseTerm
id_prefixes:
- MONDO
annotations:
  annotators:
    tag: annotators
    value: bioportal:OMIM, sqlite:obo:mondo
  prompt:
    tag: prompt
    value: 'The name of a disease, with specific subtype if provided. Examples include:
      neurothekoma, retinal vasculitis, chicken monocytic leukemia, neoplasm of spinal
      cord, moyamoya disease 3, noninsulin-dependent diabetes mellitus with deafness,
      Teebi hypertelorism syndrome 1, multiple pterygium syndrome escobar variant,
      Otopalatodigital syndrome type II, Alzheimer disease type 3'
from_schema: http://w3id.org/ontogpt/all_disease_grounding
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
    from_schema: http://w3id.org/ontogpt/all_disease_grounding
    rank: 1000
    identifier: true
    alias: id
    owner: DiseaseTerm
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
    from_schema: http://w3id.org/ontogpt/all_disease_grounding
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: DiseaseTerm
    domain_of:
    - NamedEntity
    range: string

```
</details>