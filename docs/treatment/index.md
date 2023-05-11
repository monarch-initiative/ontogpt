# MAXO treatment Template

A template for MAXO treatments

URI: http://w3id.org/ontogpt/treatment
Name: treatment-template



## Schema Diagram

```mermaid
erDiagram
DiseaseTreatmentSummary {

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

DiseaseTreatmentSummary ||--|o Disease : "disease"
DiseaseTreatmentSummary ||--}o Drug : "drugs"
DiseaseTreatmentSummary ||--}o Treatment : "treatments"
DiseaseTreatmentSummary ||--}o Treatment : "contraindications"
DiseaseTreatmentSummary ||--}o TreatmentMechanism : "treatment_mechanisms"
DiseaseTreatmentSummary ||--}o TreatmentEfficacy : "treatment_efficacies"
DiseaseTreatmentSummary ||--}o TreatmentAdverseEffect : "treatment_adverse_effects"
TreatmentAdverseEffect ||--|o Treatment : "treatment"
TreatmentAdverseEffect ||--}o AdverseEffect : "adverse_effects"
TreatmentEfficacy ||--|o Treatment : "treatment"
TreatmentMechanism ||--|o Treatment : "treatment"
TreatmentMechanism ||--|o Mechanism : "mechanism"

```


## Classes

| Class | Description |
| --- | --- |
| [AdverseEffect](AdverseEffect.md) |  |
| [AnnotatorResult](AnnotatorResult.md) |  |
| [Any](Any.md) |  |
| [CompoundExpression](CompoundExpression.md) |  |
| [Disease](Disease.md) |  |
| [DiseaseTreatmentSummary](DiseaseTreatmentSummary.md) |  |
| [Drug](Drug.md) |  |
| [ExtractionResult](ExtractionResult.md) | A result of extracting knowledge on text |
| [Gene](Gene.md) |  |
| [Mechanism](Mechanism.md) |  |
| [NamedEntity](NamedEntity.md) |  |
| [Publication](Publication.md) |  |
| [RelationshipType](RelationshipType.md) |  |
| [Symptom](Symptom.md) |  |
| [TextWithTriples](TextWithTriples.md) |  |
| [Treatment](Treatment.md) |  |
| [TreatmentAdverseEffect](TreatmentAdverseEffect.md) |  |
| [TreatmentEfficacy](TreatmentEfficacy.md) |  |
| [TreatmentMechanism](TreatmentMechanism.md) |  |
| [Triple](Triple.md) | Abstract parent for Relation Extraction tasks |


## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) | The abstract of the publication |
| [adverse_effects](adverse_effects.md) |  |
| [combined_text](combined_text.md) |  |
| [contraindications](contraindications.md) | semicolon-separated list of therapies and treatments that are contra-indicate... |
| [disease](disease.md) | the name of the disease that is treated |
| [drugs](drugs.md) | semicolon-separated list of named small molecule drugs |
| [efficacy](efficacy.md) |  |
| [extracted_object](extracted_object.md) | The complex objects extracted from the text |
| [full_text](full_text.md) | The full text of the publication |
| [id](id.md) | A unique identifier for the named entity |
| [input_id](input_id.md) |  |
| [input_text](input_text.md) |  |
| [input_title](input_title.md) |  |
| [label](label.md) | The label (name) of the named thing |
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
