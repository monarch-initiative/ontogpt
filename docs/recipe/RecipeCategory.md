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
| [id](id.md) | 1..1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | The label (name) of the named thing | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Recipe](Recipe.md) | [categories](categories.md) | range | [RecipeCategory](RecipeCategory.md) |






## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* dbpediaont

* FOODON

* HANCESTRO






### Annotations

| property | value |
| --- | --- |
| annotators | sqlite:obo:foodon, sqlite:obo:dbpediaont |



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
- dbpediaont
- FOODON
- HANCESTRO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:foodon, sqlite:obo:dbpediaont
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
- dbpediaont
- FOODON
- HANCESTRO
annotations:
  annotators:
    tag: annotators
    value: sqlite:obo:foodon, sqlite:obo:dbpediaont
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
    from_schema: https://w3id.org/ontogpt/recipe
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
    annotations:
      owl:
        tag: owl
        value: AnnotationProperty, AnnotationAssertion
    description: The label (name) of the named thing
    from_schema: https://w3id.org/ontogpt/recipe
    aliases:
    - name
    slot_uri: rdfs:label
    alias: label
    owner: RecipeCategory
    domain_of:
    - Recipe
    - NamedEntity
    range: string

```
</details>