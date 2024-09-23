

# Slot: unit


_The unit of the quantity, or N/A if not provided._



URI: [qudt:unit](qudt:unit)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantitativeValueWithFrequency](QuantitativeValueWithFrequency.md) |  |  no  |
| [QuantitativeValueWithMetric](QuantitativeValueWithMetric.md) |  |  no  |
| [QuantitativeValue](QuantitativeValue.md) |  |  no  |







## Properties

* Range: [Unit](Unit.md)





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| owl | ObjectProperty, ObjectSomeValuesFrom |



### Schema Source


* from schema: http://w3id.org/ontogpt/dietician_notes




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qudt:unit |
| native | dietitian_notes:unit |




## LinkML Source

<details>
```yaml
name: unit
annotations:
  owl:
    tag: owl
    value: ObjectProperty, ObjectSomeValuesFrom
description: The unit of the quantity, or N/A if not provided.
from_schema: http://w3id.org/ontogpt/dietician_notes
rank: 1000
slot_uri: qudt:unit
alias: unit
owner: QuantitativeValue
domain_of:
- QuantitativeValue
range: Unit

```
</details>