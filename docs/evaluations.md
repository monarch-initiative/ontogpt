# Evaluations

OpenAI's functions have been evaluated on test data sets.

All evaluation results include OpenAI cache databases (`openai_cache.db.gz`) as a reference of the prompts and responses obtained during the evaluation. This may be used by extracting the cache database to the root directory of the project.

Tests may be run with the `eval` command followed by the test name, e.g., for the BC5CDR test below:

```bash
ontogpt eval EvalCTD 
```

By default, the evaluation will only be executed over a subset of the test corpus.

The exact number of inputs to run the test over can be controlled with the `--num-tests` option, like this:

```bash
ontogpt eval --num-tests 1 EvalCTD
```

To run the full set of tests, set `num-tests` to the input count for a given evaluation, as defined below.

For each document, the evaluation process will attempt to process the full text without preprocessing.

If the `--chunking` option is used, then the input text will instead be chunked into segments of a few tokens each, essentially creating new queries for each segment. This alternate strategy may impact test results and will result in longer run time.

## BC5CDR

*Test Name:* EvalCTD
*Input Count:* 500

Results for OntoGPT on the [BioCreative V Chemical Disease Relation Task (BC5CDR)](https://biocreative.bioinformatics.udel.edu/media/store/files/2015/BC5CDR_overview.final.pdf) are available on Zenodo here: <https://zenodo.org/record/7657763>

Evaluation functions for BC5CDR are available in `src/ontogpt/evaluation/ctd/eval_ctd.py`.

Note that the project also includes test and train data (`CDR_TestSet.BioC.xml.gz` and `CDR_TrainSet.BioC.xml.gz`, respectively) as well as a set of synonyms for MeSH terms (see `synonyms.yaml`).

### Template

This evaluation uses the following schema template:

```yaml
id: http://w3id.org/ontogpt/ctd
name: ctd
title: Chemical to Disease Template
description: >-
  A template for Chemical to Disease associations.
  
  This template is intended to represent associations between chemicals and diseases,
  and for evaluating Semantic Llama against BioCreative V Chemical Disease
  Relation (CDR) Task (BC5CDR).
see_also:
  - https://biocreative.bioinformatics.udel.edu/media/store/files/2015/BC5CDR_overview.final.pdf
  - https://academic.oup.com/database/article/doi/10.1093/database/baw068/2630414
source: https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/
license: https://creativecommons.org/publicdomain/zero/1.0/
prefixes:
  linkml: https://w3id.org/linkml/
  drug: http://w3id.org/ontogpt/drug/

default_prefix: drug
default_range: string

imports:
  - linkml:types
  - core

classes:

  ChemicalToDiseaseDocument:
    description: A document that contains chemical to disease relations.
    is_a: TextWithTriples
    slot_usage:
      triples:
        range: ChemicalToDiseaseRelationship
        annotations:
          prompt: >-
            A semi-colon separated list of chemical to disease relationships, where the relationship is either INDUCES
            or TREATS.
            for example: Lidocaine INDUCES cardiac asystole; 
            Hydroxychloroquine NOT TREATS COVID-19;
            Methyldopa INDUCES Hypotension;
            Monosodium Glutamate NOT INDUCES Headache;
            Imatinib TREATS cancer
          exclude: Lidocaine, cardiac asystole, Hydroxychloroquine, COVID-19, Methyldopa, Headache, Imatinib, cancer


  ChemicalToDiseaseRelationship:
    is_a: Triple
    description: A triple where the subject is a chemical and the object is a disease.
    slot_usage:
      subject:
        range: Chemical
        description: >-
          The chemical substance, drug, or small molecule. 
          For example: Lidocaine, Monosodium Glutamate, Imatinib.
      object:
        range: Disease
        description: >-
          The disease or condition that is being treated or induced by the chemical.
          For example, asthma, cancer, covid-19, cardiac asystole, Hypotension, Headache.
      predicate:
        range: ChemicalToDiseasePredicate
        description: The relationship type, e.g. INDUCES, TREATS.
      subject_qualifier:
        range: NamedEntity
        description: >-
          An optional qualifier or modifier for the chemical, e.g. "high dose" or "intravenously administered"
      object_qualifier:
        range: NamedEntity
        description: >-
          An optional qualifier or modifier for the disease, e.g. "severe" or "with additional complications"

  Disease:
    is_a: NamedEntity
    annotations:
      annotators: "sqlite:obo:mesh, sqlite:obo:mondo, sqlite:obo:hp, sqlite:obo:ncit, sqlite:obo:doid, bioportal:meddra"
      prompt.examples: cardiac asystole, COVID-19, Headache, cancer
    id_prefixes:
      - MESH
    slot_usage:
      id:
        pattern: "^MESH:[CD][0-9]{6}$"
        values_from:
          - MeshDiseaseIdentifier

  Chemical:
    is_a: NamedEntity
    annotations:
      annotators: "sqlite:obo:mesh, sqlite:obo:chebi, sqlite:obo:ncit, bioportal:mdm, sqlite:obo:drugbank, gilda:"
      prompt.examples: Lidocaine, Hydroxychloroquine, Methyldopa, Imatinib
    id_prefixes:
      - MESH
    slot_usage:
      id:
        pattern: "^MESH:[CD][0-9]{6}$"
        values_from:
          - MeshChemicalIdentifier

  ChemicalToDiseasePredicate:
    is_a: RelationshipType
    description: >-
      A predicate for chemical to disease relationships
    comments:
      - for the purposes of evaluation against BC5CDR, any predicate other than INDUCES is ignored.

enums:

  MeshChemicalIdentifier:
    reachable_from:
      source_ontology: obo:mesh
      source_nodes:
        - MESH:D000602 ## Amino Acids, Peptides, and Proteins
        - MESH:D001685 ## Biological Factors
        - MESH:D002241 ## Carbohydrates
        - MESH:D004364 ## Pharmaceutical Preparations
        - MESH:D006571 ## Heterocyclic Compounds
        - MESH:D007287 ## Inorganic Chemicals
        - MESH:D008055 ## Lipids
        - MESH:D009706 ## Nucleic Acids, Nucleotides, and Nucleosides
        - MESH:D009930 ## Organic Chemicals
        - MESH:D011083 ## Polycyclic Compounds
        - MESH:D013812 ## Therapeutics
        - MESH:D019602 ## Food and Beverages
        - MESH:D045424 ## Complex Mixtures
        - MESH:D045762 ## Enzymes and Coenzymes
        - MESH:D046911 ## Macromolecular Substances
  MeshDiseaseIdentifier:
    reachable_from:
      source_ontology: obo:mesh
      source_nodes:
        - MESH:D001423 ## Bacterial Infections and Mycoses
        - MESH:D001523 ## Mental Disorders
        - MESH:D002318 ## Cardiovascular Diseases
        - MESH:D002943 ## Circulatory and Respiratory Physiological Phenomena
        - MESH:D004066 ## Digestive System Diseases
        - MESH:D004700 ## Endocrine System Diseases
        - MESH:D005128 ## Eye Diseases
        - MESH:D005261 ## Female Urogenital Diseases and Pregnancy Complications
        - MESH:D006425 ## Hemic and Lymphatic Diseases
        - MESH:D007154 ## Immune System Diseases
        - MESH:D007280 ## Disorders of Environmental Origin
        - MESH:D009057 ## Stomatognathic Diseases
        - MESH:D009140 ## Musculoskeletal Diseases
        - MESH:D009358 ## Congenital, Hereditary, and Neonatal Diseases and Abnormalities
        - MESH:D009369 ## Neoplasms
        - MESH:D009422 ## Nervous System Diseases
        - MESH:D009750 ## Nutritional and Metabolic Diseases
        - MESH:D009784 ## Occupational Diseases
        - MESH:D010038 ## Otorhinolaryngologic Diseases
        - MESH:D010272 ## Parasitic Diseases
        - MESH:D012140 ## Respiratory Tract Diseases
        - MESH:D013568 ## Pathological Conditions, Signs and Symptoms
        - MESH:D014777 ## Virus Diseases
        - MESH:D014947 ## Wounds and Injuries
        - MESH:D017437 ## Skin and Connective Tissue Diseases
        - MESH:D052801 ## Male Urogenital Diseases
        - MESH:D064419 ## Chemically-Induced Disorders
```
