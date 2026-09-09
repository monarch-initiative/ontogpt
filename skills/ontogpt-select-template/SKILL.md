---
name: ontogpt-select-template
description: Choose the right OntoGPT extraction template (LinkML schema) for a text and a goal, or decide that none of the bundled templates fits and a new one is needed. Use when asked which template or schema to use with OntoGPT, what a template extracts or grounds to, whether OntoGPT can pull a given kind of information (diseases, phenotypes, drugs, genes, GO terms, environmental samples, recipes, etc.) from text, or before any `ontogpt extract` run where the template is not already given.
license: BSD-3-Clause
compatibility: The helper script needs the ontogpt package installed; the catalog is plain text.
metadata:
  project: OntoGPT
  homepage: https://github.com/monarch-initiative/ontogpt
---

# Selecting an OntoGPT template

A template decides three things: **what fields** the model is asked for, **which of those fields are grounded**, and **to which ontologies**. Choosing well is most of the work. A template that grounds diseases to MONDO will not give you HPO phenotypes no matter how good the model is.

## Procedure

1. **State the target in one line.** "Drug, disease, and mechanism triples from pharmacology abstracts." "HPO phenotypes from case reports." "Sampling site, environmental material, and taxa from a metagenomics methods section." Name the entity types and, if the user needs them, the relations between them.
2. **Name the identifier namespaces the user needs downstream.** MONDO or MESH for disease? HGNC or UniProt for genes? This decides between templates that look alike. Ask only if the downstream use is unstated and it changes the answer.
3. **Scan the catalog.** [references/template-catalog.md](references/template-catalog.md) lists every bundled template with its root class, grounding prefixes, and purpose. Shortlist by entity types first, then by prefixes, then by input shape (abstract, full paper, clinical note, table).
4. **Inspect the shortlist.** For each candidate run
   ```bash
   uv run python skills/ontogpt-select-template/scripts/describe_template.py <name>
   ```
   (or `python ...` in an environment where ontogpt is installed). It prints the exact prompt text per field, which fields nest, and which annotators ground each entity class. Match those fields against the target from step 1. `ontogpt suggest-templates "<goal>"` gives an LLM's opinion; treat it as one more candidate, not a decision.
5. **Decide.**
   - Fields match and prefixes match: use it as is.
   - Fields match, the user only needs one class: use `-t name.ClassName` or `-T ClassName`.
   - Fields match, prefixes or annotators do not: copy the template YAML, change `id_prefixes` and `annotators` on the entity classes, and run it as a custom template (`-t my_copy.yaml`). See the `ontogpt-author-template` skill.
   - No template covers the fields: write a new one with the `ontogpt-author-template` skill. Start from the closest bundled template.
6. **Test on one document before a batch.** Read the `raw_completion_output` and the `AUTO:` values. If the model returns the right things and grounding fails, the template needs annotator changes, not a different template.

## Quick map from goal to template

| Goal | Start with | Grounds to |
|---|---|---|
| Diseases only | `mondo_simple`, `all_disease_grounding` | MONDO |
| Human phenotypes, signs, symptoms | `human_phenotype` | HP |
| Traits and qualities of organisms or parts (not HPO) | `phenotype`, `traits` | PATO, UBERON, CHEBI, OBA |
| Chemical or drug to disease relations | `ctd` (relations; no root, use `-t ctd.ChemicalToDiseaseDocument`), `ctd_ner` (entities only) | MESH |
| Drug mechanism of action | `drug`, `drug_to_disease` | DRUGBANK, CHEBI, MESH, MONDO, HGNC |
| Medical actions, treatments, diagnostics | `maxo` (MAXO), `treatment` (genes and phenotypes of treated disease), `diagnostic_procedure` (HP, LOINC) | MAXO, HP, MONDO, HGNC |
| Gene functions, GO terms | `go_simple` (terms), `go_terms`, `go_terms_relational`, `gocam`, `biological_process` | GO, HGNC |
| Gene symbols from ambiguous text | `gene_extraction` | HGNC |
| Cell types and markers | `cell_type` | CL, UBERON, PR |
| Mendelian disease summary (genes, phenotypes, inheritance) | `mendelian_disease` | HGNC, HP, MONDO |
| Clinical case as a phenopacket | `phenopackets` (HP, MONDO, many more); `condition` (SNOMED via BioPortal, needs a key) | HP, MONDO, SNOMEDCT |
| Pathology or clinical notes | `pathology`, `dietitian_notes` | SNOMEDCT, UBERON, PATO; FOODON, MAXO, MONDO |
| Environmental samples, sites, materials | `environmental_sample`, `metagenome_study` (no root, use `-T`), `nmdc_schema_data` | ENVO, GAZ, MIXS, NCBITaxon, UO |
| Ecological interactions | `predator_prey` (NCBITaxon), `biotic_interaction` (relations only, RO) | NCBITaxon, RO |
| Food and recipes | `food`, `foodon_simple`, `recipe` | FOODON |
| Chemical reactions and enzymes | `reaction`, `metabolic_process` (no root, use `-T`) | CHEBI, GO, HGNC, NCBITaxon |
| Adverse outcome pathways | `aop`, `adverse_outcome_pathway` | CHEBI, GO, MONDO, UBERON |
| Dataset or ontology metadata | `datasheet`, `data_sheets_schema`, `miro`, `onto_usage` | mostly ungrounded |
| A generic "define this term" | `ontology_class` | ungrounded, structured |

## Signs you need a new template

- The entities you need are not any template's `NamedEntity` classes.
- The relation you need (for example enzyme to substrate) has no compound class.
- The right ontology is missing (plant anatomy needs PO; the bundled templates favor human and mouse).
- The input is a form or a table with fixed headings that a template should mirror.

When two templates both fit, prefer the one with fewer fields. Extra fields cost tokens and invite hallucination.
