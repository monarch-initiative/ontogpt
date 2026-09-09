# Symptoms, causes, fixes

Log lines are as OntoGPT prints them at default verbosity unless marked `-v`.

## Run errors (stage 1: nothing came back)

| Log fragment | Cause | Fix |
|---|---|---|
| `Encountered authentication error: litellm.AuthenticationError` then `Exiting...` | no key, wrong key, or key stored under a name for a different provider | set the provider's env var (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`) or `runoak set-apikey -e <provider>-key`. With `-v`, a `WARNING: No credential found for X_API_KEY` line names the exact variable. |
| `Missing Authentication header` or `Missing credentials ... OPENAI_API_KEY` with `--model-provider openai --api-base ...` | proxy form used but the key is stored under the proxy vendor's name | for OpenAI-compatible proxies the key goes in `OPENAI_API_KEY`; or drop the proxy flags and use the native provider prefix (`openrouter/...`) |
| `AuthenticationError ... AnthropicException ... API key is invalid` with an OAuth token | litellm older than 1.93 | upgrade litellm (OntoGPT requires >= 1.95) |
| `rate_limit_error` with message `Error` from Anthropic and a `sk-ant-oat` token | the OAuth token's plan does not cover that model | use a model the token allows, or an API key |
| `Encountered error due to unrecognized model or endpoint` | model string unknown to the provider | `ontogpt list-models \| grep -i <fragment>`; use the provider-qualified name |
| `Model X rejected a request parameter; retrying without it` | reasoning model refused `temperature` | expected; the retry succeeds |
| `Exceeded context window` | input plus prompt too long | `--max-text-length 20000` (characters) or a bigger-context model |
| `Encountered rate limiting` | provider throttling | rerun later; the cache keeps finished inputs |
| `Service unavailable` / `Internal server error` then `Exiting...` | provider outage or a proxy without credentials | retry; for proxies check `--api-base` and the key |
| `No response or response is empty.` after one of the above | the completion returned nothing; `extracted_object` will be empty | fix the preceding error |
| `urllib.error.HTTPError: HTTP Error 404` in a stack trace through `get_adapter` | `sqlite:obo:<name>` has no build on the semantic-sql bucket | check spelling; use `ols:` or `bioportal:` |
| `ValueError: Template X has multiple root classes` | custom template with two `tree_root: true` | keep one |
| `Template X has no root class. Consider defining one` (warning) then an odd class extracted | no `tree_root` | add one or pass `-T` |
| `ImportError: Failed to import module ... check the generated version at .../templates/<name>.py` | pydantic codegen produced code that fails to import, often from a class name clashing with core or a bad range | run `validate_template.py --codegen`; rename the class |
| `ModuleNotFoundError: No module named 'gilda'` | `gilda:` annotator without the extra | `pip install ontogpt[gilda]` |
| `bioportal` errors mentioning apikey | BioPortal annotator without a key | `runoak set-apikey -e bioportal <key>` |
| Nothing printed for minutes on first run | ontology download | wait; `ls -la ~/.data/oaklib` shows the file growing |
| `Failed to fetch remote model cost map` at startup | litellm could not reach its price list; offline | harmless; set `LITELLM_LOCAL_MODEL_COST_MAP=True` to silence |

## Output defects (stage 2: reply present, object wrong)

| What you see | Cause | Fix |
|---|---|---|
| `extracted_object: {}` but `raw_completion_output` has text | reply not in `field: value` lines (essay, table, bullet prose); or field names differ from the template | `--system-message "Answer using only the field names given, one per line, values separated by semicolons"`; check the model; a stronger model follows format better |
| a multivalued field has one element containing commas | model used commas | prompt text must say "semicolon-separated"; add `prompt.examples` with semicolons |
| a field contains the description text or `<...>` placeholder | model echoed the template | add examples; a stronger model; OntoGPT already drops values that look like empty placeholders |
| a value equals one of the examples, marked `LIKELY HALLUCINATION` | model copied `prompt.examples` | discard; choose examples that cannot occur in your corpus; or fewer examples |
| nested compound has fields shifted (dose text in `route`) | model did not follow the sub-field order | in the parent field say the order ("each as drug / dose / route"); give sub-fields prompts "This comes first" |
| the same entity appears under two fields | descriptions overlap | say what to exclude ("Do not include diseases already listed as diagnoses") |
| values are correct but the model added things not in the text | inference beyond the text | add "only if explicitly stated in the text"; a `--system-message` saying no inference |
| enum field has a value outside the list | model ignored "Must be one of" | add `other` to the enum; validate downstream |
| long input, sparse fields | model lost detail in a long context | `--max-text-length` chunking; results merge per field |

## Grounding defects (stage 3: labels right, ids wrong or missing)

| What you see | Cause | Fix |
|---|---|---|
| `AUTO:term` and `runoak -i <annotator> annotate "term"` returns nothing | not in that ontology's labels or synonyms | second annotator; `--dictionary`; prompt for canonical names |
| `AUTO:term` and `runoak` returns an id with a different prefix | prefix not in `id_prefixes` | add the prefix (and its `prefixes:` expansion) or switch annotator |
| `AUTO:long phrase with qualifiers` | annotator matches whole text first; partial matches only apply for BioPortal annotators | prompt for the bare term; separate qualifier fields |
| `-v` shows `ID X not in prefixes [...]` | as above | as above |
| `-v` shows `ID X not in value set Y` | dynamic enum filtered it | widen `reachable_from.source_nodes` or drop `values_from` |
| `-v` shows `ID X does not match pattern` | `slot_usage.id.pattern` too strict | fix the regex |
| `ERROR:root:Encountered error when normalizing X: HTTPSConnectionPool(host='nodenormalization-sri.renci.org' ...` | an id outside `id_prefixes` was sent to the Translator node normalizer for mapping and the service timed out | harmless; the id is dropped and the value becomes `AUTO:`. Align annotators with `id_prefixes` so the mapper is not needed. |
| a broad, wrong id (a parent term) | partial match or a synonym collision | reorder annotators; restrict with `values_from`; add the exact term to a `--dictionary` |
| ids from the wrong species ontology | annotator order | put the intended ontology first; drop the other |
| `WARNING:root:Could not find any mappings for ...` | `id_prefixes` do not match what the annotator returns | fix prefixes (`HP` not `HPO`) |
| grounded id but `original_spans` missing | label not verbatim in the text | expected for normalized labels; not an error |

## Cache confusion

| What you see | Cause | Fix |
|---|---|---|
| same output after changing the template prompt | prompt text changed, so this should miss the cache; if it did not, the change did not reach the prompt (edited the wrong file, or the bare template name still points at an older installed copy) | pass the YAML path again to reinstall; check `prompt` in the output |
| same output after changing the model | model name is part of the cache key; a repeat means the change did not apply | check `-m` spelling; provider prefix |
| want a fresh answer to the same input | intended cache hit | `--cache-db /tmp/fresh` or delete `./.litellm_cache` |
| `.litellm_cache` never appears | OntoGPT releases before September 2026 kept the cache in memory only | upgrade |

## Reading the log at `-v`

Useful lines, in the order they appear per value:

```
INFO:ontogpt.engines.knowledge_engine:GROUNDING community-acquired pneumonia using Disease
INFO:ontogpt.engines.knowledge_engine:Loading annotator sqlite:obo:mondo
INFO:ontogpt.engines.knowledge_engine:Could not ground and normalize community-acquired pneumonia to Disease
```

or, on success,

```
INFO:ontogpt.engines.knowledge_engine:Grounding hypertension to MONDO:0005044; next step is to normalize
INFO:ontogpt.engines.knowledge_engine:Normalized hypertension with MONDO:0005044 to MONDO:0005044
```

`ontogpt dump-completions` prints what the model actually said for every cached prompt when the result file was not kept.
