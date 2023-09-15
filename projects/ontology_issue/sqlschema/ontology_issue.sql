

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

CREATE TABLE "OntologyChange" (
	description TEXT, 
	category VARCHAR(17), 
	about TEXT, 
	PRIMARY KEY (description, category, about)
);

CREATE TABLE "OntologyClass" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "OntologyIssue" (
	title TEXT, 
	summary TEXT, 
	status TEXT, 
	domains TEXT, 
	problem_list TEXT, 
	proposed_changes TEXT, 
	PRIMARY KEY (title, summary, status, domains, problem_list, proposed_changes)
);

CREATE TABLE "OntologyProblem" (
	description TEXT, 
	severity TEXT, 
	category VARCHAR(18), 
	about TEXT, 
	PRIMARY KEY (description, severity, category, about)
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
