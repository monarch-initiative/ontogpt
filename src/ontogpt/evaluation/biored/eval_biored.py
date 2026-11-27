"""
BioRED evaluation.

This evaluation measures performance of OntoGPT
on relation extraction over the BioRED data set
(see Luo et al. 2022,
https://doi.org/10.1093/bib/bbac282).

The BioRED set includes 600 biomedical abstracts
annotated for multiple entity and relation types.
The entity types are as follows, grounded
to the following namespaces:
Gene (NCBI Gene)
Variant (dbSNP)
Species (NCBI Taxonomy)
Disease (MESH + OMIM)
Chemical (MESH Chemicals and Drugs)
CellLine (Cellosaurus)
The BioRED annotations include ungrounded but
normalized tmVar representations for variants without
corresponding dbSNP entries.

The relation types are as follows:
Disease-chemical
Disease-gene
Disease-variant
Disease-gene
Gene-gene
Gene-chemical
Chemical-chemical
Chemical-variant

Note that these relation types have subtypes as
well. See the BioRED annotation guide, Table 4,
for the full set
(https://ftp.ncbi.nlm.nih.gov/pub/lu/BioRED/BioRED_Annotation_Guideline.pdf)

Luo et al. report these F1 scores as best results:
NER: 89.3
RE: 47.7

This evaluation uses a task-specific template
(biored).

"""
