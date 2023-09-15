

CREATE TABLE "AnnotatorResult" (
	subject_text TEXT, 
	object_id TEXT, 
	object_text TEXT, 
	PRIMARY KEY (subject_text, object_id, object_text)
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

CREATE TABLE "Organism" (
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

CREATE TABLE "SequencingTechnology" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TextWithTriples" (
	publication TEXT, 
	triples TEXT, 
	PRIMARY KEY (publication, triples)
);

CREATE TABLE "Treatment" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Unit" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Variable" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "CausalRelationship" (
	cause TEXT, 
	effect TEXT, 
	PRIMARY KEY (cause, effect), 
	FOREIGN KEY(cause) REFERENCES "Variable" (id), 
	FOREIGN KEY(effect) REFERENCES "Variable" (id)
);

CREATE TABLE "Measurement" (
	value TEXT, 
	unit TEXT, 
	PRIMARY KEY (value, unit), 
	FOREIGN KEY(unit) REFERENCES "Unit" (id)
);

CREATE TABLE "Study" (
	environments TEXT, 
	causal_relationships TEXT, 
	variables TEXT, 
	treatments TEXT, 
	measurements TEXT, 
	location TEXT, 
	environmental_material TEXT, 
	sequencing_technologies TEXT, 
	organisms TEXT, 
	PRIMARY KEY (environments, causal_relationships, variables, treatments, measurements, location, environmental_material, sequencing_technologies, organisms), 
	FOREIGN KEY(sequencing_technologies) REFERENCES "SequencingTechnology" (id)
);
