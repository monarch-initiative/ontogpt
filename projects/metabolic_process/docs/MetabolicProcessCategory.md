
# Class: MetabolicProcessCategory




URI: [bp:MetabolicProcessCategory](http://w3id.org/ontogpt/metabolic-process-templateMetabolicProcessCategory)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[MetabolicProcess]-%20category%200..1>[MetabolicProcessCategory&#124;id(i):string;label(i):string%20%3F],[MetabolicProcess]-%20subclass_of%200..*>[MetabolicProcessCategory],[NamedEntity]^-[MetabolicProcessCategory],[MetabolicProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[MetabolicProcess]-%20category%200..1>[MetabolicProcessCategory&#124;id(i):string;label(i):string%20%3F],[MetabolicProcess]-%20subclass_of%200..*>[MetabolicProcessCategory],[NamedEntity]^-[MetabolicProcessCategory],[MetabolicProcess])

## Identifier prefixes

 * GO

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞category](metabolicProcess__category.md)*  <sub>0..1</sub>  **[MetabolicProcessCategory](MetabolicProcessCategory.md)**
 *  **None** *[➞subclass_of](metabolicProcess__subclass_of.md)*  <sub>0..\*</sub>  **[MetabolicProcessCategory](MetabolicProcessCategory.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
