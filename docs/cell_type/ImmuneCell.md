

# Class: ImmuneCell



URI: [cell_type:ImmuneCell](http://w3id.org/ontogpt/cell_type/ImmuneCell)



```mermaid
erDiagram
ImmuneCell {
    uriorcurie id  
    string label  
    string definition  
}
BiologicalProcess {
    string id  
    string label  
}
Disease {
    string id  
    string label  
}
Gene {
    string id  
    string label  
}
AnatomicalStructure {
    string id  
    string label  
}
CellOntologyTerm {
    string id  
    string label  
}
ProteinOrComplex {
    string id  
    string label  
}

ImmuneCell ||--}o ProteinOrComplex : "has_surface_markers"
ImmuneCell ||--|o CellOntologyTerm : "equivalent_to"
ImmuneCell ||--}o CellOntologyTerm : "parents"
ImmuneCell ||--}o CellOntologyTerm : "subtypes"
ImmuneCell ||--}o AnatomicalStructure : "localizations"
ImmuneCell ||--}o Gene : "genes"
ImmuneCell ||--}o Disease : "diseases"
ImmuneCell ||--}o BiologicalProcess : "roles"

```




## Inheritance
* [CellType](CellType.md)
    * **ImmuneCell**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_surface_markers](has_surface_markers.md) | * <br/> [ProteinOrComplex](ProteinOrComplex.md) |  | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) |  | [CellType](CellType.md) |
| [label](label.md) | 0..1 <br/> [String](String.md) | the concise name of the cell type | [CellType](CellType.md) |
| [equivalent_to](equivalent_to.md) | 0..1 <br/> [CellOntologyTerm](CellOntologyTerm.md) | the the cell type described | [CellType](CellType.md) |
| [definition](definition.md) | 0..1 <br/> [String](String.md) |  | [CellType](CellType.md) |
| [parents](parents.md) | * <br/> [CellOntologyTerm](CellOntologyTerm.md) | categorization | [CellType](CellType.md) |
| [subtypes](subtypes.md) | * <br/> [CellOntologyTerm](CellOntologyTerm.md) |  | [CellType](CellType.md) |
| [localizations](localizations.md) | * <br/> [AnatomicalStructure](AnatomicalStructure.md) |  | [CellType](CellType.md) |
| [genes](genes.md) | * <br/> [Gene](Gene.md) |  | [CellType](CellType.md) |
| [diseases](diseases.md) | * <br/> [Disease](Disease.md) |  | [CellType](CellType.md) |
| [roles](roles.md) | * <br/> [BiologicalProcess](BiologicalProcess.md) |  | [CellType](CellType.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: http://w3id.org/ontogpt/cell_type





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | cell_type:ImmuneCell |
| native | cell_type:ImmuneCell |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ImmuneCell
from_schema: http://w3id.org/ontogpt/cell_type
is_a: CellType
attributes:
  has_surface_markers:
    name: has_surface_markers
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of proteins or complexes expressed on the
          surface of the cell
      owl:
        tag: owl
        value: SubClassOf, ObjectSomeValuesFrom
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    multivalued: true
    domain_of:
    - ImmuneCell
    range: ProteinOrComplex

```
</details>

### Induced

<details>
```yaml
name: ImmuneCell
from_schema: http://w3id.org/ontogpt/cell_type
is_a: CellType
attributes:
  has_surface_markers:
    name: has_surface_markers
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of proteins or complexes expressed on the
          surface of the cell
      owl:
        tag: owl
        value: SubClassOf, ObjectSomeValuesFrom
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    multivalued: true
    alias: has_surface_markers
    owner: ImmuneCell
    domain_of:
    - ImmuneCell
    range: ProteinOrComplex
  id:
    name: id
    annotations:
      prompt.skip:
        tag: prompt.skip
        value: true
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    slot_uri: rdf:Resource
    identifier: true
    alias: id
    owner: ImmuneCell
    domain_of:
    - CellType
    - NamedEntity
    - Publication
    range: uriorcurie
    required: true
  label:
    name: label
    annotations:
      owl:
        tag: owl
        value: AnnotationAssertion
    description: the concise name of the cell type
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: ImmuneCell
    domain_of:
    - CellType
    - NamedEntity
    range: string
  equivalent_to:
    name: equivalent_to
    annotations:
      prompt:
        tag: prompt
        value: the cell type described in the text
      owl:
        tag: owl
        value: AnnotationAssertion
    description: the the cell type described
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    slot_uri: skos:exactMatch
    alias: equivalent_to
    owner: ImmuneCell
    domain_of:
    - CellType
    range: CellOntologyTerm
  definition:
    name: definition
    annotations:
      prompt:
        tag: prompt
        value: A concise textual definition in genus-differentia form, i.e  'A <genus>
          that <differentiating characteristics>'
      owl:
        tag: owl
        value: AnnotationProperty, AnnotationAssertion
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    slot_uri: IAO:0000115
    alias: definition
    owner: ImmuneCell
    domain_of:
    - CellType
    range: string
  parents:
    name: parents
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of parent (broader) cell types
      owl:
        tag: owl
        value: SubClassOf
    description: categorization
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    multivalued: true
    alias: parents
    owner: ImmuneCell
    domain_of:
    - CellType
    range: CellOntologyTerm
  subtypes:
    name: subtypes
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of the subtypes (subclasses) of this cell
          type. Use concise terms, and separate elements in a list using semicolon
          (;)
      owl.template:
        tag: owl.template
        value: '{% for subtype in subtypes %}

          SubClassOf( {{ tr(subtype) }} {{ id }} )

          {% endfor %}

          '
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    multivalued: true
    alias: subtypes
    owner: ImmuneCell
    domain_of:
    - CellType
    range: CellOntologyTerm
  localizations:
    name: localizations
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of anatomical structures in which this cell
          type is localized
      owl:
        tag: owl
        value: SubClassOf, ObjectSomeValuesFrom
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    slot_uri: BFO:0000050
    multivalued: true
    alias: localizations
    owner: ImmuneCell
    domain_of:
    - CellType
    range: AnatomicalStructure
  genes:
    name: genes
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of genes expressed in cells of this type
      owl:
        tag: owl
        value: SubClassOf, ObjectSomeValuesFrom
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    slot_uri: RO:0002292
    multivalued: true
    alias: genes
    owner: ImmuneCell
    domain_of:
    - CellType
    range: Gene
  diseases:
    name: diseases
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of diseases in which this cell type is implicated
      owl.template:
        tag: owl.template
        value: '{% for disease in diseases %}

          SubClassOf( {{ tr(disease) }} ObjectSomeValuesFrom( RO:0004026 {{ id }}
          ))

          {% endfor %}

          '
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    multivalued: true
    alias: diseases
    owner: ImmuneCell
    domain_of:
    - CellType
    range: Disease
  roles:
    name: roles
    annotations:
      prompt:
        tag: prompt
        value: semicolon-separated list of roles (e.g. biological processes) that
          this cell type plays. These should be short descriptive terms corresponding
          to ontology terms in the GO biological process hierarchy.
      owl:
        tag: owl
        value: SubClassOf, ObjectSomeValuesFrom
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    slot_uri: RO:0002215
    multivalued: true
    alias: roles
    owner: ImmuneCell
    domain_of:
    - CellType
    range: BiologicalProcess

```
</details>