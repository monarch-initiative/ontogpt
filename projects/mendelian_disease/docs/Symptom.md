
# Class: Symptom




URI: [mendelian_disease:Symptom](http://w3id.org/ontogpt/mendelian_disease/Symptom)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Onset]<onset_of_symptom%200..1-%20[Symptom&#124;characteristic:string%20%3F;affects:string%20%3F;severity:string%20%3F;id(i):string;label(i):string%20%3F],[MendelianDisease]-%20symptoms%200..*>[Symptom],[NamedEntity]^-[Symptom],[Onset],[NamedEntity],[MendelianDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[Onset]<onset_of_symptom%200..1-%20[Symptom&#124;characteristic:string%20%3F;affects:string%20%3F;severity:string%20%3F;id(i):string;label(i):string%20%3F],[MendelianDisease]-%20symptoms%200..*>[Symptom],[NamedEntity]^-[Symptom],[Onset],[NamedEntity],[MendelianDisease])

## Identifier prefixes

 * HP

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞symptoms](mendelianDisease__symptoms.md)*  <sub>0..\*</sub>  **[Symptom](Symptom.md)**

## Attributes


### Own

 * [➞characteristic](symptom__characteristic.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞affects](symptom__affects.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞severity](symptom__severity.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞onset_of_symptom](symptom__onset_of_symptom.md)  <sub>0..1</sub>
     * Range: [Onset](Onset.md)

### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
