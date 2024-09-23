

# Class: Neuron



URI: [cell_type:Neuron](http://w3id.org/ontogpt/cell_type/Neuron)



```mermaid
erDiagram
Neuron {
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
Neurotransmitter {
    string id  
    string label  
}

Neuron ||--}o Neurotransmitter : "releases_neurotransitter"
Neuron ||--|o CellOntologyTerm : "equivalent_to"
Neuron ||--}o CellOntologyTerm : "parents"
Neuron ||--}o CellOntologyTerm : "subtypes"
Neuron ||--}o AnatomicalStructure : "localizations"
Neuron ||--}o Gene : "genes"
Neuron ||--}o Disease : "diseases"
Neuron ||--}o BiologicalProcess : "roles"

```




## Inheritance
* [CellType](CellType.md)
    * **Neuron**
        * [Interneuron](Interneuron.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [releases_neurotransitter](releases_neurotransitter.md) | * <br/> [Neurotransmitter](Neurotransmitter.md) |  | direct |
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
| self | cell_type:Neuron |
| native | cell_type:Neuron |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Neuron
from_schema: http://w3id.org/ontogpt/cell_type
is_a: CellType
attributes:
  releases_neurotransitter:
    name: releases_neurotransitter
    annotations:
      prompt:
        tag: prompt
        value: named of chemical entity that this neuron releases
      owl:
        tag: owl
        value: SubClassOf, ObjectSomeValuesFrom
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    slot_uri: RO:0002111
    multivalued: true
    domain_of:
    - Neuron
    range: Neurotransmitter

```
</details>

### Induced

<details>
```yaml
name: Neuron
from_schema: http://w3id.org/ontogpt/cell_type
is_a: CellType
attributes:
  releases_neurotransitter:
    name: releases_neurotransitter
    annotations:
      prompt:
        tag: prompt
        value: named of chemical entity that this neuron releases
      owl:
        tag: owl
        value: SubClassOf, ObjectSomeValuesFrom
    from_schema: http://w3id.org/ontogpt/cell_type
    rank: 1000
    slot_uri: RO:0002111
    multivalued: true
    alias: releases_neurotransitter
    owner: Neuron
    domain_of:
    - Neuron
    range: Neurotransmitter
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
    owner: Neuron
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
    owner: Neuron
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
    owner: Neuron
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
    owner: Neuron
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
    owner: Neuron
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
    owner: Neuron
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
    owner: Neuron
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
    owner: Neuron
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
    owner: Neuron
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
    owner: Neuron
    domain_of:
    - CellType
    range: BiologicalProcess

```
</details>