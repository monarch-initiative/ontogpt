# OntoGPT CLI reference for extraction work

`ontogpt --help` lists everything. This file covers the options that matter for extraction, with the behavior that the help text leaves out.

## Global options (before the subcommand)

| Option | Effect |
|---|---|
| `-v`, `-vv` | INFO, then DEBUG logging. `-v` shows each grounding attempt and which annotator answered. |
| `-q` | errors only |
| `--cache-db <dir>` | where LiteLLM stores prompt/completion pairs on disk (default `./.litellm_cache`) |
| `--version` | package version |

## `ontogpt extract`

```
ontogpt [-v] extract -t TEMPLATE [-i INPUT] [-T CLASS] [-m MODEL] [-O FMT] [-o FILE] [options]
```

| Option | Notes |
|---|---|
| `-t/--template` | bundled name (`drug`), `name.Class` to target a class (`gocam.GeneOrganismRelationship`), or a path ending in `.yaml`. A YAML path is copied into the package's templates directory and compiled to pydantic on first use; afterwards its bare name works. |
| `-i/--inputfile` | file path, directory (all `*.txt`, not recursive), or a literal string. Tabular files (`.csv .tsv .xlsx .xls .ods`) are read row by row. |
| `--use-pdf` | read text from a PDF with pymupdf |
| `--selectcols a,b` | columns to use from tabular input |
| `--max-text-length N` | chunk input by N characters, extract each chunk, merge results. Use for full papers when fields come back empty or the context is exceeded. |
| `-T/--target-class` | extract this class instead of the template's `tree_root` |
| `-m/--model` | LiteLLM model name; `--model-provider` and `--api-base` for proxies and Azure |
| `-p/--temperature` | default 1.0; dropped with a warning on reasoning models |
| `--system-message` | prepended as the system prompt; use for domain framing ("The text is a veterinary case report") |
| `--recurse/--no-recurse` | default on: nested classes are extracted by further SPIRES calls. `--no-recurse` keeps nested fields as strings and is faster. |
| `--auto-prefix PFX` | prefix for values that could not be grounded (default `AUTO`) |
| `--dictionary FILE` | a two-column mapping of text to CURIE consulted before annotators; use for local jargon or gene symbols |
| `-S key=value` | force a slot value on the result (e.g. `-S organism=NCBITaxon:9606`) |
| `--show-prompt` | with `-v`, print every prompt sent |
| `--cut-input-text` | keep only the first 1000 characters of input text in the output record; use for large batches |
| `-O/--output-format` | `yaml` (default), `json`, `jsonl`, `md`, `html`, `csv`, `tsv`, `kgx`, `owl`, `turtle`, `pickle` |
| `-o/--output` | output path; default stdout |

A directory input produces one result per file, written as a stream of YAML documents (or JSONL with `-O jsonl`).

## Literature and web commands

| Command | What it does |
|---|---|
| `ontogpt pubmed-annotate -t T "query" --limit N` | search PubMed, fetch abstracts, extract each. `--get-pmc` fetches PMC full text when available. `--input-file ids.txt` takes PMIDs instead of a query. `--max-text-length` chunks full texts. |
| `ontogpt search-and-extract -t T "query"` | search, then extract |
| `ontogpt web-extract -t T URL` | fetch a page, strip HTML, extract |
| `ontogpt wikipedia-extract -t T "Title"` and `wikipedia-search -t T "query"` | the same for Wikipedia |
| `ontogpt recipe-extract URL` | recipe pages with the `recipe` template |

## Working with results

| Command | What it does |
|---|---|
| `ontogpt convert -t T -O FMT results.yaml` | re-render a saved result in another format |
| `ontogpt dump-completions` | print cached prompt/completion pairs (debugging what the model said) |
| `ontogpt eval` | run the built-in evaluation suites (`ctd`, `go`, `hpoa`, `maxo`, ...) |
| `ontogpt suggest-templates "text"` | ask the LLM which bundled template fits |
| `ontogpt list-templates` | id, name, description of every bundled template |
| `ontogpt list-models` | name, provider, mode, token limit for every model LiteLLM knows |

## Model and credential options

- Provider-qualified names resolve without extra flags: `openai/gpt-5.5`, `anthropic/claude-sonnet-5`, `groq/llama-3.1-8b-instant`, `mistral/mistral-large-latest`, `openrouter/<vendor>/<model>`, `ollama/<model>`.
- Keys come from the provider's LiteLLM environment variable (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GROQ_API_KEY`, `AZURE_API_KEY` with `AZURE_API_BASE` and `AZURE_API_VERSION`) or from `runoak set-apikey -e <provider>-key <key>` (`openai` for OpenAI). OntoGPT warns with the exact name it wanted when it finds nothing.
- OpenAI-compatible proxies: `-m <model> --model-provider openai --api-base https://host/v1`, key in `OPENAI_API_KEY`.
- Anthropic OAuth tokens (`sk-ant-oat...`) work in `ANTHROPIC_API_KEY`.
- Local models: install and start `ollama`, `ollama pull llama3`, then `-m ollama/llama3`. No key.

## Exit behavior

Authentication, bad-request, and not-found errors stop the run with `Exiting...`. Rate limits, timeouts, and context-window errors log an error and return an empty completion for that input, so a batch continues. Check logs for `ERROR:` lines before trusting an empty `extracted_object`.
