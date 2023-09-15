
# Class: NamedEntity




URI: [treatment:NamedEntity](http://w3id.org/ontogpt/treatments/NamedEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Treatment],[Symptom],[RelationshipType],[Triple]-%20object%200..1>[NamedEntity&#124;id:string;label:string%20%3F],[Triple]-%20object_qualifier%200..1>[NamedEntity],[Triple]-%20subject%200..1>[NamedEntity],[Triple]-%20subject_qualifier%200..1>[NamedEntity],[NamedEntity]^-[Treatment],[NamedEntity]^-[Symptom],[NamedEntity]^-[RelationshipType],[NamedEntity]^-[Mechanism],[NamedEntity]^-[Gene],[NamedEntity]^-[Drug],[NamedEntity]^-[Disease],[NamedEntity]^-[AdverseEffect],[Triple],[Mechanism],[Gene],[Drug],[Disease],[AdverseEffect])](https://yuml.me/diagram/nofunky;dir:TB/class/[Treatment],[Symptom],[RelationshipType],[Triple]-%20object%200..1>[NamedEntity&#124;id:string;label:string%20%3F],[Triple]-%20object_qualifier%200..1>[NamedEntity],[Triple]-%20subject%200..1>[NamedEntity],[Triple]-%20subject_qualifier%200..1>[NamedEntity],[NamedEntity]^-[Treatment],[NamedEntity]^-[Symptom],[NamedEntity]^-[RelationshipType],[NamedEntity]^-[Mechanism],[NamedEntity]^-[Gene],[NamedEntity]^-[Drug],[NamedEntity]^-[Disease],[NamedEntity]^-[AdverseEffect],[Triple],[Mechanism],[Gene],[Drug],[Disease],[AdverseEffect])

## Children

 * [AdverseEffect](AdverseEffect.md)
 * [Disease](Disease.md)
 * [Drug](Drug.md)
 * [Gene](Gene.md)
 * [Mechanism](Mechanism.md)
 * [RelationshipType](RelationshipType.md)
 * [Symptom](Symptom.md)
 * [Treatment](Treatment.md)

## Referenced by Class

 *  **None** *[➞object](triple__object.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **None** *[➞object_qualifier](triple__object_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **None** *[➞subject](triple__subject.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **None** *[➞subject_qualifier](triple__subject_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**

## Attributes


### Own

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
