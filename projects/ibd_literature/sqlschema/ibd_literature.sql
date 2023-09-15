

CREATE TABLE "AnnotatorResult" (
	subject_text TEXT, 
	object_id TEXT, 
	object_text TEXT, 
	PRIMARY KEY (subject_text, object_id, object_text)
);

CREATE TABLE "CellularProcess" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ChemicalExposure" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "ChemicalExposureToGenePredicate" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Disease" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DiseaseToCellularProcessPredicate" (
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

CREATE TABLE "IBDAnnotations" (
	genes TEXT, 
	exposures TEXT, 
	gene_exposures_relationships TEXT, 
	diseases TEXT, 
	cellular_process TEXT, 
	disease_cellular_process_relationships TEXT, 
	PRIMARY KEY (genes, exposures, gene_exposures_relationships, diseases, cellular_process, disease_cellular_process_relationships)
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

CREATE TABLE "DiseaseCellularProcessRelationship" (
	qualifier TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_qualifier TEXT, 
	object_qualifier TEXT, 
	PRIMARY KEY (qualifier, subject, predicate, object, subject_qualifier, object_qualifier), 
	FOREIGN KEY(subject) REFERENCES "Disease" (id), 
	FOREIGN KEY(predicate) REFERENCES "DiseaseToCellularProcessPredicate" (id), 
	FOREIGN KEY(object) REFERENCES "CellularProcess" (id)
);

CREATE TABLE "GeneExposureRelationship" (
	qualifier TEXT, 
	subject TEXT, 
	predicate TEXT, 
	object TEXT, 
	subject_qualifier TEXT, 
	object_qualifier TEXT, 
	PRIMARY KEY (qualifier, subject, predicate, object, subject_qualifier, object_qualifier), 
	FOREIGN KEY(subject) REFERENCES "ChemicalExposure" (id), 
	FOREIGN KEY(predicate) REFERENCES "ChemicalExposureToGenePredicate" (id), 
	FOREIGN KEY(object) REFERENCES "Gene" (id)
);
