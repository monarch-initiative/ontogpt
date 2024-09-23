

# Class: Instance


_What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?_





URI: [data_sheets_schema:Instance](https://w3id.org/bridge2ai/data-sheets-schema/Instance)



```mermaid
erDiagram
Instance {
    string representation  
    string instance_type  
    string data_type  
    integer counts  
    string label  
    string id  
    string name  
    string description  
}
Software {
    string version  
    string license  
    string url  
    string id  
    string name  
    string description  
}
MissingInfo {
    stringList missing  
    stringList why_missing  
    string id  
    string name  
    string description  
}
SamplingStrategy {
    stringList is_sample  
    stringList is_random  
    stringList source_data  
    stringList is_representative  
    stringList representative_verification  
    stringList why_not_representative  
    stringList strategies  
    string id  
    string name  
    string description  
}

Instance ||--}o SamplingStrategy : "sampling_strategies"
Instance ||--}o MissingInfo : "missing_information"
Instance ||--}o Software : "used_software"
MissingInfo ||--}o Software : "used_software"
SamplingStrategy ||--}o Software : "used_software"

```




## Inheritance
* [NamedThing](NamedThing.md)
    * [DatasetProperty](DatasetProperty.md)
        * **Instance**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [representation](representation.md) | 0..1 <br/> [String](String.md) |  | direct |
| [instance_type](instance_type.md) | 0..1 <br/> [String](String.md) | Are there multiple types of instances (e | direct |
| [data_type](data_type.md) | 0..1 <br/> [String](String.md) | What data does each instance consist of? “Raw” data (e | direct |
| [counts](counts.md) | 0..1 <br/> [Integer](Integer.md) | How many instances are there in total (of each type, if appropriate)? | direct |
| [label](label.md) | 0..1 <br/> [String](String.md) | Is there a label or target associated with each instance? | direct |
| [sampling_strategies](sampling_strategies.md) | * <br/> [SamplingStrategy](SamplingStrategy.md) |  | direct |
| [missing_information](missing_information.md) | * <br/> [MissingInfo](MissingInfo.md) |  | direct |
| [used_software](used_software.md) | * <br/> [Software](Software.md) | What software was used as part of this dataset property? | [DatasetProperty](DatasetProperty.md) |
| [id](id.md) | 1 <br/> [String](String.md) | the unique name of the dataset | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | human readable description of the information | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Dataset](Dataset.md) | [instances](instances.md) | range | [Instance](Instance.md) |
| [DataSubset](DataSubset.md) | [instances](instances.md) | range | [Instance](Instance.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | data_sheets_schema:Instance |
| native | data_sheets_schema:Instance |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Instance
description: What do the instances that comprise the dataset represent (e.g., documents,
  photos, people, countries)?
in_subset:
- Composition
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
is_a: DatasetProperty
attributes:
  representation:
    name: representation
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    domain_of:
    - Instance
    range: string
  instance_type:
    name: instance_type
    description: Are there multiple types of instances (e.g., movies, users, and ratings;
      people and interactions between them; nodes and edges)?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    domain_of:
    - Instance
    range: string
  data_type:
    name: data_type
    description: What data does each instance consist of? “Raw” data (e.g., unprocessed
      text or images) or features? In either case, please provide a description.
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    domain_of:
    - Instance
    range: string
  counts:
    name: counts
    description: How many instances are there in total (of each type, if appropriate)?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    domain_of:
    - Instance
    range: integer
  label:
    name: label
    description: Is there a label or target associated with each instance?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    domain_of:
    - Instance
    range: string
  sampling_strategies:
    name: sampling_strategies
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    multivalued: true
    domain_of:
    - Dataset
    - Instance
    range: SamplingStrategy
  missing_information:
    name: missing_information
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    multivalued: true
    domain_of:
    - Instance
    range: MissingInfo

```
</details>

### Induced

<details>
```yaml
name: Instance
description: What do the instances that comprise the dataset represent (e.g., documents,
  photos, people, countries)?
in_subset:
- Composition
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
is_a: DatasetProperty
attributes:
  representation:
    name: representation
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    alias: representation
    owner: Instance
    domain_of:
    - Instance
    range: string
  instance_type:
    name: instance_type
    description: Are there multiple types of instances (e.g., movies, users, and ratings;
      people and interactions between them; nodes and edges)?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    alias: instance_type
    owner: Instance
    domain_of:
    - Instance
    range: string
  data_type:
    name: data_type
    description: What data does each instance consist of? “Raw” data (e.g., unprocessed
      text or images) or features? In either case, please provide a description.
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    alias: data_type
    owner: Instance
    domain_of:
    - Instance
    range: string
  counts:
    name: counts
    description: How many instances are there in total (of each type, if appropriate)?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    alias: counts
    owner: Instance
    domain_of:
    - Instance
    range: integer
  label:
    name: label
    description: Is there a label or target associated with each instance?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    alias: label
    owner: Instance
    domain_of:
    - Instance
    range: string
  sampling_strategies:
    name: sampling_strategies
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    multivalued: true
    alias: sampling_strategies
    owner: Instance
    domain_of:
    - Dataset
    - Instance
    range: SamplingStrategy
  missing_information:
    name: missing_information
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    multivalued: true
    alias: missing_information
    owner: Instance
    domain_of:
    - Instance
    range: MissingInfo
  used_software:
    name: used_software
    description: What software was used as part of this dataset property?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    multivalued: true
    alias: used_software
    owner: Instance
    domain_of:
    - DatasetProperty
    range: Software
  id:
    name: id
    description: the unique name of the dataset
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    exact_mappings:
    - schema:name
    rank: 1000
    slot_uri: dcterms:identifier
    identifier: true
    alias: id
    owner: Instance
    domain_of:
    - NamedThing
    - Information
    range: string
    required: true
  name:
    name: name
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    slot_uri: schema:name
    alias: name
    owner: Instance
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: human readable description of the information
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    slot_uri: dcterms:description
    alias: description
    owner: Instance
    domain_of:
    - NamedThing
    - Information
    - Relationships
    - Splits
    - DataAnomaly
    - Confidentiality
    - Deidentification
    - SensitiveElement
    - InstanceAcquisition
    - CollectionMechanism
    - DataCollector
    - CollectionTimeframe
    - EthicalReview
    - DirectCollection
    - CollectionNotification
    - CollectionConsent
    - ConsentRevocation
    - DataProtectionImpact
    - PreprocessingStrategy
    - CleaningStrategy
    - LabelingStrategy
    - RawData
    - ExistingUse
    - UseRepository
    - OtherTask
    - FutureUseImpact
    - DiscouragedUse
    - ThirdPartySharing
    - DistributionFormat
    - DistributionDate
    - LicenseAndUseTerms
    - IPRestrictions
    - ExportControlRegulatoryRestrictions
    - Maintainer
    - Erratum
    - UpdatePlan
    - RetentionLimits
    - VersionAccess
    - ExtensionMechanism
    range: string

```
</details>