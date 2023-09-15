

CREATE TABLE "AnnotatorResult" (
	subject_text TEXT, 
	object_id TEXT, 
	object_text TEXT, 
	PRIMARY KEY (subject_text, object_id, object_text)
);

CREATE TABLE "ChemicalEntity" (
	id TEXT NOT NULL, 
	label TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Evidence" (
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

CREATE TABLE "Organism" (
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

CREATE TABLE "ReactionGrouping" (
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

CREATE TABLE "GeneToReaction" (
	gene TEXT, 
	reactions TEXT, 
	organism TEXT, 
	PRIMARY KEY (gene, reactions, organism), 
	FOREIGN KEY(gene) REFERENCES "Gene" (id), 
	FOREIGN KEY(organism) REFERENCES "Organism" (id)
);

CREATE TABLE "Reaction" (
	id TEXT NOT NULL, 
	label TEXT, 
	description TEXT, 
	subclass_of TEXT, 
	left_side TEXT, 
	right_side TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(subclass_of) REFERENCES "ReactionGrouping" (id)
);

CREATE TABLE "ReactionDocument" (
	genes TEXT, 
	reactions TEXT, 
	gene_reaction_pairings TEXT, 
	organism TEXT, 
	has_evidence TEXT, 
	PRIMARY KEY (genes, reactions, gene_reaction_pairings, organism, has_evidence), 
	FOREIGN KEY(organism) REFERENCES "Organism" (id)
);

CREATE TABLE "GeneReactionPairing" (
	gene TEXT, 
	reaction TEXT, 
	PRIMARY KEY (gene, reaction), 
	FOREIGN KEY(gene) REFERENCES "Gene" (id), 
	FOREIGN KEY(reaction) REFERENCES "Reaction" (id)
);

CREATE TABLE "Reaction_synonyms" (
	backref_id TEXT, 
	synonyms TEXT, 
	PRIMARY KEY (backref_id, synonyms), 
	FOREIGN KEY(backref_id) REFERENCES "Reaction" (id)
);
