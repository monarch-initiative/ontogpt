

# Slot: value


_The value of the quantity, or N/A if not provided._



URI: [dietitian_notes:value](dietitian_notes:value)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantitativeValueWithFrequency](QuantitativeValueWithFrequency.md) |  |  no  |
| [QuantitativeValueWithMetric](QuantitativeValueWithMetric.md) |  |  no  |
| [QuantitativeValue](QuantitativeValue.md) |  |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| owl | DataProperty, DataHasValue |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dietitian_notes:value |
| native | dietitian_notes:value |




## LinkML Source

<details>
```yaml
name: value
annotations:
  owl:
    tag: owl
    value: DataProperty, DataHasValue
description: The value of the quantity, or N/A if not provided.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
alias: value
owner: QuantitativeValue
domain_of:
- QuantitativeValue
range: string

```
</details>