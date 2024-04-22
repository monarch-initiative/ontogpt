

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
	metabolic_traits TEXT, 
	morphological_traits TEXT, 
	genetic_traits TEXT, 
	cellular_traits TEXT, 
	ecological_traits TEXT, 
	reproductive_traits TEXT, 
	survival_traits TEXT, 
	phenotypic_plasticiticy_traits TEXT, 
	preferred_environments TEXT, 
	PRIMARY KEY (metabolic_traits, morphological_traits, genetic_traits, cellular_traits, ecological_traits, reproductive_traits, survival_traits, phenotypic_plasticiticy_traits, preferred_environments)
);

CREATE TABLE "TextWithTriples" (
	publication TEXT, 
	triples TEXT, 
	PRIMARY KEY (publication, triples)
);

CREATE TABLE "Trait" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);
