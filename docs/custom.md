# Custom Schemas

## Build a custom schema

There are a number of pre-defined LinkML data models already developed here - [src/ontogpt/templates/](src/ontogpt/templates/) which you can use as reference when creating your own data models.

Define a schema (using a subset of [LinkML](https://linkml.io)) that describes the structure in which you want to extract knowledge from your text.

An example:

```yaml
classes:
  MendelianDisease:
    attributes:
      name:
        description: the name of the disease
        examples:
          - value: peroxisome biogenesis disorder
        identifier: true  ## needed for inlining
      description:
        description: a description of the disease
        examples:
          - value: >-
            Peroxisome biogenesis disorders, Zellweger syndrome spectrum (PBD-ZSS) is a group of autosomal recessive disorders affecting the formation of functional peroxisomes, characterized by sensorineural hearing loss, pigmentary retinal degeneration, multiple organ dysfunction and psychomotor impairment
      synonyms:
        multivalued: true
        examples:
          - value: Zellweger syndrome spectrum
          - value: PBD-ZSS
      subclass_of:
        multivalued: true
        range: MendelianDisease
        examples:
          - value: lysosomal disease
          - value: autosomal recessive disorder
      symptoms:
        range: Symptom
        multivalued: true
        examples:
          - value: sensorineural hearing loss
          - value: pigmentary retinal degeneration
      inheritance:
        range: Inheritance
        examples:
          - value: autosomal recessive
      genes:
        range: Gene
        multivalued: true
        examples:
          - value: PEX1
          - value: PEX2
          - value: PEX3

  Gene:
    is_a: NamedThing
    id_prefixes:
      - HGNC
    annotations:
      annotators: gilda:, bioportal:hgnc-nr

  Symptom:
    is_a: NamedThing
    id_prefixes:
      - HP
    annotations:
      annotators: sqlite:obo:hp

  Inheritance:
    is_a: NamedThing
    annotations:
      annotators: sqlite:obo:hp
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
