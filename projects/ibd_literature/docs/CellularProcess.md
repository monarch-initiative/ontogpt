
# Class: CellularProcess




URI: [ibdlit:CellularProcess](http://w3id.org/ontogpt/ibd_literature/CellularProcess)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[DiseaseCellularProcessRelationship],[DiseaseCellularProcessRelationship]-%20object%200..1>[CellularProcess&#124;id(i):string;label(i):string%20%3F],[IBDAnnotations]-%20cellular_process%200..*>[CellularProcess],[NamedEntity]^-[CellularProcess],[IBDAnnotations])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[DiseaseCellularProcessRelationship],[DiseaseCellularProcessRelationship]-%20object%200..1>[CellularProcess&#124;id(i):string;label(i):string%20%3F],[IBDAnnotations]-%20cellular_process%200..*>[CellularProcess],[NamedEntity]^-[CellularProcess],[IBDAnnotations])

## Identifier prefixes

 * GO

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **[DiseaseCellularProcessRelationship](DiseaseCellularProcessRelationship.md)** *[DiseaseCellularProcessRelationship➞object](DiseaseCellularProcessRelationship_object.md)*  <sub>0..1</sub>  **[CellularProcess](CellularProcess.md)**
 *  **None** *[➞cellular_process](iBDAnnotations__cellular_process.md)*  <sub>0..\*</sub>  **[CellularProcess](CellularProcess.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
