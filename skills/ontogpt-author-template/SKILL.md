---
name: ontogpt-author-template
description: Write or modify an OntoGPT extraction template (a LinkML schema with SPIRES annotations), including choosing the ontologies and OAK annotators that ground each entity class, setting id_prefixes, writing field prompts, and validating the schema before use. Use when no bundled template fits, when a template must ground to a different ontology, when asked to add fields or entity classes to a template, or when asked which ontology to use for a kind of entity.
license: BSD-3-Clause
compatibility: The validator needs the ontogpt package; opening annotators downloads ontologies (tens of MB to a few GB for NCBITaxon or CHEBI).
metadata:
  project: OntoGPT
  homepage: https://github.com/monarch-initiative/ontogpt
---

# Authoring an OntoGPT template

A template is a LinkML YAML file. OntoGPT turns each attribute of the root class into one line of the prompt, sends the text, parses the reply line by line, and grounds every value whose range is a `NamedEntity` subclass using that class's `annotators`. The template is the whole contract. Everything the model is told, and everything the grounder is allowed to return, lives in it.

Read [references/schema-reference.md](references/schema-reference.md) for every field OntoGPT reads, and [references/ontology-guide.md](references/ontology-guide.md) to pick ontologies and annotator strings. Start from [assets/template_skeleton.yaml](assets/template_skeleton.yaml).

## Procedure

1. **Write the target as a record.** List the fields. For each: single or list, free text or entity, and if entity, what kind. Sketch the YAML you want *out* before writing the schema. Keep it small: five to eight fields on the root, one level of nesting at most, two at the very most.
2. **Find the closest bundled template** (`ontogpt list-templates`, or the catalog in the `ontogpt-select-template` skill) and copy it. Its prefixes, annotators, and phrasing are tested.
3. **Choose ontologies per entity class** with [references/ontology-guide.md](references/ontology-guide.md). Write `id_prefixes` (bare prefixes, e.g. `MONDO`, `HP`, `CHEBI`) and `annotators` (`sqlite:obo:mondo, sqlite:obo:hp`) so that the prefixes the annotators return are in `id_prefixes`. Mismatch here is the most common failure: `sqlite:obo:hp` returns `HP:`, not `HPO:`.
4. **Write the prompts.** Each attribute's `description` (or `annotations: prompt:`) is what the model sees, verbatim, after `field_name: <`. Say what to extract, from the text only, and how to separate values (`semicolon-separated list of ...`). Add `annotations: prompt.examples:` with two to four short examples for anything the model might format oddly. Never mention identifiers or ontologies in prompts. The model produces labels; OAK produces ids.
5. **Set one `tree_root: true`.** Nested records are classes whose attributes are themselves entity or string fields; they are extracted by a second SPIRES pass per item. Mark them `is_a: CompoundExpression` when they represent relations.
6. **Validate.**
   ```bash
   uv run python skills/ontogpt-author-template/scripts/validate_template.py my_template.yaml --codegen
   ```
   Fix every ERROR. Read every WARNING. Add `--check-annotators` once to confirm each annotator opens (this downloads ontologies).
7. **Run on one short text** that contains known answers:
   ```bash
   ontogpt -v extract -t my_template.yaml -i sample.txt
   ```
   Check `raw_completion_output` (did the model answer the fields?), then `extracted_object` (did parsing keep them?), then the `AUTO:` values (did grounding fail?). Adjust prompts for the first, separators for the second, annotators and prefixes for the third.
8. **Install.** A YAML path passed to `-t` is copied into the package's templates directory and compiled; afterwards its bare name works. To contribute it to OntoGPT, add the YAML under `src/ontogpt/templates/`, run `make` to regenerate the pydantic module, and add a docs entry in `mkdocs.yml`.

## Design rules that matter

- **One entity class per ontology target.** `Disease` grounds to MONDO; do not reuse it for phenotypes.
- **Descriptions are prompts.** A description written for a human ("the disease field") produces bad extractions. Write "the name of the disease or condition the patient was diagnosed with, as written in the text".
- **Say "semicolon-separated" on every multivalued field.** The parser splits on `;`. Commas inside values are kept.
- **Free text stays `range: string`.** It is never grounded and never nested. Use it for quantities, dates, quoted findings.
- **Enums restrict, not suggest.** A fixed enum (`permissible_values`) is appended to the prompt as "Must be one of: ...". A dynamic enum (`reachable_from` an ontology node) filters grounded ids after the fact and is invisible to the model.
- **`prompt.skip: "true"`** hides a field from the prompt. Use it for provenance fields you fill later.
- **Two annotators are usually enough.** More annotators mean more downloads and more false partial matches. Order them by trust; the first hit wins.
- **Test the grounding independently** when in doubt: `runoak -i sqlite:obo:mondo annotate "type 2 diabetes"`.

## Do not

- Do not put identifiers, URIs, or "use MONDO terms" in prompt text.
- Do not nest deeper than two levels; SPIRES recursion multiplies calls and errors.
- Do not use capital letters or hyphens in the file name; it becomes a Python module name.
- Do not declare a class `tree_root` and `is_a: NamedEntity` at once unless the whole document is one entity (see `ontology_class`).
