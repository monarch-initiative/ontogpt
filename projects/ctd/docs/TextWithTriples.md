
# Class: TextWithTriples




URI: [drug:TextWithTriples](http://w3id.org/ontogpt/drug/TextWithTriples)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[Triple]<triples%200..*-++[TextWithTriples],[Publication]<publication%200..1-++[TextWithTriples],[TextWithTriples]^-[ChemicalToDiseaseDocument],[Publication],[ChemicalToDiseaseDocument])](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[Triple]<triples%200..*-++[TextWithTriples],[Publication]<publication%200..1-++[TextWithTriples],[TextWithTriples]^-[ChemicalToDiseaseDocument],[Publication],[ChemicalToDiseaseDocument])

## Children

 * [ChemicalToDiseaseDocument](ChemicalToDiseaseDocument.md) - A document that contains chemical to disease relations.

## Referenced by Class


## Attributes


### Own

 * [➞publication](textWithTriples__publication.md)  <sub>0..1</sub>
     * Range: [Publication](Publication.md)
 * [➞triples](textWithTriples__triples.md)  <sub>0..\*</sub>
     * Range: [Triple](Triple.md)
