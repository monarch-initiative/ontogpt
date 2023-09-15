
# Class: ChemicalExposure




URI: [ibdlit:ChemicalExposure](http://w3id.org/ontogpt/ibd_literature/ChemicalExposure)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneExposureRelationship],[GeneExposureRelationship]-%20subject%200..1>[ChemicalExposure&#124;id(i):string;label(i):string%20%3F],[IBDAnnotations]-%20exposures%200..*>[ChemicalExposure],[NamedEntity]^-[ChemicalExposure],[IBDAnnotations])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneExposureRelationship],[GeneExposureRelationship]-%20subject%200..1>[ChemicalExposure&#124;id(i):string;label(i):string%20%3F],[IBDAnnotations]-%20exposures%200..*>[ChemicalExposure],[NamedEntity]^-[ChemicalExposure],[IBDAnnotations])

## Identifier prefixes

 * CHEBI
 * ECTO
 * ExO
 * NCIT

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **[GeneExposureRelationship](GeneExposureRelationship.md)** *[GeneExposureRelationship➞subject](GeneExposureRelationship_subject.md)*  <sub>0..1</sub>  **[ChemicalExposure](ChemicalExposure.md)**
 *  **None** *[➞exposures](iBDAnnotations__exposures.md)*  <sub>0..\*</sub>  **[ChemicalExposure](ChemicalExposure.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
