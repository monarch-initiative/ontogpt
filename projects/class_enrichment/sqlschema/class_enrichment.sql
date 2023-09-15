

CREATE TABLE "ClassEnrichmentConfiguration" (
	p_value_cutoff FLOAT NOT NULL, 
	PRIMARY KEY (p_value_cutoff)
);

CREATE TABLE "ClassEnrichmentResult" (
	class_id TEXT NOT NULL, 
	class_label TEXT, 
	rank INTEGER, 
	p_value FLOAT NOT NULL, 
	p_value_adjusted FLOAT, 
	false_discovery_rate FLOAT, 
	fold_enrichment FLOAT, 
	probability FLOAT, 
	sample_count INTEGER, 
	sample_total INTEGER, 
	background_count INTEGER, 
	background_total INTEGER, 
	ancestor_of_more_informative_result BOOLEAN, 
	descendant_of_more_informative_result BOOLEAN, 
	PRIMARY KEY (class_id, class_label, rank, p_value, p_value_adjusted, false_discovery_rate, fold_enrichment, probability, sample_count, sample_total, background_count, background_total, ancestor_of_more_informative_result, descendant_of_more_informative_result)
);

CREATE TABLE "ClassEnrichmentResultSet" (
	results TEXT, 
	PRIMARY KEY (results)
);
