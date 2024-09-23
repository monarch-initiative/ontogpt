# Class: Ingredient



URI: [coffee:Ingredient](http://w3id.org/ontogpt/coffee/Ingredient)



```mermaid
erDiagram
Ingredient {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **Ingredient**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Beverage](Beverage.md) | [ingredients](ingredients.md) | range | [Ingredient](Ingredient.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* FOODON






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:foodon |



### Schema Source


* from schema: http://w3id.org/ontogpt/coffee





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | coffee:Ingredient |
| native | coffee:Ingredient |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Ingredient
id_prefixes:
- FOODON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:foodon
from_schema: http://w3id.org/ontogpt/coffee
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: Ingredient
id_prefixes:
- FOODON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:foodon
from_schema: http://w3id.org/ontogpt/coffee
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
    from_schema: http://w3id.org/ontogpt/coffee
    rank: 1000
    identifier: true
    alias: id
    owner: Ingredient
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
    from_schema: http://w3id.org/ontogpt/coffee
    aliases:
    - name
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: Ingredient
    domain_of:
    - NamedEntity
    range: string

```
</details>