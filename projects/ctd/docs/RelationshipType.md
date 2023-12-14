
# Class: RelationshipType




URI: [drug:RelationshipType](http://w3id.org/ontogpt/drug/RelationshipType)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple]-%20predicate%200..1>[RelationshipType&#124;id(i):string;label(i):string%20%3F],[RelationshipType]^-[ChemicalToDiseasePredicate],[NamedEntity]^-[RelationshipType],[Triple],[NamedEntity],[ChemicalToDiseasePredicate])](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple]-%20predicate%200..1>[RelationshipType&#124;id(i):string;label(i):string%20%3F],[RelationshipType]^-[ChemicalToDiseasePredicate],[NamedEntity]^-[RelationshipType],[Triple],[NamedEntity],[ChemicalToDiseasePredicate])

## Identifier prefixes

 * RO
 * biolink

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Children

 * [ChemicalToDiseasePredicate](ChemicalToDiseasePredicate.md) - A predicate for chemical to disease relationships

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