

# Slot: percentile


_The reported percentile of the value, as compared to a reference patient population. Always positive, on a scale from 0 to 99%. May be reported as "X%", "X%ile", or "Xth percentile", where X is the value. N/A if not provided._



URI: [dietitian_notes:percentile](dietitian_notes:percentile)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantitativeValueWithMetric](QuantitativeValueWithMetric.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:percentile |
| native | dietitian_notes:percentile |




## LinkML Source

<details>
```yaml
name: percentile
description: The reported percentile of the value, as compared to a reference patient
  population. Always positive, on a scale from 0 to 99%. May be reported as "X%",
  "X%ile", or "Xth percentile", where X is the value. N/A if not provided.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: percentile
owner: QuantitativeValueWithMetric
domain_of:
- QuantitativeValueWithMetric
range: string

```
</details>