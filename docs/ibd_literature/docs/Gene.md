
# Class: Gene




URI: [ibdlit:Gene](http://w3id.org/ontogpt/ibd_literature/Gene)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneExposureRelationship],[GeneExposureRelationship]-%20object%200..1>[Gene&#124;id(i):string;label(i):string%20%3F],[IBDAnnotations]-%20genes%200..*>[Gene],[NamedEntity]^-[Gene],[IBDAnnotations])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneExposureRelationship],[GeneExposureRelationship]-%20object%200..1>[Gene&#124;id(i):string;label(i):string%20%3F],[IBDAnnotations]-%20genes%200..*>[Gene],[NamedEntity]^-[Gene],[IBDAnnotations])

## Identifier prefixes

 * HGNC

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **[GeneExposureRelationship](GeneExposureRelationship.md)** *[GeneExposureRelationship➞object](GeneExposureRelationship_object.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**
 *  **None** *[➞genes](iBDAnnotations__genes.md)*  <sub>0..\*</sub>  **[Gene](Gene.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
