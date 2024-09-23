

# Class: ClassEnrichmentResultSet


_A collection of enrichemt results_





URI: [ontoenrich:ClassEnrichmentResultSet](https://w3id.org/oak/class-enrichment/ClassEnrichmentResultSet)



```mermaid
erDiagram
ClassEnrichmentResultSet {

}
ClassEnrichmentResult {
    uriorcurie class_id  
    string class_label  
    integer rank  
    float p_value  
    float p_value_adjusted  
    float false_discovery_rate  
    float fold_enrichment  
    float probability  
    integer sample_count  
    integer sample_total  
    integer background_count  
    integer background_total  
    boolean ancestor_of_more_informative_result  
    boolean descendant_of_more_informative_result  
}

ClassEnrichmentResultSet ||--}o ClassEnrichmentResult : "results"

```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [results](results.md) | * <br/> [ClassEnrichmentResult](ClassEnrichmentResult.md) | The enrichment results | direct |









## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/oak/class-enrichment





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ontoenrich:ClassEnrichmentResultSet |
| native | ontoenrich:ClassEnrichmentResultSet |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ClassEnrichmentResultSet
description: A collection of enrichemt results
from_schema: https://w3id.org/oak/class-enrichment
attributes:
  results:
    name: results
    description: The enrichment results
    from_schema: https://w3id.org/oak/class-enrichment
    rank: 1000
    multivalued: true
    domain_of:
    - ClassEnrichmentResultSet
    range: ClassEnrichmentResult

```
</details>

### Induced

<details>
```yaml
name: ClassEnrichmentResultSet
description: A collection of enrichemt results
from_schema: https://w3id.org/oak/class-enrichment
attributes:
  results:
    name: results
    description: The enrichment results
    from_schema: https://w3id.org/oak/class-enrichment
    rank: 1000
    multivalued: true
    alias: results
    owner: ClassEnrichmentResultSet
    domain_of:
    - ClassEnrichmentResultSet
    range: ClassEnrichmentResult

```
</details>