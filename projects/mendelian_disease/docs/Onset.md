
# Class: Onset




URI: [mendelian_disease:Onset](http://w3id.org/ontogpt/mendelian_disease/Onset)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[MendelianDisease]-%20disease_onsets%200..*>[Onset&#124;years_old:string%20%3F;decades:string%20*;juvenile_or_adult:string%20%3F;id(i):string;label(i):string%20%3F],[Symptom]-%20onset_of_symptom%200..1>[Onset],[NamedEntity]^-[Onset],[Symptom],[NamedEntity],[MendelianDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[MendelianDisease]-%20disease_onsets%200..*>[Onset&#124;years_old:string%20%3F;decades:string%20*;juvenile_or_adult:string%20%3F;id(i):string;label(i):string%20%3F],[Symptom]-%20onset_of_symptom%200..1>[Onset],[NamedEntity]^-[Onset],[Symptom],[NamedEntity],[MendelianDisease])

## Identifier prefixes

 * HP

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞disease_onsets](mendelianDisease__disease_onsets.md)*  <sub>0..\*</sub>  **[Onset](Onset.md)**
 *  **None** *[➞onset_of_symptom](symptom__onset_of_symptom.md)*  <sub>0..1</sub>  **[Onset](Onset.md)**

## Attributes


### Own

 * [➞years_old](onset__years_old.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [➞decades](onset__decades.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [➞juvenile_or_adult](onset__juvenile_or_adult.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
