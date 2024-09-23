

# Class: Dataset



URI: [envmd:Dataset](http://w3id.org/ontogpt/environmental-metadataDataset)



```mermaid
erDiagram
Dataset {
    string packageid  
}
Method {
    string id  
    string label  
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
Topic {
    string id  
    string label  
}

Dataset ||--}o Topic : "topic"
Dataset ||--}o Location : "location"
Dataset ||--}o EnvironmentalMaterial : "environmental_material"
Dataset ||--}o Environment : "environments"
Dataset ||--}o Method : "methods"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [packageid](packageid.md) | 0..1 <br/> [String](String.md) | The internal identifier for the dataset | direct |
| [topic](topic.md) | * <br/> [Topic](Topic.md) | the general scientific area of study concerning the sample(s) | direct |
| [location](location.md) | * <br/> [Location](Location.md) | the geographic location where the sample was isolated | direct |
| [environmental_material](environmental_material.md) | * <br/> [EnvironmentalMaterial](EnvironmentalMaterial.md) | the environmental material that was sampled | direct |
| [environments](environments.md) | * <br/> [Environment](Environment.md) | the environmental context in which the study was conducted | direct |
| [methods](methods.md) | * <br/> [Method](Method.md) |  | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/environmental-metadata





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | envmd:Dataset |
| native | envmd:Dataset |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Dataset
from_schema: http://w3id.org/ontogpt/environmental-metadata
attributes:
  packageid:
    name: packageid
    annotations:
      prompt:
        tag: prompt
        value: single unique identifier for the dataset
    description: The internal identifier for the dataset
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: false
    domain_of:
    - Dataset
    range: string
  topic:
    name: topic
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of scientific areas of study concerning the
          sample(s)
    description: the general scientific area of study concerning the sample(s)
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: true
    domain_of:
    - Dataset
    range: Topic
  location:
    name: location
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of geographic locations of sample isolations
    description: the geographic location where the sample was isolated
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: true
    domain_of:
    - Dataset
    range: Location
  environmental_material:
    name: environmental_material
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of environmental materials
    description: the environmental material that was sampled
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: true
    domain_of:
    - Dataset
    range: EnvironmentalMaterial
  environments:
    name: environments
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of environmental contexts in which the study
          was conducted
    description: the environmental context in which the study was conducted
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: true
    domain_of:
    - Dataset
    range: Environment
  methods:
    name: methods
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of methods used in measuring sample variables
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: true
    domain_of:
    - Dataset
    range: Method
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: Dataset
from_schema: http://w3id.org/ontogpt/environmental-metadata
attributes:
  packageid:
    name: packageid
    annotations:
      prompt:
        tag: prompt
        value: single unique identifier for the dataset
    description: The internal identifier for the dataset
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: false
    alias: packageid
    owner: Dataset
    domain_of:
    - Dataset
    range: string
  topic:
    name: topic
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of scientific areas of study concerning the
          sample(s)
    description: the general scientific area of study concerning the sample(s)
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: true
    alias: topic
    owner: Dataset
    domain_of:
    - Dataset
    range: Topic
  location:
    name: location
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of geographic locations of sample isolations
    description: the geographic location where the sample was isolated
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: true
    alias: location
    owner: Dataset
    domain_of:
    - Dataset
    range: Location
  environmental_material:
    name: environmental_material
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of environmental materials
    description: the environmental material that was sampled
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: true
    alias: environmental_material
    owner: Dataset
    domain_of:
    - Dataset
    range: EnvironmentalMaterial
  environments:
    name: environments
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of environmental contexts in which the study
          was conducted
    description: the environmental context in which the study was conducted
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: true
    alias: environments
    owner: Dataset
    domain_of:
    - Dataset
    range: Environment
  methods:
    name: methods
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of methods used in measuring sample variables
    from_schema: http://w3id.org/ontogpt/environmental-metadata
    rank: 1000
    multivalued: true
    alias: methods
    owner: Dataset
    domain_of:
    - Dataset
    range: Method
tree_root: true

```
</details>