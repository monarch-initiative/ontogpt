---
name: ontogpt-extract
description: Run OntoGPT to turn unstructured text (abstracts, papers, clinical or field notes, PDFs, PubMed results) into structured, ontology-grounded data. Use when asked to extract entities, relations, or structured records from text with OntoGPT or SPIRES, to run `ontogpt extract`, to set up models and API keys for it, to batch over documents, or to read and convert its YAML/JSON output.
license: BSD-3-Clause
compatibility: Needs Python 3.10 to 3.14 with the ontogpt package installed, an LLM API key (or a local ollama server), and internet access the first time each ontology annotator is downloaded.
metadata:
  project: OntoGPT
  homepage: https://github.com/monarch-initiative/ontogpt
---

# Extracting structured data with OntoGPT

OntoGPT's job is one thing: take text in, give back objects whose fields follow a schema and whose entity values are ontology identifiers. The schema is called a **template**. The engine is **SPIRES**: it prompts an LLM field by field, parses the reply, and then **grounds** each named entity against ontologies with the Ontology Access Kit (OAK). The LLM never invents the identifiers. OAK does the lookup.

Read this file for the workflow. Read [references/cli.md](references/cli.md) for every option and [references/output-format.md](references/output-format.md) before interpreting results.

## Workflow

1. **Confirm the install and a working model.**
   ```bash
   ontogpt --version
   ontogpt list-models | head          # every model LiteLLM knows; use column 1 with -m
   ```
   Keys: `export OPENAI_API_KEY=...`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, and so on, or `runoak set-apikey -e openai <key>` (the name must match the provider; `openrouter-key` for OpenRouter). Default model is `gpt-5.5`. Provider-qualified names are safest: `openai/gpt-5.5`, `anthropic/claude-sonnet-5`, `openrouter/anthropic/claude-sonnet-4.5`, `ollama/llama3`. A quick smoke test:
   ```bash
   echo "Reply with one word: ready" > /tmp/ping.txt && ontogpt complete -i /tmp/ping.txt -m <model>
   ```
2. **Pick the template.** If the user named one, use it. Otherwise follow the `ontogpt-select-template` skill. `ontogpt list-templates` prints the bundled names. If nothing fits, the `ontogpt-author-template` skill covers writing one; a custom YAML path works directly with `-t path/to/schema.yaml`.
3. **Prepare the input.** `-i` accepts a file, a directory (every `*.txt` in it, not recursive), or a literal string. PDFs need `--use-pdf`. Tabular input (`.csv`, `.tsv`, `.xlsx`) is read row by row; `--selectcols a,b` picks columns. Very long inputs: `--max-text-length N` chunks by characters and merges results. Give the model the text as it is; do not pre-summarize.
4. **Run.**
   ```bash
   ontogpt extract -t drug -i paper.txt -m openai/gpt-5.5 -O yaml -o out.yaml
   ```
   Add `-v` to see grounding decisions and `--show-prompt -v` to see the exact prompt. `-T ClassName` extracts one class instead of the root. `--auto-prefix` sets the prefix used for ungrounded values (default `AUTO`).
5. **Read the output** (see [references/output-format.md](references/output-format.md)). `extracted_object` holds the structured record. Values shaped like `MONDO:0005044` are grounded. Values shaped like `AUTO:beta%20receptors` were extracted but matched nothing. `named_entities` lists every grounded id with its label. Report both counts to the user and name the fields that stayed ungrounded.
6. **Convert or export** as needed: `-O json|yaml|md|html|csv|tsv|jsonl|kgx|owl|turtle` on `extract`, or `ontogpt convert -t <template> -O <fmt> out.yaml` afterward.
7. **Iterate.** Ungrounded values, empty fields, or merged values are the usual defects. The `ontogpt-troubleshoot` skill has the symptom table. Do not hand-edit identifiers into the output; fix the template, the annotators, or the model, and rerun.

## Other entry points

| Task | Command |
|---|---|
| PubMed search, fetch abstracts or PMC full text, extract | `ontogpt pubmed-annotate -t <template> "<query>" --limit 5 [--get-pmc]` |
| Extract from a web page or Wikipedia | `ontogpt web-extract -t <template> <url>`, `ontogpt wikipedia-extract -t <template> "<title>"` |
| Batch: PubMed IDs from a file | `ontogpt pubmed-annotate -t <template> --input-file ids.txt` |
| Guess a template from a description | `ontogpt suggest-templates "<what you need>"` (LLM-powered; verify against the catalog) |
| Plain completion, no schema | `ontogpt complete -i text.txt` |
| Re-render saved results | `ontogpt convert -t <template> -O html out.yaml` |

## Rules of the road

- Reasoning models (GPT-5 family, Claude Sonnet 5 and Opus 5) accept only their default temperature. OntoGPT drops `-p/--temperature` for them with a warning. Do not fight it.
- Every run caches prompt and completion under `./.litellm_cache` (or `--cache-db <dir>`). A repeated identical run costs nothing and returns instantly. Delete the cache or change the input when you want a fresh answer.
- First use of an annotator such as `sqlite:obo:mondo` downloads the ontology into `~/.data/oaklib` (override with `PYSTOW_HOME`). NCBITaxon and CHEBI are large. A long silent pause on the first run is the download, not a hang.
- `bioportal:` annotators need `runoak set-apikey -e bioportal <key>`. `gilda:` needs `pip install ontogpt[gilda]`.
- Do not paste API keys into commands the user can see in logs; read them from the environment.
- Quality varies by model. A mid-tier model is fine for entity lists. Relation-heavy templates (`gocam`, `drug`, `ctd`) want a capable model.
