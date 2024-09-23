

# Class: NutritionSupportMethod


_A method of nutrition support therapy used to treat or prevent malnutrition. This includes any method of feeding intended to replace or support oral feeding._





URI: [dietitian_notes:NutritionSupportMethod](dietitian_notes:NutritionSupportMethod)



```mermaid
erDiagram
NutritionSupportMethod {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **NutritionSupportMethod**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NutritionSupport](NutritionSupport.md) | [method](method.md) | range | [NutritionSupportMethod](NutritionSupportMethod.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* MAXO

* EFO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:maxo, sqlite:obo:efo, sqlite:obo:mesh || prompt.examples | enteral nutrition intake, gavage nutrition intake, parenteral nutrition intake, partial parenteral nutrition intake |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:NutritionSupportMethod |
| native | dietitian_notes:NutritionSupportMethod |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NutritionSupportMethod
id_prefixes:
- MAXO
- EFO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:maxo, sqlite:obo:efo, sqlite:obo:mesh
  prompt.examples:
    tag: prompt.examples
    value: enteral nutrition intake, gavage nutrition intake, parenteral nutrition
      intake, partial parenteral nutrition intake
description: A method of nutrition support therapy used to treat or prevent malnutrition.
  This includes any method of feeding intended to replace or support oral feeding.
from_schema: http://w3id.org/ontogpt/dietician_notes
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: NutritionSupportMethod
id_prefixes:
- MAXO
- EFO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:maxo, sqlite:obo:efo, sqlite:obo:mesh
  prompt.examples:
    tag: prompt.examples
    value: enteral nutrition intake, gavage nutrition intake, parenteral nutrition
      intake, partial parenteral nutrition intake
description: A method of nutrition support therapy used to treat or prevent malnutrition.
  This includes any method of feeding intended to replace or support oral feeding.
from_schema: http://w3id.org/ontogpt/dietician_notes
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
    from_schema: http://w3id.org/ontogpt/dietician_notes
    rank: 1000
    identifier: true
    alias: id
    owner: NutritionSupportMethod
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
    from_schema: http://w3id.org/ontogpt/dietician_notes
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: NutritionSupportMethod
    domain_of:
    - NamedEntity
    range: string

```
</details>