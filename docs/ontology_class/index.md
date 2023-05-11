# Ontology Class Template

A template for Ontology Classes

URI: https://w3id.org/ontogpt/ontology_class
Name: ontology-class



## Schema Diagram

```mermaid
erDiagram
OntologyClass {
    string label  
    string description  
    stringList synonyms  
    string id  
}
LogicalDefinition {

}
Relation {
    string id  
    string label  
}

OntologyClass ||--}o OntologyClass : "categories"
OntologyClass ||--}o OntologyClass : "subclass_of"
OntologyClass ||--|o LogicalDefinition : "logical_definition"
LogicalDefinition ||--}o OntologyClass : "genus"
LogicalDefinition ||--|o Relation : "differentiating_characteristic_relationship"
LogicalDefinition ||--}o OntologyClass : "differentiating_characteristic_parents"

```


## Classes

| Class | Description |
| --- | --- |
| [AnnotatorResult](AnnotatorResult.md) |  |
| [Any](Any.md) |  |
| [CompoundExpression](CompoundExpression.md) |  |
| [ExtractionResult](ExtractionResult.md) | A result of extracting knowledge on text |
| [LogicalDefinition](LogicalDefinition.md) |  |
| [NamedEntity](NamedEntity.md) |  |
| [OntologyClass](OntologyClass.md) |  |
| [Publication](Publication.md) |  |
| [Relation](Relation.md) |  |
| [RelationshipType](RelationshipType.md) |  |
| [TextWithTriples](TextWithTriples.md) |  |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |


## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) | The abstract of the publication |
| [categories](categories.md) | the categories to which this entity belongs |
| [combined_text](combined_text.md) |  |
| [description](description.md) | a textual description of the entity |
| [differentiating_characteristic_parents](differentiating_characteristic_parents.md) |  |
| [differentiating_characteristic_relationship](differentiating_characteristic_relationship.md) |  |
| [extracted_object](extracted_object.md) | The complex objects extracted from the text |
| [full_text](full_text.md) | The full text of the publication |
| [genus](genus.md) |  |
| [id](id.md) | A unique identifier for the named entity |
| [input_id](input_id.md) |  |
| [input_text](input_text.md) |  |
| [input_title](input_title.md) |  |
| [label](label.md) | the name of the main entity being defined |
| [logical_definition](logical_definition.md) | the necessary and sufficient conditions for this entity to be an instance of ... |
| [named_entities](named_entities.md) | Named entities extracted from the text |
| [object](object.md) |  |
| [object_id](object_id.md) |  |
| [object_qualifier](object_qualifier.md) | An optional qualifier or modifier for the object of the statement, e |
| [object_text](object_text.md) |  |
| [predicate](predicate.md) |  |
| [prompt](prompt.md) |  |
| [publication](publication.md) |  |
| [qualifier](qualifier.md) | A qualifier for the statements, e |
| [raw_completion_output](raw_completion_output.md) |  |
| [subclass_of](subclass_of.md) |  |
| [subject](subject.md) |  |
| [subject_qualifier](subject_qualifier.md) | An optional qualifier or modifier for the subject of the statement, e |
| [subject_text](subject_text.md) |  |
| [synonyms](synonyms.md) | alternative names of the entity |
| [title](title.md) | The title of the publication |
| [triples](triples.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
