

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

CREATE TABLE "GeneLocation" (
	label TEXT, 
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "GoCamAnnotations" (
	genes TEXT, 
	organisms TEXT, 
	gene_organisms TEXT, 
	activities TEXT, 
	gene_functions TEXT, 
	cellular_processes TEXT, 
	pathways TEXT, 
	gene_gene_interactions TEXT, 
	gene_localizations TEXT, 
	PRIMARY KEY (genes, organisms, gene_organisms, activities, gene_functions, cellular_processes, pathways, gene_gene_interactions, gene_localizations)
);

CREATE TABLE "MolecularActivity" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Molecule" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Organism" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Pathway" (
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

CREATE TABLE "GeneGeneInteraction" (
	gene1 TEXT, 
	gene2 TEXT, 
	PRIMARY KEY (gene1, gene2), 
	FOREIGN KEY(gene1) REFERENCES "Gene" (id), 
	FOREIGN KEY(gene2) REFERENCES "Gene" (id)
);

CREATE TABLE "GeneMolecularActivityRelationship" (
	gene TEXT, 
	molecular_activity TEXT, 
	PRIMARY KEY (gene, molecular_activity), 
	FOREIGN KEY(gene) REFERENCES "Gene" (id), 
	FOREIGN KEY(molecular_activity) REFERENCES "MolecularActivity" (id)
);

CREATE TABLE "GeneMolecularActivityRelationship2" (
	gene TEXT, 
	molecular_activity TEXT, 
	target TEXT, 
	PRIMARY KEY (gene, molecular_activity, target), 
	FOREIGN KEY(gene) REFERENCES "Gene" (id), 
	FOREIGN KEY(molecular_activity) REFERENCES "MolecularActivity" (id), 
	FOREIGN KEY(target) REFERENCES "Molecule" (id)
);

CREATE TABLE "GeneOrganismRelationship" (
	gene TEXT, 
	organism TEXT, 
	PRIMARY KEY (gene, organism), 
	FOREIGN KEY(gene) REFERENCES "Gene" (id), 
	FOREIGN KEY(organism) REFERENCES "Organism" (id)
);

CREATE TABLE "GeneSubcellularLocalizationRelationship" (
	gene TEXT, 
	location TEXT, 
	PRIMARY KEY (gene, location), 
	FOREIGN KEY(gene) REFERENCES "Gene" (id), 
	FOREIGN KEY(location) REFERENCES "GeneLocation" (id)
);
