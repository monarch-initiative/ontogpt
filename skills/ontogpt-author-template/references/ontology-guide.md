# Choosing ontologies and annotators

The grounder is OAK. An annotator string is an OAK selector. The prefix in `id_prefixes` must be the prefix OAK returns for that source, spelled the way OAK spells it.

## Selector forms

| Selector | Source | Needs | Notes |
|---|---|---|---|
| `sqlite:obo:<ont>` | prebuilt SQLite of an OBO ontology, downloaded from the semantic-sql S3 bucket on first use | internet once; disk under `~/.data/oaklib` (`PYSTOW_HOME` to move) | the default choice. Fast after download. Exact and partial label and synonym matches. |
| `bioportal:<ACRONYM>` | NCBO BioPortal annotator | `runoak set-apikey -e bioportal <key>`; network per call | any of ~1000 BioPortal ontologies, e.g. `bioportal:SNOMEDCT`, `bioportal:hgnc-nr`, `bioportal:ENVTHES`. Returns purl-style ids that OntoGPT normalizes. Slow in batches. |
| `gilda:` | Gilda grounding service (genes, proteins, chemicals, families) | `pip install ontogpt[gilda]` | returns HGNC, UniProtKB, FPLX, CHEBI, MESH ids. Good first annotator for genes. |
| `ols:<ont>` | EBI Ontology Lookup Service | network | fallback when no sqlite build exists |
| `ubergraph:` | Ubergraph SPARQL over merged OBO | network | rarely needed |

Check a selector before trusting it:

```bash
runoak -i sqlite:obo:mondo annotate "type 2 diabetes mellitus"
runoak -i sqlite:obo:hp info HP:0001250
```

If `sqlite:obo:<ont>` fails with a 404, no build exists for that ontology name; try `ols:` or `bioportal:`.

## Which ontology for which entity

Prefer OBO Foundry ontologies; they have sqlite builds, stable prefixes, and cross-references. Bundled templates use these combinations.

| Entity kind | Ontology (prefix) | Annotator | When to add a second |
|---|---|---|---|
| Disease, disorder, syndrome | MONDO (`MONDO`) | `sqlite:obo:mondo` | `sqlite:obo:mesh` (`MESH`) for MeSH-indexed literature; `sqlite:obo:doid` for DOID users; `sqlite:obo:ncit` for oncology |
| Human phenotype, sign, symptom, clinical finding | HPO (`HP`) | `sqlite:obo:hp` | `sqlite:obo:mp` (`MP`) for mouse; `sqlite:obo:pato` (`PATO`) for bare qualities |
| Chemical, metabolite, small molecule | ChEBI (`CHEBI`) | `sqlite:obo:chebi` | `sqlite:obo:mesh` for drug names not in ChEBI |
| Drug, medication | DrugBank (`DRUGBANK`), ChEBI | `sqlite:obo:drugbank, sqlite:obo:chebi` | `sqlite:obo:mesh`; `sqlite:obo:ncit` for oncology regimens |
| Gene (human) | HGNC (`HGNC`) | `gilda:` then `sqlite:obo:hgnc` or `bioportal:hgnc-nr` | `sqlite:obo:pr` (`PR`) for proteins; UniProt via gilda |
| Gene (mouse, other) | MGI (`MGI`), or organism gene DBs | `gilda:` | consider a `--dictionary` of symbols to ids for the organism |
| Protein, complex, enzyme | PRO (`PR`) | `sqlite:obo:pr` | `gilda:` for families (`FPLX`) |
| Biological process, molecular function, cellular component | GO (`GO`) | `sqlite:obo:go` | restrict with a dynamic enum rooted at `GO:0008150`, `GO:0003674`, or `GO:0005575` |
| Pathway | GO, Pathway Ontology (`PW`) | `sqlite:obo:go, sqlite:obo:pw` | |
| Anatomy (vertebrate, human) | Uberon (`UBERON`) | `sqlite:obo:uberon` | `sqlite:obo:fma`; species anatomy: `sqlite:obo:emapa` mouse dev, `sqlite:obo:zfa`, `sqlite:obo:fbbt`, `sqlite:obo:wbbt`, `sqlite:obo:po` plants |
| Cell type | CL (`CL`) | `sqlite:obo:cl` | `sqlite:obo:uberon` for tissues |
| Organism, taxon, strain | NCBI Taxonomy (`NCBITaxon`) | `sqlite:obo:ncbitaxon` | large download (~1 GB). `gilda:` handles common names. `sqlite:obo:vbo` for breeds. |
| Environment, biome, habitat, material | ENVO (`ENVO`) | `sqlite:obo:envo` | `bioportal:ENVTHES` |
| Food, ingredient, dish | FoodOn (`FOODON`) | `sqlite:obo:foodon` | `sqlite:obo:chebi` for nutrients |
| Medical action, treatment, procedure | MAXO (`MAXO`) | `sqlite:obo:maxo` | `sqlite:obo:ncit`, `bioportal:SNOMEDCT` |
| Assay, instrument, protocol | OBI (`OBI`) | `sqlite:obo:obi` | `sqlite:obo:ncit` |
| Unit | UO (`UO`) | `sqlite:obo:uo` | |
| Quality, trait | PATO (`PATO`), OBA (`OBA`) | `sqlite:obo:pato, sqlite:obo:oba` | plant traits: `sqlite:obo:to`, conditions `sqlite:obo:peco` |
| Sequence feature, variant type | SO (`SO`) | `sqlite:obo:so` | |
| Relation, predicate | RO (`RO`), Biolink (`biolink`) | `sqlite:obo:ro, sqlite:obo:biolink` | predicates often stay `AUTO:`; that is acceptable if downstream only needs entities |
| Behavior | NBO (`NBO`) | `sqlite:obo:nbo` | |
| Broad clinical or biomedical catch-all | NCIT (`NCIT`) | `sqlite:obo:ncit` | large; good last resort |
| Clinical terminology with SNOMED requirement | SNOMED (`SNOMEDCT`) | `bioportal:SNOMEDCT` | needs a BioPortal key |
| Literature-indexed anything | MeSH (`MESH`) | `sqlite:obo:mesh` | prefer a domain ontology first, MeSH second |

## Rules

- **Prefix spelling is OAK's.** `HP` not `HPO`. `NCBITaxon` with that capitalization. `CHEBI` upper. `biolink` lower in `core` (`RelationshipType`). When unsure, run `runoak -i <selector> annotate "<term>"` and read the prefix it returns.
- **Order annotators by trust.** The first annotator that matches wins, and whole-text matches from any annotator beat partial matches from all of them.
- **Declare every prefix under `prefixes:`** with its URI expansion so exports can expand it.
- **Restrict with `values_from` when a broad ontology would over-match.** Grounding "cell" to GO returns cellular component terms unless you filter to `GO:0005575` descendants or use CL.
- **Two or three annotators per class.** Each adds download time and partial-match noise.
- **Consider a `--dictionary` file** for project-specific vocabularies (strain names, local gene symbols) instead of a new annotator.

## Availability

`sqlite:obo:<id>` works for every OBO Foundry ontology (use the lowercase OBO id: `hp`, `mondo`, `mp`, `doid`, `emapa`, `po`, `so`, and so on) and for the extra sources registered in semantic-sql, including `mesh`, `drugbank`, `hgnc`, `ncit`, `biolink`, `efo`, `omim`, `icd10cm`, `rhea`, `uniprot`, `cellosaurus`, and `envthes`. The extra list lives at https://github.com/INCATools/semantic-sql/blob/main/src/semsql/builder/registry/ontologies.yaml. Confirm with `runoak -i sqlite:obo:<ont> annotate "<a term you expect>"` before writing a template that depends on one; a 404 on download means no build.
