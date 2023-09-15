
# Class: MetabolicProcess




URI: [bp:MetabolicProcess](http://w3id.org/ontogpt/metabolic-process-templateMetabolicProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[MetabolicProcessCategory],[ChemicalEntity]<outputs%200..*-%20[MetabolicProcess&#124;label:string%20%3F;description:string%20%3F;synonyms:string%20*;id(i):string],[ChemicalEntity]<inputs%200..*-%20[MetabolicProcess],[MetabolicProcessCategory]<category%200..1-%20[MetabolicProcess],[MetabolicProcessCategory]<subclass_of%200..*-%20[MetabolicProcess],[NamedEntity]^-[MetabolicProcess],[ChemicalEntity])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[MetabolicProcessCategory],[ChemicalEntity]<outputs%200..*-%20[MetabolicProcess&#124;label:string%20%3F;description:string%20%3F;synonyms:string%20*;id(i):string],[ChemicalEntity]<inputs%200..*-%20[MetabolicProcess],[MetabolicProcessCategory]<category%200..1-%20[MetabolicProcess],[MetabolicProcessCategory]<subclass_of%200..*-%20[MetabolicProcess],[NamedEntity]^-[MetabolicProcess],[ChemicalEntity])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Attributes


### Own

 * [➞label](metabolicProcess__label.md)  <sub>0..1</sub>
     * Description: the name of the metabolic process
     * Range: [String](types/String.md)
 * [➞description](metabolicProcess__description.md)  <sub>0..1</sub>
     * Description: a textual description of the metabolic process
     * Range: [String](types/String.md)
 * [➞synonyms](metabolicProcess__synonyms.md)  <sub>0..\*</sub>
     * Description: alternative names of the metabolic process
     * Range: [String](types/String.md)
 * [➞subclass_of](metabolicProcess__subclass_of.md)  <sub>0..\*</sub>
     * Description: a semicolon separated list of broader metabolic processes which this is a subclass of
     * Range: [MetabolicProcessCategory](MetabolicProcessCategory.md)
 * [➞category](metabolicProcess__category.md)  <sub>0..1</sub>
     * Description: the category of metabolic process, e.g metabolic process, catabolic process, biosynthetic process, small molecule sensor activity
     * Range: [MetabolicProcessCategory](MetabolicProcessCategory.md)
 * [➞inputs](metabolicProcess__inputs.md)  <sub>0..\*</sub>
     * Description: the inputs of the metabolic process
     * Range: [ChemicalEntity](ChemicalEntity.md)
 * [➞outputs](metabolicProcess__outputs.md)  <sub>0..\*</sub>
     * Description: the outputs of the metabolic process
     * Range: [ChemicalEntity](ChemicalEntity.md)

### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
