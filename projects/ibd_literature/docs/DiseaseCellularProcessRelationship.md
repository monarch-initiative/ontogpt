
# Class: DiseaseCellularProcessRelationship




URI: [ibdlit:DiseaseCellularProcessRelationship](http://w3id.org/ontogpt/ibd_literature/DiseaseCellularProcessRelationship)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[NamedEntity],[DiseaseToCellularProcessPredicate],[NamedEntity]<object_qualifier%200..1-%20[DiseaseCellularProcessRelationship&#124;qualifier(i):string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[DiseaseCellularProcessRelationship],[CellularProcess]<object%200..1-%20[DiseaseCellularProcessRelationship],[DiseaseToCellularProcessPredicate]<predicate%200..1-%20[DiseaseCellularProcessRelationship],[Disease]<subject%200..1-%20[DiseaseCellularProcessRelationship],[IBDAnnotations]++-%20disease_cellular_process_relationships%200..*>[DiseaseCellularProcessRelationship],[Triple]^-[DiseaseCellularProcessRelationship],[IBDAnnotations],[Disease],[CellularProcess])](https://yuml.me/diagram/nofunky;dir:TB/class/[Triple],[NamedEntity],[DiseaseToCellularProcessPredicate],[NamedEntity]<object_qualifier%200..1-%20[DiseaseCellularProcessRelationship&#124;qualifier(i):string%20%3F],[NamedEntity]<subject_qualifier%200..1-%20[DiseaseCellularProcessRelationship],[CellularProcess]<object%200..1-%20[DiseaseCellularProcessRelationship],[DiseaseToCellularProcessPredicate]<predicate%200..1-%20[DiseaseCellularProcessRelationship],[Disease]<subject%200..1-%20[DiseaseCellularProcessRelationship],[IBDAnnotations]++-%20disease_cellular_process_relationships%200..*>[DiseaseCellularProcessRelationship],[Triple]^-[DiseaseCellularProcessRelationship],[IBDAnnotations],[Disease],[CellularProcess])

## Parents

 *  is_a: [Triple](Triple.md) - Abstract parent for Relation Extraction tasks

## Referenced by Class

 *  **None** *[➞disease_cellular_process_relationships](iBDAnnotations__disease_cellular_process_relationships.md)*  <sub>0..\*</sub>  **[DiseaseCellularProcessRelationship](DiseaseCellularProcessRelationship.md)**

## Attributes


### Own

 * [DiseaseCellularProcessRelationship➞subject](DiseaseCellularProcessRelationship_subject.md)  <sub>0..1</sub>
     * Description: The name of the disease.
     * Range: [Disease](Disease.md)
 * [DiseaseCellularProcessRelationship➞predicate](DiseaseCellularProcessRelationship_predicate.md)  <sub>0..1</sub>
     * Description: The name of the type of relationship between a disease and a cellular process.
     * Range: [DiseaseToCellularProcessPredicate](DiseaseToCellularProcessPredicate.md)
 * [DiseaseCellularProcessRelationship➞object](DiseaseCellularProcessRelationship_object.md)  <sub>0..1</sub>
     * Description: The name of the cellular process.
     * Range: [CellularProcess](CellularProcess.md)
 * [DiseaseCellularProcessRelationship➞subject_qualifier](DiseaseCellularProcessRelationship_subject_qualifier.md)  <sub>0..1</sub>
     * Range: [NamedEntity](NamedEntity.md)
 * [DiseaseCellularProcessRelationship➞object_qualifier](DiseaseCellularProcessRelationship_object_qualifier.md)  <sub>0..1</sub>
     * Range: [NamedEntity](NamedEntity.md)

### Inherited from Triple:

 * [➞qualifier](triple__qualifier.md)  <sub>0..1</sub>
     * Description: A qualifier for the statements, e.g. "NOT" for negation
     * Range: [String](types/String.md)
