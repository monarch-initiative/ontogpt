

# Class: DatasetProperty


_Represents a single property of a dataset, or a set of related properties._





URI: [data_sheets_schema:DatasetProperty](https://w3id.org/bridge2ai/data-sheets-schema/DatasetProperty)



```mermaid
erDiagram
DatasetProperty {
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

DatasetProperty ||--}o Software : "used_software"

```




## Inheritance
* [NamedThing](NamedThing.md)
    * **DatasetProperty**
        * [Purpose](Purpose.md)
        * [Task](Task.md)
        * [AddressingGap](AddressingGap.md)
        * [Creator](Creator.md)
        * [FundingMechanism](FundingMechanism.md)
        * [Instance](Instance.md)
        * [SamplingStrategy](SamplingStrategy.md)
        * [MissingInfo](MissingInfo.md)
        * [Relationships](Relationships.md)
        * [Splits](Splits.md)
        * [DataAnomaly](DataAnomaly.md)
        * [ExternalResource](ExternalResource.md)
        * [Confidentiality](Confidentiality.md)
        * [ContentWarning](ContentWarning.md)
        * [Subpopulation](Subpopulation.md)
        * [Deidentification](Deidentification.md)
        * [SensitiveElement](SensitiveElement.md)
        * [InstanceAcquisition](InstanceAcquisition.md)
        * [CollectionMechanism](CollectionMechanism.md)
        * [DataCollector](DataCollector.md)
        * [CollectionTimeframe](CollectionTimeframe.md)
        * [EthicalReview](EthicalReview.md)
        * [DirectCollection](DirectCollection.md)
        * [CollectionNotification](CollectionNotification.md)
        * [CollectionConsent](CollectionConsent.md)
        * [ConsentRevocation](ConsentRevocation.md)
        * [DataProtectionImpact](DataProtectionImpact.md)
        * [PreprocessingStrategy](PreprocessingStrategy.md)
        * [CleaningStrategy](CleaningStrategy.md)
        * [LabelingStrategy](LabelingStrategy.md)
        * [RawData](RawData.md)
        * [ExistingUse](ExistingUse.md)
        * [UseRepository](UseRepository.md)
        * [OtherTask](OtherTask.md)
        * [FutureUseImpact](FutureUseImpact.md)
        * [DiscouragedUse](DiscouragedUse.md)
        * [ThirdPartySharing](ThirdPartySharing.md)
        * [DistributionFormat](DistributionFormat.md)
        * [DistributionDate](DistributionDate.md)
        * [LicenseAndUseTerms](LicenseAndUseTerms.md)
        * [IPRestrictions](IPRestrictions.md)
        * [ExportControlRegulatoryRestrictions](ExportControlRegulatoryRestrictions.md)
        * [Maintainer](Maintainer.md)
        * [Erratum](Erratum.md)
        * [UpdatePlan](UpdatePlan.md)
        * [RetentionLimits](RetentionLimits.md)
        * [VersionAccess](VersionAccess.md)
        * [ExtensionMechanism](ExtensionMechanism.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [used_software](used_software.md) | * <br/> [Software](Software.md) | What software was used as part of this dataset property? | direct |
| [id](id.md) | 1 <br/> [String](String.md) | the unique name of the dataset | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | human readable description of the information | [NamedThing](NamedThing.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | data_sheets_schema:DatasetProperty |
| native | data_sheets_schema:DatasetProperty |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DatasetProperty
description: Represents a single property of a dataset, or a set of related properties.
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
is_a: NamedThing
attributes:
  used_software:
    name: used_software
    description: What software was used as part of this dataset property?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    multivalued: true
    domain_of:
    - DatasetProperty
    range: Software

```
</details>

### Induced

<details>
```yaml
name: DatasetProperty
description: Represents a single property of a dataset, or a set of related properties.
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
is_a: NamedThing
attributes:
  used_software:
    name: used_software
    description: What software was used as part of this dataset property?
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    multivalued: true
    alias: used_software
    owner: DatasetProperty
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
    owner: DatasetProperty
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
    owner: DatasetProperty
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
    owner: DatasetProperty
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