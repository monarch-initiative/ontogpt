
# Class: RelationshipType




URI: [ibdlit:RelationshipType](http://w3id.org/ontogpt/ibd_literature/RelationshipType)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple]-%20predicate%200..1>[RelationshipType&#124;id(i):string;label(i):string%20%3F],[RelationshipType]^-[DiseaseToCellularProcessPredicate],[RelationshipType]^-[ChemicalExposureToGenePredicate],[NamedEntity]^-[RelationshipType],[Triple],[NamedEntity],[DiseaseToCellularProcessPredicate],[ChemicalExposureToGenePredicate])](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple]-%20predicate%200..1>[RelationshipType&#124;id(i):string;label(i):string%20%3F],[RelationshipType]^-[DiseaseToCellularProcessPredicate],[RelationshipType]^-[ChemicalExposureToGenePredicate],[NamedEntity]^-[RelationshipType],[Triple],[NamedEntity],[DiseaseToCellularProcessPredicate],[ChemicalExposureToGenePredicate])

## Identifier prefixes

 * RO
 * biolink

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Children

 * [ChemicalExposureToGenePredicate](ChemicalExposureToGenePredicate.md)
 * [DiseaseToCellularProcessPredicate](DiseaseToCellularProcessPredicate.md)

## Referenced by Class

 *  **None** *[➞predicate](triple__predicate.md)*  <sub>0..1</sub>  **[RelationshipType](RelationshipType.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
