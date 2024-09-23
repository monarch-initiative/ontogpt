

# Class: BiologicalProcess



URI: [bp:BiologicalProcess](http://w3id.org/ontogpt/biological-process-templateBiologicalProcess)



```mermaid
erDiagram
BiologicalProcess {
    string label  
    string description  
    stringList synonyms  
    string id  
}
GeneMolecularActivityRelationship {

}
MolecularActivity {
    string id  
    string label  
}
Gene {
    string id  
    string label  
}
ChemicalEntity {
    string id  
    string label  
}

BiologicalProcess ||--|o BiologicalProcess : "subclass_of"
BiologicalProcess ||--}o ChemicalEntity : "inputs"
BiologicalProcess ||--}o ChemicalEntity : "outputs"
BiologicalProcess ||--}o MolecularActivity : "steps"
BiologicalProcess ||--}o Gene : "genes"
BiologicalProcess ||--}o GeneMolecularActivityRelationship : "gene_activities"
GeneMolecularActivityRelationship ||--|o Gene : "gene"
GeneMolecularActivityRelationship ||--|o MolecularActivity : "molecular_activity"

```




## Inheritance
* [NamedEntity](NamedEntity.md)
    * **BiologicalProcess**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [label](label.md) | 0..1 <br/> [String](String.md) | the name of the biological process | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | a textual description of the biological process | direct |
| [synonyms](synonyms.md) | * <br/> [String](String.md) | alternative names of the biological process | direct |
| [subclass_of](subclass_of.md) | 0..1 <br/> [BiologicalProcess](BiologicalProcess.md) | the category to which this biological process belongs | direct |
| [inputs](inputs.md) | * <br/> [ChemicalEntity](ChemicalEntity.md) | the inputs of the biological process | direct |
| [outputs](outputs.md) | * <br/> [ChemicalEntity](ChemicalEntity.md) | the outputs of the biological process | direct |
| [steps](steps.md) | * <br/> [MolecularActivity](MolecularActivity.md) | the steps involved in this biological process | direct |
| [genes](genes.md) | * <br/> [Gene](Gene.md) |  | direct |
| [gene_activities](gene_activities.md) | * <br/> [GeneMolecularActivityRelationship](GeneMolecularActivityRelationship.md) | semicolon-separated list of gene to molecular activity relationships | direct |
| [id](id.md) | 1 <br/> [String](String.md) | A unique identifier for the named entity | [NamedEntity](NamedEntity.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [BiologicalProcess](BiologicalProcess.md) | [subclass_of](subclass_of.md) | range | [BiologicalProcess](BiologicalProcess.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/ontogpt/biological_process





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | bp:BiologicalProcess |
| native | bp:BiologicalProcess |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: BiologicalProcess
from_schema: https://w3id.org/ontogpt/biological_process
is_a: NamedEntity
attributes:
  label:
    name: label
    description: the name of the biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    domain_of:
    - BiologicalProcess
    - NamedEntity
  description:
    name: description
    description: a textual description of the biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    domain_of:
    - BiologicalProcess
  synonyms:
    name: synonyms
    description: alternative names of the biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    domain_of:
    - BiologicalProcess
  subclass_of:
    name: subclass_of
    description: the category to which this biological process belongs
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    domain_of:
    - BiologicalProcess
    range: BiologicalProcess
  inputs:
    name: inputs
    description: the inputs of the biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    domain_of:
    - BiologicalProcess
    range: ChemicalEntity
  outputs:
    name: outputs
    description: the outputs of the biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    domain_of:
    - BiologicalProcess
    range: ChemicalEntity
  steps:
    name: steps
    description: the steps involved in this biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    domain_of:
    - BiologicalProcess
    range: MolecularActivity
  genes:
    name: genes
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    domain_of:
    - BiologicalProcess
    range: Gene
  gene_activities:
    name: gene_activities
    description: semicolon-separated list of gene to molecular activity relationships
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    domain_of:
    - BiologicalProcess
    range: GeneMolecularActivityRelationship
tree_root: true

```
</details>

### Induced

<details>
```yaml
name: BiologicalProcess
from_schema: https://w3id.org/ontogpt/biological_process
is_a: NamedEntity
attributes:
  label:
    name: label
    description: the name of the biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    alias: label
    owner: BiologicalProcess
    domain_of:
    - BiologicalProcess
    - NamedEntity
    range: string
  description:
    name: description
    description: a textual description of the biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    alias: description
    owner: BiologicalProcess
    domain_of:
    - BiologicalProcess
    range: string
  synonyms:
    name: synonyms
    description: alternative names of the biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    alias: synonyms
    owner: BiologicalProcess
    domain_of:
    - BiologicalProcess
    range: string
  subclass_of:
    name: subclass_of
    description: the category to which this biological process belongs
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    alias: subclass_of
    owner: BiologicalProcess
    domain_of:
    - BiologicalProcess
    range: BiologicalProcess
  inputs:
    name: inputs
    description: the inputs of the biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    alias: inputs
    owner: BiologicalProcess
    domain_of:
    - BiologicalProcess
    range: ChemicalEntity
  outputs:
    name: outputs
    description: the outputs of the biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    alias: outputs
    owner: BiologicalProcess
    domain_of:
    - BiologicalProcess
    range: ChemicalEntity
  steps:
    name: steps
    description: the steps involved in this biological process
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    alias: steps
    owner: BiologicalProcess
    domain_of:
    - BiologicalProcess
    range: MolecularActivity
  genes:
    name: genes
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    alias: genes
    owner: BiologicalProcess
    domain_of:
    - BiologicalProcess
    range: Gene
  gene_activities:
    name: gene_activities
    description: semicolon-separated list of gene to molecular activity relationships
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    multivalued: true
    alias: gene_activities
    owner: BiologicalProcess
    domain_of:
    - BiologicalProcess
    range: GeneMolecularActivityRelationship
  id:
    name: id
    annotations:
      prompt.skip:
        tag: prompt.skip
        value: 'true'
    description: A unique identifier for the named entity
    comments:
    - this is populated during the grounding and normalization step
    from_schema: https://w3id.org/ontogpt/biological_process
    rank: 1000
    identifier: true
    alias: id
    owner: BiologicalProcess
    domain_of:
    - NamedEntity
    - Publication
    range: string
    required: true
tree_root: true

```
</details>