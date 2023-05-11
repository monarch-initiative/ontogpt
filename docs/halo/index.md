# Ontology Class Template

A template for Ontology Classes

URI: https://w3id.org/ontogpt/halo
Name: ontology-class



## Schema Diagram

```mermaid
erDiagram
Ontology {

}
OntologyElement {
    string name  
    string context  
    string description  
    stringList synonyms  
    string equivalent_to  
}
Category {
    string name  
    string context  
    string description  
    stringList synonyms  
    string equivalent_to  
}
Any {

}
ExtractionResult {
    string input_id  
    string input_title  
    string input_text  
    string raw_completion_output  
    string prompt  
}
NamedEntity {
    string id  
    string label  
}
CompoundExpression {

}
Triple {
    string qualifier  
}
TextWithTriples {

}
RelationshipType {
    string id  
    string label  
}
Publication {
    string id  
    string title  
    string abstract  
    string combined_text  
    string full_text  
}
AnnotatorResult {
    string subject_text  
    string object_id  
    string object_text  
}

Ontology ||--}o OntologyElement : "elements"
OntologyElement ||--}o Category : "categories"
OntologyElement ||--}o OntologyElement : "subclass_of"
OntologyElement ||--}o OntologyElement : "part_of"
OntologyElement ||--}o OntologyElement : "subtypes"
OntologyElement ||--}o OntologyElement : "parts"
Category ||--}o Category : "categories"
Category ||--}o OntologyElement : "subclass_of"
Category ||--}o OntologyElement : "part_of"
Category ||--}o OntologyElement : "subtypes"
Category ||--}o OntologyElement : "parts"
ExtractionResult ||--|o Any : "extracted_object"
ExtractionResult ||--}o Any : "named_entities"
Triple ||--|o NamedEntity : "subject"
Triple ||--|o RelationshipType : "predicate"
Triple ||--|o NamedEntity : "object"
Triple ||--|o NamedEntity : "subject_qualifier"
Triple ||--|o NamedEntity : "object_qualifier"
TextWithTriples ||--|o Publication : "publication"
TextWithTriples ||--}o Triple : "triples"

```


## Classes

| Class | Description |
| --- | --- |
| [AnnotatorResult](AnnotatorResult.md) |  |
| [Any](Any.md) |  |
| [Category](Category.md) |  |
| [CompoundExpression](CompoundExpression.md) |  |
| [ExtractionResult](ExtractionResult.md) | A result of extracting knowledge on text |
| [NamedEntity](NamedEntity.md) |  |
| [Ontology](Ontology.md) |  |
| [OntologyElement](OntologyElement.md) |  |
| [Publication](Publication.md) |  |
| [RelationshipType](RelationshipType.md) |  |
| [TextWithTriples](TextWithTriples.md) |  |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |


## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) | The abstract of the publication |
| [categories](categories.md) | a list of the categories to which this entity belongs |
| [combined_text](combined_text.md) |  |
| [context](context.md) | the ontology to which this belongs (single-valued) |
| [description](description.md) | a textual description of the entity (single-valued) |
| [elements](elements.md) |  |
| [equivalent_to](equivalent_to.md) | an OWL class expression with the necessary and sufficient conditions for this... |
| [extracted_object](extracted_object.md) | The complex objects extracted from the text |
| [full_text](full_text.md) | The full text of the publication |
| [id](id.md) | A unique identifier for the named entity |
| [input_id](input_id.md) |  |
| [input_text](input_text.md) |  |
| [input_title](input_title.md) |  |
| [label](label.md) | The label (name) of the named thing |
| [name](name.md) | the name of the entity |
| [named_entities](named_entities.md) | Named entities extracted from the text |
| [object](object.md) |  |
| [object_id](object_id.md) |  |
| [object_qualifier](object_qualifier.md) | An optional qualifier or modifier for the object of the statement, e |
| [object_text](object_text.md) |  |
| [part_of](part_of.md) | a list of things this element is part of |
| [parts](parts.md) | a list of names of things this element has as parts (components) |
| [predicate](predicate.md) |  |
| [prompt](prompt.md) |  |
| [publication](publication.md) |  |
| [qualifier](qualifier.md) | A qualifier for the statements, e |
| [raw_completion_output](raw_completion_output.md) |  |
| [subclass_of](subclass_of.md) | a list of parent class (superclasses) of this entity |
| [subject](subject.md) |  |
| [subject_qualifier](subject_qualifier.md) | An optional qualifier or modifier for the subject of the statement, e |
| [subject_text](subject_text.md) |  |
| [subtypes](subtypes.md) | a list of child classes (subclasses) of this entity |
| [synonyms](synonyms.md) | a list of alternative names of the entity |
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
