

# Slot: sections


_A semicolon-separated list of full sections of the document, including the full text of that section alone, beginning with the major division of the document, such as ABSTRACT, INTRODUCTION, METHODS, RESULTS, DISCUSSION, CONCLUSIONS, or a similar heading used by the text. The text should include the section title. If semicolons are present in the section text, they must be replaced with (SEMICOLON) to avoid parsing errors. A single phrase or ID is not a section. Do not format in Markdown._



URI: [alzrd:sections](http://w3id.org/ontogpt/alzrd_sectionsections)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Document](Document.md) |  |  no  |







## Properties

* Range: [DocumentSection](DocumentSection.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/alzrd_section




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | alzrd:sections |
| native | alzrd:sections |




## LinkML Source

<details>
```yaml
name: sections
description: A semicolon-separated list of full sections of the document, including
  the full text of that section alone, beginning with the major division of the document,
  such as ABSTRACT, INTRODUCTION, METHODS, RESULTS, DISCUSSION, CONCLUSIONS, or a
  similar heading used by the text. The text should include the section title. If
  semicolons are present in the section text, they must be replaced with (SEMICOLON)
  to avoid parsing errors. A single phrase or ID is not a section. Do not format in
  Markdown.
from_schema: http://w3id.org/ontogpt/alzrd_section
rank: 1000
alias: sections
owner: Document
domain_of:
- Document
range: DocumentSection
multivalued: true

```
</details>