# TALISMAN

## Introduction

_TALISMAN_ is a Python package for summarizing gene set functions using large language models (LLMs).

It uses the OntoGPT package to interface with LLMs.

[For more details, please see the full documentation.](https://monarch-initiative.github.io/talisman/)

## Quick Start

TBD

## Functionality

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

## Citation

The gene summarization approach used in TALISMAN is described further in: Joachimiak MP, Caufield JH, Harris NL, Kim H, Mungall CJ. Gene Set Summarization using Large Language Models. arXiv publication: <http://arxiv.org/abs/2305.13338>

## Acknowledgements

This project is part of the [Monarch Initiative](https://monarchinitiative.org/).
