"""
Evaluation on the CRAFT corpus.

This is an NER evaluation, or specifically
concept recognition.

It uses a specific template (craft_concepts)

The corpus is retrieved from:
https://github.com/UCDenver-ccp/CRAFT

This evaluation use the v5.0.2 release.

Funk et al. 2014 BMC Bioinformatics
(https://doi.org/10.1186/1471-2105-15-59)
reported that the ConceptMapper dictionary
lookup tool generally performed the best
across most ontologies,
with F-scores on these:
Cell Type Ontology (CL)  0.83
Gene Ontology (GO) Cellular Component  0.77
Gene Ontology (GO) Biological Process  0.37
Gene Ontology (GO) Molecular Function* 0.48
Sequence Ontology (SO)  0.56
Protein Ontology (PR) 0.57
NCBI Taxonomy (NCBITaxon) 0.69
CHEBI  0.56

* after adding synonyms without the word "activity"

"""