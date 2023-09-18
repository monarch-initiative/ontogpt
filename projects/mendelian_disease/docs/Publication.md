
# Class: Publication




URI: [mendelian_disease:Publication](http://w3id.org/ontogpt/mendelian_disease/Publication)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MendelianDisease]++-%20publications%200..*>[Publication&#124;id:string%20%3F;title:string%20%3F;abstract:string%20%3F;combined_text:string%20%3F;full_text:string%20%3F],[TextWithTriples]++-%20publication%200..1>[Publication],[TextWithTriples],[MendelianDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[MendelianDisease]++-%20publications%200..*>[Publication&#124;id:string%20%3F;title:string%20%3F;abstract:string%20%3F;combined_text:string%20%3F;full_text:string%20%3F],[TextWithTriples]++-%20publication%200..1>[Publication],[TextWithTriples],[MendelianDisease])

## Referenced by Class

 *  **None** *[➞publications](mendelianDisease__publications.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**
 *  **None** *[➞publication](textWithTriples__publication.md)*  <sub>0..1</sub>  **[Publication](Publication.md)**

## Attributes


### Own

 * [➞id](publication__id.md)  <sub>0..1</sub>
     * Description: The publication identifier
     * Range: [String](types/String.md)
 * [➞title](publication__title.md)  <sub>0..1</sub>
     * Description: The title of the publication
     * Range: [String](types/String.md)
 * [➞abstract](publication__abstract.md)  <sub>0..1</sub>
     * Description: The abstract of the publication
     * Range: [String](types/String.md)
 * [➞combined_text](publication__combined_text.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞full_text](publication__full_text.md)  <sub>0..1</sub>
     * Description: The full text of the publication
     * Range: [String](types/String.md)
