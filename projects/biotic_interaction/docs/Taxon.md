
# Class: Taxon




URI: [bp:Taxon](http://w3id.org/ontogpt/biotic-interaction-templateTaxon)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[BioticInteraction]-%20source_taxon%200..1>[Taxon&#124;id(i):string;label(i):string%20%3F],[BioticInteraction]-%20target_taxon%200..1>[Taxon],[NamedEntity]^-[Taxon],[NamedEntity],[BioticInteraction])](https://yuml.me/diagram/nofunky;dir:TB/class/[BioticInteraction]-%20source_taxon%200..1>[Taxon&#124;id(i):string;label(i):string%20%3F],[BioticInteraction]-%20target_taxon%200..1>[Taxon],[NamedEntity]^-[Taxon],[NamedEntity],[BioticInteraction])

## Identifier prefixes

 * NCBITaxon
 * COL
 * ITIS
 * GBIF

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞source_taxon](bioticInteraction__source_taxon.md)*  <sub>0..1</sub>  **[Taxon](Taxon.md)**
 *  **None** *[➞target_taxon](bioticInteraction__target_taxon.md)*  <sub>0..1</sub>  **[Taxon](Taxon.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
