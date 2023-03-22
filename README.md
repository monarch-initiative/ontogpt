# OntoGPT

Generation of Ontologies and Knowledge Bases using GPT

A knowledge extraction tool that uses a large language model to extract semantic information from text.

This makes use of so-called *instruction prompts* in Large Language Models (LLMs) such as GPT-4.

Currently there are two different pipelines implemented:

- SPIRES: Structured Prompt Interrogation and Recursive Extraction of Semantics
    - Zero-shot learning approach to extracting nested semantic structures from text
    - Inputs: LinkML schema + text
    - Outputs: JSON, YAML, or RDF or OWL that conforms to the schema
    - Uses text-davinci-003
- HALO: HAllucinating Latent Ontologies 
    - Few-shot learning approach to generating/hallucinating a domain ontology given a few examples
    - Uses code-davinci-002

## SPIRES: Usage

Given a short text `abstract.txt` with content such as:

   > The cGAS/STING-mediated DNA-sensing signaling pathway is crucial
   for interferon (IFN) production and host antiviral
   responses
   > 
   > ...
   > [snip] 
   > ...
   > 
   > The underlying mechanism was the
   interaction of US3 with β-catenin and its hyperphosphorylation of
   β-catenin at Thr556 to block its nuclear translocation
   > ...
   > ...

(see [full input](tests/input/cases/gocam-betacat.txt))

We can extract this into the [GO pathway datamodel](src/ontogpt/templates/gocam.yaml):

```bash
ontogpt extract -t gocam.GoCamAnnotations abstract.txt
```

Giving schema-compliant yaml such as:

```yaml
genes:
- HGNC:2514
- HGNC:21367
- HGNC:27962
- US3
- FPLX:Interferon
- ISG
gene_gene_interactions:
- gene1: US3
  gene2: HGNC:2514
gene_localizations:
- gene: HGNC:2514
  location: Nuclear
gene_functions:
- gene: HGNC:2514
  molecular_activity: Transcription
- gene: HGNC:21367
  molecular_activity: Production
...
```

See [full output](tests/output/gocam-betacat.yaml)

Note in the above the grounding is very preliminary and can be improved. Ungrounded NamedEntities appear as text.

## How it works

1. You provide an arbitrary data model, describing the structure you want to extract text into
    - this can be nested (but see limitations below)
2. provide your preferred annotations for grounding NamedEntity fields
3. ontogpt will:
    - generate a prompt
    - feed the prompt to a language model (currently OpenAI)
    - parse the results into a dictionary structure
    - ground the results using a preferred annotator

## Pre-requisites

- python 3.9+
- an OpenAI account
- a BioPortal account (optional, for grounding)

You will need to set both API keys using OAK (which is a dependency of this project)

```
poetry run runoak set-apikey -e openai <your openai api key>
poetry run runoak set-apikey -e bioportal <your bioportal api key>
```

## How to define your own extraction data model

### Step 1: Define a schema

See [src/ontogpt/templates/](src/ontogpt/templates/) for examples.

Define a schema (using a subset of [LinkML](https://linkml.io)) that describes the structure you want to extract from your text.

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

- the schema is defined in LinkML
- prompt hints can be specified using the `prompt` annotation (otherwise description is used)
- multivalued fields are supported
- the default range is string - these are not grounded. E.g. disease name, synonyms
- define a class for each NamedEntity
- for any NamedEntity, you can specify a preferred annotator using the `annotators` annotation

We recommend following an established schema like Biolink, but you can define your own.

### Step 2: Compile the schema

Run the `make` command at the top level. This will compile the schema to pedantic

### Step 3: Run the command line

e.g.

```
ontogpt extract -t mendelian_disease.MendelianDisease marfan-wikipedia.txt
```

## Web Application

There is a bare bones web application

```
poetry run web-ontogpt
```

Note that the agent running uvicorn must have the API key set, so for obvious reasons
don't host this publicly without authentication, unless you want your credits drained. 

## Features

### Multiple levels of nesting

Currently no more than two levels of nesting are recommended.

If a field has a range which is itself a class and not a primitive, it will attempt to nest

E.g. the gocam schema has an attribute:

```yaml
  attributes:
      ...
      gene_functions:
        description: semicolon-separated list of gene to molecular activity relationships
        multivalued: true
        range: GeneMolecularActivityRelationship
```

Because GeneMolecularActivityRelationship is *inlined* it will nest

The generated prompt is:

`gene_functions : <semicolon-separated list of gene to molecular activities relationships>`

The output of this is then passed through further SPIRES iterations.

### Text length limit

Currently SPIRES must use text-davinci-003, which has a total 4k token limit (prompt + completion).

You can pass in a parameter to split the text into chunks, results will be recombined automatically,
but more experiments need to be done to determined how reliable this is.

## Schema Tips

It helps to have an understanding of the [LinkML](https://linkml.io) schema language, but it should be possible
to define your own schemas using the examples as a guide.

OntoGPT-specific extensions are specified as *annotations*

You can specify a set of annotators for a field using the `annotators` annotation

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

- specify the valid set of ID prefixes using `id_prefixes`
- some vocabularies have structural IDs that are amenable to regexes, you can specify these using `pattern`
- you can make use of `values_from` slot to specify a [Dynamic Value Set](https://linkml.io/linkml/schemas/enums.html#dynamic-enums)
    - for example, you can constrain the set of valid locations for a gene product to be subclasses of `cellular_component` in GO or `cell` in CL.

For example:

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

## OWL Exports

The `extract` command will let you export the results as OWL axioms, utilizing linkml-owl mappings in the schema.

For example:

```bash
ontogpt extract -t recipe recipe-spaghetti.txt -o recipe-spaghetti.owl -O owl
```

See [src/ontogpt/templates/recipe.yaml](src/ontogpt/templates/recipe.yaml) 
for an example of a schema that uses linkml-owl mappings.

See the Makefile for a full pipeline that involves using robot to extract a subset of FOODON
and merge in the extracted results.

## HALO: Usage

TODO



## OntoGPT Limitations

### Non-deterministic

This relies on an existing LLM, and LLMs can be fickle in their responses.

### Coupled to OpenAI

You will need an openai account. In theory any LLM can be used but in practice the parser is tuned for OpenAI



# Acknowledgements

This [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) project was developed from the [sphintoxetry-cookiecutter](https://github.com/hrshdhgd/sphintoxetry-cookiecutter) template and will be kept up-to-date using [cruft](https://cruft.github.io/cruft/).
