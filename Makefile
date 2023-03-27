RUN = poetry run
# NOTE: we are currently pinned to an earlier linkml because pydantic...
TMPRUN = 
PACKAGE = ontogpt
TEMPLATE_DIR = src/$(PACKAGE)/templates
EVAL_DIR = src/$(PACKAGE)/evaluation
TEMPLATES = core gocam mendelian_disease biological_process treatment environmental_sample metagenome_study reaction recipe ontology_class metabolic_process drug ctd halo
ENTRY_CLASSES = recipe.Recipe gocam.GoCamAnnotations reaction.ReactionDocument ctd.ChemicalToDiseaseDocument

all: all_pydantic all_projects

all_pydantic: $(patsubst %, $(TEMPLATE_DIR)/%.py, $(TEMPLATES))
all_projects: $(patsubst %, projects/%, $(TEMPLATES))
all_docs: $(patsubst %, docs/%/index.md, $(TEMPLATES))

test: unit-test

unit-test:
	$(RUN) python -m unittest discover tests.unit

integration-test:
	$(RUN) python -m unittest


$(TEMPLATE_DIR)/%.py: src/$(PACKAGE)/templates/%.yaml
	$(RUN) gen-pydantic $< > $@.tmp && mv $@.tmp $@

%.py: %.yaml
	$(RUN) gen-pydantic $< > $@

#all_images: $(patsubst %, docs/images/%.png, $(ENTRY_CLASSES))
#docs/images/%.png:
#	$(RUN) erdantic ontogpt.templates.$* -o $@

projects/%: src/$(PACKAGE)/templates/%.yaml
	$(RUN) gen-project $< -d $@ && cp -pr $@/docs docs/$*

docs/index.md: README.md
	cp $< $@

docs/%/index.md: src/$(PACKAGE)/templates/%.yaml
	$(TMPRUN) gen-doc --include-top-level-diagram --diagram-type er_diagram $< -d docs/$*


serve:
	$(RUN) mkdocs serve

gh-deploy:
	$(RUN) mkdocs gh-deploy

tests/output/owl/recipe-%.owl: tests/input/cases/recipe-%.txt
	$(RUN) ontogpt extract -t recipe $< -o $@ -O owl

tests/output/owl/seed-recipe-%.txt: tests/output/owl/recipe-%.owl
	robot query -i $< -f csv -q tests/input/queries/terms.rq $@

FOODON = tests/output/owl/imports/foodon.owl
$(FOODON):
	curl -L -s http://purl.obolibrary.org/obo/foodon.owl > $@

tests/output/owl/imports/recipe-%-import.owl: tests/output/owl/seed-recipe-%.txt $(FOODON)
	robot extract -i $(FOODON) -m BOT -T $< -o $@

tests/output/owl/merged/recipe-%-merged.owl: tests/output/owl/imports/recipe-%-import.owl
	robot merge -i tests/output/owl/recipe-$*.owl -i $< reason -r elk -o $@
