# GO-CAM Template

A template for GO-CAMs

URI: http://w3id.org/ontogpt/mendelian_disease
Name: mendelian_disease-template



## Schema Diagram

```mermaid
erDiagram
MendelianDisease {
    string name  
    string description  
    stringList synonyms  
    string id  
    string label  
}
DiseaseCategory {
    string id  
    string label  
}
Gene {
    string id  
    string label  
}
Symptom {
    string characteristic  
    string affects  
    string severity  
    string id  
    string label  
}
Onset {
    string years_old  
    stringList decades  
    string juvenile_or_adult  
    string id  
    string label  
}
Inheritance {
    string id  
    string label  
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

MendelianDisease ||--}o DiseaseCategory : "subclass_of"
MendelianDisease ||--}o Symptom : "symptoms"
MendelianDisease ||--|o Inheritance : "inheritance"
MendelianDisease ||--}o Gene : "genes"
MendelianDisease ||--}o Onset : "disease_onsets"
MendelianDisease ||--}o Publication : "publications"
Symptom ||--|o Onset : "onset_of_symptom"
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
| [CompoundExpression](CompoundExpression.md) |  |
| [DiseaseCategory](DiseaseCategory.md) |  |
| [ExtractionResult](ExtractionResult.md) | A result of extracting knowledge on text |
| [Gene](Gene.md) |  |
| [Inheritance](Inheritance.md) |  |
| [MendelianDisease](MendelianDisease.md) |  |
| [NamedEntity](NamedEntity.md) |  |
| [Onset](Onset.md) |  |
| [Publication](Publication.md) |  |
| [RelationshipType](RelationshipType.md) |  |
| [Symptom](Symptom.md) |  |
| [TextWithTriples](TextWithTriples.md) |  |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |


## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) | The abstract of the publication |
| [affects](affects.md) |  |
| [characteristic](characteristic.md) |  |
| [combined_text](combined_text.md) |  |
| [decades](decades.md) |  |
| [description](description.md) | a description of the disease |
| [disease_onsets](disease_onsets.md) |  |
| [extracted_object](extracted_object.md) | The complex objects extracted from the text |
| [full_text](full_text.md) | The full text of the publication |
| [genes](genes.md) |  |
| [id](id.md) | A unique identifier for the named entity |
| [inheritance](inheritance.md) |  |
| [input_id](input_id.md) |  |
| [input_text](input_text.md) |  |
| [input_title](input_title.md) |  |
| [juvenile_or_adult](juvenile_or_adult.md) |  |
| [label](label.md) | The label (name) of the named thing |
| [name](name.md) | the name of the disease |
| [named_entities](named_entities.md) | Named entities extracted from the text |
| [object](object.md) |  |
| [object_id](object_id.md) |  |
| [object_qualifier](object_qualifier.md) | An optional qualifier or modifier for the object of the statement, e |
| [object_text](object_text.md) |  |
| [onset_of_symptom](onset_of_symptom.md) |  |
| [predicate](predicate.md) |  |
| [prompt](prompt.md) |  |
| [publication](publication.md) |  |
| [publications](publications.md) |  |
| [qualifier](qualifier.md) | A qualifier for the statements, e |
| [raw_completion_output](raw_completion_output.md) |  |
| [severity](severity.md) |  |
| [subclass_of](subclass_of.md) |  |
| [subject](subject.md) |  |
| [subject_qualifier](subject_qualifier.md) | An optional qualifier or modifier for the subject of the statement, e |
| [subject_text](subject_text.md) |  |
| [symptoms](symptoms.md) |  |
| [synonyms](synonyms.md) |  |
| [title](title.md) | The title of the publication |
| [triples](triples.md) |  |
| [years_old](years_old.md) |  |


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
