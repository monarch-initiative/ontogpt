# IBD Literature Template

A template for extracting information from IBD literature

URI: http://w3id.org/ontogpt/ibd_literature

Name: ibd-literature-template



## Schema Diagram

```mermaid
erDiagram
IBDAnnotations {

}
DiseaseCellularProcessRelationship {

}
NamedEntity {
    string id  
    string label  
}
CellularProcess {
    string id  
    string label  
}
DiseaseToCellularProcessPredicate {
    string id  
    string label  
}
Disease {
    string id  
    string label  
}
GeneExposureRelationship {

}
Gene {
    string id  
    string label  
}
ChemicalExposureToGenePredicate {
    string id  
    string label  
}
ChemicalExposure {
    string id  
    string label  
}

IBDAnnotations ||--}o Gene : "genes"
IBDAnnotations ||--}o ChemicalExposure : "exposures"
IBDAnnotations ||--}o GeneExposureRelationship : "gene_exposures_relationships"
IBDAnnotations ||--}o Disease : "diseases"
IBDAnnotations ||--}o CellularProcess : "cellular_process"
IBDAnnotations ||--}o DiseaseCellularProcessRelationship : "disease_cellular_process_relationships"
DiseaseCellularProcessRelationship ||--|o Disease : "subject"
DiseaseCellularProcessRelationship ||--|o DiseaseToCellularProcessPredicate : "predicate"
DiseaseCellularProcessRelationship ||--|o CellularProcess : "object"
DiseaseCellularProcessRelationship ||--|o NamedEntity : "subject_qualifier"
DiseaseCellularProcessRelationship ||--|o NamedEntity : "object_qualifier"
GeneExposureRelationship ||--|o ChemicalExposure : "subject"
GeneExposureRelationship ||--|o ChemicalExposureToGenePredicate : "predicate"
GeneExposureRelationship ||--|o Gene : "object"
GeneExposureRelationship ||--|o NamedEntity : "subject_qualifier"
GeneExposureRelationship ||--|o NamedEntity : "object_qualifier"

```


## Classes

| Class | Description |
| --- | --- |
| [AnnotatorResult](AnnotatorResult.md) | None |
| [Any](Any.md) | None |
| [CompoundExpression](CompoundExpression.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseCellularProcessRelationship](DiseaseCellularProcessRelationship.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneExposureRelationship](GeneExposureRelationship.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Triple](Triple.md) | Abstract parent for Relation Extraction tasks |
| [ExtractionResult](ExtractionResult.md) | A result of extracting knowledge on text |
| [IBDAnnotations](IBDAnnotations.md) | None |
| [NamedEntity](NamedEntity.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellularProcess](CellularProcess.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalExposure](ChemicalExposure.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ChemicalExposureToGenePredicate](ChemicalExposureToGenePredicate.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Disease](Disease.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DiseaseToCellularProcessPredicate](DiseaseToCellularProcessPredicate.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gene](Gene.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelationshipType](RelationshipType.md) | None |
| [Publication](Publication.md) | None |
| [TextWithEntity](TextWithEntity.md) | A text containing one or more instances of a single type of entity. |
| [TextWithTriples](TextWithTriples.md) | A text containing one or more relations of the Triple type. |



## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) | The abstract of the publication |
| [cellular_process](cellular_process.md) | semicolon-separated list of cellular processes |
| [combined_text](combined_text.md) |  |
| [disease_cellular_process_relationships](disease_cellular_process_relationships.md) | semicolon-separated list of disease to cellular process relationships |
| [diseases](diseases.md) | semicolon-separated list of diseases |
| [entities](entities.md) |  |
| [exposures](exposures.md) | semicolon-separated list of exposures |
| [extracted_object](extracted_object.md) | The complex objects extracted from the text |
| [full_text](full_text.md) | The full text of the publication |
| [gene_exposures_relationships](gene_exposures_relationships.md) | semicolon-separated list of gene to molecular activity relationships |
| [genes](genes.md) | semicolon-separated list of genes |
| [id](id.md) | A unique identifier for the named entity |
| [input_id](input_id.md) |  |
| [input_text](input_text.md) |  |
| [input_title](input_title.md) |  |
| [label](label.md) | The label (name) of the named thing |
| [named_entities](named_entities.md) | Named entities extracted from the text |
| [object](object.md) | The name of the gene in the pair |
| [object_id](object_id.md) |  |
| [object_qualifier](object_qualifier.md) | An optional qualifier or modifier for the gene |
| [object_text](object_text.md) |  |
| [predicate](predicate.md) | The name of the type of relationship between a chemical exposure and a gene |
| [prompt](prompt.md) |  |
| [publication](publication.md) |  |
| [qualifier](qualifier.md) | A qualifier for the statements, e |
| [raw_completion_output](raw_completion_output.md) |  |
| [subject](subject.md) | The name of the exposure, such as a exposure to a chemical toxin |
| [subject_qualifier](subject_qualifier.md) | An optional qualifier or modifier for the chemical exposure |
| [subject_text](subject_text.md) |  |
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
