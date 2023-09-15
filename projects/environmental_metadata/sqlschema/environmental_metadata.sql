

CREATE TABLE "AnnotatorResult" (
	subject_text TEXT, 
	object_id TEXT, 
	object_text TEXT, 
	PRIMARY KEY (subject_text, object_id, object_text)
);

CREATE TABLE "Dataset" (
	packageid TEXT, 
	topic TEXT, 
	location TEXT, 
	environmental_material TEXT, 
	environments TEXT, 
	methods TEXT, 
	PRIMARY KEY (packageid, topic, location, environmental_material, environments, methods)
);

CREATE TABLE "Environment" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "EnvironmentalMaterial" (
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

CREATE TABLE "Location" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Method" (
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

CREATE TABLE "Topic" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);
