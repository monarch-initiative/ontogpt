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

WIP