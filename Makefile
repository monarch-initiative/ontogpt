RUN = poetry run
PACKAGE = ontogpt
TEMPLATE_DIR = src/$(PACKAGE)/templates
EVAL_DIR = src/$(PACKAGE)/evaluation
TEMPLATES = core gocam mendelian_disease biological_process treatment environmental_sample metagenome_study reaction recipe ontology_class metabolic_process drug ctd halo
ENTRY_CLASSES = recipe.Recipe gocam.GoCamAnnotations reaction.ReactionDocument ctd.ChemicalToDiseaseDocument

all: all_pydantic all_projects

all_pydantic: $(patsubst %, $(TEMPLATE_DIR)/%.py, $(TEMPLATES))
all_projects: $(patsubst %, projects/%, $(TEMPLATES))
all_docs: $(patsubst %, docs/%/index.md, $(TEMPLATES))

test:
	$(RUN) pytest

$(TEMPLATE_DIR)/%.py: src/$(PACKAGE)/templates/%.yaml
	$(RUN) gen-pydantic $< > $@.tmp && mv $@.tmp $@

%.py: %.yaml
	$(RUN) gen-pydantic $< > $@

all_images: $(patsubst %, docs/images/%.png, $(ENTRY_CLASSES))
docs/images/%.png:
	$(RUN) erdantic ontogpt.templates.$* -o $@

projects/%: src/$(PACKAGE)/templates/%.yaml
	$(RUN) gen-project $< -d $@ && cp -pr $@/docs docs/$*

docs/index.md: README.md
	cp $< $@

docs/%/index.md: src/$(PACKAGE)/templates/%.yaml
	$(RUN) gen-doc --include-top-level-diagram --diagram-type er_diagram $< -d docs/$*


serve:
	$(RUN) mkdocs serve

gh-deploy:
	$(RUN) mkdocs gh-deploy
