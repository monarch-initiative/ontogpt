

# Class: OntologyElement



URI: [oc:OntologyElement](http://w3id.org/ontogpt/ontology-class-templateOntologyElement)



```mermaid
erDiagram
OntologyElement {
    string name  
    string context  
    string description  
    stringList synonyms  
    string equivalent_to  
}
Category {
    string name  
    string context  
    string description  
    stringList synonyms  
    string equivalent_to  
}

OntologyElement ||--}o Category : "categories"
OntologyElement ||--}o OntologyElement : "subclass_of"
OntologyElement ||--}o OntologyElement : "part_of"
OntologyElement ||--}o OntologyElement : "subtypes"
OntologyElement ||--}o OntologyElement : "parts"
Category ||--}o Category : "categories"
Category ||--}o OntologyElement : "subclass_of"
Category ||--}o OntologyElement : "part_of"
Category ||--}o OntologyElement : "subtypes"
Category ||--}o OntologyElement : "parts"

```




## Inheritance
* **OntologyElement**
    * [Category](Category.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [name](name.md) | 1 <br/> [String](String.md) | the name of the entity | direct |
| [context](context.md) | 0..1 <br/> [String](String.md) | the ontology to which this belongs (single-valued) | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | a textual description of the entity (single-valued) | direct |
| [synonyms](synonyms.md) | * <br/> [String](String.md) | a list of alternative names of the entity | direct |
| [categories](categories.md) | * <br/> [Category](Category.md) | a list of the categories to which this entity belongs | direct |
| [subclass_of](subclass_of.md) | * <br/> [OntologyElement](OntologyElement.md) | a list of parent class (superclasses) of this entity | direct |
| [part_of](part_of.md) | * <br/> [OntologyElement](OntologyElement.md) | a list of things this element is part of | direct |
| [subtypes](subtypes.md) | * <br/> [OntologyElement](OntologyElement.md) | a list of child classes (subclasses) of this entity | direct |
| [parts](parts.md) | * <br/> [OntologyElement](OntologyElement.md) | a list of names of things this element has as parts (components) | direct |
| [equivalent_to](equivalent_to.md) | 0..1 <br/> [String](String.md) | an OWL class expression with the necessary and sufficient conditions for this... | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Ontology](Ontology.md) | [elements](elements.md) | range | [OntologyElement](OntologyElement.md) |
| [OntologyElement](OntologyElement.md) | [subclass_of](subclass_of.md) | range | [OntologyElement](OntologyElement.md) |
| [OntologyElement](OntologyElement.md) | [part_of](part_of.md) | range | [OntologyElement](OntologyElement.md) |
| [OntologyElement](OntologyElement.md) | [subtypes](subtypes.md) | range | [OntologyElement](OntologyElement.md) |
| [OntologyElement](OntologyElement.md) | [parts](parts.md) | range | [OntologyElement](OntologyElement.md) |
| [Category](Category.md) | [subclass_of](subclass_of.md) | range | [OntologyElement](OntologyElement.md) |
| [Category](Category.md) | [part_of](part_of.md) | range | [OntologyElement](OntologyElement.md) |
| [Category](Category.md) | [subtypes](subtypes.md) | range | [OntologyElement](OntologyElement.md) |
| [Category](Category.md) | [parts](parts.md) | range | [OntologyElement](OntologyElement.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/ontogpt/halo





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | oc:OntologyElement |
| native | oc:OntologyElement |





## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: OntologyElement
from_schema: https://w3id.org/ontogpt/halo
attributes:
  name:
    name: name
    description: the name of the entity
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    identifier: true
    domain_of:
    - OntologyElement
    required: true
  context:
    name: context
    description: the ontology to which this belongs (single-valued)
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    domain_of:
    - OntologyElement
  description:
    name: description
    description: a textual description of the entity (single-valued)
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    domain_of:
    - OntologyElement
  synonyms:
    name: synonyms
    description: a list of alternative names of the entity
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    multivalued: true
    domain_of:
    - OntologyElement
  categories:
    name: categories
    description: a list of the categories to which this entity belongs
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    multivalued: true
    domain_of:
    - OntologyElement
    range: Category
  subclass_of:
    name: subclass_of
    description: a list of parent class (superclasses) of this entity
    from_schema: https://w3id.org/ontogpt/halo
    slot_uri: rdfs:subClassOf
    multivalued: true
    domain_of:
    - OntologyElement
    range: OntologyElement
  part_of:
    name: part_of
    description: a list of things this element is part of
    from_schema: https://w3id.org/ontogpt/halo
    slot_uri: BFO:0000050
    multivalued: true
    domain_of:
    - OntologyElement
    range: OntologyElement
  subtypes:
    name: subtypes
    description: a list of child classes (subclasses) of this entity
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    multivalued: true
    domain_of:
    - OntologyElement
    inverse: subclass_of
    range: OntologyElement
  parts:
    name: parts
    description: a list of names of things this element has as parts (components)
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    multivalued: true
    domain_of:
    - OntologyElement
    inverse: part_of
    range: OntologyElement
  equivalent_to:
    name: equivalent_to
    description: an OWL class expression with the necessary and sufficient conditions
      for this entity to be an instance of this class
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    domain_of:
    - OntologyElement
    range: string

```
</details>

### Induced

<details>
```yaml
name: OntologyElement
from_schema: https://w3id.org/ontogpt/halo
attributes:
  name:
    name: name
    description: the name of the entity
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    identifier: true
    alias: name
    owner: OntologyElement
    domain_of:
    - OntologyElement
    range: string
    required: true
  context:
    name: context
    description: the ontology to which this belongs (single-valued)
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    alias: context
    owner: OntologyElement
    domain_of:
    - OntologyElement
    range: string
  description:
    name: description
    description: a textual description of the entity (single-valued)
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    alias: description
    owner: OntologyElement
    domain_of:
    - OntologyElement
    range: string
  synonyms:
    name: synonyms
    description: a list of alternative names of the entity
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    multivalued: true
    alias: synonyms
    owner: OntologyElement
    domain_of:
    - OntologyElement
    range: string
  categories:
    name: categories
    description: a list of the categories to which this entity belongs
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    multivalued: true
    alias: categories
    owner: OntologyElement
    domain_of:
    - OntologyElement
    range: Category
  subclass_of:
    name: subclass_of
    description: a list of parent class (superclasses) of this entity
    from_schema: https://w3id.org/ontogpt/halo
    slot_uri: rdfs:subClassOf
    multivalued: true
    alias: subclass_of
    owner: OntologyElement
    domain_of:
    - OntologyElement
    range: OntologyElement
  part_of:
    name: part_of
    description: a list of things this element is part of
    from_schema: https://w3id.org/ontogpt/halo
    slot_uri: BFO:0000050
    multivalued: true
    alias: part_of
    owner: OntologyElement
    domain_of:
    - OntologyElement
    range: OntologyElement
  subtypes:
    name: subtypes
    description: a list of child classes (subclasses) of this entity
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    multivalued: true
    alias: subtypes
    owner: OntologyElement
    domain_of:
    - OntologyElement
    inverse: subclass_of
    range: OntologyElement
  parts:
    name: parts
    description: a list of names of things this element has as parts (components)
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    multivalued: true
    alias: parts
    owner: OntologyElement
    domain_of:
    - OntologyElement
    inverse: part_of
    range: OntologyElement
  equivalent_to:
    name: equivalent_to
    description: an OWL class expression with the necessary and sufficient conditions
      for this entity to be an instance of this class
    from_schema: https://w3id.org/ontogpt/halo
    rank: 1000
    alias: equivalent_to
    owner: OntologyElement
    domain_of:
    - OntologyElement
    range: string

```
</details>