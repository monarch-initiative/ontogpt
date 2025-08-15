RUN = uv run
TMPRUN = 
PACKAGE = ontogpt
TEMPLATE_DIR = src/$(PACKAGE)/templates
EVAL_DIR = src/$(PACKAGE)/evaluation
TEMPLATES = $(notdir $(basename $(wildcard $(TEMPLATE_DIR)/*.yaml)))
ENTRY_CLASSES = recipe.Recipe gocam.GoCamAnnotations reaction.ReactionDocument ctd.ChemicalToDiseaseDocument figure.FigureCaption

all: all_pydantic

all_pydantic: $(patsubst %, $(TEMPLATE_DIR)/%.py, $(TEMPLATES))
all_projects: $(patsubst %, projects/%, $(TEMPLATES))
all_docs: $(patsubst %, docs/%/index.md, $(TEMPLATES))

list_templates: $(TEMPLATE_DIR)/*.yaml
	@echo $(basename $^)

test: unit-test

unit-test:
	$(RUN) python -m unittest discover tests.unit

integration-test:
	$(RUN) python -m unittest

get_version:
	$(RUN) python -c "import ontogpt;print('.'.join((ontogpt.__version__).split('.', 3)[:3]))"

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
	$(RUN) gen-doc --include-top-level-diagram --diagram-type er_diagram $< -d docs/$*

serve:
	$(RUN) mkdocs serve

gh-deploy:
	$(RUN) mkdocs gh-deploy

# -- OWL Pipeline --


all_recipes: tests/output/owl/merged/recipe-all-merged.owl

# prefix with 'web' for a URL in recipe-urls.csv
# prefix with 'case' for a previously downloaded recipe in cases/ directory
RECIPES = case-spaghetti case-egg-noodles case-tortilla-soup \
 web-spinach-and-feta-turkey-burgers \
 web-shrimp-and-cheesy-grits-with-bacon \
 web-easy-french-toast-waffles \
 web-easy-palak-paneer \
 web-sweet-chili-thai-sauce \
 web-grilled-asparagus \
 web-sauteed-lacinato-kale \
 web-quick-pickled-onions \
 web-deviled-eggs-106562 \
 web-corn-dog \
 web-spicy-thai-basil-chicken-pad-krapow-gai \
 web-marinated-summer-squash-with-hazelnuts-and-ricotta \
 web-Waldorf \
 web-red-lentil-soup \
 web-sweet-and-spicy-pork-and-napa-cabbage-stir-fry-with-spicy-noodles

RECIPE_URLS_FILE = tests/input/recipe-urls.csv
RECIPE_GROUPINGS = src/ontogpt/owl/recipe-groupings.ofn

tests/output/owl/recipe-case-%.owl: tests/input/cases/recipe-%.txt
	$(RUN) ontogpt extract -t recipe $< --set-slot-value url=https://w3id.org/ontogpt/recipes/instances/$* -o $@ -O owl
.PRECIOUS: tests/output/owl/recipe-case-%.owl

tests/output/owl/recipe-web-%.owl: 
	$(RUN) ontogpt recipe-extract $* -R $(RECIPE_URLS_FILE) -o $@ -O owl
.PRECIOUS: tests/output/owl/recipe-web-%.owl

tests/output/owl/recipe-web-%.yaml: 
	$(RUN) ontogpt recipe-extract $* -R $(RECIPE_URLS_FILE) -o $@ -O yaml
.PRECIOUS: tests/output/owl/recipe-web-%.yaml

tests/output/owl/recipe-all.owl: $(patsubst %, tests/output/owl/recipe-%.owl, $(RECIPES))
	robot merge $(patsubst %, -i %, $^) -o $@
.PRECIOUS: tests/output/owl/recipe-all.owl

# seed terms for ROBOT extract
tests/output/owl/seed-recipe-%.txt: tests/output/owl/recipe-%.owl
	robot query -i $< -f csv -q tests/input/queries/terms.rq $@
.PRECIOUS: tests/output/owl/seed-recipe-%.txt

FOODON = tests/output/owl/imports/foodon.owl
$(FOODON):
	curl -L -s http://purl.obolibrary.org/obo/foodon.owl > $@
.PRECIOUS: $(FOODON)

tests/output/owl/imports/recipe-%-import.owl: tests/output/owl/seed-recipe-%.txt $(FOODON)
	robot extract -i $(FOODON) -m BOT -T $< -o $@

tests/output/owl/merged/recipe-%-merged.owl: tests/output/owl/imports/recipe-%-import.owl $(RECIPE_GROUPINGS)
	robot merge -i tests/output/owl/recipe-$*.owl -i $(RECIPE_GROUPINGS) -i $< reason -r elk -o $@
