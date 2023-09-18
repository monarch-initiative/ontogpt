

CREATE TABLE "AnnotatorResult" (
	subject_text TEXT, 
	object_id TEXT, 
	object_text TEXT, 
	PRIMARY KEY (subject_text, object_id, object_text)
);

CREATE TABLE "Disease" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Drug" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
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

CREATE TABLE "MechanismElement" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Predicate" (
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

CREATE TABLE "DrugMechanism" (
	disease TEXT, 
	drug TEXT, 
	mechanism_links TEXT, 
	"references" TEXT, 
	source_text TEXT, 
	PRIMARY KEY (disease, drug, mechanism_links, "references", source_text), 
	FOREIGN KEY(disease) REFERENCES "Disease" (id), 
	FOREIGN KEY(drug) REFERENCES "Drug" (id)
);

CREATE TABLE "MechanismLink" (
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	PRIMARY KEY (subject, predicate, object), 
	FOREIGN KEY(subject) REFERENCES "MechanismElement" (id), 
	FOREIGN KEY(predicate) REFERENCES "Predicate" (id), 
	FOREIGN KEY(object) REFERENCES "MechanismElement" (id)
);
