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

Use the option `--cache-db` to specify the directory where the cache should be stored.

LiteLLM saves prompts and responses to this cache. It is always enabled.

If this value is not provided, the cache (named `cache.db`) will be written to a directory named `.litellm_cache` in your current working directory.

Specifying an absolute path will work best here.

### skip-annotator

Use the option `--skip-annotator` to skip one or more annotators (e.g. `--skip-annotator gilda`).

## Common Parameters

The following options are available for most functions unless stated otherwise.

### inputfile

Use the option `--inputfile` to specify a path to a file containing input text.

For the `extract` command, this may be a single file or a directory of files.

In the latter case, all files in the following formats will be assumed to be input:

```txt
".csv", ".tsv", ".txt", ".od", ".odf", ".ods", ".pdf", ".xls", ".xlsx"
```

The path will *not* be parsed recursively.

When parsing PDF files, use the `use-pdf` option as described below.

When parsing tabular files like tsv or xlsx, you may specify exact columns to load with the `selectcols` option as described below.

### template

Use the option `--template` to specify a template to use. This is a required parameter.

Only the name is required, without any filename suffix, unless you are using a custom schema for the first time. In that case, provide the path to the schema, including the .yaml file extension.

To use the `gocam` template, for example, the parameter will be `--template gocam`

Or, for a custom template, the parameter may be `--template custom.yaml`

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

Note this will list all models available across a variety of sources - API keys will still be required to access many.

The name in the first column is the model name to be used with the `--model` option, e.g., `--model mistral/mistral-medium`.

### recurse

Use the option `recurse` to specify whether recursion should be used when parsing the schema.

Recursion is on by default.

Disable it with `--no-recurse`.

### use-pdf

Use the option `use-pdf` to specify whether to extract text from a PDF.

This is done through the `pymupdf` package.

Example:

```bash
ontogpt extract -i temp/test1.pdf -m gpt-4o --use-pdf -t composite_disease --output-format json -o test.json
```

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

### api-base

Use the option `api-base` to specify a base URL to use for your LLM API, e.g. for the Azure OpenAI API.

Note this may also be set through the runoak set-apikey command (e.g., `runoak set-apikey -e azure-base`)

### api-version

Use the option `api-version` to specify an API version to use for your LLM API, e.g. for the Azure OpenAI API.

Note this may also be set through the runoak set-apikey command (e.g., `runoak set-apikey -e azure-version`)

### model-provider

Use the option `model-provider` to specify a provider if not specified in the model name.

For example, if using a proxy using the OpenAI API format, this should be set to 'openai'

### temperature

Use the option `temperature` to specify the temperature the model should generate using.

The range may vary per model, but for the OpenAI API this value must range from 0 to 2, with a default of 1.0.

Higher temperatures generally correspond to greater randomness, which may be desirable.

### cut-input-text

Use the option `cut-input-text` to truncate all input_text in output to 1000 characters each.

This can be useful when processing many inputs and/or full texts, as without this option the full input will be included.

### system-message

Use the option `system-message` to pass a system-level message to the LLM.

For example, with an input file named `greeting.txt` containing "How are you today":

```bash
$ ontogpt complete -m llama-3 -i greeting.txt
I'm just a language model, I don't have emotions or feelings like humans do, so I don't have good or bad days. I'm always here and ready to chat with you, 24/7! How can I assist you today?
$ ontogpt complete -m llama-3 -i greeting.txt --system-message "You are very grumpy today"
*grumble grumble* I'm terrible, thanks for asking. Everything is just so... annoying. The sun is shining too brightly, the birds are singing too loudly, and the air is filled with the scent of... *sigh*... everything. Just, ugh. Can't anyone just leave me alone for once? What's it to you, anyway? *mutter mutter*
```

Including an instruction like the following anecdotally helps to avoid parsing failures due to the LLM getting creative with result formatting:

```bash
--system-message "You are going to extract information from text in the specified format. You will not deviate from the format; do not provide results in JSON format."
```

### selectcols

Use the option `selectcols` to specify exact columns to use when parsing tabular files as input.

Example:

```bash
ontogpt extract -t food -i inputs/myfile.tsv -o output.yaml --selectcols cheeses,grapes,flavors
```

## Functions

### categorize-mappings

Categorize a collection of mappings in the Simple Standard for Sharing Ontological Mappings (SSSOM) format.

Mappings in this format may not include their specific mapping types (e.g., broad or close mappings).

This function will attempt to apply more specific mappings wherever possible.

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

*This command has been deprecated. It is now available through the TALISMAN package at:* <https://github.com/monarch-initiative/talisman>

### create-gene-set

*This command has been deprecated. It is now available through the TALISMAN package at:* <https://github.com/monarch-initiative/talisman>

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

*This command has been deprecated. It is now available through the TALISMAN package at:* <https://github.com/monarch-initiative/talisman>

### entity-similarity

Determine similarity between ontology entities by comparing their embeddings.

Options:

* `-r`, `--ontology TEXT` - name of the ontology to use. This should be an OAK adapter name such as "sqlite:obo:hp".
* `--definitions` / `--no-definitions` - Include text definitions in the text to embed. Defaults to True.
* `--parents` / `--no-parents` - Include is-a parent terms in the text to embed. Defaults to True.
* `--ancestors` / `--no-ancestors` - Include all ancestors in the text to embed. Defaults to True.
* `--logical-definitions` / `--no-logical-definitions`- Include logical definitions in the text to embed. Defaults to True.
* `--autolabel` / `--no-autolabel` - Add labels to each subject and object identifier. Defaults to True.
* `--synonyms` / `--no-synonyms` - Include synonyms in the text to embed. Defaults to True.

Example:

```bash
ontogpt entity-similarity -r sqlite:obo:hp HP:0012228 HP:0000629
```

In this case, the output will look like this:

```text
subject_id      subject_label   object_id       object_label    embedding_cosine_similarity     object_rank_for_subject
HP:0012228      Tension-type headache   HP:0012228      Tension-type headache   0.9999999999999999      0
HP:0012228      Tension-type headache   HP:0000629      Periorbital fullness    0.7755551231762359      1
HP:0000629      Periorbital fullness    HP:0000629      Periorbital fullness    1.0000000000000002      0
HP:0000629      Periorbital fullness    HP:0012228      Tension-type headache   0.7755551231762359      1
```

### eval

Evaluate an extractor.

See the Evaluations section for more details.

Options:

* `--num-tests INTEGER` - number of test iterations to cycle through. Defaults to 5.
* `--chunking` / `--no-chunking` - If set, chunk input text, then prepare a separate prompt for each chunk. Otherwise the full input text is passed. Defaults to False.

Example:

```bash
ontogpt eval --num-tests 1 EvalCTD
```

### eval-enrichment

*This command has been deprecated. It is now available through the TALISMAN package at:* <https://github.com/monarch-initiative/talisman>

### extract

Extract knowledge from text guided by a schema.

This is OntoGPT's implementation of SPIRES.

Output includes the input text (or a truncated part), the raw completion output, the prompt (specifically, the last iteration of the prompts used), and an extracted object containing all parts identified in the input text, as well as a list of named entities and their labels.

Options:

* `-S`, `--set-slot-value TEXT` - Set slot value manually, e.g., `--set-slot-value has_participant=protein`

Examples:

```bash
ontogpt extract -t gocam.GoCamAnnotations -i tests/input/cases/gocam-33246504.txt
```

In this case, you will an extracted object in the output like:

```yaml
extracted_object:
  genes:
    - HGNC:5992
    - AUTO:F4/80
    - HGNC:16400
    - HGNC:1499
    - HGNC:5992
    - HGNC:5993
  organisms:
    - NCBITaxon:10088
    - AUTO:bone%20marrow-derived%20macrophages
    - AUTO:astrocytes
    - AUTO:bipolar%20cells
    - AUTO:vascular%20cells
    - AUTO:perivascular%20MPs
  gene_organisms:
    - gene: HGNC:5992
      organism: AUTO:mononuclear%20phagocytes
    - gene: HGNC:16400
      organism: AUTO:F4/80%2B%20mononuclear%20phagocytes
    - gene: HGNC:1499
      organism: AUTO:F4/80%2B%20mononuclear%20phagocytes
    - gene: HGNC:5992
      organism: AUTO:perivascular%20macrophages
    - gene: HGNC:5993
      organism: AUTO:None
  activities:
    - GO:0006954
    - AUTO:photoreceptor%20death
    - AUTO:retinal%20function
  gene_functions:
    - gene: HGNC:5992
      molecular_activity: GO:0006954
    - gene: AUTO:F4/80
      molecular_activity: AUTO:mononuclear%20phagocyte%20recruitment
    - gene: HGNC:1499
      molecular_activity: GO:0006954
    - gene: HGNC:5992
      molecular_activity: AUTO:immune-specific%20expression
    - gene: HGNC:5993
      molecular_activity: AUTO:IL-1%CE%B2%20receptor
    - gene: AUTO:rytvela
      molecular_activity: AUTO:IL-1R%20modulation
    - gene: AUTO:Kineret
      molecular_activity: AUTO:IL-1R%20antagonism
  cellular_processes:
    - AUTO:macrophage-induced%20photoreceptor%20death
  gene_localizations:
    - gene: HGNC:5992
      location: AUTO:subretinal%20space
```

Or, we can extract information about a drug and specify which model to use:

```bash
ontogpt extract -t drug -i tests/input/cases/drug-DB00316-moa.txt --auto-prefix UNKNOWN -m gpt-4
```

The `ontology_class` schema may be used to perform more domain-agnostic entity recognition, though this is generally incompatible with grounding.

```bash
ontogpt extract -t ontology_class -i tests/input/cases/human_urban_green_space.txt
```

### fill

Fill in missing values.

Requires the path to a file containing a data object to be passed (as an argument) and a set of examples as an input file.

Options:

* `-E`, `--examples FILENAME` - Path to a file of example objects.

### generate-extract

Generate text and then extract knowledge from it.

This command runs two operations:

1. Generate a natural language description of something
2. Parse the generated description using SPIRES

For example, given a cell type such as [Acinar Cell Of Salivary Gland](https://cellxgene.cziscience.com/cellguide/CL_0002623), generate a description using GPT describing many aspects of the cell type, from its marker genes through to its function and diseases it is implicated in.

After that, use the [cell-type schema](https://w3id.org/ontogpt/cell_type) to extract this into structured form.

As an optional next step use [linkml-owl](https://github.com/linkml/linkml-owl) to generate OWL TBox axioms.

See also: `iteratively-generate-extract` below.

Example:

```bash
ontogpt generate-extract -t cell_type CL:0002623
```

### iteratively-generate-extract

Iterate through generate-extract.

This runs the `generate-extract` command in iterative mode. It will traverse the extracted subtypes with each iteration, gradually building up an ontology that is entirely generated from the "latent knowledge" in the LLM.

Currently each iteration is independent so the method remains unaware as to whether it has already made a concept. Ungrounded concepts may indicate gaps in available knowledgebases.

Unlike the `generate-extract` command, this command requires some additional parameters to be specified.

Please specify the input ontology and the output path.

Options:

* `-r`, `--ontology TEXT` - Ontology to use. Use the OAK selector format, e.g., "sqlite:obo:cl"
* `-M`, `--max-iterations INTEGER` - Maximum number of iterations.
* `-I`, `--iteration-slot TEXT` - Slots to iterate over.
* `-D`, `--db TEXT` - Path to the output, in YAML format.
* `--clear` / `--no-clear` - If set, clear the output database before starting. Defaults to False.

Example:

```bash
ontogpt iteratively-generate-extract -t cell_type -r sqlite:obo:cl -D cells.yaml CL:0002623 
```

### list-models

List all available models. These will include all models `litellm` knows about, but may not include all local models present on your system (use `ollama list` to see those).

Example:

```bash
ontogpt list-models
```

### list-templates

List the templates.

Alternatively, run `make list_templates`.

Example:

```bash
ontogpt list-templates
```

### pubmed-annotate

Retrieve a collection of PubMed IDs for a given search, then perform extraction on them with SPIRES.

The search argument will accept all parameters known to PubMed search, such as filtering by publication year.

Works for single publications, too - set the `--limit` parameter to 1 and specify a PubMed ID as the search argument.

Options:

* `--limit INTEGER` - Total number of citation records to return. Limited by the NCBI API.
* `--get-pmc` / `--no-get-pmc` - Attempt to parse PubMed Central full text(s) rather than abstract(s) alone.

Examples:

```bash
ontogpt pubmed-annotate -t phenotype "Takotsubo Cardiomyopathy: A Brief Review" --get-pmc --model gpt-4o --limit 3
```

```bash
ontogpt pubmed-annotate -t environmental_sample "33126925" --limit 1
```

```bash
ontogpt pubmed-annotate -t composite_disease "(earplugs) AND (("1950"[Date - Publication] : "1990"[Date - Publication]))" --limit 4
```

### pubmed-extract

Extract knowledge from a single PubMed ID.

_DEPRECATED_ - use `pubmed-annotate` instead.

### recipe-extract

Extract from a recipe on the web.

This uses the `recipe` template and the [recipe_scrapers](https://github.com/hhursev/recipe-scrapers) package. The latter supports many different recipe web sites, so give your favorite a try.

Pass a URL as the argument, or use the -R option to specify the path to a file containing one URL per line.

Options:

* `-R`, `--recipes-urls-file TEXT` - File with URLs to recipes to use for extraction.

Example:

```bash
ontogpt recipe-extract https://www.allrecipes.com/recipe/17445/grilled-asparagus/
```

In this case, expect an extracted object like the following:

```yaml
extracted_object:
  url: https://www.allrecipes.com/recipe/17445/grilled-asparagus/
  label: Grilled Asparagus
  description: Grilled asparagus with olive oil, salt, and pepper.
  categories:
    - AUTO:None
  ingredients:
    - food_item:
        food: FOODON:03311349
        state: fresh, spears
      amount:
        value: '1'
        unit: UO:0010034
    - food_item:
        food: FOODON:03301826
      amount:
        value: '1'
        unit: UO:0010042
    - food_item:
        food: AUTO:salt
        state: and pepper
      amount:
        value: N/A
        unit: AUTO:N/A
  steps:
    - action: AUTO:Preheat
      inputs:
        - food: AUTO:outdoor%20grill
          state: None
      outputs:
        - food: AUTO:None
          state: None
      utensils:
        - AUTO:None
    - action: dbpediaont:season
      inputs:
        - food: FOODON:00003458
          state: coated
        - food: AUTO:salt
          state: None
        - food: FOODON:00003520
      outputs:
        - food: FOODON:00003458
          state: seasoned
      utensils:
        - AUTO:None
    - action: AUTO:cook
      inputs:
        - food: FOODON:03311349
          state: None
      outputs:
        - food: FOODON:03311349
          state: cooked
      utensils:
        - AUTO:grill
```

### suggest-template

Suggest a template for a stated topic or purpose.

This uses an LLM, so all options supported by the `extract` or `complete` functions are usable here as well.

Example:

```bash
ontogpt suggest-template "Takotsubo Cardiomyopathy"
```

In this case, expect a response like this:

```
The most appropriate template for the topic of Takotsubo Cardiomyopathy would be the composite_disease template. This template is specifically designed for representing composite disease concepts, which fits well with the complex nature of Takotsubo Cardiomyopathy.
```

### synonyms

Extract synonyms, based on embeddings.

The context parameter is required.

Options:

* `-C`, `--context TEXT` - domain, e.g., anatomy, industry, health-related

Example:

```bash
ontogpt synonyms --context astronomy star
```

### text-distance

Embed text and calculate euclidian distance between the embeddings.

The terms must be separated by an `@` character.

Options:

* `-C`, `--context TEXT` - domain, e.g., anatomy, industry, health-related

Example:

```bash
ontogpt text-distance pancakes @ syrup
```

### text-similarity

Like `text-distance`, this command compares the embeddings of input terms.

This command returns the cosine similarity of the embedding vectors.

Options:

* `-C`, `--context TEXT` - domain, e.g., anatomy, industry, health-related

Example:

```bash
ontogpt text-similarity basketball @ basket-weaving
```

### web-extract

Extract knowledge from web page.

Pass a URL as an argument and OntoGPT will use the SPIRES method to extract information based on the specified template.

Because this depends upon scraping a page, results may vary depending on a site's complexity and structure.

Even relatively short pages may exceed a model's context size, so larger context models may be necessary.

Example:

```bash
ontogpt web-extract -t reaction.Reaction -m gpt-4o https://www.scienceofcooking.com/maillard_reaction.htm 
```

### wikipedia-extract

Extract knowledge from a Wikipedia page.

Pass an article title as an argument and OntoGPT will use the SPIRES method to extract information based on the specified template.

Even relatively short pages may exceed a model's context size, so larger context models may be necessary.

Example:

```bash
ontogpt wikipedia-extract -t mendelian_disease.MendelianDisease -m gpt-4o  "Cartilage–hair hypoplasia"
```

### wikipedia-search

Extract knowledge from Wikipedia pages based on a search.

Pass a search phrase as an argument and OntoGPT will use the SPIRES method to extract information based on the specified template.

Even relatively short pages may exceed a model's context size, so larger context models may be necessary.

Example:

```bash
ontogpt wikipedia-search -t biological_process -m gpt-4o "digestion"
```
