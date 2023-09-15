
# Class: Topic




URI: [envmd:Topic](http://w3id.org/ontogpt/environmental-metadataTopic)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Dataset]-%20topic%200..*>[Topic&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Topic],[NamedEntity],[Dataset])](https://yuml.me/diagram/nofunky;dir:TB/class/[Dataset]-%20topic%200..*>[Topic&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Topic],[NamedEntity],[Dataset])

## Identifier prefixes

 * ENVTHES

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞topic](dataset__topic.md)*  <sub>0..\*</sub>  **[Topic](Topic.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
