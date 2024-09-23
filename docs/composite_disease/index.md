# Composite Disease

A template for representing composite disease concepts

URI: http://w3id.org/ontogpt/composite_disease

Name: composite_disease



## Schema Diagram

```mermaid
erDiagram
CompositeDisease {

}
TreatmentAdverseEffect {

}
AdverseEffect {
    string id  
    string label  
}
Treatment {
    string id  
    string label  
}
TreatmentEfficacy {
    string efficacy  
}
TreatmentMechanism {

}
Mechanism {
    string id  
    string label  
}
Drug {
    string id  
    string label  
}
Disease {
    string id  
    string label  
}

CompositeDisease ||--|o Disease : "main_disease"
CompositeDisease ||--}o Drug : "drugs"
CompositeDisease ||--}o Treatment : "treatments"
CompositeDisease ||--}o Treatment : "contraindications"
CompositeDisease ||--}o TreatmentMechanism : "treatment_mechanisms"
CompositeDisease ||--}o TreatmentEfficacy : "treatment_efficacies"
CompositeDisease ||--}o TreatmentAdverseEffect : "treatment_adverse_effects"
TreatmentAdverseEffect ||--|o Treatment : "treatment"
TreatmentAdverseEffect ||--}o AdverseEffect : "adverse_effects"
TreatmentEfficacy ||--|o Treatment : "treatment"
TreatmentMechanism ||--|o Treatment : "treatment"
TreatmentMechanism ||--|o Mechanism : "mechanism"

```


## Classes

| Class | Description |
| --- | --- |
| [AnnotatorResult](AnnotatorResult.md) | None |
| [Any](Any.md) | None |
| [CompositeDisease](CompositeDisease.md) | None |
| [CompoundExpression](CompoundExpression.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TreatmentAdverseEffect](TreatmentAdverseEffect.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TreatmentEfficacy](TreatmentEfficacy.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TreatmentMechanism](TreatmentMechanism.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Triple](Triple.md) | Abstract parent for Relation Extraction tasks |
| [ExtractionResult](ExtractionResult.md) | A result of extracting knowledge on text |
| [NamedEntity](NamedEntity.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AdverseEffect](AdverseEffect.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Disease](Disease.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Drug](Drug.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gene](Gene.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Mechanism](Mechanism.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelationshipType](RelationshipType.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Symptom](Symptom.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Treatment](Treatment.md) | None |
| [Publication](Publication.md) | None |
| [TextWithEntity](TextWithEntity.md) | A text containing one or more instances of a single type of entity. |
| [TextWithTriples](TextWithTriples.md) | A text containing one or more relations of the Triple type. |



## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) | The abstract of the publication |
| [adverse_effects](adverse_effects.md) |  |
| [combined_text](combined_text.md) |  |
| [contraindications](contraindications.md) | semicolon-separated list of therapies and treatments that are contra-indicate... |
| [drugs](drugs.md) | semicolon-separated list of named small molecule drugs |
| [efficacy](efficacy.md) |  |
| [entities](entities.md) |  |
| [extracted_object](extracted_object.md) | The complex objects extracted from the text |
| [full_text](full_text.md) | The full text of the publication |
| [id](id.md) | A unique identifier for the named entity |
| [input_id](input_id.md) |  |
| [input_text](input_text.md) |  |
| [input_title](input_title.md) |  |
| [label](label.md) | The label (name) of the named thing |
| [main_disease](main_disease.md) | the name of the disease that is treated |
| [mechanism](mechanism.md) |  |
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
| [subject](subject.md) |  |
| [subject_qualifier](subject_qualifier.md) | An optional qualifier or modifier for the subject of the statement, e |
| [subject_text](subject_text.md) |  |
| [title](title.md) | The title of the publication |
| [treatment](treatment.md) |  |
| [treatment_adverse_effects](treatment_adverse_effects.md) | semicolon-separated list of treatment to adverse effect associations, e |
| [treatment_efficacies](treatment_efficacies.md) | semicolon-separated list of treatment to efficacy associations, e |
| [treatment_mechanisms](treatment_mechanisms.md) | semicolon-separated list of treatment to asterisk-separated mechanism associa... |
| [treatments](treatments.md) | semicolon-separated list of therapies and treatments are indicated for treati... |
| [triples](triples.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CHEBIDrugType](CHEBIDrugType.md) |  |
| [MAXOActionType](MAXOActionType.md) |  |
| [MESHTherapeuticType](MESHTherapeuticType.md) |  |
| [NCITDrugType](NCITDrugType.md) |  |
| [NCITTActivityType](NCITTActivityType.md) |  |
| [NCITTreatmentType](NCITTreatmentType.md) |  |
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
