
# Class: ClassEnrichmentResult


A single enrichment result

URI: [ontoenrich:ClassEnrichmentResult](https://w3id.org/oak/class-enrichment/ClassEnrichmentResult)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ClassEnrichmentResultSet]++-%20results%200..*>[ClassEnrichmentResult&#124;class_id:uriorcurie;class_label:string%20%3F;rank:integer%20%3F;p_value:float;p_value_adjusted:float%20%3F;false_discovery_rate:float%20%3F;fold_enrichment:float%20%3F;probability:float%20%3F;sample_count:integer%20%3F;sample_total:integer%20%3F;background_count:integer%20%3F;background_total:integer%20%3F;ancestor_of_more_informative_result:boolean%20%3F;descendant_of_more_informative_result:boolean%20%3F],[ClassEnrichmentResultSet])](https://yuml.me/diagram/nofunky;dir:TB/class/[ClassEnrichmentResultSet]++-%20results%200..*>[ClassEnrichmentResult&#124;class_id:uriorcurie;class_label:string%20%3F;rank:integer%20%3F;p_value:float;p_value_adjusted:float%20%3F;false_discovery_rate:float%20%3F;fold_enrichment:float%20%3F;probability:float%20%3F;sample_count:integer%20%3F;sample_total:integer%20%3F;background_count:integer%20%3F;background_total:integer%20%3F;ancestor_of_more_informative_result:boolean%20%3F;descendant_of_more_informative_result:boolean%20%3F],[ClassEnrichmentResultSet])

## Referenced by Class

 *  **None** *[➞results](classEnrichmentResultSet__results.md)*  <sub>0..\*</sub>  **[ClassEnrichmentResult](ClassEnrichmentResult.md)**

## Attributes


### Own

 * [➞class_id](classEnrichmentResult__class_id.md)  <sub>1..1</sub>
     * Description: The class id
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [➞class_label](classEnrichmentResult__class_label.md)  <sub>0..1</sub>
     * Description: The class label
     * Range: [String](types/String.md)
 * [➞rank](classEnrichmentResult__rank.md)  <sub>0..1</sub>
     * Description: The rank of this result
     * Range: [Integer](types/Integer.md)
 * [➞p_value](classEnrichmentResult__p_value.md)  <sub>1..1</sub>
     * Description: The p-value
     * Range: [Float](types/Float.md)
 * [➞p_value_adjusted](classEnrichmentResult__p_value_adjusted.md)  <sub>0..1</sub>
     * Description: The adjusted p-value
     * Range: [Float](types/Float.md)
 * [➞false_discovery_rate](classEnrichmentResult__false_discovery_rate.md)  <sub>0..1</sub>
     * Description: The false discovery rate
     * Range: [Float](types/Float.md)
 * [➞fold_enrichment](classEnrichmentResult__fold_enrichment.md)  <sub>0..1</sub>
     * Description: The fold enrichment
     * Range: [Float](types/Float.md)
 * [➞probability](classEnrichmentResult__probability.md)  <sub>0..1</sub>
     * Description: The probability, as estimated by model-based approaches
     * Range: [Float](types/Float.md)
 * [➞sample_count](classEnrichmentResult__sample_count.md)  <sub>0..1</sub>
     * Description: The number of entities in the sample with this class
     * Range: [Integer](types/Integer.md)
 * [➞sample_total](classEnrichmentResult__sample_total.md)  <sub>0..1</sub>
     * Description: The total number of entities in the sample
     * Range: [Integer](types/Integer.md)
 * [➞background_count](classEnrichmentResult__background_count.md)  <sub>0..1</sub>
     * Description: The background count
     * Range: [Integer](types/Integer.md)
 * [➞background_total](classEnrichmentResult__background_total.md)  <sub>0..1</sub>
     * Description: The background total
     * Range: [Integer](types/Integer.md)
 * [➞ancestor_of_more_informative_result](classEnrichmentResult__ancestor_of_more_informative_result.md)  <sub>0..1</sub>
     * Description: This term is more general than a previously reported result
     * Range: [Boolean](types/Boolean.md)
 * [➞descendant_of_more_informative_result](classEnrichmentResult__descendant_of_more_informative_result.md)  <sub>0..1</sub>
     * Description: This term is more specific than a previously reported result
     * Range: [Boolean](types/Boolean.md)
