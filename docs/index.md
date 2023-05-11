# OntoGPT

Generation of Ontologies and Knowledge Bases using GPT

A knowledge extraction tool that uses a large language model (LLM) to extract semantic information from text.

This exploits the ability of LLMs such as GPT-3 to return user-defined data structures as a response.

Currently there are two different pipelines implemented:

- SPIRES: Structured Prompt Interrogation and Recursive Extraction of Semantics
    - Zero-shot learning approach to extracting nested semantic structures from text
    - Inputs: LinkML schema + text
    - Outputs: JSON, YAML, or RDF or OWL that conforms to the schema
- HALO: HAllucinating Latent Ontologies 
    - Few-shot learning approach to generating/hallucinating a domain ontology given a few examples

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

(see [full input](https://github.com/monarch-initiative/ontogpt/blob/main/tests/input/cases/gocam-betacat.txt))

We can extract this into the [GO pathway datamodel](https://github.com/monarch-initiative/ontogpt/blob/main/src/ontogpt/templates/gocam.yaml):

```bash
ontogpt extract -t gocam.GoCamAnnotations abstract.txt
```

Giving schema-compliant YAML such as:

```yaml
genes:
- HGNC:2514
- HGNC:21367
- HGNC:27962
- AUTO:US3
- FPLX:Interferon
- AUTO:ISG
gene_gene_interactions:
- gene1: AUTO:US3
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

See [full output](https://github.com/monarch-initiative/ontogpt/blob/main/tests/output/gocam-betacat.yaml).

Ungrounded named entities appear as text preceded by AUTO (or your preferred prefix, provided with the --auto-prefix option when using the extract command).

## How it works

1. You provide an arbitrary data model, describing the structure you want to extract text into
    - this can be nested (but see limitations below)
2. Provide your preferred annotations for grounding NamedEntity fields
3. OntoGPT will:
    - generate a prompt
    - feed the prompt to a language model (currently one of OpenAI's models)
    - parse the results into a dictionary structure
    - ground the results using a preferred annotator

## Pre-requisites

- Python 3.9+
- an OpenAI account
- a BioPortal account (optional, for grounding)

You will need to set both API keys using OAK (which is a dependency of this project) as:

```
poetry run runoak set-apikey -e openai <your openai api key>
poetry run runoak set-apikey -e bioportal <your bioportal api key>
```

## How to define your own extraction data model

### Step 1: Define a schema

See [src/ontogpt/templates/](https://github.com/monarch-initiative/ontogpt/tree/main/src/ontogpt/templates) for examples.

Define a schema (using a subset of [LinkML](https://linkml.io/)) that describes the structure you want to extract from your text.

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

- The schema is defined in LinkML.
- Prompt hints can be specified using the `prompt` annotation (otherwise description is used).
- Multivalued fields are supported.
- The default range is string - these are not grounded, e.g., disease name, synonyms.
- Define a class for each NamedEntity.
- For any NamedEntity, you can specify one or more preferred annotators using the `annotators` annotation.

We recommend following an established schema like [Biolink Model](https://biolink.github.io/biolink-model/), but you can define your own.

### Step 2: Compile the schema

Run the `make` command at the top level. This will compile the schemas in the templates directory to Pydantic classes.

Alternatively, run `make src/templates/{name_of_schema}.py` to compile just this schema.
For example, if your schema is defined within `entities.yaml`, run `make src/templates/entities.py`.

### Step 3: Run the command line

e.g.

```
ontogpt extract -t mendelian_disease.MendelianDisease marfan-wikipedia.txt
```

## Web Application

There is a bare bones web application for running OntoGPT and viewing results.

Install the required dependencies first with the following command:
```
poetry install -E web
```

Then run the following command to start the web application:

```
poetry run web-ontogpt
```

Note that the agent running uvicorn must have the API key set, so for obvious reasons
don't host this publicly without authentication, unless you want your credits drained.

## Features

### Multiple Levels of nesting

Currently no more than two levels of nesting are recommended.

If a field has a range which is itself a class and not a primitive, it will attempt to nest

E.g. the [GO-CAM](http://geneontology.org/docs/gocam-overview/) schema has an attribute:

```yaml
  attributes:
      ...
      gene_functions:
        description: semicolon-separated list of gene to molecular activity relationships
        multivalued: true
        range: GeneMolecularActivityRelationship
```

Because GeneMolecularActivityRelationship is *inlined* it will nest.

The generated prompt is:

`gene_functions : <semicolon-separated list of gene to molecular activities relationships>`

The output of this is then passed through further llama iterations.

## Text length limit

Currently SPIRES must use text-davinci-003, which has a total 4k token limit (prompt + completion).

You can pass in a parameter to split the text into chunks, results will be recombined automatically,
but more experiments need to be done to determined how reliable this is.

```

## HALOE: Usage

TODO

## Limitations

### Non-deterministic

This relies on an existing LLM, and LLMs can be fickle in their responses.

### Coupled to OpenAI

At present, you will need an OpenAI account.


# Acknowledgements

This [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html) project was developed from the [sphintoxetry-cookiecutter](https://github.com/hrshdhgd/sphintoxetry-cookiecutter) template and will be kept up-to-date using [cruft](https://cruft.github.io/cruft/).
