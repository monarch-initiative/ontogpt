

# Slot: fatal_result_summary


_Identify similarities among errors in the report with the category of FATAL. What is similar about these errors? Do they include many of the same prefixes or namespaces? If the same patterns or rules are violated, what are they? Separate each summary with a semicolons. If no errors are present, this field should be NONE._



URI: [error_analysis:fatal_result_summary](http://w3id.org/ontogpt/error_analysisfatal_result_summary)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ValidationReport](ValidationReport.md) | A report object containing one or more validation errors or notifications |  no  |







## Properties

* Range: [String](String.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/error_analysis




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | error_analysis:fatal_result_summary |
| native | error_analysis:fatal_result_summary |




## LinkML Source

<details>
```yaml
name: fatal_result_summary
description: Identify similarities among errors in the report with the category of
  FATAL. What is similar about these errors? Do they include many of the same prefixes
  or namespaces? If the same patterns or rules are violated, what are they? Separate
  each summary with a semicolons. If no errors are present, this field should be NONE.
from_schema: http://w3id.org/ontogpt/error_analysis
rank: 1000
alias: fatal_result_summary
owner: ValidationReport
domain_of:
- ValidationReport
range: string
multivalued: true

```
</details>