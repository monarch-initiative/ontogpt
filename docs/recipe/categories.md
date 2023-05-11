# Slot: categories
_a semicolon separated list of the categories to which this recipe belongs_


URI: [dcterms:subject](http://purl.org/dc/terms/subject)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[Recipe](Recipe.md) | 






## Properties

* Range: [RecipeCategory](RecipeCategory.md)
* Multivalued: True








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| owl | AnnotationAssertion |



### Schema Source


* from schema: https://w3id.org/ontogpt/recipe




## LinkML Source

<details>
```yaml
name: categories
annotations:
  owl:
    tag: owl
    value: AnnotationAssertion
description: a semicolon separated list of the categories to which this recipe belongs
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
slot_uri: dcterms:subject
multivalued: true
alias: categories
owner: Recipe
domain_of:
- Recipe
range: RecipeCategory

```
</details>