
# Class: LinkedElement




URI: [diag:LinkedElement](http://w3id.org/ontogpt/diagnostic_procedure/LinkedElement)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[Link]-%20object%200..1>[LinkedElement&#124;id(i):string;label(i):string%20%3F],[Link]-%20subject%200..1>[LinkedElement],[NamedEntity]^-[LinkedElement],[Link])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[Link]-%20object%200..1>[LinkedElement&#124;id(i):string;label(i):string%20%3F],[Link]-%20subject%200..1>[LinkedElement],[NamedEntity]^-[LinkedElement],[Link])

## Identifier prefixes

 * MESH

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞object](link__object.md)*  <sub>0..1</sub>  **[LinkedElement](LinkedElement.md)**
 *  **None** *[➞subject](link__subject.md)*  <sub>0..1</sub>  **[LinkedElement](LinkedElement.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
