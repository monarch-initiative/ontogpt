
# Class: Disease




URI: [composite_disease:Disease](http://w3id.org/ontogpt/composite_disease/Disease)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[CompositeDisease]-%20main_disease%200..1>[Disease&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Disease],[CompositeDisease])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[CompositeDisease]-%20main_disease%200..1>[Disease&#124;id(i):string;label(i):string%20%3F],[NamedEntity]^-[Disease],[CompositeDisease])

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞main_disease](compositeDisease__main_disease.md)*  <sub>0..1</sub>  **[Disease](Disease.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
