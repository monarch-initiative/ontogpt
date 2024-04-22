

CREATE TABLE "AnnotatorResult" (
	subject_text TEXT, 
	object_id TEXT, 
	object_text TEXT, 
	PRIMARY KEY (subject_text, object_id, object_text)
);

CREATE TABLE "DiagnosticProcedure" (
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

CREATE TABLE "Phenotype" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ProcedureToAttributePredicate" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ProcedureToPhenotypePredicate" (
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

CREATE TABLE "Quality" (
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

CREATE TABLE "Unit" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ClinicalAttribute" (
	id TEXT NOT NULL, 
	label TEXT, 
	unit TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(unit) REFERENCES "Unit" (id)
);

CREATE TABLE "DiagnosticProceduretoAttributeAssociation" (
	qualifier TEXT, 
	subject TEXT, 
	object TEXT, 
	predicate TEXT, 
	subject_qualifier TEXT, 
	object_qualifier TEXT, 
	PRIMARY KEY (qualifier, subject, object, predicate, subject_qualifier, object_qualifier), 
	FOREIGN KEY(subject) REFERENCES "DiagnosticProcedure" (id), 
	FOREIGN KEY(predicate) REFERENCES "ProcedureToAttributePredicate" (id), 
	FOREIGN KEY(object_qualifier) REFERENCES "Quality" (id)
);

CREATE TABLE "DiagnosticProceduretoPhenotypeAssociation" (
	qualifier TEXT, 
	subject TEXT, 
	object TEXT, 
	predicate TEXT, 
	subject_qualifier TEXT, 
	object_qualifier TEXT, 
	PRIMARY KEY (qualifier, subject, object, predicate, subject_qualifier, object_qualifier), 
	FOREIGN KEY(subject) REFERENCES "DiagnosticProcedure" (id), 
	FOREIGN KEY(predicate) REFERENCES "ProcedureToPhenotypePredicate" (id)
);
