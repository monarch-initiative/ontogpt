
# class-enrichment


**metamodel version:** 1.7.0

**version:** None


A datamodel for representing the results of class enrichment on gene sets


### Classes

 * [ClassEnrichmentConfiguration](ClassEnrichmentConfiguration.md) - configuration for search
 * [ClassEnrichmentResult](ClassEnrichmentResult.md) - A single enrichment result
 * [ClassEnrichmentResultSet](ClassEnrichmentResultSet.md) - A collection of enrichemt results

### Mixins


### Slots

 * [➞p_value_cutoff](classEnrichmentConfiguration__p_value_cutoff.md) - p-value cutoff for enrichment
 * [➞results](classEnrichmentResultSet__results.md) - The enrichment results
 * [➞ancestor_of_more_informative_result](classEnrichmentResult__ancestor_of_more_informative_result.md) - This term is more general than a previously reported result
 * [➞background_count](classEnrichmentResult__background_count.md) - The background count
 * [➞background_total](classEnrichmentResult__background_total.md) - The background total
 * [➞class_id](classEnrichmentResult__class_id.md) - The class id
 * [➞class_label](classEnrichmentResult__class_label.md) - The class label
 * [➞descendant_of_more_informative_result](classEnrichmentResult__descendant_of_more_informative_result.md) - This term is more specific than a previously reported result
 * [➞false_discovery_rate](classEnrichmentResult__false_discovery_rate.md) - The false discovery rate
 * [➞fold_enrichment](classEnrichmentResult__fold_enrichment.md) - The fold enrichment
 * [➞p_value](classEnrichmentResult__p_value.md) - The p-value
 * [➞p_value_adjusted](classEnrichmentResult__p_value_adjusted.md) - The adjusted p-value
 * [➞probability](classEnrichmentResult__probability.md) - The probability, as estimated by model-based approaches
 * [➞rank](classEnrichmentResult__rank.md) - The rank of this result
 * [➞sample_count](classEnrichmentResult__sample_count.md) - The number of entities in the sample with this class
 * [➞sample_total](classEnrichmentResult__sample_total.md) - The total number of entities in the sample

### Enums

 * [SortFieldEnum](SortFieldEnum.md) - The field to sort by

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

 * [Position](types/Position.md)  ([Integer](types/Integer.md)) 
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
