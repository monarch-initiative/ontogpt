

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

CREATE TABLE "OntologyClass" (
	id TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	categories TEXT, 
	subclass_of TEXT, 
	logical_definition TEXT, 
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

CREATE TABLE "Relation" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
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

CREATE TABLE "LogicalDefinition" (
	genus TEXT, 
	differentiating_characteristic_relationship TEXT, 
	differentiating_characteristic_parents TEXT, 
	PRIMARY KEY (genus, differentiating_characteristic_relationship, differentiating_characteristic_parents), 
	FOREIGN KEY(differentiating_characteristic_relationship) REFERENCES "Relation" (id)
);

CREATE TABLE "OntologyClass_synonyms" (
	backref_id TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (backref_id, synonyms), 
	FOREIGN KEY(backref_id) REFERENCES "OntologyClass" (id)
);
