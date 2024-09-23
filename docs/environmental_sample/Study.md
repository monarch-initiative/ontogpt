

# Class: Study



URI: [sample:Study](http://w3id.org/ontogpt/environmental-sample/Study)



```mermaid
erDiagram
Study {

}
Measurement {
    string value  
}
Unit {
    string id  
    string label  
}
Variable {
    string id  
    string label  
}
CausalRelationship {

}
Environment {
    string id  
    string label  
}
EnvironmentalMaterial {
    string id  
    string label  
}
Location {
    string id  
    string label  
}

Study ||--}o Location : "location"
Study ||--}o EnvironmentalMaterial : "environmental_material"
Study ||--}o Environment : "environments"
Study ||--}o CausalRelationship : "causal_relationships"
Study ||--}o Variable : "variables"
Study ||--}o Measurement : "measurements"
Measurement ||--|o Unit : "unit"
CausalRelationship ||--|o Variable : "cause"
CausalRelationship ||--|o Variable : "effect"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [location](location.md) | * <br/> [Location](Location.md) | the sites at which the study was conducted | direct |
| [environmental_material](environmental_material.md) | * <br/> [EnvironmentalMaterial](EnvironmentalMaterial.md) | the environmental material that was sampled | direct |
| [environments](environments.md) | * <br/> [Environment](Environment.md) |  | direct |
| [causal_relationships](causal_relationships.md) | * <br/> [CausalRelationship](CausalRelationship.md) |  | direct |
| [variables](variables.md) | * <br/> [Variable](Variable.md) |  | direct |
| [measurements](measurements.md) | * <br/> [Measurement](Measurement.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-sample




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | sample:Study |
| native | sample:Study |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Study
from_schema: http://w3id.org/ontogpt/environmental-sample
attributes:
  location:
    name: location
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of sites at which the study was conducted.
          Give specific place names. if you cannot find a specific place name leave
          the field as empty.
    description: the sites at which the study was conducted
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    domain_of:
    - Study
    range: Location
    multivalued: true
  environmental_material:
    name: environmental_material
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of environmental materials
    description: the environmental material that was sampled
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    domain_of:
    - Study
    range: EnvironmentalMaterial
    multivalued: true
  environments:
    name: environments
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of environment terms for the location in which
          the study was conducted
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    domain_of:
    - Study
    range: Environment
    multivalued: true
  causal_relationships:
    name: causal_relationships
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of cause-effect pairs, for example, effect
          of temperature on growth
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    domain_of:
    - Study
    range: CausalRelationship
    multivalued: true
  variables:
    name: variables
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of study variables
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    domain_of:
    - Study
    range: Variable
    multivalued: true
  measurements:
    name: measurements
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of value-measurement pairs
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    domain_of:
    - Study
    range: Measurement
    multivalued: true
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Study
from_schema: http://w3id.org/ontogpt/environmental-sample
attributes:
  location:
    name: location
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of sites at which the study was conducted.
          Give specific place names. if you cannot find a specific place name leave
          the field as empty.
    description: the sites at which the study was conducted
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    alias: location
    owner: Study
    domain_of:
    - Study
    range: Location
    multivalued: true
  environmental_material:
    name: environmental_material
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of environmental materials
    description: the environmental material that was sampled
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    alias: environmental_material
    owner: Study
    domain_of:
    - Study
    range: EnvironmentalMaterial
    multivalued: true
  environments:
    name: environments
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of environment terms for the location in which
          the study was conducted
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    alias: environments
    owner: Study
    domain_of:
    - Study
    range: Environment
    multivalued: true
  causal_relationships:
    name: causal_relationships
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of cause-effect pairs, for example, effect
          of temperature on growth
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    alias: causal_relationships
    owner: Study
    domain_of:
    - Study
    range: CausalRelationship
    multivalued: true
  variables:
    name: variables
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of study variables
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    alias: variables
    owner: Study
    domain_of:
    - Study
    range: Variable
    multivalued: true
  measurements:
    name: measurements
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of value-measurement pairs
    from_schema: http://w3id.org/ontogpt/environmental-sample
    rank: 1000
    alias: measurements
    owner: Study
    domain_of:
    - Study
    range: Measurement
    multivalued: true
tree_root: true

```
</details>