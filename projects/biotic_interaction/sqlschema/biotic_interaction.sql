

CREATE TABLE "AnnotatorResult" (
	subject_text TEXT, 
	object_id TEXT, 
	object_text TEXT, 
	PRIMARY KEY (subject_text, object_id, object_text)
);

CREATE TABLE "Container" (
	interactions TEXT, 
	PRIMARY KEY (interactions)
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

CREATE TABLE "InteractionType" (
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

CREATE TABLE "Taxon" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "TextWithTriples" (
	publication TEXT, 
	triples TEXT, 
	PRIMARY KEY (publication, triples)
);

CREATE TABLE "BioticInteraction" (
	source_taxon TEXT, 
	target_taxon TEXT, 
	interaction_type TEXT, 
	PRIMARY KEY (source_taxon, target_taxon, interaction_type), 
	FOREIGN KEY(source_taxon) REFERENCES "Taxon" (id), 
	FOREIGN KEY(target_taxon) REFERENCES "Taxon" (id), 
	FOREIGN KEY(interaction_type) REFERENCES "InteractionType" (id)
);
