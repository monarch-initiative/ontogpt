
# Class: Gene




URI: [gocam:Gene](http://w3id.org/ontogpt/gocam/Gene)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneGeneInteraction]-%20gene1%200..1>[Gene&#124;id(i):string;label(i):string%20%3F],[GeneGeneInteraction]-%20gene2%200..1>[Gene],[GeneMolecularActivityRelationship2]-%20gene%200..1>[Gene],[GeneMolecularActivityRelationship]-%20gene%200..1>[Gene],[GeneOrganismRelationship]-%20gene%200..1>[Gene],[GeneSubcellularLocalizationRelationship]-%20gene%200..1>[Gene],[GoCamAnnotations]-%20genes%200..*>[Gene],[NamedEntity]^-[Gene],[GoCamAnnotations],[GeneSubcellularLocalizationRelationship],[GeneOrganismRelationship],[GeneMolecularActivityRelationship2],[GeneMolecularActivityRelationship],[GeneGeneInteraction])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedEntity],[GeneGeneInteraction]-%20gene1%200..1>[Gene&#124;id(i):string;label(i):string%20%3F],[GeneGeneInteraction]-%20gene2%200..1>[Gene],[GeneMolecularActivityRelationship2]-%20gene%200..1>[Gene],[GeneMolecularActivityRelationship]-%20gene%200..1>[Gene],[GeneOrganismRelationship]-%20gene%200..1>[Gene],[GeneSubcellularLocalizationRelationship]-%20gene%200..1>[Gene],[GoCamAnnotations]-%20genes%200..*>[Gene],[NamedEntity]^-[Gene],[GoCamAnnotations],[GeneSubcellularLocalizationRelationship],[GeneOrganismRelationship],[GeneMolecularActivityRelationship2],[GeneMolecularActivityRelationship],[GeneGeneInteraction])

## Identifier prefixes

 * HGNC
 * PR
 * UniProtKB

## Parents

 *  is_a: [NamedEntity](NamedEntity.md)

## Referenced by Class

 *  **None** *[➞gene1](geneGeneInteraction__gene1.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**
 *  **None** *[➞gene2](geneGeneInteraction__gene2.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**
 *  **None** *[➞gene](geneMolecularActivityRelationship2__gene.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**
 *  **None** *[➞gene](geneMolecularActivityRelationship__gene.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**
 *  **None** *[➞gene](geneOrganismRelationship__gene.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**
 *  **None** *[➞gene](geneSubcellularLocalizationRelationship__gene.md)*  <sub>0..1</sub>  **[Gene](Gene.md)**
 *  **None** *[➞genes](goCamAnnotations__genes.md)*  <sub>0..\*</sub>  **[Gene](Gene.md)**

## Attributes


### Inherited from NamedEntity:

 * [➞id](namedEntity__id.md)  <sub>1..1</sub>
     * Description: A unique identifier for the named entity
     * Range: [String](types/String.md)
 * [➞label](namedEntity__label.md)  <sub>0..1</sub>
     * Description: The label (name) of the named thing
     * Range: [String](types/String.md)
