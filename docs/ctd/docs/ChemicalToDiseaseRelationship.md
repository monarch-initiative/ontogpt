
# Class: ChemicalToDiseaseRelationship


A triple where the subject is a chemical and the object is a disease.

URI: [drug:ChemicalToDiseaseRelationship](http://w3id.org/ontogpt/drug/ChemicalToDiseaseRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[NamedEntity],[Disease],[NamedEntity]<object_qualifier%200..1-%20[ChemicalToDiseaseRelationship&#124;qualifier(i):string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[ChemicalToDiseaseRelationship],[ChemicalToDiseasePredicate]<predicate%200..1-%20[ChemicalToDiseaseRelationship],[Disease]<object%200..1-%20[ChemicalToDiseaseRelationship],[Chemical]<subject%200..1-%20[ChemicalToDiseaseRelationship],[ChemicalToDiseaseDocument]++-%20triples%200..*>[ChemicalToDiseaseRelationship],[Triple]^-[ChemicalToDiseaseRelationship],[ChemicalToDiseasePredicate],[ChemicalToDiseaseDocument],[Chemical])](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[NamedEntity],[Disease],[NamedEntity]<object_qualifier%200..1-%20[ChemicalToDiseaseRelationship&#124;qualifier(i):string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[ChemicalToDiseaseRelationship],[ChemicalToDiseasePredicate]<predicate%200..1-%20[ChemicalToDiseaseRelationship],[Disease]<object%200..1-%20[ChemicalToDiseaseRelationship],[Chemical]<subject%200..1-%20[ChemicalToDiseaseRelationship],[ChemicalToDiseaseDocument]++-%20triples%200..*>[ChemicalToDiseaseRelationship],[Triple]^-[ChemicalToDiseaseRelationship],[ChemicalToDiseasePredicate],[ChemicalToDiseaseDocument],[Chemical])

## Parents

 *  is_a: [Triple](Triple.md) - Abstract parent for Relation Extraction tasks

## Referenced by Class

 *  **[ChemicalToDiseaseDocument](ChemicalToDiseaseDocument.md)** *[ChemicalToDiseaseDocument➞triples](ChemicalToDiseaseDocument_triples.md)*  <sub>0..\*</sub>  **[ChemicalToDiseaseRelationship](ChemicalToDiseaseRelationship.md)**

## Attributes


### Own

 * [ChemicalToDiseaseRelationship➞subject](ChemicalToDiseaseRelationship_subject.md)  <sub>0..1</sub>
     * Description: The chemical substance, drug, or small molecule.  For example: Lidocaine, Monosodium Glutamate, Imatinib.
     * Range: [Chemical](Chemical.md)
 * [ChemicalToDiseaseRelationship➞object](ChemicalToDiseaseRelationship_object.md)  <sub>0..1</sub>
     * Description: The disease or condition that is being treated or induced by the chemical. For example, asthma, cancer, covid-19, cardiac asystole, Hypotension, Headache.
     * Range: [Disease](Disease.md)
 * [ChemicalToDiseaseRelationship➞predicate](ChemicalToDiseaseRelationship_predicate.md)  <sub>0..1</sub>
     * Description: The relationship type, e.g. INDUCES, TREATS.
     * Range: [ChemicalToDiseasePredicate](ChemicalToDiseasePredicate.md)
 * [ChemicalToDiseaseRelationship➞subject_qualifier](ChemicalToDiseaseRelationship_subject_qualifier.md)  <sub>0..1</sub>
     * Description: An optional qualifier or modifier for the chemical, e.g. "high dose" or "intravenously administered"
     * Range: [NamedEntity](NamedEntity.md)
 * [ChemicalToDiseaseRelationship➞object_qualifier](ChemicalToDiseaseRelationship_object_qualifier.md)  <sub>0..1</sub>
     * Description: An optional qualifier or modifier for the disease, e.g. "severe" or "with additional complications"
     * Range: [NamedEntity](NamedEntity.md)

### Inherited from Triple:

 * [➞qualifier](triple__qualifier.md)  <sub>0..1</sub>
     * Description: A qualifier for the statements, e.g. "NOT" for negation
     * Range: [String](types/String.md)
