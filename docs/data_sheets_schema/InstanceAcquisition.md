

# Class: InstanceAcquisition


_How was the data associated with each instance acquired? Was the data directly observable (e.g., raw text, movie ratings), reported by subjects (e.g., survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)? If the data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified?_





URI: [data_sheets_schema:InstanceAcquisition](https://w3id.org/bridge2ai/data-sheets-schema/InstanceAcquisition)



```mermaid
erDiagram
InstanceAcquisition {
    stringList description  
    string was_directly_observed  
    string was_reported_by_subjects  
    string was_inferred_derived  
    string was_validated_verified  
    string id  
    string name  
}
Software {
    string version  
    string license  
    string url  
    string id  
    string name  
    string description  
}

InstanceAcquisition ||--}o Software : "used_software"

```




## Inheritance
* [NamedThing](NamedThing.md)
    * [DatasetProperty](DatasetProperty.md)
        * **InstanceAcquisition**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [description](description.md) | * <br/> [String](String.md) |  | direct |
| [was_directly_observed](was_directly_observed.md) | 0..1 <br/> [String](String.md) | Was the data directly observable (e | direct |
| [was_reported_by_subjects](was_reported_by_subjects.md) | 0..1 <br/> [String](String.md) | Was the data reported by subjects (e | direct |
| [was_inferred_derived](was_inferred_derived.md) | 0..1 <br/> [String](String.md) | Was the data indirectly inferred/derived from other data (e | direct |
| [was_validated_verified](was_validated_verified.md) | 0..1 <br/> [String](String.md) | Was the data validated/verified? | direct |
| [used_software](used_software.md) | * <br/> [Software](Software.md) | What software was used as part of this dataset property? | [DatasetProperty](DatasetProperty.md) |
| [id](id.md) | 1 <br/> [String](String.md) | the unique name of the dataset | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Dataset](Dataset.md) | [acquisition_methods](acquisition_methods.md) | range | [InstanceAcquisition](InstanceAcquisition.md) |
| [DataSubset](DataSubset.md) | [acquisition_methods](acquisition_methods.md) | range | [InstanceAcquisition](InstanceAcquisition.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | data_sheets_schema:InstanceAcquisition |
| native | data_sheets_schema:InstanceAcquisition |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InstanceAcquisition
description: How was the data associated with each instance acquired? Was the data
  directly observable (e.g., raw text, movie ratings), reported by subjects (e.g.,
  survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech
  tags, model-based guesses for age or language)? If the data was reported by subjects
  or indirectly inferred/derived from other data, was the data validated/verified?
in_subset:
- Collection
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
is_a: DatasetProperty
attributes:
  description:
    name: description
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    multivalued: true
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
  was_directly_observed:
    name: was_directly_observed
    description: Was the data directly observable (e.g., raw text, movie ratings)?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    domain_of:
    - InstanceAcquisition
    range: string
  was_reported_by_subjects:
    name: was_reported_by_subjects
    description: Was the data reported by subjects (e.g., survey responses)?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    domain_of:
    - InstanceAcquisition
    range: string
  was_inferred_derived:
    name: was_inferred_derived
    description: Was the data indirectly inferred/derived from other data (e.g., part-of-speech
      tags, model-based guesses for age or language)?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    domain_of:
    - InstanceAcquisition
    range: string
  was_validated_verified:
    name: was_validated_verified
    description: Was the data validated/verified?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    domain_of:
    - InstanceAcquisition
    range: string

```
</details>

### Induced

<details>
```yaml
name: InstanceAcquisition
description: How was the data associated with each instance acquired? Was the data
  directly observable (e.g., raw text, movie ratings), reported by subjects (e.g.,
  survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech
  tags, model-based guesses for age or language)? If the data was reported by subjects
  or indirectly inferred/derived from other data, was the data validated/verified?
in_subset:
- Collection
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
is_a: DatasetProperty
attributes:
  description:
    name: description
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    multivalued: true
    alias: description
    owner: InstanceAcquisition
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
  was_directly_observed:
    name: was_directly_observed
    description: Was the data directly observable (e.g., raw text, movie ratings)?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    alias: was_directly_observed
    owner: InstanceAcquisition
    domain_of:
    - InstanceAcquisition
    range: string
  was_reported_by_subjects:
    name: was_reported_by_subjects
    description: Was the data reported by subjects (e.g., survey responses)?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    alias: was_reported_by_subjects
    owner: InstanceAcquisition
    domain_of:
    - InstanceAcquisition
    range: string
  was_inferred_derived:
    name: was_inferred_derived
    description: Was the data indirectly inferred/derived from other data (e.g., part-of-speech
      tags, model-based guesses for age or language)?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    alias: was_inferred_derived
    owner: InstanceAcquisition
    domain_of:
    - InstanceAcquisition
    range: string
  was_validated_verified:
    name: was_validated_verified
    description: Was the data validated/verified?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    alias: was_validated_verified
    owner: InstanceAcquisition
    domain_of:
    - InstanceAcquisition
    range: string
  used_software:
    name: used_software
    description: What software was used as part of this dataset property?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    multivalued: true
    alias: used_software
    owner: InstanceAcquisition
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
    owner: InstanceAcquisition
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
    owner: InstanceAcquisition
    domain_of:
    - NamedThing
    range: string

```
</details>