# Custom Schemas

## Build a custom schema

Define a schema (using a subset of [LinkML](https://linkml.io)) that describes the structure in which you want to extract knowledge from your text.

There are a number of pre-defined LinkML data models already developed here - [src/ontogpt/templates/](src/ontogpt/templates/) which you can use as reference when creating your own data models.

### The header

The header of the schema defines metadata, parameters instructing LinkML to interpret prefixes in specific ways, and names of imports.

You will find these fields in the schema header:

* `id`: A unique identifier for the schema. These may take the form of W3IDs like `http://w3id.org/ontogpt/schemaname`.
* `name`: Name of the schema. Should resemble the filename.
* `title`: Title of the schema for human readability.
* `description`: A human readable description of the schema. Detail is welcome!
* `license`: A license indicating reusability of the schema. We prefer a [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/).
* `prefixes`: This is a list (actually a dictionary, as each item contains a key and a value) of short prefixes for the identifier namespaces used in the schema along with their corresponding identifier prefixes. At minimum, this shoulc include `linkml: https://w3id.org/linkml/` and the prefix for your schema itself. If the schema is named `salmon`, this will be something like `salmon: http://w3id.org/ontogpt/salmon/`. If you're using Gene Ontology identifiers, specify their prefixes as `GO: http://purl.obolibrary.org/obo/GO_`, because each Gene Ontology term has an identifier prefixed with `GO:`.
* `default_prefix`: This is the prefix for your schema. It should match what you used in the `prefixes` list, so following the above example, that would be `salmon`.
* `default_range`: This is the default data type LinkML will assume each class should be unless specified otherwise. Using `string` is usually safe.

* `imports`: A list of other schemas to import types from. These may be any schemas in the same directory (e.g., if you have another schema named `francine` then you may simply include `francine` in the list of imports) but note that LinkML will raise an error if multiple classes have the same name across the imports. Minimally, this list should include `linkml:types` and `core` to import the base LinkML data types and the generic OntoGPT classes, respectively.

An example:

```yaml
id: http://w3id.org/ontogpt/gocam
name: gocam-template
title: GO-CAM Template
description: >-
  A template for GO-CAMs
license: https://creativecommons.org/publicdomain/zero/1.0/
prefixes:
  linkml: https://w3id.org/linkml/
  gocam: http://w3id.org/ontogpt/gocam/
  GO: http://purl.obolibrary.org/obo/GO_
  CL: http://purl.obolibrary.org/obo/CL_

default_prefix: gocam
default_range: string

imports:
  - linkml:types
  - core
```

### The classes

The classes in the schema define the "things" you are interested in extracting. LinkML doesn't make many assumptions about the difference between a class and a relationship, a node and an edge, or a relation and a property. It's designed to be flexibile enough to handle a variety of data models.

An example, continuing from where the header left off:

```yaml
classes:
  GoCamAnnotations:
    tree_root: true
    attributes:
      genes:
        description: semicolon-separated list of genes
        multivalued: true
        range: Gene
      organisms:
        description: semicolon-separated list of organism taxons
        multivalued: true
        range: Organism
      gene_organisms:
        annotations:
          prompt: semicolon-separated list of asterisk separated gene to organism relationships
        multivalued: true
        range: GeneOrganismRelationship
      activities:
        description: semicolon-separated list of molecular activities
        multivalued: true
        range: MolecularActivity
      gene_functions:
        description: semicolon-separated list of gene to molecular activity relationships
        multivalued: true
        range: GeneMolecularActivityRelationship
      cellular_processes:
        description: semicolon-separated list of cellular processes
        multivalued: true
        range: CellularProcess
      pathways:
        description: semicolon-separated list of pathways
        multivalued: true
        range: Pathway
      gene_gene_interactions:
        description: semicolon-separated list of gene to gene interactions
        multivalued: true
        range: GeneGeneInteraction
      gene_localizations:
        description: >-
          semicolon-separated list of genes plus their location in the cell;
          for example, "gene1 / cytoplasm; gene2 / mitochondrion"
        multivalued: true
        range: GeneSubcellularLocalizationRelationship

  Gene:
    is_a: NamedEntity
    id_prefixes:
      - HGNC
      - PR
      - UniProtKB
    annotations:
      annotators: gilda:, bioportal:hgnc-nr
  Pathway:
    is_a: NamedEntity
    id_prefixes:
      - GO
      - PW
    annotations:
      annotators: sqlite:obo:go, sqlite:obo:pw
  CellularProcess:
    is_a: NamedEntity
    id_prefixes:
      - GO
    annotations:
      annotators: sqlite:obo:go
  MolecularActivity:
    is_a: NamedEntity
    id_prefixes:
      - GO
    annotations:
      annotators: sqlite:obo:go
  GeneLocation:
    is_a: NamedEntity
    id_prefixes:
      - GO
      - CL
      - UBERON
    annotations:
      annotators: "sqlite:obo:go, sqlite:obo:cl"
    slot_usage:
      id:
        values_from:
          - GOCellComponentType
          - CellType
  Organism:
    is_a: NamedEntity
    id_prefixes:
      - NCBITaxon
      - EFO
    annotations:
      annotators: gilda:, sqlite:obo:ncbitaxon
  Molecule:
    is_a: NamedEntity
    id_prefixes:
      - CHEBI
      - PR
    annotations:
      annotators: gilda:, sqlite:obo:chebi

  GeneOrganismRelationship:
    is_a: CompoundExpression
    attributes:
      gene:
        range: Gene
      organism:
        range: Organism

  GeneMolecularActivityRelationship:
    is_a:   CompoundExpression
    attributes:
      gene:
        range: Gene
        annotations:
          prompt: the name of the gene in the pair. This comes first.
      molecular_activity:
        range: MolecularActivity
        annotations:
          prompt: the name of the molecular function in the pair. This comes second. May be a GO term.
    annotations:
      prompt.example: |-
        TODO
        
        gene: HGNC:1234
        molecular_activity: GO:0003674

  GeneMolecularActivityRelationship2:
    is_a:   CompoundExpression
    attributes:
      gene:
        range: Gene
        annotations:
          prompt: the name of the gene.
      molecular_activity:
        range: MolecularActivity
        annotations:
          prompt: the name of the molecular activity, for example, ubiquitination. May be a GO term.
      target:
        range: Molecule
        annotations:
          prompt: the name of the molecular entity that is the target of the molecular activity.

  GeneSubcellularLocalizationRelationship:
    is_a:   CompoundExpression
    attributes:
      gene:
        range: Gene
      location:
        range: GeneLocation

  GeneGeneInteraction:
    is_a:   CompoundExpression
    attributes:
      gene1:
        range: Gene
      gene2:
        range: Gene

enums:

  GeneLocationEnum:
    inherits:
      - GOCellComponent
      - CellType

  GOCellComponentType:
    reachable_from:
      source_ontology: obo:go
      source_nodes:
        - GO:0005575 ## cellular_component
  CellType:
    reachable_from:
      source_ontology: obo:cl
      source_nodes:
        - CL:0000000 ## cell
```

* Prompt hints can be specified using the `prompt` annotation (otherwise description is used)
* Multivalued fields are supported
* The default range is string — these are not grounded. Ex.: disease name, synonyms
* Define a class for each `NamedEntity`
* For any `NamedEntity`, you can specify a preferred annotator using the `annotators` annotation

We recommend following an established schema like [BioLink Model](https://github.com/biolink/biolink-model), but you can define your own.

Next step is to compile the schema. For that, you should place the schema YAML in the directory [src/ontogpt/templates/](src/ontogpt/templates/). Then, run the `make` command at the top level. This will compile the schema to Python (Pydantic classes).

Once you have defined your own schema / data model and placed in the correct directory, you can run the `extract` command.

Ex.:

```bash
ontogpt extract -t mendelian_disease.MendelianDisease -i marfan-wikipedia.txt
```

### Multiple levels of nesting

Currently no more than two levels of nesting are recommended.

If a field has a range which is itself a class and not a primitive, it will attempt to nest.

Ex. the `gocam` schema has an attribute:

```yaml
  attributes:
      ...
      gene_functions:
        description: semicolon-separated list of gene to molecular activity relationships
        multivalued: true
        range: GeneMolecularActivityRelationship
```

The range `GeneMolecularActivityRelationship` has been specified _inline_, so it will nest.

The generated prompt is:

```bash
gene_functions : <semicolon-separated list of gene to molecular activities relationships>
```

The output of this is then passed through further SPIRES iterations.

### Text length limit

LLMs have context sizes limiting the combined length of their inputs and outputs. The `gpt-3.5-turbo` model, for example, has a 4,096 token limit (prompt + completion), while the `gpt-3.5-turbo-16k` model has a larger context of 16,384 tokens.

### Schema tips

It helps to have an understanding of the [LinkML](https://linkml.io) schema language, but it should be possible to define your own schemas using the examples in [src/ontogpt/templates](src/ontogpt/templates/) as a guide.

OntoGPT-specific extensions are specified as _annotations_.

You can specify a set of annotators for a field using the `annotators` annotation.

Ex.:

```yaml
  Gene:
    is_a: NamedThing
    id_prefixes:
      - HGNC
    annotations:
      annotators: gilda:, bioportal:hgnc-nr, obo:pr
```

The annotators are applied in order.

Additionally, when performing grounding, the following measures can be taken to improve accuracy:

* Specify the valid set of ID prefixes using `id_prefixes`
* Some vocabularies have structural IDs that are amenable to regexes, you can specify these using `pattern`
* You can make use of `values_from` slot to specify a [Dynamic Value Set](https://linkml.io/linkml/schemas/enums.html#dynamic-enums)
  * For example, you can constrain the set of valid locations for a gene product to be subclasses of `cellular_component` in GO or `cell` in CL

Ex.:

```yaml
classes:
  ...
  GeneLocation:
    is_a: NamedEntity
    id_prefixes:
      - GO
      - CL
    annotations:
      annotators: "sqlite:obo:go, sqlite:obo:cl"
    slot_usage:
      id:
        values_from:
          - GOCellComponentType
          - CellType

enums:
  GOCellComponentType:
    reachable_from:
      source_ontology: obo:go
      source_nodes:
        - GO:0005575 ## cellular_component
  CellType:
    reachable_from:
      source_ontology: obo:cl
      source_nodes:
        - CL:0000000 ## cell
```

## Install a custom schema

If you have installed OntoGPT directly from its GitHub repository, then you may install a custom schema like this:

1. Move the schema file to the `src/ontogpt/templates` directory.
2. Run `make` from the root of the repository to generate Pydantic versions of the schema.

If you have installed OntoGPT from `pip`, _or_ if you can't use the `make` command, the process is similar, though it will depend on where the package is installed.

1. Use the LinkML `gen-pydantic` tool to generate Pydantic classes. If your schema is named `alfred.yaml`, then run the following:
  
    ```bash
    gen-pydantic --pydantic_version 2 alfred.yaml > alfred.py
    ```

2. Move both the .yaml and the .py versions of your schema to the `templates` directory of wherever OntoGPT is installed. In a virtual environment named `temp` that may be something like `/temp/lib/python3.9/site-packages/ontogpt/templates`.

You may then use the schema like any other. For example, if your schema is named `albatross.yaml`, then an extract command is:

```bash
ontogpt extract -t albatross -i input.txt
```
