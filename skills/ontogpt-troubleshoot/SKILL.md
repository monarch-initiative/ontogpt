---
name: ontogpt-troubleshoot
description: Diagnose and fix problems with OntoGPT runs and outputs, including empty or partial extracted objects, values left as AUTO instead of ontology ids, hallucinated or merged values, wrong identifiers, authentication and model errors, slow first runs, annotator download failures, and cache confusion. Use when an `ontogpt extract` result looks wrong, when the command errors or exits, or when asked why an entity did not ground.
license: BSD-3-Clause
compatibility: Needs the ontogpt package and the same environment the failing run used.
metadata:
  project: OntoGPT
  homepage: https://github.com/monarch-initiative/ontogpt
---

# Troubleshooting OntoGPT

An extraction has three stages, and each fails in its own way. Find the stage first, then the fix.

```
text --(1 prompt)--> model reply --(2 parse)--> extracted_object with labels --(3 ground)--> ids
```

The result file holds the evidence for all three: `prompt`, `raw_completion_output`, `extracted_object`, `named_entities`. Rerun with `-v` (and `--show-prompt`) when you need the nested prompts and the grounding log.

## Locate the stage

1. **Is there a reply at all?** Empty `raw_completion_output` plus an `ERROR:` line in the log means stage 1 never completed: credentials, model name, rate limit, context window. See "Run errors" in [references/symptoms.md](references/symptoms.md).
2. **Does the reply contain the value?** Read `raw_completion_output`. If the value the user expects is not there, it is a prompting or model problem: the field description was unclear, the model missed it, or it was told to use only the text and the text does not say it. If the value is there but missing from `extracted_object`, it is a parsing problem: wrong separator, prose around the fields, a JSON reply with renamed keys.
3. **Is the value present but not an id?** `AUTO:...` means grounding found nothing. Work through the grounding checklist below.
4. **Is the id wrong?** A plausible but incorrect id is either an over-eager partial match (a substring matched a broader term), a prefix outside `id_prefixes` that was mapped through the Translator normalizer to a different ontology, or a label the model paraphrased.

## Grounding checklist for an `AUTO:` value

Run the annotator by hand on the exact label:

```bash
runoak -i sqlite:obo:mondo annotate "community-acquired pneumonia"
```

- **No output:** the ontology has no label or synonym for that string. Options: add a second annotator with broader coverage (`sqlite:obo:mesh`, `sqlite:obo:ncit`); add a `--dictionary` entry; rephrase the field prompt so the model returns the canonical name ("use the standard disease name"); accept `AUTO:` for that value.
- **Output with a prefix not in `id_prefixes`:** OntoGPT dropped it. Add the prefix to `id_prefixes` (and `prefixes:`), or choose an annotator that returns the prefix you want. Spelling matters: `HP` not `HPO`.
- **Output only for a shorter string:** the label carries qualifiers ("crackles over the right lower lobe"). Tell the model in the prompt to give the finding without location or severity, or add a separate field for those.
- **Annotator errors or a 404:** the selector is wrong or no sqlite build exists; see the ontology guide in `ontogpt-author-template`.
- **A `values_from` or `pattern` restriction rejected it:** the id was found but filtered. Loosen the enum root or the regex.

## Fixes by stage

| Stage | Symptom | Fix |
|---|---|---|
| prompt | field empty, reply lacks it | sharpen the description; add `prompt.examples`; a stronger model; chunk with `--max-text-length` if the text is long |
| prompt | reply invents things not in the text | add "only if explicitly stated in the text" to the description; check `LIKELY HALLUCINATION` markers; lower the model's freedom (a different model; temperature only on non-reasoning models) |
| parse | one item holding several values with commas | say "semicolon-separated" in the prompt; add examples with semicolons |
| parse | reply is prose or JSON and fields are lost | the parser strips code fences and handles JSON objects, but not narrative. Add "Answer only in the field: value format" via `--system-message` |
| parse | nested compound fields shifted (dose in route) | in the parent prompt spell out the order: "each as drug / dose / route"; give each compound attribute a prompt saying "This comes first/second" |
| ground | `AUTO:` values | checklist above |
| ground | wrong ontology id | tighten `id_prefixes`; reorder annotators; add a dynamic enum (`values_from`) rooted where the answers must live |
| ground | slow, then `nodenormalization-sri.renci.org` timeout in the log | the Translator normalizer is queried when an id's prefix is not in `id_prefixes`. Harmless; the id is dropped. Avoid it by making annotators and `id_prefixes` agree. |
| run | `AuthenticationError`, `Missing credentials`, `Exiting...` | key name does not match the provider; OntoGPT's warning names the variable. See setup docs. |
| run | `UnsupportedParamsError` about temperature | reasoning model; OntoGPT retries without it. Nothing to do. |
| run | `NotFoundError` for the model | wrong model string; `ontogpt list-models \| grep <name>`; provider-qualify it |
| run | `ContextWindowExceededError` | chunk with `--max-text-length`; or a model with a larger window |
| run | `RateLimitError` | wait; batch smaller; cached inputs do not count |
| run | long silence on first run | ontology download to `~/.data/oaklib`; NCBITaxon and CHEBI are ~1 GB. Watch the directory grow. |
| run | same wrong answer every time | it is cached. Change `--cache-db` or delete `./.litellm_cache` |
| run | `HTTP Error 404` from `get_adapter` | annotator name has no sqlite build; check the selector |
| run | `ImportError ... ontogpt.templates.<name>` | codegen of a custom template failed; run `validate_template.py --codegen` from `ontogpt-author-template`; file name must be a valid module name |
| run | `Template X has multiple root classes` or `has no root class` | one `tree_root: true`, or pass `-T ClassName` |

## When to stop fixing

Some values will not ground. Relation words ("blocks", "is used for") rarely have ontology terms unless the template grounds predicates to RO or Biolink. Compound clinical phrases need decomposition the ontology does not do. Report these as `AUTO:` with the label and move on. A run where the grounded ids are correct and the `AUTO:` ones are honest is a good run.

Full symptom table with log fragments: [references/symptoms.md](references/symptoms.md).
