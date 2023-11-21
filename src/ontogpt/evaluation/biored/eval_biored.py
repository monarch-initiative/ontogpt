"""
BioRED evaluation.

This evaluation measures performance of OntoGPT
on relation extraction over the BioRED data set
(see Luo et al. 2022,
https://doi.org/10.1093/bib/bbac282).

The BioRED set includes 600 biomedical abstracts
annotated for multiple entity and relation types.

Luo et al. report these F1 scores as best results:
NER: 89.3
RE: 47.7

This evaluation uses a task-specific template
(biored).

"""
