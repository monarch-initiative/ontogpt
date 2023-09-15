

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

CREATE TABLE "Inheritance" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Onset" (
	id TEXT NOT NULL, 
	label TEXT, 
	years_old TEXT, 
	juvenile_or_adult TEXT, 
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

CREATE TABLE "MendelianDisease" (
	id TEXT NOT NULL, 
	label TEXT, 
	name TEXT, 
	description TEXT, 
	inheritance TEXT, 
	disease_onsets TEXT, 
	publications TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(inheritance) REFERENCES "Inheritance" (id)
);

CREATE TABLE "Onset_decades" (
	backref_id TEXT, 
	decades TEXT, 
	PRIMARY KEY (backref_id, decades), 
	FOREIGN KEY(backref_id) REFERENCES "Onset" (id)
);

CREATE TABLE "DiseaseCategory" (
	id TEXT NOT NULL, 
	label TEXT, 
	"MendelianDisease_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("MendelianDisease_id") REFERENCES "MendelianDisease" (id)
);

CREATE TABLE "Gene" (
	id TEXT NOT NULL, 
	label TEXT, 
	"MendelianDisease_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("MendelianDisease_id") REFERENCES "MendelianDisease" (id)
);

CREATE TABLE "Symptom" (
	id TEXT NOT NULL, 
	label TEXT, 
	characteristic TEXT, 
	affects TEXT, 
	severity TEXT, 
	onset_of_symptom TEXT, 
	"MendelianDisease_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(onset_of_symptom) REFERENCES "Onset" (id), 
	FOREIGN KEY("MendelianDisease_id") REFERENCES "MendelianDisease" (id)
);

CREATE TABLE "MendelianDisease_synonyms" (
	backref_id TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (backref_id, synonyms), 
	FOREIGN KEY(backref_id) REFERENCES "MendelianDisease" (id)
);
