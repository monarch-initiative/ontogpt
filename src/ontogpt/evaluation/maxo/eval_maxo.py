"""
MAXO annotation evaluation.

Annotations in the Medical Action Ontology (MAXO)
may be between a MAXO term and a phenotype,
denoted with a Human Phenotype Ontology (HP) term,
or between a MAXO term and a disease,
denoted with a Mondo Disease Ontology (MONDO) term.

See:
https://github.com/monarch-initiative/maxo-annotations/

This evaluation uses the maxo template to extract
annotations from the text provided in each test case
(see the test_cases directory) and compares them to
the annotations accompanying the case. The existing
annotations are from the set of manual annotations
in the above repository
(see https://github.com/monarch-initiative/maxo-annotations/blob/master/annotations/maxo-annotations.tsv)
though the annotations are not considered disease-specific
for the purposes of this evaluation.

"""

