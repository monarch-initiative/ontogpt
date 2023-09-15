
# core


**metamodel version:** 1.7.0

**version:** None


Core upper level


### Classes

 * [AnnotatorResult](AnnotatorResult.md)
 * [Any](Any.md)
 * [CompoundExpression](CompoundExpression.md)
     * [Triple](Triple.md) - Abstract parent for Relation Extraction tasks
 * [ExtractionResult](ExtractionResult.md) - A result of extracting knowledge on text
 * [NamedEntity](NamedEntity.md)
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
 * [➞id](namedEntity__id.md) - A unique identifier for the named entity
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
