# Bundled template catalog

Generated from `src/ontogpt/templates/*.yaml`. Regenerate when templates change. Use a template with `ontogpt extract -t <name>`; `<name>.<ClassName>` targets one class. Grounding prefixes tell you which identifier namespaces the output will carry.

| Template | Root class | Grounds to | What it extracts |
|---|---|---|---|
| `adverse_outcome_pathway` | AOPExtraction | CHEBI, CL, ENVO, GO, MONDO, NCIT, OPMI, UBERON | Template for extracting Adverse Outcome Pathways (AOPs) from literature. AOPs are conceptual frameworks that link a molecular initiating event to an adverse outcome through a series of key events. |
| `all_disease_grounding` | DiseaseTermSet | MONDO | Template for grounding disease names |
| `alzrd` | Document | CHEBI, ENVO, HP, MAXO, MESH, MONDO, MP, NBO, NCBITaxon, SNOMEDCT | Template for extracting phenotypes of Alzheimer's disease and related dementias along with experimental metrics and model organisms. Assumes a large input text, on the order of a full scientific article or review. Focus is on... |
| `alzrd_section` | Document | CHEBI, ENVO, HP, MAXO, MESH, MONDO, MP, NBO, NCBITaxon, SNOMEDCT | Template for extracting phenotypes of Alzheimer's disease and related dementias along with experimental metrics and model organisms. Assumes a large input text, on the order of a full scientific article or review. Focus is on... |
| `aop` | AOPExtraction | CHEBI, CL, ENVO, GO, MONDO, NCIT, OPMI, UBERON | Template for extracting Adverse Outcome Pathways (AOPs) from literature. AOPs are conceptual frameworks that link a molecular initiating event to an adverse outcome through a series of key events. |
| `biological_process` | BiologicalProcess | CHEBI, CL, GO, HGNC | A template for GO-CAMs |
| `biomed_terminology` | Document | GO, LOINC, MESH, NCIT, OBI, UBERON | A template for Biomedical Terminology |
| `biotic_interaction` | Container | RO | A template for biotic interactions |
| `cell_type` | CellType | CHEBI, CL, FBbt, GO, HGNC, HP, MGI, MONDO, PR, PW, UBERON, UniProtKB, WBbt | A template for representing cell types |
| `composite_disease` | CompositeDisease | HGNC, HP | A template for representing composite disease concepts |
| `condition` | Condition | SNOMEDCT | A FHIR-compliant template for conditions mentioned in a clinical note |
| `ctd` | (none; use -T) | MESH | A template for Chemical to Disease associations. This template is intended to represent associations between chemicals and diseases, and for evaluating Semantic Llama against BioCreative V Chemical Disease Relation (CDR) Task... |
| `ctd_ner` | (none; use -T) | MESH | A template for Chemical and Disease named entity recognition. This template is intended to represent entities (chemicals and diseases), and for evaluating SPIRES against the BioCreative V Disease Named Entity Recognition... |
| `data_sheets_schema` | DatasetCollection | ungrounded | A LinkML schema for Datasheets for Datasets. |
| `datasheet` | Dataset | NCIT, wikidata | A template for extracting metadata about a dataset, as defined by the Datasheets for Datasets model (see https://github.com/bridge2ai/data-sheets-schema), itself based on Gebru et al. (2021)... |
| `desiccation` | EntityContainingDocument | NCBITaxon, PECO, TO | A template for extracting ChEBI, GO, NCBITAXON, PO, TO, PECO |
| `diagnostic_procedure` | DiagnosticProceduretoPhenotypeAssociation | HP, LOINC, OBA, PATO, UO | A template for clinical diagnostic procedures and the phenotypes they may contribute to. |
| `dietitian_notes` | ClinicalObservations | CHEBI, DRUGBANK, EFO, FOODON, MAXO, MESH, MONDO, NCIT, UO, dbpediaont | A template for extracting clinical observations from dietitian notes. Developed with guidance from Lauren Chan, PhD, RD and Alyson Lawrence, RD, CNSC |
| `drug` | DrugMechanismSet | BIOLINK, CHEBI, CL, DRUGBANK, HGNC, MESH, MI, MONDO, PR, RO, UBERON | A template for extracting information about drug mechanisms of action, including the diseases they treat, the drugs themselves, and the detailed mechanistic pathways by which drugs produce their therapeutic effects. This... |
| `drug_to_disease` | Article | CHEBI, DRUGBANK, MONDO | A template for extracting relationships between drugs and diseases |
| `ecosim_methods` | TermSet | ungrounded | EcoSIM Methods Extraction Template |
| `ecosim_simple` | TermSet | ungrounded | Simple EcoSIM Extraction Template |
| `emapa_simple` | OntologyTermSet | EMAPA | Simple Mouse Developmental Anatomy Ontology Extraction Template |
| `environmental_metadata` | Dataset | ENVO, ENVTHES, GAZ | A template for categorizing Environmental Data Initiative data entries. See https://github.com/EDIorg/EDIorg-repository-index |
| `environmental_sample` | Study | ENVO, ENVTHES, GAZ, MIXS, NCIT, PATO, UO | A template for Environmental Samples |
| `environmental_sample_ungrounded` | Study | UO | A template for Environmental Samples, without any grounding beyond units |
| `figure` | FigureCaption | ungrounded | A template for Plazi figures and sub-parts |
| `food` | FoodSet | FOODON | A template for extracting food names and terms from text. |
| `foodon_simple` | OntologyTermSet | CHEBI, FOODON | Simple Food Ontology Extraction Template |
| `gene_description_term` | GeneDescriptionTerm | GO, HGNC, MESH, MONDO, UBERON | A simple GO term template for NER |
| `gene_extraction` | AcronymList | HGNC | A template demonstrating a general strategy for extracting gene symbols from ambiguous context. |
| `go_simple` | OntologyTermSet | GO | Simple Gene Ontology Extraction Template |
| `go_terms` | Document | GO | A template for GO Term and ID extraction. |
| `go_terms_relational` | Document | GO, HGNC, PR | A template for GO Term and ID extraction, as relations involving specific proteins. Note this does not make a distinction between GO term types. |
| `gocam` | GoCamAnnotations | CHEBI, CL, EFO, GO, HGNC, NCBITaxon, PR, PW, UBERON, UniProtKB | A template for GO-CAMs |
| `human_phenotype` | HumanPhenotypeSet | HP | A template for extracting human phenotypes to HPO terms |
| `ibd` | IBDAnnotations | CHEBI, CL, EFO, GO, HGNC, NCBITaxon, PR, PW, UBERON, UniProtKB | A template for GO-CAMs |
| `ibd_literature` | IBDAnnotations | CHEBI, ECTO, ExO, GO, HGNC, MONDO, NCIT, RO | A template for extracting information from IBD literature |
| `kidney` | KidneyAnnotations | CL, HGNC, UBERON | A template for extracting kidney info from literature |
| `maxo` | MaxoAnnotations | CHEBI, HP, MAXO, MONDO | A template for extracting relationships relevant to the MAXO medical action ontology. |
| `mendelian_disease` | MendelianDisease | HGNC, HP, MONDO | A template for GO-CAMs |
| `metabolic_process` | (none; use -T) | CHEBI, GO | A template for GO-CAMs |
| `metagenome_study` | (none; use -T) | EFO, ENVO, GAZ, IDO, MIXS, NCBITaxon, NCIT, OBI, PATO, PECO, UO | A template for Environmental Metagenome Studies |
| `mic` | Document | CHEBI, EFO, FOODON, GO, HP, MONDO, RO, UBERON, biolink | A template for micronutrient information from text, including its participation in biochemical pathways and relationships to genes and diseases. Intended for use with the Micronutrient Information Center, a resource curated... |
| `miro` | Ontology | ungrounded | A template for extracting the minimal information for reporting an ontology, as per the MIRO guidelines. See doi:10.1186/s13326-017-0172-7 The target for this template should be a report or publication describing a single... |
| `mondo_simple` | OntologyTermSet | MONDO | Simple MONDO Disease Ontology Extraction Template |
| `nmdc_schema_data` | Dataset | ENVO | A template for populating nmdc-schema required slots from data entries. Primarily, this involves three different levels corresponding to ENVO terms, as well as conversion of NLCD values and FAO soil taxonomy classes to ENVO. |
| `onto_usage` | Document | ungrounded | A template for extracting statements about the usage of ontologies in scientific literature. |
| `ontology_class` | OntologyClass | RO | A template for Ontology Classes |
| `ontology_issue` | OntologyIssue | ungrounded | A data model for representing the contents of a GitHub issue on an ontology tracker |
| `pathology` | PathologyReport | ICD10CM, PATO, SNOMEDCT, UBERON | A template for extracting and grounding pathology descriptions from text. |
| `pet_breed` | BreedDescription | PATO, UBERON, UPHENO, VBO | Extracts a structured description of a single cat or dog breed from an encyclopedia-style text such as a Wikipedia article. Breed grounds to VBO (restricted to cat and dog breeds); each characteristic is split into phenotype (UPHENO), body part (UBERON), and quality (PATO). Also year established, origin, coat colours, temperament. |
| `phenopackets` | PhenopacketCollection | CHEBI, CL, CMO, DRUGBANK, ECO, EFO, GENO, GSSO, HP, MAXO, MONDO, NCIT, OAE, PATO, SO, UBERON, UO | A template for extracting a phenopacket, an anonymous phenotypic description of an individual or biosample with potential genes of interest and/or diagnoses. This template is based on the Phenopackets schema v2, originally... |
| `phenotype` | Trait | CHEBI, PATO, PR, UBERON | A template for Computational Phenotypes |
| `predator_prey` | PredatorPreyRelationship | NCBITaxon | A template for extracting information about predator-prey relationships in ecological contexts |
| `reaction` | Reaction | CHEBI, ECO, GO, HGNC, MS, NCBITaxon, OBI | A template for reactions |
| `recipe` | Recipe | FOODON, HANCESTRO, NCIT, UO, dbpediaont | A template for food recipes |
| `storms` | STORMSChecklist | ungrounded | A template for extracting information using STORMS checklist |
| `traits` | Taxon | BIODIVTHES, ECOCORE, GO, OBA, PATO | A template for Traits |
| `treatment` | DiseaseTreatmentSummary | HGNC, HP | A template for MAXO treatments |
| `vbo_char` | NameSet | ungrounded | An extraction template for animal names present in VBO, along with the characteristics of each breed |
| `vbo_names` | NameSet | ungrounded | An extraction template for animal names present in VBO |

## Templates that are not for text extraction

- `core`: the upper-level schema every template imports (NamedEntity, CompoundExpression, Triple).
- `halo`: schema for the HALO ontology-growing engine (`ontogpt halo`), not SPIRES.
- `class_enrichment`, `genesummary`: gene-set enrichment and summary experiments (`ontogpt enrichment`, `eval`).
- `error_analysis`, `matrix_eval`: data-model templates for reports and evaluations, not literature.
- `personinfo`: a demo schema with no grounding.
- `table_arrays`, `table_values`: numeric table capture from PDFs; no ontology grounding.
