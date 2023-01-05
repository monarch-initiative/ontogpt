# Class: FoodItem



URI: [recipe:FoodItem](http://w3id.org/ontogpt/recipe/FoodItem)


```mermaid
erDiagram
FoodItem {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **FoodItem**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Ingredient](Ingredient.md) | [food_item](food_item.md) | range | [FoodItem](FoodItem.md) |
| [Step](Step.md) | [inputs](inputs.md) | range | [FoodItem](FoodItem.md) |
| [Step](Step.md) | [outputs](outputs.md) | range | [FoodItem](FoodItem.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* FOODON






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:foodon |



### Schema Source


* from schema: https://w3id.org/ontogpt/recipe





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | recipe:FoodItem |
| native | recipe:FoodItem |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FoodItem
id_prefixes:
- FOODON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:foodon
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
is_a: NamedEntity

```
</details>

### Induced

<details>
```yaml
name: FoodItem
id_prefixes:
- FOODON
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:foodon
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
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
    from_schema: http://w3id.org/ontogpt/core
    rank: 1000
    identifier: true
    alias: id
    owner: FoodItem
    domain_of:
    - NamedEntity
    - Publication
    range: string
  label:
    name: label
    description: The label (name) of the named thing
    from_schema: http://w3id.org/ontogpt/core
    aliases:
    - name
    alias: label
    owner: FoodItem
    domain_of:
    - Recipe
    - NamedEntity
    range: string

```
</details>