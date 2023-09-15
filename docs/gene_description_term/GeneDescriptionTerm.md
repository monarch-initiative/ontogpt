
# Class: GeneDescriptionTerm




URI: [bp:GeneDescriptionTerm](http://w3id.org/ontogpt/biological-process-templateGeneDescriptionTerm)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneDescription]-%20terms%200..*>[GeneDescriptionTerm&#124;label:string%20%3F;id(i):string],[NamedEntity]^-[GeneDescriptionTerm],[GeneDescription])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneDescription]-%20terms%200..*>[GeneDescriptionTerm&#124;label:string%20%3F;id(i):string],[NamedEntity]^-[GeneDescriptionTerm],[GeneDescription])

## Identifier prefixes

 * GO
 * MONDO
 * UBERON
 * MESH

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞terms](geneDescription__terms.md)*  <sub>0..\*</sub>  **[GeneDescriptionTerm](GeneDescriptionTerm.md)**

## Attributes


### Own

 * [➞label](geneDescriptionTerm__label.md)  <sub>0..1</sub>
     * Description: the name of the GO term
     * Range: [String](types/String.md)

### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
