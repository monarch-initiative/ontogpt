# Template schema reference

What OntoGPT reads from a template, and what it does with each part. Everything here is LinkML; only the `annotations` keys are OntoGPT's own.

## Header

```yaml
id: http://w3id.org/ontogpt/my_template      # unique; w3id.org/ontogpt/<name> by convention
name: my_template                            # match the file name
title: My Template
description: >-                              # shown by list-templates; write it for a person choosing templates
  What this extracts, from what kind of text, grounded to which ontologies.
license: https://creativecommons.org/publicdomain/zero/1.0/
prefixes:
  linkml: https://w3id.org/linkml/
  my_template: http://w3id.org/ontogpt/my_template/
  MONDO: http://purl.obolibrary.org/obo/MONDO_   # one line per prefix used in id_prefixes
  HP: http://purl.obolibrary.org/obo/HP_
default_prefix: my_template
default_range: string
imports:
  - linkml:types
  - core                                     # NamedEntity, CompoundExpression, Triple, Publication
```

Prefix expansions for OBO ontologies follow `http://purl.obolibrary.org/obo/<PREFIX>_`. Others used in bundled templates: `HGNC: http://identifiers.org/hgnc/`, `MESH: http://identifiers.org/mesh/`, `DRUGBANK: https://go.drugbank.com/drugs/`, `UniProtKB: http://purl.uniprot.org/uniprot/`, `NCBITaxon: http://purl.obolibrary.org/obo/NCBITaxon_`, `biolink: https://w3id.org/biolink/vocab/`.

## Classes

Three kinds of class appear in a template.

### The root

```yaml
classes:
  CaseReport:
    tree_root: true
    description: A clinical case report
    attributes:
      patient_age:
        description: the age of the patient at presentation, as written in the text
      diagnoses:
        description: semicolon-separated list of the diseases the patient was diagnosed with
        multivalued: true
        range: Disease
      findings:
        description: semicolon-separated list of clinical findings, signs, and symptoms observed in the patient
        multivalued: true
        range: Phenotype
        annotations:
          prompt.examples: seizures, short stature, hypotonia
      treatments:
        description: semicolon-separated list of drug treatments, each as "drug / dose / route"
        multivalued: true
        range: Treatment
```

Each attribute becomes one prompt line: `name: <description>`. Order in the file is order in the prompt.

| Attribute key | Effect |
|---|---|
| `description` | prompt text unless `annotations.prompt` is set |
| `annotations.prompt` | prompt text; overrides description |
| `annotations.prompt.examples` | comma-separated example values; appended to the prompt and also used to flag echoed examples as `LIKELY HALLUCINATION` |
| `annotations.prompt.skip: "true"` | field is not prompted; use for provenance or computed fields |
| `multivalued: true` | the reply is split on `;` into a list. Say "semicolon-separated" in the text. |
| `range` | `string` (kept as text), a `NamedEntity` subclass (grounded), a compound class (nested extraction), or an enum |
| `examples: [{value: ...}]` | documentation only; not sent to the model |
| `identifier: true` | marks the id slot (already set on `NamedEntity.id`) |

### Entity classes

```yaml
  Disease:
    is_a: NamedEntity
    id_prefixes:
      - MONDO
      - MESH
    annotations:
      annotators: sqlite:obo:mondo, sqlite:obo:mesh
```

| Key | Effect |
|---|---|
| `is_a: NamedEntity` | gives the class `id` and `label`; marks it for grounding |
| `id_prefixes` | bare prefixes (no colon) that a grounded id may carry. Ids with other prefixes are mapped through the Translator node normalizer, and dropped if no mapping lands in this list. Omit the list to accept anything. |
| `annotations.annotators` | comma-and-space separated OAK selectors, tried in order. See the ontology guide. |
| `annotations.prompt.examples` | as above |
| `annotations.ner.recurse: "true"` | if grounding fails, run a nested extraction on the value text using this class's own attributes |
| `slot_usage.id.pattern` | regex the id must match, e.g. `"^MESH:[CD][0-9]{6}$"` |
| `slot_usage.id.values_from` | list of enum names; the id must be in the expanded value set |

An entity class may also have attributes. They are then extracted for it in a nested pass, which is how `ontology_class` produces a definition with parents.

### Compound (relation) classes

```yaml
  Treatment:
    is_a: CompoundExpression
    attributes:
      drug:
        range: Drug
        annotations:
          prompt: the name of the drug. This comes first.
      dose:
        description: the dose and unit, e.g. 10 mg
      route:
        range: RouteEnum
```

When a root attribute has this class as its range, each semicolon-separated item from the first reply is sent back to the model with this class's prompt ("Split the following piece of text into fields..."). Keep the compound's fields few and tell the model their order in the parent prompt ("each as drug / dose / route"). `Triple` in `core` is a ready-made subject, predicate, object compound; subclass it for relation extraction and give `predicate` a `RelationshipType` range grounded to RO or Biolink.

## Enums

Fixed values are shown to the model:

```yaml
enums:
  RouteEnum:
    permissible_values:
      oral:
      intravenous:
      topical:
```

Prompt becomes `route: <the route of administration Must be one of: oral, intravenous, topical>`. Add `meaning: NCIT:C38288` under a value to map it to an ontology term.

Dynamic value sets filter grounded ids and are not shown to the model:

```yaml
enums:
  NeurotransmitterIdentifier:
    reachable_from:
      source_ontology: obo:chebi
      relationship_types:
        - rdfs:subClassOf
        - RO:0000087         # has role
      source_nodes:
        - CHEBI:35942        # neurotransmitter agent
```

Reference it from an entity class with `slot_usage: {id: {values_from: [NeurotransmitterIdentifier]}}`. Expansion happens once per run and can take a while on large ontologies. `include:` with several `reachable_from` blocks unions them (see `cell_type.yaml`).

## Loading and codegen

`-t path/to/my_template.yaml` copies the file into the package's `templates/` directory, runs `gen-pydantic`, and imports the module `ontogpt.templates.my_template`. So:

- the file name must be a valid Python module name: lowercase, digits, underscores, no hyphens;
- a name that collides with a bundled template overwrites it for that environment;
- after the first run `-t my_template` (no path) works in that environment;
- `imports` of other custom schemas must also be present in that directory.

`validate_template.py --codegen` performs the same generation in a temporary directory and reports errors before you touch the package.

## OWL export

Add `annotations: {owl: ...}` and `owl.template` blocks (see `recipe.yaml` and the OWL exports doc) if results must become OWL axioms. Plain templates still export to `-O owl`/`turtle`, but only as instance data.
