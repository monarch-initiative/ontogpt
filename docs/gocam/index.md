# GO-CAM Template

A template for GO-CAMs

URI: http://w3id.org/ontogpt/gocam

Name: gocam-template



## Schema Diagram

```mermaid
erDiagram
GoCamAnnotations {

}
GeneSubcellularLocalizationRelationship {

}
GeneLocation {
    string id  
    string label  
}
Gene {
    string id  
    string label  
}
GeneGeneInteraction {

}
Pathway {
    string id  
    string label  
}
CellularProcess {
    string id  
    string label  
}
GeneMolecularActivityRelationship {

}
MolecularActivity {
    string id  
    string label  
}
GeneOrganismRelationship {

}
Organism {
    string id  
    string label  
}

GoCamAnnotations ||--}o Gene : "genes"
GoCamAnnotations ||--}o Organism : "organisms"
GoCamAnnotations ||--}o GeneOrganismRelationship : "gene_organisms"
GoCamAnnotations ||--}o MolecularActivity : "activities"
GoCamAnnotations ||--}o GeneMolecularActivityRelationship : "gene_functions"
GoCamAnnotations ||--}o CellularProcess : "cellular_processes"
GoCamAnnotations ||--}o Pathway : "pathways"
GoCamAnnotations ||--}o GeneGeneInteraction : "gene_gene_interactions"
GoCamAnnotations ||--}o GeneSubcellularLocalizationRelationship : "gene_localizations"
GeneSubcellularLocalizationRelationship ||--|o Gene : "gene"
GeneSubcellularLocalizationRelationship ||--|o GeneLocation : "location"
GeneGeneInteraction ||--|o Gene : "gene1"
GeneGeneInteraction ||--|o Gene : "gene2"
GeneMolecularActivityRelationship ||--|o Gene : "gene"
GeneMolecularActivityRelationship ||--|o MolecularActivity : "molecular_activity"
GeneOrganismRelationship ||--|o Gene : "gene"
GeneOrganismRelationship ||--|o Organism : "organism"

```


## Classes

| Class | Description |
| --- | --- |
| [AnnotatorResult](AnnotatorResult.md) | None |
| [Any](Any.md) | None |
| [CompoundExpression](CompoundExpression.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneGeneInteraction](GeneGeneInteraction.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneMolecularActivityRelationship2](GeneMolecularActivityRelationship2.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneOrganismRelationship](GeneOrganismRelationship.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneSubcellularLocalizationRelationship](GeneSubcellularLocalizationRelationship.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Triple](Triple.md) | Abstract parent for Relation Extraction tasks |
| [ExtractionResult](ExtractionResult.md) | A result of extracting knowledge on text |
| [GoCamAnnotations](GoCamAnnotations.md) | None |
| [NamedEntity](NamedEntity.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CellularProcess](CellularProcess.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Gene](Gene.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeneLocation](GeneLocation.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MolecularActivity](MolecularActivity.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Molecule](Molecule.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Organism](Organism.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Pathway](Pathway.md) | None |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RelationshipType](RelationshipType.md) | None |
| [Publication](Publication.md) | None |
| [TextWithEntity](TextWithEntity.md) | A text containing one or more instances of a single type of entity. |
| [TextWithTriples](TextWithTriples.md) | A text containing one or more relations of the Triple type. |



## Slots

| Slot | Description |
| --- | --- |
| [abstract](abstract.md) | The abstract of the publication |
| [activities](activities.md) | semicolon-separated list of molecular activities |
| [cellular_processes](cellular_processes.md) | semicolon-separated list of cellular processes |
| [combined_text](combined_text.md) |  |
| [entities](entities.md) |  |
| [extracted_object](extracted_object.md) | The complex objects extracted from the text |
| [full_text](full_text.md) | The full text of the publication |
| [gene](gene.md) |  |
| [gene1](gene1.md) |  |
| [gene2](gene2.md) |  |
| [gene_functions](gene_functions.md) | semicolon-separated list of gene to molecular activity relationships |
| [gene_gene_interactions](gene_gene_interactions.md) | semicolon-separated list of gene to gene interactions |
| [gene_localizations](gene_localizations.md) | semicolon-separated list of genes plus their location in the cell; for exampl... |
| [gene_organisms](gene_organisms.md) |  |
| [genes](genes.md) | semicolon-separated list of genes |
| [id](id.md) | A unique identifier for the named entity |
| [input_id](input_id.md) |  |
| [input_text](input_text.md) |  |
| [input_title](input_title.md) |  |
| [label](label.md) | The label (name) of the named thing |
| [location](location.md) |  |
| [molecular_activity](molecular_activity.md) |  |
| [named_entities](named_entities.md) | Named entities extracted from the text |
| [object](object.md) |  |
| [object_id](object_id.md) |  |
| [object_qualifier](object_qualifier.md) | An optional qualifier or modifier for the object of the statement, e |
| [object_text](object_text.md) |  |
| [organism](organism.md) |  |
| [organisms](organisms.md) | semicolon-separated list of organism taxons |
| [pathways](pathways.md) | semicolon-separated list of pathways |
| [predicate](predicate.md) |  |
| [prompt](prompt.md) |  |
| [publication](publication.md) |  |
| [qualifier](qualifier.md) | A qualifier for the statements, e |
| [raw_completion_output](raw_completion_output.md) |  |
| [subject](subject.md) |  |
| [subject_qualifier](subject_qualifier.md) | An optional qualifier or modifier for the subject of the statement, e |
| [subject_text](subject_text.md) |  |
| [target](target.md) |  |
| [title](title.md) | The title of the publication |
| [triples](triples.md) |  |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CellType](CellType.md) |  |
| [GeneLocationEnum](GeneLocationEnum.md) |  |
| [GOCellComponentType](GOCellComponentType.md) |  |
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
