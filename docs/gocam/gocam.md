
# gocam-template


**metamodel version:** 1.7.0

**version:** None


A template for GO-CAMs


### Classes

 * [AnnotatorResult](AnnotatorResult.md)
 * [Any](Any.md)
 * [CompoundExpression](CompoundExpression.md)
     * [GeneGeneInteraction](GeneGeneInteraction.md)
     * [GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md)
     * [GeneMolecularActivityRelationship2](GeneMolecularActivityRelationship2.md)
     * [GeneOrganismRelationship](GeneOrganismRelationship.md)
     * [GeneSubcellularLocalizationRelationship](GeneSubcellularLocalizationRelationship.md)
     * [Triple](Triple.md) - Abstract parent for Relation Extraction tasks
 * [ExtractionResult](ExtractionResult.md) - A result of extracting knowledge on text
 * [GoCamAnnotations](GoCamAnnotations.md)
 * [NamedEntity](NamedEntity.md)
     * [CellularProcess](CellularProcess.md)
     * [Gene](Gene.md)
     * [GeneLocation](GeneLocation.md)
     * [MolecularActivity](MolecularActivity.md)
     * [Molecule](Molecule.md)
     * [Organism](Organism.md)
     * [Pathway](Pathway.md)
     * [RelationshipType](RelationshipType.md)
 * [Publication](Publication.md)
 * [TextWithTriples](TextWithTriples.md)

### Mixins


### Slots

 * [➞object_id](annotatorResult__object_id.md)
 * [➞object_text](annotatorResult__object_text.md)
 * [➞subject_text](annotatorResult__subject_text.md)
 * [➞extracted_object](extractionResult__extracted_object.md) - The complex objects extracted from the text
 * [➞input_id](extractionResult__input_id.md)
 * [➞input_text](extractionResult__input_text.md)
 * [➞input_title](extractionResult__input_title.md)
 * [➞named_entities](extractionResult__named_entities.md) - Named entities extracted from the text
 * [➞prompt](extractionResult__prompt.md)
 * [➞raw_completion_output](extractionResult__raw_completion_output.md)
 * [➞gene1](geneGeneInteraction__gene1.md)
 * [➞gene2](geneGeneInteraction__gene2.md)
 * [➞gene](geneMolecularActivityRelationship2__gene.md)
 * [➞molecular_activity](geneMolecularActivityRelationship2__molecular_activity.md)
 * [➞target](geneMolecularActivityRelationship2__target.md)
 * [➞gene](geneMolecularActivityRelationship__gene.md)
 * [➞molecular_activity](geneMolecularActivityRelationship__molecular_activity.md)
 * [➞gene](geneOrganismRelationship__gene.md)
 * [➞organism](geneOrganismRelationship__organism.md)
 * [➞gene](geneSubcellularLocalizationRelationship__gene.md)
 * [➞location](geneSubcellularLocalizationRelationship__location.md)
 * [➞activities](goCamAnnotations__activities.md) - semicolon-separated list of molecular activities
 * [➞cellular_processes](goCamAnnotations__cellular_processes.md) - semicolon-separated list of cellular processes
 * [➞gene_functions](goCamAnnotations__gene_functions.md) - semicolon-separated list of gene to molecular activity relationships
 * [➞gene_gene_interactions](goCamAnnotations__gene_gene_interactions.md) - semicolon-separated list of gene to gene interactions
 * [➞gene_localizations](goCamAnnotations__gene_localizations.md) - semicolon-separated list of genes plus their location in the cell; for example, "gene1 / cytoplasm; gene2 / mitochondrion"
 * [➞gene_organisms](goCamAnnotations__gene_organisms.md)
 * [➞genes](goCamAnnotations__genes.md) - semicolon-separated list of genes
 * [➞organisms](goCamAnnotations__organisms.md) - semicolon-separated list of organism taxons
 * [➞pathways](goCamAnnotations__pathways.md) - semicolon-separated list of pathways
 * [➞id](namedEntity__id.md) - A unique identifier for the named entity
     * [GeneLocation➞id](GeneLocation_id.md)
 * [➞label](namedEntity__label.md) - The label (name) of the named thing
 * [➞abstract](publication__abstract.md) - The abstract of the publication
 * [➞combined_text](publication__combined_text.md)
 * [➞full_text](publication__full_text.md) - The full text of the publication
 * [➞id](publication__id.md) - The publication identifier
 * [➞title](publication__title.md) - The title of the publication
 * [➞publication](textWithTriples__publication.md)
 * [➞triples](textWithTriples__triples.md)
 * [➞object](triple__object.md)
 * [➞object_qualifier](triple__object_qualifier.md) - An optional qualifier or modifier for the object of the statement, e.g. "severe" or "with additional complications"
 * [➞predicate](triple__predicate.md)
 * [➞qualifier](triple__qualifier.md) - A qualifier for the statements, e.g. "NOT" for negation
 * [➞subject](triple__subject.md)
 * [➞subject_qualifier](triple__subject_qualifier.md) - An optional qualifier or modifier for the subject of the statement, e.g. "high dose" or "intravenously administered"

### Enums

 * [CellType](CellType.md)
 * [GOCellComponentType](GOCellComponentType.md)
 * [GeneLocationEnum](GeneLocationEnum.md)
 * [NullDataOptions](NullDataOptions.md)

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
