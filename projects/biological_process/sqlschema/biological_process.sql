

CREATE TABLE "AnnotatorResult" (
	subject_text TEXT, 
	object_id TEXT, 
	object_text TEXT, 
	PRIMARY KEY (subject_text, object_id, object_text)
);

CREATE TABLE "BiologicalProcess" (
	id TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	inputs TEXT, 
	outputs TEXT, 
	steps TEXT, 
	genes TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subclass_of) REFERENCES "BiologicalProcess" (id)
);

CREATE TABLE "ChemicalEntity" (
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

CREATE TABLE "Gene" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "MolecularActivity" (
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

CREATE TABLE "GeneMolecularActivityRelationship" (
	gene TEXT, 
	molecular_activity TEXT, 
	"BiologicalProcess_id" TEXT, 
	PRIMARY KEY (gene, molecular_activity, "BiologicalProcess_id"), 
	FOREIGN KEY(gene) REFERENCES "Gene" (id), 
	FOREIGN KEY(molecular_activity) REFERENCES "MolecularActivity" (id), 
	FOREIGN KEY("BiologicalProcess_id") REFERENCES "BiologicalProcess" (id)
);

CREATE TABLE "BiologicalProcess_synonyms" (
	backref_id TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (backref_id, synonyms), 
	FOREIGN KEY(backref_id) REFERENCES "BiologicalProcess" (id)
);
