# Class: Step



URI: [recipe:Step](http://w3id.org/ontogpt/recipe/Step)


```mermaid
 classDiagram
    class Step
      CompoundExpression <|-- Step
      
      Step : action
      Step : inputs
      Step : outputs
      
```




## Inheritance
* [CompoundExpression](CompoundExpression.md)
    * **Step**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [action](action.md) | 0..1 <br/> [Action](Action.md) | the action taken in this step (e | direct |
| [inputs](inputs.md) | 0..* <br/> [FoodItem](FoodItem.md) | a semicolon separated list of the inputs of this step | direct |
| [outputs](outputs.md) | 0..* <br/> [FoodItem](FoodItem.md) | a semicolon separated list of the outputs of this step | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Recipe](Recipe.md) | [steps](steps.md) | range | [Step](Step.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/ontogpt/recipe





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | recipe:Step |
| native | recipe:Step |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Step
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
is_a: CompoundExpression
attributes:
  action:
    name: action
    description: the action taken in this step (e.g. mix, add)
    from_schema: https://w3id.org/ontogpt/recipe
    rank: 1000
    range: Action
  inputs:
    name: inputs
    description: a semicolon separated list of the inputs of this step
    from_schema: https://w3id.org/ontogpt/recipe
    rank: 1000
    multivalued: true
    range: FoodItem
  outputs:
    name: outputs
    description: a semicolon separated list of the outputs of this step
    from_schema: https://w3id.org/ontogpt/recipe
    rank: 1000
    multivalued: true
    range: FoodItem

```
</details>

### Induced

<details>
```yaml
name: Step
from_schema: https://w3id.org/ontogpt/recipe
rank: 1000
is_a: CompoundExpression
attributes:
  action:
    name: action
    description: the action taken in this step (e.g. mix, add)
    from_schema: https://w3id.org/ontogpt/recipe
    rank: 1000
    alias: action
    owner: Step
    domain_of:
    - Step
    range: Action
  inputs:
    name: inputs
    description: a semicolon separated list of the inputs of this step
    from_schema: https://w3id.org/ontogpt/recipe
    rank: 1000
    multivalued: true
    alias: inputs
    owner: Step
    domain_of:
    - Step
    range: FoodItem
  outputs:
    name: outputs
    description: a semicolon separated list of the outputs of this step
    from_schema: https://w3id.org/ontogpt/recipe
    rank: 1000
    multivalued: true
    alias: outputs
    owner: Step
    domain_of:
    - Step
    range: FoodItem

```
</details>