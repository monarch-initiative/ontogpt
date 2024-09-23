

# Slot: subpanel


_a subpanel of the figure_



URI: [fig:subpanel](http://w3id.org/ontogpt/figure-templatesubpanel)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [FigureCaption](FigureCaption.md) | A caption for a figure from a scientific paper |  no  |







## Properties

* Range: [SubPanel](SubPanel.md)

* Multivalued: True





## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| prompt | a semicolon separated list of descriptions of every panel in the text. Keep the panel id and text together. for example: "1A: A side view of the foo; 1B: A frontal view of the foo" |



### Schema Source


* from schema: https://w3id.org/ontogpt/figure




## LinkML Source

<details>
```yaml
name: subpanel
annotations:
  prompt:
    tag: prompt
    value: 'a semicolon separated list of descriptions of every panel in the text.
      Keep the panel id and text together. for example: "1A: A side view of the foo;
      1B: A frontal view of the foo"'
description: a subpanel of the figure
from_schema: https://w3id.org/ontogpt/figure
rank: 1000
multivalued: true
alias: subpanel
owner: FigureCaption
domain_of:
- FigureCaption
range: SubPanel

```
</details>