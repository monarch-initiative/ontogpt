

# Class: Grantor


_What is the name and/or identifier of the organization providing monetary support or other resources supporting creation of the dataset?_





URI: [data_sheets_schema:Grantor](https://w3id.org/bridge2ai/data-sheets-schema/Grantor)



```mermaid
erDiagram
Grantor {
    string email  
    ror_identifier ror_id  
    wikidata_identifier wikidata_id  
    string id  
    string name  
    string description  
}



```




## Inheritance
* [NamedThing](NamedThing.md)
    * [Organization](Organization.md)
        * **Grantor**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [email](email.md) | 0..1 <br/> [String](String.md) | The email address of the organization | [Organization](Organization.md) |
| [ror_id](ror_id.md) | 0..1 <br/> [RorIdentifier](RorIdentifier.md) | Unique ROR identifier | [Organization](Organization.md) |
| [wikidata_id](wikidata_id.md) | 0..1 <br/> [WikidataIdentifier](WikidataIdentifier.md) | Unique Wikidata identifier | [Organization](Organization.md) |
| [id](id.md) | 1 <br/> [String](String.md) | the unique name of the dataset | [NamedThing](NamedThing.md) |
| [name](name.md) | 0..1 <br/> [String](String.md) |  | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | human readable description of the information | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [FundingMechanism](FundingMechanism.md) | [grantor](grantor.md) | range | [Grantor](Grantor.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/bridge2ai/data-sheets-schema





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | data_sheets_schema:Grantor |
| native | data_sheets_schema:Grantor |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Grantor
description: What is the name and/or identifier of the organization providing monetary
  support or other resources supporting creation of the dataset?
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
is_a: Organization

```
</details>

### Induced

<details>
```yaml
name: Grantor
description: What is the name and/or identifier of the organization providing monetary
  support or other resources supporting creation of the dataset?
from_schema: https://w3id.org/bridge2ai/data-sheets-schema
is_a: Organization
attributes:
  email:
    name: email
    description: The email address of the organization.
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    alias: email
    owner: Grantor
    domain_of:
    - Person
    - Organization
    range: string
  ror_id:
    name: ror_id
    description: Unique ROR identifier.
    examples:
    - value: ROR:02mp31p96
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    values_from:
    - ROR
    alias: ror_id
    owner: Grantor
    domain_of:
    - Organization
    range: ror_identifier
  wikidata_id:
    name: wikidata_id
    description: Unique Wikidata identifier.
    examples:
    - value: WIKIDATA:Q282186
    from_schema: https://w3id.org/bridge2ai/data-sheets-schema
    rank: 1000
    values_from:
    - WIKIDATA
    alias: wikidata_id
    owner: Grantor
    domain_of:
    - Organization
    range: wikidata_identifier
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
    owner: Grantor
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
    owner: Grantor
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
    owner: Grantor
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