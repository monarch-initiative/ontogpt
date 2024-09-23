# Template for Medical Action Extraction

A template for extracting relationships relevant to the MAXO medical action ontology.

URI: http://w3id.org/ontogpt/maxo

Name: maxo



## Schema Diagram

```mermaid
erDiagram
MaxoAnnotations {

}
ActionAnnotationRelationship {

}
NamedEntity {
    string id  
    string label  
}
Disease {
    string id  
    string label  
}
Symptom {
    string id  
    string label  
}
MedicalAction {
    string id  
    string label  
}
Chemical {
    string id  
    string label  
}

MaxoAnnotations ||--|o Disease : "primary_disease"
MaxoAnnotations ||--}o MedicalAction : "medical_actions"
MaxoAnnotations ||--}o Symptom : "symptoms"
MaxoAnnotations ||--}o Chemical : "chemicals"
MaxoAnnotations ||--}o ActionAnnotationRelationship : "action_annotation_relationships"
ActionAnnotationRelationship ||--|o Chemical : "subject_extension"
ActionAnnotationRelationship ||--|o NamedEntity : "object_extension"
ActionAnnotationRelationship ||--|o MedicalAction : "subject"
ActionAnnotationRelationship ||--|o NamedEntity : "predicate"
ActionAnnotationRelationship ||--|o Symptom : "object"
ActionAnnotationRelationship ||--|o Disease : "qualifier"
ActionAnnotationRelationship ||--|o NamedEntity : "subject_qualifier"
ActionAnnotationRelationship ||--|o NamedEntity : "object_qualifier"

```


## Classes

| Class | Description |
| --- | --- |
| [AnnotatorResult](AnnotatorResult.md) | None |
| [Any](Any.md) | None |
| [CompoundExpression](CompoundExpression.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Triple](Triple.md) | Abstract parent for Relation Extraction tasks |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExtendedTriple](ExtendedTriple.md) | Abstract parent for Relation Extraction tasks, with additional support for an extension term describing some aspect of the subject and object. |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ActionAnnotationRelationship](ActionAnnotationRelationship.md) | An association representing a relationships between a disease, the mentioned signs and symptoms associated with that disease, the medical actions relating to each symptom, and the type of relationship between each action and symptom (usually TREATS or PREVENTS). |
| [ExtractionResult](ExtractionResult.md) | A result of extracting knowledge on text |
| [MaxoAnnotations](MaxoAnnotations.md) | None |
| [NamedEntity](NamedEntity.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Chemical](Chemical.md) | A substance that has a defined molecular structure and is produced by or used in a chemical process. Includes drugs used as part of medical actions. For example: corticosteroid, folic acid, opioid analgesic |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Disease](Disease.md) | A disposition to undergo pathological processes that exists in an organism because of one or more disorders in that organism. For example: Beck-Fahrner syndrome, hereditary retinoblastoma, progeria, diabetes mellitus, infectious otitis media |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MedicalAction](MedicalAction.md) | A clinically prescribed procedure, therapy, intervention, or recommendation. For example: blood transfusion, radiation therapy, cardiac catheterization, pulse oximetry, otoscopy |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelationshipType](RelationshipType.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Symptom](Symptom.md) | A condition or phenotype resulting from an abnormal health state. For example: Low serum calcitriol, hypoplasia of the thymus, chronic cough, aortic stiffness, low pulse pressure |
| [Publication](Publication.md) | None |
| [TextWithEntity](TextWithEntity.md) | A text containing one or more instances of a single type of entity. |
| [TextWithTriples](TextWithTriples.md) | A text containing one or more relations of the Triple type. |



## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) | The abstract of the publication |
| [action_annotation_relationships](action_annotation_relationships.md) | Semicolon-separated list of relationships between a disease, the mentioned si... |
| [chemicals](chemicals.md) | Semicolon-separated list of chemicals or drugs |
| [combined_text](combined_text.md) |  |
| [entities](entities.md) |  |
| [extracted_object](extracted_object.md) | The complex objects extracted from the text |
| [full_text](full_text.md) | The full text of the publication |
| [id](id.md) | A unique identifier for the named entity |
| [input_id](input_id.md) |  |
| [input_text](input_text.md) |  |
| [input_title](input_title.md) |  |
| [label](label.md) | The label (name) of the named thing |
| [medical_actions](medical_actions.md) | Semicolon-separated list of medical actions |
| [named_entities](named_entities.md) | Named entities extracted from the text |
| [object](object.md) |  |
| [object_extension](object_extension.md) | An optional term describing some specific aspect of the object, e |
| [object_id](object_id.md) |  |
| [object_qualifier](object_qualifier.md) | An optional qualifier or modifier for the object of the statement, e |
| [object_text](object_text.md) |  |
| [predicate](predicate.md) |  |
| [primary_disease](primary_disease.md) | The main disease the text is about, or its central disease topic |
| [prompt](prompt.md) |  |
| [publication](publication.md) |  |
| [qualifier](qualifier.md) | A qualifier for the statements, e |
| [raw_completion_output](raw_completion_output.md) |  |
| [subject](subject.md) |  |
| [subject_extension](subject_extension.md) | An optional term describing some specific aspect of the subject, e |
| [subject_qualifier](subject_qualifier.md) | An optional qualifier or modifier for the subject of the statement, e |
| [subject_text](subject_text.md) |  |
| [symptoms](symptoms.md) | Semicolon-separated list of signs or symptoms |
| [title](title.md) | The title of the publication |
| [triples](triples.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [NullDataOptions](NullDataOptions.md) |  |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
