# Evaluations

OpenAI's functions have been evaluated on test data sets.

All evaluation results include OpenAI cache databases (`openai_cache.db.gz`) as a reference of the prompts and responses obtained during the evaluation. This may be used by extracting the cache database to the root directory of the project.

## BC5CDR

Results for OntoGPT on the [BioCreative V Chemical Disease Relation Task (BC5CDR)](https://biocreative.bioinformatics.udel.edu/media/store/files/2015/BC5CDR_overview.final.pdf) are available on Zenodo here: <https://zenodo.org/record/7657763>

Evaluation functions for BC5CDR are available in `src/ontogpt/evaluation/ctd/eval_ctd.py`.

Note that the project also included test and train data (`CDR_TestSet.BioC.xml.gz` and `CDR_TrainSet.BioC.xml.gz`, respectively) as well as a set of synonyms for MeSH terms (see `synonyms.yaml`).
