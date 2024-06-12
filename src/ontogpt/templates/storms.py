from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass


class NullDataOptions(str, Enum):
    UNSPECIFIED_METHOD_OF_ADMINISTRATION = "UNSPECIFIED_METHOD_OF_ADMINISTRATION"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    NOT_MENTIONED = "NOT_MENTIONED"


class ExtractionResult(ConfiguredBaseModel):
    """
    A result of extracting knowledge on text
    """
    input_id: Optional[str] = Field(None)
    input_title: Optional[str] = Field(None)
    input_text: Optional[str] = Field(None)
    raw_completion_output: Optional[str] = Field(None)
    prompt: Optional[str] = Field(None)
    extracted_object: Optional[Any] = Field(None, description="""The complex objects extracted from the text""")
    named_entities: Optional[List[Any]] = Field(default_factory=list, description="""Named entities extracted from the text""")


class NamedEntity(ConfiguredBaseModel):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class CompoundExpression(ConfiguredBaseModel):
    pass


class Triple(CompoundExpression):
    """
    Abstract parent for Relation Extraction tasks
    """
    subject: Optional[str] = Field(None)
    predicate: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    qualifier: Optional[str] = Field(None, description="""A qualifier for the statements, e.g. \"NOT\" for negation""")
    subject_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the subject of the statement, e.g. \"high dose\" or \"intravenously administered\"""")
    object_qualifier: Optional[str] = Field(None, description="""An optional qualifier or modifier for the object of the statement, e.g. \"severe\" or \"with additional complications\"""")


class TextWithTriples(ConfiguredBaseModel):
    """
    A text containing one or more relations of the Triple type.
    """
    publication: Optional[Publication] = Field(None)
    triples: Optional[List[Triple]] = Field(default_factory=list)


class TextWithEntity(ConfiguredBaseModel):
    """
    A text containing one or more instances of a single type of entity.
    """
    publication: Optional[Publication] = Field(None)
    entities: Optional[List[str]] = Field(default_factory=list)


class RelationshipType(NamedEntity):
    id: str = Field(..., description="""A unique identifier for the named entity""")
    label: Optional[str] = Field(None, description="""The label (name) of the named thing""")


class Publication(ConfiguredBaseModel):
    id: Optional[str] = Field(None, description="""The publication identifier""")
    title: Optional[str] = Field(None, description="""The title of the publication""")
    abstract: Optional[str] = Field(None, description="""The abstract of the publication""")
    combined_text: Optional[str] = Field(None)
    full_text: Optional[str] = Field(None, description="""The full text of the publication""")


class AnnotatorResult(ConfiguredBaseModel):
    subject_text: Optional[str] = Field(None)
    object_id: Optional[str] = Field(None)
    object_text: Optional[str] = Field(None)


class STORMSChecklist(ConfiguredBaseModel):
    """
    The complete STORMS checklist.
    """
    abstract_structured_or_unstructured: Optional[str] = Field(None, description="""Abstract should include information on background, methods, results, and conclusions in structured or unstructured format.""")
    abstract_study_design: Optional[str] = Field(None, description="""State study design in abstract.""")
    abstract_sequencing_methods: Optional[str] = Field(None, description="""State the strategy used for metagenomic classification.""")
    abstract_specimens: Optional[str] = Field(None, description="""Describe body site(s) studied.""")
    introduction_background_and_rationale: Optional[str] = Field(None, description="""Summarize the underlying background, scientific evidence, or theory driving the current hypothesis as well as the study objectives.""")
    introduction_hypotheses: Optional[str] = Field(None, description="""State the pre-specified hypothesis. If the study is exploratory, state any pre-specified study objectives.""")
    methods_study_design: Optional[str] = Field(None, description="""Describe the study design.""")
    methods_participants: Optional[str] = Field(None, description="""State what the population of interest is, and the method by which participants are sampled from that population.""")
    methods_geographic_location: Optional[str] = Field(None, description="""State the geographic region(s) where participants were sampled from.""")
    methods_relevant_dates: Optional[str] = Field(None, description="""State the start and end dates for recruitment, follow-up, and data collection.""")
    methods_eligibility_criteria: Optional[str] = Field(None, description="""List any criteria for inclusion and exclusion of recruited participants.""")
    methods_antibiotics_usage: Optional[str] = Field(None, description="""List what is known about antibiotics usage before or during sample collection.""")
    methods_analytic_sample_size: Optional[str] = Field(None, description="""Explain how the final analytic sample size was calculated, including the number of cases and controls if relevant, and reasons for dropout at each stage of the study.""")
    methods_longitudinal_studies: Optional[str] = Field(None, description="""For longitudinal studies, state how many follow-ups were conducted, describe sample size at follow-up by group or condition, and discuss any loss to follow-up.""")
    methods_matching: Optional[str] = Field(None, description="""For matched studies, give matching criteria.""")
    methods_ethics: Optional[str] = Field(None, description="""State the name of the institutional review board that approved the study and protocols, protocol number and date of approval, and procedures for obtaining informed consent from participants.""")
    methods_laboratory_methods: Optional[str] = Field(None, description="""State the laboratory/center where laboratory work was done.""")
    methods_specimen_collection: Optional[str] = Field(None, description="""State the body site(s) sampled from and how specimens were collected.""")
    methods_shipping: Optional[str] = Field(None, description="""Describe how samples were stored and shipped to the laboratory.""")
    methods_storage: Optional[str] = Field(None, description="""Describe how the laboratory stored samples, including time between collection and storage and any preservation buffers or refrigeration used.""")
    methods_dna_extraction: Optional[str] = Field(None, description="""Provide DNA extraction method, including kit and version if relevant.""")
    methods_human_dna_sequence_depletion_or_microbial_dna_enrichment: Optional[str] = Field(None, description="""Describe whether human DNA sequence depletion or enrichment of microbial or viral DNA was performed.""")
    methods_primer_selection: Optional[str] = Field(None, description="""Provide primer selection and DNA amplification methods as well as variable region sequenced (if applicable).""")
    methods_positive_controls: Optional[str] = Field(None, description="""Describe any positive controls (mock communities) if used.""")
    methods_negative_controls: Optional[str] = Field(None, description="""Describe any negative controls if used.""")
    methods_contaminant_mitigation_and_identification: Optional[str] = Field(None, description="""Provide any laboratory or computational methods used to control for or identify microbiome contamination from the environment, reagents, or laboratory.""")
    methods_replication: Optional[str] = Field(None, description="""Describe any biological or technical replicates included in the sequencing, including which steps were replicated between them.""")
    methods_sequencing_strategy: Optional[str] = Field(None, description="""Major divisions of strategy, such as shotgun or amplicon sequencing.""")
    methods_sequencing_methods: Optional[str] = Field(None, description="""State whether experimental quantification was used (QMP/cell count based, spike-in based) or whether relative abundance methods were applied.""")
    methods_batch_effects: Optional[str] = Field(None, description="""Detail any blocking or randomization used in study design to avoid confounding of batches with exposures or outcomes. Discuss any likely sources of batch effects, if known.""")
    methods_metatranscriptomics: Optional[str] = Field(None, description="""Detail whether any mRNA enrichment was performed and whether/how retrotranscription was performed prior to sequencing. Provide size range of isolated transcripts. Describe whether the sequencing library was stranded or not. Provide details on sequencing methods and platforms.""")
    methods_metaproteomics: Optional[str] = Field(None, description="""Detail which protease was used for digestion. Provide details on proteomic methods and platforms (e.g. LC-MS/MS, instrument type, column type, mass range, resolution, scan speed, maximum injection time, isolation window, normalised collision energy, and resolution).""")
    methods_metabolomics: Optional[str] = Field(None, description="""Specify the analytic method used (such as nuclear magnetic resonance spectroscopy or mass spectrometry). For mass spectrometry, detail which fractions were obtained (polar and/or non polar) and how these were analyzed. Provide details on metabolomics methods and platforms (e.g. derivatization, instrument type, injection type, column type and instrument settings).""")
    results_descriptive_data: Optional[str] = Field(None, description="""Give characteristics of study participants (e.g. dietary, demographic, clinical, social) and information on exposures and potential confounders.""")
    results_microbiome_data: Optional[str] = Field(None, description="""Report descriptive findings for microbiome analyses with all applicable outcomes and covariates.""")
    results_taxonomy: Optional[str] = Field(None, description="""Identify taxonomy using standardized taxon classifications that are sufficient to uniquely identify taxa.""")
    results_differential_abundance: Optional[str] = Field(None, description="""Report results of differential abundance analysis by the variable of interest and (if applicable) by time, clearly indicating the direction of change and total number of taxa tested.""")
    results_other_data_types: Optional[str] = Field(None, description="""Report other data analyzed--e.g. metabolic function, functional potential, MAG assembly, and RNAseq.""")
    results_other_statistical_analysis: Optional[str] = Field(None, description="""Report any statistical data analysis not covered above.""")
    discussion_key_results: Optional[str] = Field(None, description="""Summarize key results with reference to study objectives.""")
    discussion_interpretation: Optional[str] = Field(None, description="""Give a cautious overall interpretation of results considering objectives, limitations, multiplicity of analyses, results from similar studies, and other relevant evidence.""")
    discussion_limitations: Optional[str] = Field(None, description="""Discuss limitations of the study, taking into account sources of potential bias or imprecision.""")
    discussion_bias: Optional[str] = Field(None, description="""Discuss any potential for bias to influence study findings.""")
    discussion_generalizability: Optional[str] = Field(None, description="""Discuss the generalizability (external validity) of the study results.""")
    discussion_ongoing_future_work: Optional[str] = Field(None, description="""Describe potential future research or ongoing research based on the study's findings.""")
    other_information_funding: Optional[str] = Field(None, description="""Give the source of funding and the role of the funders for the present study and, if applicable, for the original study on which the present article is based.""")
    other_information_acknowledgements: Optional[str] = Field(None, description="""Include acknowledgements of those who contributed to the research but did not meet criteria for authorship.""")
    other_information_conflicts_of_interest: Optional[str] = Field(None, description="""Include a conflicts of interest statement.""")
    other_information_supplements: Optional[str] = Field(None, description="""Indicate where supplements may be accessed and what materials they contain.""")
    other_information_supplementary_data: Optional[str] = Field(None, description="""Provide supplementary data files of results with all taxa and all outcome variables analyzed. Indicate the taxonomic level of all taxa.""")


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
ExtractionResult.model_rebuild()
NamedEntity.model_rebuild()
CompoundExpression.model_rebuild()
Triple.model_rebuild()
TextWithTriples.model_rebuild()
TextWithEntity.model_rebuild()
RelationshipType.model_rebuild()
Publication.model_rebuild()
AnnotatorResult.model_rebuild()
STORMSChecklist.model_rebuild()

