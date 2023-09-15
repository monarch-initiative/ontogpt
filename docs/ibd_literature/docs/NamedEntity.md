
# Class: NamedEntity




URI: [ibdlit:NamedEntity](http://w3id.org/ontogpt/ibd_literature/NamedEntity)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipType],[DiseaseCellularProcessRelationship]-%20object_qualifier%200..1>[NamedEntity&#124;id:string;label:string%20%3F],[DiseaseCellularProcessRelationship]-%20subject_qualifier%200..1>[NamedEntity],[GeneExposureRelationship]-%20object_qualifier%200..1>[NamedEntity],[GeneExposureRelationship]-%20subject_qualifier%200..1>[NamedEntity],[Triple]-%20object%200..1>[NamedEntity],[Triple]-%20object_qualifier%200..1>[NamedEntity],[Triple]-%20subject%200..1>[NamedEntity],[Triple]-%20subject_qualifier%200..1>[NamedEntity],[NamedEntity]^-[RelationshipType],[NamedEntity]^-[Gene],[NamedEntity]^-[Disease],[NamedEntity]^-[ChemicalExposure],[NamedEntity]^-[CellularProcess],[Triple],[GeneExposureRelationship],[Gene],[DiseaseCellularProcessRelationship],[Disease],[ChemicalExposure],[CellularProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[RelationshipType],[DiseaseCellularProcessRelationship]-%20object_qualifier%200..1>[NamedEntity&#124;id:string;label:string%20%3F],[DiseaseCellularProcessRelationship]-%20subject_qualifier%200..1>[NamedEntity],[GeneExposureRelationship]-%20object_qualifier%200..1>[NamedEntity],[GeneExposureRelationship]-%20subject_qualifier%200..1>[NamedEntity],[Triple]-%20object%200..1>[NamedEntity],[Triple]-%20object_qualifier%200..1>[NamedEntity],[Triple]-%20subject%200..1>[NamedEntity],[Triple]-%20subject_qualifier%200..1>[NamedEntity],[NamedEntity]^-[RelationshipType],[NamedEntity]^-[Gene],[NamedEntity]^-[Disease],[NamedEntity]^-[ChemicalExposure],[NamedEntity]^-[CellularProcess],[Triple],[GeneExposureRelationship],[Gene],[DiseaseCellularProcessRelationship],[Disease],[ChemicalExposure],[CellularProcess])

## Children

 * [CellularProcess](CellularProcess.md)
 * [ChemicalExposure](ChemicalExposure.md)
 * [Disease](Disease.md)
 * [Gene](Gene.md)
 * [RelationshipType](RelationshipType.md)

## Referenced by Class

 *  **[DiseaseCellularProcessRelationship](DiseaseCellularProcessRelationship.md)** *[DiseaseCellularProcessRelationship➞object_qualifier](DiseaseCellularProcessRelationship_object_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **[DiseaseCellularProcessRelationship](DiseaseCellularProcessRelationship.md)** *[DiseaseCellularProcessRelationship➞subject_qualifier](DiseaseCellularProcessRelationship_subject_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **[GeneExposureRelationship](GeneExposureRelationship.md)** *[GeneExposureRelationship➞object_qualifier](GeneExposureRelationship_object_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
 *  **[GeneExposureRelationship](GeneExposureRelationship.md)** *[GeneExposureRelationship➞subject_qualifier](GeneExposureRelationship_subject_qualifier.md)*  <sub>0..1</sub>  **[NamedEntity](NamedEntity.md)**
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
