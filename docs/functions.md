# OntoGPT Functions

All OntoGPT functions are run from the command line.

Precede all commands with `ontogpt`.

To see the full list of available commands, run this:

```bash
ontogpt --help
```

## Basic Parameters

To see verbose output, run:

```bash
ontogpt -v
```

The options `-vv` and `-vvv` will enable progressively more verbose output.

### cache-db

Use the option `--cache-db` to specify a path to a sqlite database to cache the prompt-completion results.

### skip-annotator

Use the option `--skip-annotator` to skip one or more annotators (e.g. `--skip-annotator gilda`).

## Common Parameters

The following options are available for most functions unless stated otherwise.

### inputfile

Use the option `--inputfile` to specify a path to a file containing input text.

### template

Use the option `--template` to specify a template to use. This is a required parameter.

Only the name is required, without any filename suffix.

To use the `gocam` template, for example, the parameter will be `--template gocam`

This may be one of the templates included with OntoGPT or a custom template, but in the latter case, the schema, generated Pydantic classes, and any imported schemas should be present in the same location.

### target-class

Use the option `--target-class` to specify a class in a schema to treat as the root.

If a schema does not already specify a root class, this is required.

Alternatively, the target class can be specified as part of the `--template` option, like so: `--template mendelian_disease.MendelianDisease`

### model

Use the option `model` to specify the name of a large language model to be used.

For example, this may be `--model gpt-4`.

Consult the full list of available models with:

```bash
ontogpt list-models
```

### recurse

Use the option `recurse` to specify whether recursion should be used when parsing the schema.

Recursion is on by default.

Disable it with `--no-recurse`.

### use-textract

Use the option `use-textract` to specify whether to use the [textract](https://textract.readthedocs.io/en/stable/) package to extract text from the input document. Textract supports retrieving raw text from PDFs, images, audio, and a variety of other formats.

Textract extraction is off by default.

Enable it with `--use-textract`.

### output

Use the option `output` to provide a path to write an output file to.

If this path is not provided, OntoGPT will write to stdout.

### output-format

Use the option `output-format` to specify the desired output file format.

This may be one of:

* html
* json
* jsonl
* md
* owl
* pickle
* turtle
* yaml

### auto-prefix

Use the option `auto-prefix` to define a prefix to use for entities without a matching namespace.

When OntoGPT's extract functions find an entity matching the input schema but cannot ground it, the entity will still be included in the output.

By default, these entities will be assigned identifiers like `AUTO:tangerine`. If you ground this term to the [Food Ontology](https://foodon.org), however, the entity may be `FOODON:00003488` instead.

### show-prompt

Use the option `show-prompt` to show _all_ prompts constructed and sent to the model. Otherwise, only the final prompt will be shown.

Showing the full prompt is off by default.

Enable it by using `--show-prompt` and setting the verbosity level to high (`-vvv`).

## Functions

### categorize-mappings

Categorize a collection of mappings in the Simple Standard for Sharing Ontological Mappings (SSSOM) format.

Example:

Using an [example SSSOM mapping collection](https://github.com/mapping-commons/sssom/blob/master/examples/embedded/mp-hp-exact-0.0.1.sssom.tsv)

```bash
ontogpt categorize-mappings -i mp-hp-exact-0.0.1.sssom.tsv
```

Note that OntoGPT will attempt to retrieve the resources specified in the mapping (in the above example, that will include HP and MP). If it cannot find a corresponding resource it will raise a HTTP 404 error.

### clinical-notes

Create mock clinical notes.

Options:

* `-d`, `--description TEXT` - a text description of the contents of the generated notes.
* `--sections TEXT` - sections to include in the generated notes, for example, medications, vital signs. Use multiple times for multiple sections, e.g., `--sections medications --sections "vital signs"`

Example:

```bash
ontogpt clinical-notes -d "middle-aged female patient with syncope and recent travel to the Amazon rainforest"
```

### complete

Prompt completion.

Given the path to a file containing text to continue, this command will simply pass it to the model as a completion task.

Example:

The file `example2.txt` contains the text "Here's a good joke about high blood pressure:"

```bash
ontogpt complete example2.txt
```

We take no responsibility for joke quality or lack thereof.

### convert

Convert output format.

Rather than a direct format translation, this function performs a full SPIRES extraction on the input file and writes the output in the specified format.

Example:

```bash
ontogpt convert -o outputfile.md -O md inputfile.yaml
```

### convert-examples

Convert training examples from YAML.

This can be necessary for performing evaluations.

Given the path to a YAML-format input file containing training examples in a format like this:

```yaml
---
examples:
    - prompt: <text prompt>
      completion: <text of completion of the prompt>
    - prompt: <another text prompt>
      completion: <text of completion of another prompt>
```

the function will convert it to equivalent JSON.

Example:

```bash
ontogpt convert-examples inputfile.yaml
```

### convert-geneset

Convert gene set to YAML.

The gene set may be in JSON (msigdb format) or text (one gene symbol per line) format.

See also the `create-gene-set` command (see below).

Options:

* `--fill` / `--no-fill` - Defaults to False (`--no-fill`). If True (`--fill`), the function will attempt to fill in missing gene values.
* `-U`, `--input-file TEXT` - Path to a file with gene IDs to enrich (if not passed as arguments).

Example:

```bash
ontogpt convert-geneset -U inputfile.json
```

### create-gene-set

Create a gene set.

This is primarily relevant to the TALISMAN method for creating gene set summaries.

It creates a gene set given a set of gene annotations in two-column TSV or GAF format.

The function also requires a single argument for the term to create the gene set with.

The output is provided in YAML format.

Options:

* `-A`, `--annotation-path TEXT` - Path to a file containing annotations.

Example:

```bash
ontogpt create-gene-set -A inputfile.tsv "positive regulation of mitotic cytokinesis"
```

### diagnose

Diagnose a clinical case represented as one or more [Phenopackets](http://phenopackets.org/).

This function takes one or more file paths as arguments, where each must contain a phenopacket in JSON format.

Example inputs may be found at the [Phenomics Exchange repository](https://github.com/phenopackets/phenomics-exchange-ig).

Example:

```bash
ontogpt diagnose case1.json case2.json 
```

### dump-completions

Dump cached completions.

OntoGPT saves queries and successful text completions to an sqlite database.

Caching is not currently supported for local models.

Use this function to retrieve the contents of this database.

See also: the `cache-db` parameter described above.

Options:

* `-m TEXT` - Match string to use for filtering.
* `-D TEXT` - Path to sqlite database.

Example:

```bash
ontogpt dump-completions -m "soup"
```

### embed

Embed text.

This function will return an embedding vector for the input text or texts.

Embedding retrieval is not currently supported for local models.

Options:

* `-C`, `--context TEXT` - domain e.g. anatomy, industry, health-related

Example:

```bash
ontogpt embed "obstreperous muskrat"
```

For OpenAI's "text-embedding-ada-002" model, the output will be a vector of length 1536, like so:

```bash
[-0.015013165771961212, -0.013102399185299873, -0.005333086010068655, ...]
```

### enrichment

Gene class summary enriching. This is OntoGPT's implementation of TALISMAN.

The goal of gene summary enrichment is to assemble a textual summary of the functions of a set of genes and their products.

TALISMAN can run in three different ways:

1. Map gene symbols to IDs using the resolver (unless IDs are specified)
2. Fetch gene descriptions using Alliance API
3. Create a prompt using descriptions

Options:

* `-r`, `--resolver TEXT` - OAK selector for the gene ID resolver, e.g., `sqlite:obo:hgnc` for HGNC gene IDs.
* `-C`, `--context TEXT` - domain, e.g., anatomy, industry, health-related
* `--strict` / `--no-strict` - If set, there must be a unique mappings from labels to IDs. Defaults to True.
* `-U`, `--input-file TEXT` - Path to a file with gene IDs to enrich if not passed as arguments.
* `--randomize-gene-descriptions-using-file TEXT` - For evaluation only. Path to a file containing gene identifiers and descriptions; if this option is used, TALISMAN will swap out gene descriptions with those from this gene set file.
* `--ontological-synopsis` / `--no-ontological-synopsis` - If set, use automated rather than manual gene descriptions. Defaults to True.
* `--combined-synopsis` / `--no-combined-synopsis` - If set, combine gene descriptions. Defaults to False.
* `--end-marker TEXT` - Specify a character or string to end prompts with. For testing minor variants of prompts.
* `--annotations` / `--no-annotations` - If set, include annotations in the prompt. Defaults to True.
* `--prompt-template TEXT` - Path to a file containing the prompt.
* `--interactive` / `--no-interactive` - Interactive mode - rather than call the API, the function will present a walkthrough process. Defaults to False.

Example:

```bash
ontogpt enrichment -r sqlite:obo:hgnc -U tests/input/genesets/EDS.yaml
```

In this case, the prompt will include gene summaries retrieved from the database.

The response text will include, among other fields, a summary like this:

```text
Summary: The common function among these genes is their involvement in the regulation and organization of the extracellular matrix, particularly collagen fibril organization and biosynthesis.
```

### entity-similarity

Embed text.

### eval

Evaluate an extractor.

### eval-enrichment

Run enrichment using multiple methods.

### extract

Extract knowledge from text guided by a schema. This is OntoGPT's implementation of SPIRES.

### fill

Fill in missing values.

### generate-extract

Generate text and then extract knowledge from it.

### halo

Run HALO over inputs.

### iteratively-generate-extract

Iterate through generate-extract.

### list-models

List all available models.

### list-templates

List the templates.

### openai-models

List OpenAI models for prompt completion.

### parse

Parse OpenAI results.

### pubmed-annotate

Retrieve a collection of PubMed IDs for a given search, then perform extraction on them with SPIRES.

### pubmed-extract

Extract knowledge from a single PubMed ID.

### reason

Reason.

### recipe-extract

Extract from recipe on the web.

### search-and-extract

Search for relevant literature and extract knowledge from it.

### synonyms

Extract synonyms.

### text-distance

Embed text and calculate euclidian distance between the embeddings.

### text-similarity

Embed text.

### web-extract

Extract knowledge from web page.

### wikipedia-extract

Extract knowledge from a Wikipedia page.

### wikipedia-search

Extract knowledge from a Wikipedia page.
