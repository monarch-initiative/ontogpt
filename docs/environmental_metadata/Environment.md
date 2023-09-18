
# Class: Environment




URI: [envmd:Environment](http://w3id.org/ontogpt/environmental-metadataEnvironment)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[Dataset]-%20environments%200..*>[Environment&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Environment],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[Dataset]-%20environments%200..*>[Environment&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Environment],[Dataset])

## Identifier prefixes

 * ENVO
 * ENVTHES

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞environments](dataset__environments.md)*  <sub>0..\*</sub>  **[Environment](Environment.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
