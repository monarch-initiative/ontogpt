
# Class: ExtractionResult


A result of extracting knowledge on text

URI: [phenotype:ExtractionResult](http://w3id.org/ontogpt/phenotype/ExtractionResult)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Any]<named_entities%200..*-++[ExtractionResult&#124;input_id:string%20%3F;input_title:string%20%3F;input_text:string%20%3F;raw_completion_output:string%20%3F;prompt:string%20%3F],[Any]<extracted_object%200..1-++[ExtractionResult],[Any])](https://yuml.me/diagram/nofunky;dir:TB/class/[Any]<named_entities%200..*-++[ExtractionResult&#124;input_id:string%20%3F;input_title:string%20%3F;input_text:string%20%3F;raw_completion_output:string%20%3F;prompt:string%20%3F],[Any]<extracted_object%200..1-++[ExtractionResult],[Any])

## Attributes


### Own

 * [➞input_id](extractionResult__input_id.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞input_title](extractionResult__input_title.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞input_text](extractionResult__input_text.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞raw_completion_output](extractionResult__raw_completion_output.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞prompt](extractionResult__prompt.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞extracted_object](extractionResult__extracted_object.md)  <sub>0..1</sub>
     * Description: The complex objects extracted from the text
     * Range: [Any](Any.md)
 * [➞named_entities](extractionResult__named_entities.md)  <sub>0..\*</sub>
     * Description: Named entities extracted from the text
     * Range: [Any](Any.md)
