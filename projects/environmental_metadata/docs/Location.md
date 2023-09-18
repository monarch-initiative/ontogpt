
# Class: Location




URI: [envmd:Location](http://w3id.org/ontogpt/environmental-metadataLocation)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[Dataset]-%20location%200..*>[Location&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Location],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[Dataset]-%20location%200..*>[Location&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Location],[Dataset])

## Identifier prefixes

 * ENVO
 * GAZ

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞location](dataset__location.md)*  <sub>0..\*</sub>  **[Location](Location.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
