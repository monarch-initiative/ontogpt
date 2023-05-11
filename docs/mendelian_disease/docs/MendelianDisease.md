
# Class: MendelianDisease




URI: [mendelian_disease:MendelianDisease](http://w3id.org/ontogpt/mendelian_disease/MendelianDisease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Symptom],[Publication],[Onset],[NamedEntity],[Publication]<publications%200..*-++[MendelianDisease&#124;name:string%20%3F;description:string%20%3F;synonyms:string%20*;id(i):string;label(i):string%20%3F],[Onset]<disease_onsets%200..*-%20[MendelianDisease],[Gene]<genes%200..*-%20[MendelianDisease],[Inheritance]<inheritance%200..1-%20[MendelianDisease],[Symptom]<symptoms%200..*-%20[MendelianDisease],[DiseaseCategory]<subclass_of%200..*-%20[MendelianDisease],[NamedEntity]^-[MendelianDisease],[Inheritance],[Gene],[DiseaseCategory])](https://yuml.me/diagram/nofunky;dir:TB/class/[Symptom],[Publication],[Onset],[NamedEntity],[Publication]<publications%200..*-++[MendelianDisease&#124;name:string%20%3F;description:string%20%3F;synonyms:string%20*;id(i):string;label(i):string%20%3F],[Onset]<disease_onsets%200..*-%20[MendelianDisease],[Gene]<genes%200..*-%20[MendelianDisease],[Inheritance]<inheritance%200..1-%20[MendelianDisease],[Symptom]<symptoms%200..*-%20[MendelianDisease],[DiseaseCategory]<subclass_of%200..*-%20[MendelianDisease],[NamedEntity]^-[MendelianDisease],[Inheritance],[Gene],[DiseaseCategory])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Attributes


### Own

 * [➞name](mendelianDisease__name.md)  <sub>0..1</sub>
     * Description: the name of the disease
     * Range: [String](types/String.md)
     * Example: peroxisome biogenesis disorder None
 * [➞description](mendelianDisease__description.md)  <sub>0..1</sub>
     * Description: a description of the disease
     * Range: [String](types/String.md)
     * Example: Peroxisome biogenesis disorders, Zellweger syndrome spectrum (PBD-ZSS) is a group of autosomal recessive disorders affecting the formation of functional peroxisomes, characterized by sensorineural hearing loss, pigmentary retinal degeneration, multiple organ dysfunction and psychomotor impairment None
 * [➞synonyms](mendelianDisease__synonyms.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
     * Example: Zellweger syndrome spectrum None
     * Example: PBD-ZSS None
 * [➞subclass_of](mendelianDisease__subclass_of.md)  <sub>0..\*</sub>
     * Range: [DiseaseCategory](DiseaseCategory.md)
     * Example: lysosomal disease None
     * Example: autosomal recessive disorder None
 * [➞symptoms](mendelianDisease__symptoms.md)  <sub>0..\*</sub>
     * Range: [Symptom](Symptom.md)
     * Example: sensorineural hearing loss None
     * Example: pigmentary retinal degeneration None
 * [➞inheritance](mendelianDisease__inheritance.md)  <sub>0..1</sub>
     * Range: [Inheritance](Inheritance.md)
     * Example: autosomal recessive None
 * [➞genes](mendelianDisease__genes.md)  <sub>0..\*</sub>
     * Range: [Gene](Gene.md)
     * Example: PEX1 None
     * Example: PEX2 None
     * Example: PEX3 None
 * [➞disease_onsets](mendelianDisease__disease_onsets.md)  <sub>0..\*</sub>
     * Range: [Onset](Onset.md)
 * [➞publications](mendelianDisease__publications.md)  <sub>0..\*</sub>
     * Range: [Publication](Publication.md)

### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
