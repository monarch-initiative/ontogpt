

CREATE TABLE "Action" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnnotatorResult" (
	subject_text TEXT, 
	object_id TEXT, 
	object_text TEXT, 
	PRIMARY KEY (subject_text, object_id, object_text)
);

CREATE TABLE "ExtractionResult" (
	input_id TEXT, 
	input_title TEXT, 
	input_text TEXT, 
	raw_completion_output TEXT, 
	prompt TEXT, 
	extracted_object TEXT, 
	named_entities TEXT, 
	PRIMARY KEY (input_id, input_title, input_text, raw_completion_output, prompt, extracted_object, named_entities)
);

CREATE TABLE "FoodType" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Publication" (
	id TEXT, 
	title TEXT, 
	abstract TEXT, 
	combined_text TEXT, 
	full_text TEXT, 
	PRIMARY KEY (id, title, abstract, combined_text, full_text)
);

CREATE TABLE "Recipe" (
	url TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	PRIMARY KEY (url)
);

CREATE TABLE "RelationshipType" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TextWithTriples" (
	publication TEXT, 
	triples TEXT, 
	PRIMARY KEY (publication, triples)
);

CREATE TABLE "Unit" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "UtensilType" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "FoodItem" (
	food TEXT, 
	state TEXT, 
	PRIMARY KEY (food, state), 
	FOREIGN KEY(food) REFERENCES "FoodType" (id)
);

CREATE TABLE "Ingredient" (
	food_item TEXT, 
	amount TEXT, 
	"Recipe_url" TEXT, 
	PRIMARY KEY (food_item, amount, "Recipe_url"), 
	FOREIGN KEY("Recipe_url") REFERENCES "Recipe" (url)
);

CREATE TABLE "Quantity" (
	value TEXT, 
	unit TEXT, 
	PRIMARY KEY (value, unit), 
	FOREIGN KEY(unit) REFERENCES "Unit" (id)
);

CREATE TABLE "RecipeCategory" (
	id TEXT NOT NULL, 
	label TEXT, 
	"Recipe_url" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Recipe_url") REFERENCES "Recipe" (url)
);

CREATE TABLE "Step" (
	action TEXT, 
	inputs TEXT, 
	outputs TEXT, 
	utensils TEXT, 
	"Recipe_url" TEXT, 
	PRIMARY KEY (action, inputs, outputs, utensils, "Recipe_url"), 
	FOREIGN KEY(action) REFERENCES "Action" (id), 
	FOREIGN KEY("Recipe_url") REFERENCES "Recipe" (url)
);
