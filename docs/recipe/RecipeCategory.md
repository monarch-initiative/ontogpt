# Class: RecipeCategory



URI: [recipe:RecipeCategory](http://w3id.org/ontogpt/recipe/RecipeCategory)


```mermaid
erDiagram
RecipeCategory {
    string id  
    string label  
}



```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **RecipeCategory**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |
| [id](id.md) | 0..1 <br/> NONE |  | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Recipe](Recipe.md) | [category](category.md) | range | [RecipeCategory](RecipeCategory.md) |






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
| self | recipe:RecipeCategory |
| native | recipe:RecipeCategory |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RecipeCategory
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
name: RecipeCategory
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
    owner: RecipeCategory
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
    owner: RecipeCategory
    domain_of:
    - Recipe
    - NamedEntity
    range: string

```
</details>