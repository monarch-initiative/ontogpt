# Class: GeneSubcellularLocalizationRelationship



URI: [gocam:GeneSubcellularLocalizationRelationship](http://w3id.org/ontogpt/gocam/GeneSubcellularLocalizationRelationship)


```mermaid
erDiagram
GeneSubcellularLocalizationRelationship {

}
GeneLocation {
    string id  
    string label  
}
Gene {
    string id  
    string label  
}

GeneSubcellularLocalizationRelationship ||--|o Gene : "gene"
GeneSubcellularLocalizationRelationship ||--|o GeneLocation : "location"

```




## Inheritance
* [CompoundExpression](CompoundExpression.md)
    * **GeneSubcellularLocalizationRelationship**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [gene](gene.md) | 0..1 <br/> [String](String.md) |  | direct |
| [location](location.md) | 0..1 <br/> [GeneLocation](GeneLocation.md) |  | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IBDAnnotations](IBDAnnotations.md) | [gene_localizations](gene_localizations.md) | range | [GeneSubcellularLocalizationRelationship](GeneSubcellularLocalizationRelationship.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/gocam





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | gocam:GeneSubcellularLocalizationRelationship |
| native | gocam:GeneSubcellularLocalizationRelationship |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GeneSubcellularLocalizationRelationship
from_schema: http://w3id.org/ontogpt/gocam
rank: 1000
is_a: CompoundExpression
attributes:
  gene:
    name: gene
    from_schema: http://w3id.org/ontogpt/gocam
    range: Gene
  location:
    name: location
    from_schema: http://w3id.org/ontogpt/gocam
    rank: 1000
    range: GeneLocation

```
</details>

### Induced

<details>
```yaml
name: GeneSubcellularLocalizationRelationship
from_schema: http://w3id.org/ontogpt/gocam
rank: 1000
is_a: CompoundExpression
attributes:
  gene:
    name: gene
    from_schema: http://w3id.org/ontogpt/gocam
    alias: gene
    owner: GeneSubcellularLocalizationRelationship
    domain_of:
    - GeneOrganismRelationship
    - GeneMolecularActivityRelationship
    - GeneMolecularActivityRelationship2
    - GeneSubcellularLocalizationRelationship
    range: Gene
  location:
    name: location
    from_schema: http://w3id.org/ontogpt/gocam
    rank: 1000
    alias: location
    owner: GeneSubcellularLocalizationRelationship
    domain_of:
    - GeneSubcellularLocalizationRelationship
    range: GeneLocation

```
</details>