

CREATE TABLE "AdverseEffect" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AnnotatorResult" (
	subject_text TEXT, 
	object_id TEXT, 
	object_text TEXT, 
	PRIMARY KEY (subject_text, object_id, object_text)
);

CREATE TABLE "Disease" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Drug" (
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

CREATE TABLE "Mechanism" (
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

CREATE TABLE "Symptom" (
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

CREATE TABLE "DiseaseTreatmentSummary" (
	disease TEXT, 
	drugs TEXT, 
	treatments TEXT, 
	contraindications TEXT, 
	treatment_mechanisms TEXT, 
	treatment_efficacies TEXT, 
	treatment_adverse_effects TEXT, 
	PRIMARY KEY (disease, drugs, treatments, contraindications, treatment_mechanisms, treatment_efficacies, treatment_adverse_effects), 
	FOREIGN KEY(disease) REFERENCES "Disease" (id)
);

CREATE TABLE "TreatmentAdverseEffect" (
	treatment TEXT, 
	adverse_effects TEXT, 
	PRIMARY KEY (treatment, adverse_effects), 
	FOREIGN KEY(treatment) REFERENCES "Treatment" (id)
);

CREATE TABLE "TreatmentEfficacy" (
	treatment TEXT, 
	efficacy TEXT, 
	PRIMARY KEY (treatment, efficacy), 
	FOREIGN KEY(treatment) REFERENCES "Treatment" (id)
);

CREATE TABLE "TreatmentMechanism" (
	treatment TEXT, 
	mechanism TEXT, 
	PRIMARY KEY (treatment, mechanism), 
	FOREIGN KEY(treatment) REFERENCES "Treatment" (id), 
	FOREIGN KEY(mechanism) REFERENCES "Mechanism" (id)
);
