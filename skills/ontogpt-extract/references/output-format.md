# Reading OntoGPT output

Every extraction returns an `ExtractionResult` (defined in the `core` template). In YAML:

```yaml
input_id: paper.txt
input_title: null
input_text: "One treatment for high blood pressure is carvedilol, a beta blocker..."
raw_completion_output: |
  drug_mechanisms: carvedilol treats hypertension; carvedilol blocks beta receptors
prompt: |
  From the text below, extract the following entities in the following format:

  drug_mechanisms: <A semicolon-delimited list of individual drug mechanisms ...>

  Text:
  One treatment for high blood pressure is carvedilol ...
extracted_object:
  drug_mechanisms:
    - disease: MESH:D006973
      drug: DRUGBANK:DB01136
      mechanism_links:
        - subject: MESH:C043211
          predicate: AUTO:blocks
          object: AUTO:beta%20receptors
named_entities:
  - id: MESH:D006973
    label: hypertension
  - id: DRUGBANK:DB01136
    label: carvedilol
  - id: MESH:C043211
    label: carvedilol
  - id: AUTO:blocks
    label: blocks
  - id: AUTO:beta%20receptors
    label: beta receptors
```

## Validation section

Since September 2026 every result also carries a `validation` block, produced after extraction by linkml-term-validator. Each grounded identifier is checked for existence, obsolescence, and label agreement (label or synonym). Invalid identifiers are replaced from the obsolete term's successor, from re-grounding the label, or from an ontology search; when nothing is found they are rewritten as `AUTO:<label>` so the output holds no invalid id.

```yaml
validation:
  validator: linkml-term-validator 0.4.5
  total_terms: 5
  valid_terms: 3
  replaced_terms: 1
  unresolved_terms: 0
  label_mismatches: 1
  skipped_terms: 0
  results:
    - original_id: MONDO:0005044
      label: hypertension
      entity_class: Disease
      status: VALID
      ontology_label: hypertensive disorder
      message: Label matches a synonym
```

| Status | Meaning | What to do |
|---|---|---|
| `VALID` | term exists and the extracted label is its label or a synonym | nothing |
| `LABEL_DIFFERS` | term exists but the extracted label is not its label or a synonym; kept | inspect: often a partial match to a broader term. Tighten the prompt or annotators if it recurs. |
| `REPLACED` | the id was missing, obsolete, or mislabeled and a valid term was substituted; `replacement_id` and `attempts` show the path | check `replacement_label` against the text |
| `UNRESOLVED` | invalid id, no substitute found; value rewritten with the auto prefix | treat as ungrounded |
| `SKIPPED` | no ontology adapter for that prefix | add an annotator that names the prefix's ontology, or ignore |

`--no-validate-terms` turns the step off. Absence of the block means it did not run.

## Fields

| Field | Meaning |
|---|---|
| `input_id`, `input_title`, `input_text` | provenance; `input_text` is the full text unless `--cut-input-text` |
| `prompt` | the exact prompt sent for the root class. Nested classes get their own prompts, visible with `-v --show-prompt`. |
| `raw_completion_output` | the model's reply before parsing. The first place to look when a field is empty or wrong. |
| `extracted_object` | the structured record, shaped by the template's root class |
| `named_entities` | every value that went through grounding, with the label the model produced |

## How a value gets its identifier

For each slot whose range is a `NamedEntity` class, SPIRES takes the model's text and tries, in order:

1. A literal CURIE in the text with a prefix the class allows (`MONDO:0005044` stays as is).
2. The singular form, and the parts inside parentheses or brackets.
3. The `--dictionary`, exact then partial.
4. Each annotator in the class's `annotators` list, in order, whole-text match first, then partial match.

The first hit is normalized against the class's `id_prefixes` (and any `pattern` or `values_from` restriction). If nothing survives, the value becomes `AUTO:<url-encoded text>`, or the raw text with `--auto-prefix ""`.

So:

| Value looks like | Meaning |
|---|---|
| `MONDO:0005044`, `HGNC:2514`, `CHEBI:16236` | grounded to that ontology |
| `AUTO:beta%20receptors` | extracted, not grounded. Either no annotator knows the phrase, the phrase is a relation or qualifier that has no ontology, or the prefix the annotator returned is not in `id_prefixes`. |
| `LIKELY HALLUCINATION: cancer` | the value equals one of the class's `prompt.examples`. The model echoed the example instead of reading the text. Discard it. |
| plain text in a field whose range is `string` | expected; string fields are never grounded |
| `null` or missing field | the model gave nothing for that slot, or the parser could not find the `field:` line in the reply |
| a list with one long item containing commas | the model used commas where the template asked for semicolons; the values merged |

## Judging a result

- Count grounded versus `AUTO:` entities. A relation template will always carry some `AUTO:` predicates unless the template grounds predicates to RO or Biolink.
- Check `raw_completion_output` against `extracted_object`. If the reply has the value but the object does not, it is a parsing problem (wrong separator, extra prose, JSON with different keys). If the reply lacks it, it is a prompting or model problem.
- Check `named_entities` labels against the input text. A label that does not occur in the text is a hallucination or an over-normalized paraphrase.
- Spans: `original_spans` on entities is filled only when the label is found verbatim in the input.

## Formats

`-O yaml` is the full record. `-O json` is the same. `-O md` and `-O html` render for reading. `-O csv`/`-O tsv` flatten the root object one row per top-level list item. `-O kgx` writes nodes and edges for knowledge-graph import. `-O owl`/`-O turtle` need OWL annotations in the template (see the `recipe` template). Batches write one document per input; use `-O jsonl` for machine reading.
