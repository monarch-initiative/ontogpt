# Changing these values will change the behavior of the Makefile.
TEMPLATE_DIR = src/$(PACKAGE)/templates
EVAL_DIR = src/$(PACKAGE)/evaluation
TEMPLATES = core gocam mendelian_disease biological_process treatment environmental_sample metagenome_study reaction recipe ontology_class metabolic_process drug ctd halo gene_description_term
ENTRY_CLASSES = recipe.Recipe gocam.GoCamAnnotations reaction.ReactionDocument ctd.ChemicalToDiseaseDocument
